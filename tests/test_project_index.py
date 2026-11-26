"""Check the live portfolio index against the Git index, without cloning projects."""

import configparser
from pathlib import Path
import re
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
ROW = re.compile(r"^\| \[[^\]]+\]\((https://github\.com/[^)]+)\)(?:（`[^`]+`）)? \| (.*)$", re.MULTILINE)
PIN = re.compile(r"^\[[0-9a-f]+\]\((https://github\.com/[^)]+)/tree/([0-9a-f]{40})\)")


class ProjectIndexTest(unittest.TestCase):
    def test_completed_projects_link_to_their_own_fixed_completion_marker(self):
        text = (ROOT / "PROJECTS.md").read_text(encoding="utf-8")
        completed = text.split("## 已验收完成\n", 1)[1].split("\n## ", 1)[0]
        rows = ROW.findall(completed)
        self.assertTrue(rows, "No completed repositories in PROJECTS.md")
        for url, fields in rows:
            with self.subTest(repo=url):
                marker = re.match(
                    rf"^\[([0-9a-f]{{7,40}})\]\({re.escape(url)}/blob/([0-9a-f]{{40}})/COMPLETION\.md\)",
                    fields,
                )
                self.assertIsNotNone(marker, "Expected this repository's fixed COMPLETION.md")
                abbreviated, full = marker.groups()
                self.assertTrue(full.startswith(abbreviated), "Completion label disagrees with its commit")

    def test_unfinished_projects_match_submodules_and_pins(self):
        text = (ROOT / "PROJECTS.md").read_text(encoding="utf-8")
        rows = ROW.findall(text)
        self.assertEqual(len(rows), len({url for url, _ in rows}), "Duplicate repository in PROJECTS.md")

        current = text.split("## 进行中与待验收\n", 1)[1]
        unfinished = current.split("## 历史归档与已被替代\n", 1)[0]
        expected = {}
        for url, fields in ROW.findall(unfinished):
            match = PIN.match(fields)
            self.assertIsNotNone(match, f"Missing fixed version for {url}")
            pinned_repo, sha = match.groups()
            self.assertEqual(pinned_repo, url)
            expected[url] = sha

        config = configparser.ConfigParser(interpolation=None)
        config.read(ROOT / ".gitmodules", encoding="utf-8")
        staged = subprocess.check_output(["git", "ls-files", "--stage", "-z"], cwd=ROOT)
        links = {}
        for entry in staged.rstrip(b"\0").split(b"\0"):
            metadata, path = entry.split(b"\t", 1)
            mode, sha, _ = metadata.decode("ascii").split()
            if mode == "160000":
                links[path.decode("utf-8")] = sha

        declared = {}
        for section in config.sections():
            module = config[section]
            url = module["url"].removesuffix(".git")
            path = module["path"]
            self.assertNotIn(url, declared, f"Duplicate submodule URL {url}")
            self.assertIn(path, links, f"Missing gitlink for {path}")
            declared[url] = links.pop(path)
        self.assertEqual(links, {}, "Gitlinks without a .gitmodules declaration")
        self.assertDictEqual(declared, expected)
