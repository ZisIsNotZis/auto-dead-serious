# Auto Dead Serious 🧱

[English](README.md) | 简体中文

> 一个认真收纳“奇怪软件想法”的可检查作品集：每个项目独立维护，并以固定版本汇总，不抹平历史。

**适合谁：** 想判断作者到底能不能把东西做出来的人——合作者、招聘方的读者、只想看源码不想看推销的工程师。
**不适合谁：** 这不是包仓库，不是统一构建的 monorepo，也不承诺任何项目可用在生产环境。每个子项目拥有自己的工具链、许可证、测试和发布路径。

[![项目数](https://img.shields.io/badge/projects-70-6f42c1)](docs/result/catalogue-redesign/README.md)
[![许可证](https://img.shields.io/badge/license-AGPL--3.0--only-blue)](LICENSE)
[![规范](https://img.shields.io/badge/docs-AGENTS.md-0f766e)](AGENTS.md)

![作品集中的四个项目](docs/media/showcase.jpg)

*从左到右：VibeOS、Raid Calc、Pelican Bike、AutoFE——各自仓库里已提交截图的裁切，不是为本页渲染的图。*

## 作品概览

<!-- BEGIN GENERATED SHOWCASE -->
| 项目 | 是什么 | 状态 | 推荐度 | 想法 | 已实现 | 潜力 | 完成度 |
|---|---|---|---:|---:|---:|---:|---:|
| [helpagent](helpagent/) | A completed research campaign and harness measuring a fixed small local model in bounded… | 单次交付 | 7.6 | 7.7 | 7 | 7.2 | 9 |
| [auto_maintain_bench](auto_maintain_bench/) | A benchmark for small language models diagnosing and maintaining Linux hosts through constrained bash… | 可用 | 6.8 | 7.0 | 6 | 6.4 | 8 |
| [agentic-animation](agentic-animation/) | A local, project-agnostic pipeline for structured-story input, code-driven 2D puppet motion, replaceable… | 可用 | 6.8 | 6.3 | 7 | 6.0 | 7 |
| [murderMysteryGame](murderMysteryGame/) | 《寿宴》 is a printable six-player-and-host mystery-game POC with role booklets, host instructions, clue cards,… | 单次交付 | 6.5 | 7.0 | 6 | 5.2 | 7 |
| [fat_kakeya_needle](fat_kakeya_needle/) | A mathematical and computational research workbench on minimizing the swept area of a 1×ε rectangle during a… | 原型 | 6.3 | 7.3 | 5 | 5.6 | 6 |
| [raid_calc](raid_calc/) | Offline browser calculator for expected data loss over time in arbitrarily nested storage pools, with a CTMC… | 单次交付 | 5.9 | 6.0 | 6 | 4.5 | 8 |
| [aps](aps/) | An experimental local planning workbench that models manufacturing item flows, compiles constraints,… | 原型 | 5.8 | 5.3 | 6 | 5.2 | 7 |
| [dojo](dojo/) | A local CLI and SQLite proof of concept for storing revisable, sourced discussion candidates, alternatives,… | 原型 | 5.8 | 6.3 | 5 | 4.9 | 6 |

**70 个固定版本项目**：5 可用 · 33 原型 · 1 仅设计 · 18 单次交付 · 9 归档 · 4 私有。其中 52 行仍是首轮估计。

项目描述沿用各仓库的英文原文，避免同一事实出现两份译文。

全部 70 个固定版本项目，每项都写明能实际看到什么、每个数字怎么来的、哪些尚未验证、评分如何变化：[**打开作品总览**](docs/result/catalogue-redesign/README.md)。所有分数是基于书面证据的 0–10 序数判断估计，不是测量，量表定义见该页。

<!-- 由 scripts/catalogue_final.py 从 assessments.json 生成。请改评分，不要改这段。 -->
<!-- END GENERATED SHOWCASE -->

## 快速开始

```sh
git clone --recurse-submodules https://github.com/ZisIsNotZis/auto-dead-serious.git
cd auto-dead-serious
git submodule status | wc -l
```

最后一行输出 `71`：70 个项目加上本工作区自己的规范。其中 4 个项目是私有的（`colleague_private`、`tutor_private`、`resume_private`、`timecolumn`），没有权限会失败；其余 66 个项目可匿名克隆，规范仓库同样可匿名克隆。远端已改为 HTTPS，不需要 SSH 密钥。

重新生成本页所有表格只需要标准库（Python 3.12，无需安装依赖）：

```sh
python3 scripts/catalogue_final.py
```

输出 `PASS: 70 projects, 70 rows rendered, …`，在作者机器上实测约 0.04 秒。全新克隆无法重建的只有上面 4 个私有子项目：工作树本身就是项目，仓库里没有放置构建产物。

## 状态与限制

- **本页每个分数都是依据书面证据给出的 0–10 序数判断估计。** 没有任何构建、测试、渲染或模型运行作为支撑，没有一个是测量值。
- **70 行中有 52 行未复核。** 它们保留首轮估计，只有复核过的行会在“评分轨迹”里注明。
- 已发布的作品总览逐项写明：访客实际能看到什么、每个维度怎么得出、哪些尚未验证、评分如何变化——[打开总览](docs/result/catalogue-redesign/README.md)。
- 本页图片均来自子仓库中已提交文件的裁切，并标注来源；没有为本页渲染、摆拍或修图。
- 可选的检出说明在 [WORKSPACE.md](WORKSPACE.md)，代理遵循的规范在 [AGENTS.md](AGENTS.md)，它是指向 [agent-policy](https://github.com/ZisIsNotZis/agent-policy) 子模块的软链接，规范在那里维护。

## 这里的“严肃”指什么

- **可复现：** 版本、变更记录、命令和有日期的证据——例如把证书和结论放在一起的[这个项目](fat_kakeya_needle/)。
- **可读：** 一页 README 先说清是什么、不是什么，再谈功能。
- **可见：** 有截图、录屏和演示包就放出来，而不是堆形容词。
- **可维护：** 欢迎 issue 和 PR；代理可以协助，人类保留评审与合并权。

## 范围与非目标

这里是索引和发布边界，不是 monorepo、不是共享构建系统，也不宣称每个实验都已可用于生产。生成依赖、凭据、私有材料和未审阅的媒体不属于这里。

## 未来愿景 🛰️

作品集应当成为一份连贯的、可运行的清单：每个有用的项目都能在几分钟内试起来，每项创新都有可度量的证据，每个成熟应用都有可安装的发布。项目保留各自的文档与发布路径；路线图由下一个有意义的项目驱动，而不是一份固定清单。

## 贡献

请向对应子仓库提 issue 或 PR；关于成员与目录的改动，向本索引提出；规范本身在 [agent-policy](https://github.com/ZisIsNotZis/agent-policy) 提 issue。请附上受影响的路径、证据和验证命令。代理可以协助分诊、调研、测试、文档与实现；维护者负责评审与合并。

## 许可证

本汇总仓库的原创材料采用 AGPL-3.0-only，`agent-policy/` 里的规范采用 MIT。子仓库保留各自许可证；复用前请逐个检查。
