#!/usr/bin/env python3
"""One bounded, read-only cgroup and host-resource preflight probe."""
import os
import re


def unescape_mount(value):
    return re.sub(r"\\([0-7]{3})", lambda match: chr(int(match.group(1), 8)), value)


def read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as stream:
            return stream.read().strip()
    except (OSError, UnicodeError) as error:
        return f"UNKNOWN ({type(error).__name__}: {error})"


def parse_cpu_set(value):
    if not value or value.startswith("UNKNOWN"):
        return None
    cpus = set()
    try:
        for part in value.split(","):
            bounds = part.split("-", 1)
            start = int(bounds[0])
            end = int(bounds[1]) if len(bounds) == 2 else start
            cpus.update(range(start, end + 1))
        return sorted(cpus)
    except ValueError:
        return None


def parse_limit(value):
    if value == "max":
        return None
    try:
        return int(value)
    except ValueError:
        return None


def main():
    print("probe=read-only; no repository paths or Git commands accessed")
    cgroup_text = read_text("/proc/self/cgroup")
    print(f"/proc/self/cgroup={cgroup_text}")
    cgroup_path = None
    if not cgroup_text.startswith("UNKNOWN"):
        for line in cgroup_text.splitlines():
            fields = line.split(":", 2)
            if len(fields) == 3 and fields[0] == "0" and fields[1] == "":
                cgroup_path = os.path.normpath(fields[2])
                break

    mountpoint = None
    mount_root = None
    mountinfo = read_text("/proc/self/mountinfo")
    if not mountinfo.startswith("UNKNOWN"):
        for line in mountinfo.splitlines():
            sides = line.split(" - ", 1)
            if len(sides) != 2 or not sides[1].startswith("cgroup2 "):
                continue
            left = sides[0].split()
            if len(left) >= 5:
                mount_root = os.path.normpath(unescape_mount(left[3]))
                mountpoint = os.path.normpath(unescape_mount(left[4]))
                break

    cgroup_dir = None
    if cgroup_path is not None and mountpoint is not None and mount_root is not None:
        if mount_root == "/":
            relative = cgroup_path.lstrip("/")
        elif cgroup_path == mount_root:
            relative = ""
        elif cgroup_path.startswith(mount_root.rstrip("/") + "/"):
            relative = cgroup_path[len(mount_root):].lstrip("/")
        else:
            relative = None
        if relative is not None:
            candidate = os.path.normpath(os.path.join(mountpoint, relative))
            if os.path.commonpath((mountpoint, candidate)) == mountpoint:
                cgroup_dir = candidate
    print(f"cgroup_v2_mountpoint={mountpoint or 'UNKNOWN'}")
    print(f"cgroup_v2_mount_root={mount_root or 'UNKNOWN'}")
    print(f"current_cgroup_directory={cgroup_dir or 'UNKNOWN'}")

    if cgroup_dir:
        ancestors = []
        current = cgroup_dir
        while True:
            ancestors.append(current)
            if current == mountpoint:
                break
            parent = os.path.dirname(current)
            if parent == current or os.path.commonpath((mountpoint, parent)) != mountpoint:
                break
            current = parent

        cpu_quotas = []
        memory_limits = []
        process_limits = []
        for directory in ancestors:
            cpu_value = read_text(os.path.join(directory, "cpu.max"))
            if not cpu_value.startswith("UNKNOWN"):
                fields = cpu_value.split()
                if len(fields) == 2 and fields[0] != "max":
                    try:
                        quota, period = int(fields[0]), int(fields[1])
                        if period > 0:
                            cpu_quotas.append((quota, period, directory))
                    except ValueError:
                        pass
            for filename, values in (("memory.max", memory_limits), ("pids.max", process_limits)):
                value = read_text(os.path.join(directory, filename))
                parsed = parse_limit(value)
                if parsed is not None:
                    values.append((parsed, directory))

        cpuset_value = "UNKNOWN"
        for directory in ancestors:
            value = read_text(os.path.join(directory, "cpuset.cpus.effective"))
            if value and not value.startswith("UNKNOWN"):
                cpuset_value = value
                break
        cpus = parse_cpu_set(cpuset_value)
        effective_quota = min((quota / period for quota, period, _ in cpu_quotas), default=None)
        cpuset_count = len(cpus) if cpus is not None else None
        effective_cpu = min(effective_quota, cpuset_count) if effective_quota is not None and cpuset_count is not None else effective_quota if effective_quota is not None else cpuset_count
        print(f"cpu_quota_cores_min_across_ancestors={effective_quota if effective_quota is not None else 'unlimited_or_unknown'}")
        print(f"cpu_quota_source={min(cpu_quotas, key=lambda item: item[0] / item[1])[2] if cpu_quotas else 'unlimited_or_unknown'}")
        print(f"cpuset_cpus_effective={cpuset_value}")
        print(f"effective_cpu_capacity_cores_from_quota_and_cpuset={effective_cpu if effective_cpu is not None else 'UNKNOWN'}")
        print(f"memory_limit_bytes_min_across_ancestors={min(memory_limits, default=(None,))[0] if memory_limits else 'unlimited_or_unknown'}")
        print(f"memory_limit_source={min(memory_limits)[1] if memory_limits else 'unlimited_or_unknown'}")
        print(f"memory_current_bytes_at_current_cgroup={read_text(os.path.join(cgroup_dir, 'memory.current'))}")
        print(f"process_limit_min_across_ancestors={min(process_limits, default=(None,))[0] if process_limits else 'unlimited_or_unknown'}")
        print(f"process_limit_source={min(process_limits)[1] if process_limits else 'unlimited_or_unknown'}")
        print(f"process_current_at_current_cgroup={read_text(os.path.join(cgroup_dir, 'pids.current'))}")
        print("ancestor_limits=nearest-to-root traversal recorded by derived minimums above")
    else:
        print("cgroup-v2 effective limits/current use=UNKNOWN; no host value substituted")

    print(f"system_loadavg_1_5_15_and_runnable_total={read_text('/proc/loadavg')}")
    meminfo = read_text("/proc/meminfo")
    if meminfo.startswith("UNKNOWN"):
        print(f"system_meminfo={meminfo}")
    else:
        keys = {"MemTotal", "MemAvailable", "MemFree", "Buffers", "Cached", "SwapTotal", "SwapFree"}
        for line in meminfo.splitlines():
            key = line.split(":", 1)[0]
            if key in keys:
                print(f"system_{line}")

    try:
        process_count = sum(1 for entry in os.scandir("/proc") if entry.name.isdigit())
        print(f"numeric_proc_entries_observed={process_count}")
    except OSError as error:
        print(f"numeric_proc_entries_observed=UNKNOWN ({type(error).__name__}: {error})")

    print("allocator_or_admission_ledger=not established by resource-file probe; no authoritative endpoint was supplied")
    print("scan_specific_runtime_binding=not tested; no scan/job was launched")
    print("machine_wide_exclusivity=not established by this probe")


if __name__ == "__main__":
    main()
