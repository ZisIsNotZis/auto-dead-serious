# 项目总索引

子模块仅包含进行中的公开项目。按仓库 URL 识别项目，本地路径可保留历史别名。
本表覆盖 2026-11-26 查询到的公开自有仓库。私人项目和本地材料继续独立保管。

[评分与横向对比](docs/result/catalogue-redesign/README.md) · [推进与完成规则](WORKSPACE.md)

## 已验收完成

只收录完成范围、可验证入口和远端版本都已核对的交付。单独完成一轮研究或一个切片时，在对应项目记录范围。

| 仓库 | 完成范围 | 远端验收记录 |
|---|---|---|
| [pelican_bike](https://github.com/ZisIsNotZis/pelican_bike) | 离线单文件骑行，六档速度、昼夜和声音控制。 | [aaf2a21](https://github.com/ZisIsNotZis/pelican_bike/blob/aaf2a21/COMPLETION.md) |
| [pushbus](https://github.com/ZisIsNotZis/pushbus) | 无运行时依赖的 Python 路由总线，支持键连接、宽限计时、异常隔离和并发更新。 | [05bb147](https://github.com/ZisIsNotZis/pushbus/blob/05bb147/COMPLETION.md) |

## 进行中

有空位时优先收敛已经接近验收的本地切片。下一轮按 Monopoly11、Monopoly12、Learn Draw、Dojo、Agentic Animation 排入，随后按表中的顺序。并行上限见工作区说明。

| 仓库 | 状态 | 工作区路径 | 目标或下一步 | GitHub 简介 |
|---|---|---|---|---|
| [monoploy11](https://github.com/ZisIsNotZis/monoploy11) | 进行中 | `monoploy11` | 验收可离线玩的单文件版本和窄屏决策 | GitHub 暂无简介 |
| [monopoly12](https://github.com/ZisIsNotZis/monopoly12) | 进行中 | `monopoly12` | 验收可离线玩的单文件版本和键盘决策 | GitHub 暂无简介 |
| [learn_draw](https://github.com/ZisIsNotZis/learn_draw) | 进行中 | `learn_draw` | 用单张成图验收二维叙事与绘画工作流 | Learning to draw as a computed skill: SVG artwork built from relations and 3D depth, judged picture by picture. AGPL-3.0. |
| [agentic-animation](https://github.com/ZisIsNotZis/agentic-animation) | 进行中 | `agentic-animation` | 用完整短片验证可复用动作与道具交互 | Agent-operated toolkit that turns a written story into a narrated, deterministic 2D animated MP4 — code-driven motion, no generative video |
| [dojo](https://github.com/ZisIsNotZis/dojo) | 进行中 | `dojo` | 用本地 CLI 验收一条可追溯、可修订的知识链 | Local no-UI CLI + SQLite ledger for traceable discussion candidates: provenance, versions, boundaries, and a dao library |
| [autofe](https://github.com/ZisIsNotZis/autofe) | 进行中 | `autofe` | 同一业务意图从源证据生成并验收多个阅读视图 | Intent-driven frontend: declare what a page means, and one shared decision layer renders it as HTML, plain text and Markdown. |
| [flashdb](https://github.com/ZisIsNotZis/flashdb) | 进行中 | `flashdb` | 验收真实业务单请求、自动布局及可归因的发布包 | A log-structured document store that learns its per-region physical layout from the workload instead of asking you to declare one. |
| [socraticMirror](https://github.com/ZisIsNotZis/socraticMirror) | 进行中 | `socraticMirror` | 验收用户能自主发现知识缺口的完整交互 | GitHub 暂无简介 |
| [backseat](https://github.com/ZisIsNotZis/backseat) | 进行中 | `backseat` | 验证本地、透明、可追溯的建议工作流 | Local-first AI companion: the screen is a trigger, the substance comes from your repos and session records, and every comment cites its source. |
| [helpagent](https://github.com/ZisIsNotZis/helpagent) | 进行中 | `helpagent` | 保留已完测量，验证小模型工作流的下一处独立收益 | A pre-registered measurement of a program-shaped coding harness on a 4B local model: three verdicts, negative results, and every decisive number recomputable offline |
| [sys_gal](https://github.com/ZisIsNotZis/sys_gal) | 进行中 | `sys_gal` | 验收角色自主行动和可重放的完整叙事切片 | A reproducible Chinese narrative-simulation lab: autonomous characters see only what they perceive, and every run leaves a byte-exact replayable trace |
| [agentworld](https://github.com/ZisIsNotZis/agentworld) | 进行中 | `agentworld` | 以同一世界检验演化策略与推理成本 | An event-driven civilization simulator: deterministic simulation with cheap strategies for routine decisions and language-model reasoning spent only where it changes the outcome |
| [fat_kakeya_needle](https://github.com/ZisIsNotZis/fat_kakeya_needle) | 进行中 | `fat_kakeya_needle` | 保持证书可重建并区分有限构造与渐近结论 | Numerical study of the fat Kakeya needle problem: candidate motions, budget→quality scaling, and exact rational upper-bound certificates. |
| [pathlm](https://github.com/ZisIsNotZis/pathlm) | 进行中 | `pathlm` | 以可复现实验推进语言模型的计算分配 | Machine-checkable research tree on where a language model should spend its compute: per-axis experiments with measurement discipline, cost table and reproducibility verdicts. |
| [auto_maintain_bench](https://github.com/ZisIsNotZis/auto_maintain_bench) | 进行中 | `auto_maintain_bench` | 保留可重复的维护测量和实际运行约束 | A deterministic proving ground for tiny local models that repair Linux hosts through a single bash tool: 172 sandboxed scenarios, observable scoring, no LLM judge. |
| [nomos](https://github.com/ZisIsNotZis/nomos) | 进行中 | `nomos` | 区分策略内化、字面复述和通用能力损失 | SFT a personal operating constitution into a 2B model — then measure whether it landed and what it cost in general ability |
| [tiny-llm-eval-factors](https://github.com/ZisIsNotZis/tiny-llm-eval-factors) | 进行中 | `local_lm_research` | 复核已发布分析和可复现测量的开放范围 | Reproducible workbench for measuring which factors move a local LLM's benchmark score: quantization width, model size, decoding protocol and scoring — one SQLite database, one command to rebuild the report. |

## 待验收与推进

按表顺序进入验收。首轮另已检查 Raid Calc、cov7segDsp 和 pi-keys，进度在各行。

| 仓库 | 状态 | 工作区路径 | 目标或下一步 | GitHub 简介 |
|---|---|---|---|---|
| [cov7segDsp](https://github.com/ZisIsNotZis/cov7segDsp) | 待验收 | — | 12 项 Python 测试、7 组 JS 测试、离线构建及 6/8 遮挡演示通过；设计器完整流程待验收 | GitHub 暂无简介 |
| [murderMysteryGame](https://github.com/ZisIsNotZis/murderMysteryGame) | 待验收 | — | 复核六人打印包，确认角色人数和剧透边界 | 《寿宴》— a six-player, print-and-play Chinese murder mystery where nobody lies; every line stays true after the reveal. |
| [raid_calc](https://github.com/ZisIsNotZis/raid_calc) | 待验收 | — | 111 项测试与单文件重建通过；完整浏览器烟测待复核 | Calculate the expected data loss of nested storage pools over time — exact CTMC numerics in one offline HTML file. |
| [resume_img_gen](https://github.com/ZisIsNotZis/resume_img_gen) | 待验收 | — | 从公开样例重建 HTML 与已有支持的导出格式 | Structured resume data + reusable HTML design canvas -> HTML, PNG, or PDF. Dependency-free rendering, headless-browser capture, pandoc/WeasyPrint PDF. |
| [pi-keys](https://github.com/ZisIsNotZis/pi-keys) | 待验收 | — | 轮换单测通过；真实 Pi 客户端的回环烟测待验证 | Environment API-key rotation for Pi: advance to the next key on failure, while Pi owns retries. |
| [litellmgen](https://github.com/ZisIsNotZis/litellmgen) | 待验收 | — | 用合成配置核对字段合并与凭据边界 | Build one LiteLLM config from five model sources, with every field resolved by source priority. |
| [iba.py](https://github.com/ZisIsNotZis/iba.py) | 待验收 | — | 验收公开样例的可读写范围，明确压缩限制 | Create IBA Analyzer `.dat` Files Without the IBA Library |
| [ygoimgen.sh](https://github.com/ZisIsNotZis/ygoimgen.sh) | 待验收 | — | 从公开小样例验收生成一张卡的入口 | A bash-based Yu-Gi-Oh! card image generator that converts card data (from a SQLite database) and custom artwork into official-style card images. Uses sqlite3 for data handling and imagemagick for image rendering. |
| [suzhou-drive](https://github.com/ZisIsNotZis/suzhou-drive) | 待验收 | — | 离线启动并检查真实地图驾驶切片 | Offline-first browser driving simulator: a checked-in Suzhou OpenStreetMap extract, lane-aware navigation, signals, traffic, weather and canal hazards. No tiles, no API key, no runtime network. |
| [resume_improve_loop](https://github.com/ZisIsNotZis/resume_improve_loop) | 待验收 | — | 用合成经历验收岗位证据与修改闭环 | Adversarial multi-reviewer loop for resumes: nine independent personas score a document and quote the exact lines that hurt, until scores plateau. |
| [dinov23.cpp.py](https://github.com/ZisIsNotZis/dinov23.cpp.py) | 待验收 | — | 在已授权的轻量输入上确认 DINOv3 对照偏差 | A python ggml implementation of dinov2 and dinov3 |
| [iron-meridian](https://github.com/ZisIsNotZis/iron-meridian) | 待验收 | — | 验证 YAML 到可玩的确定性对局 | A near-future browser RTS prototype: deterministic 30 Hz simulation, scripted AI, and YAML-defined content. |
| [hypermaker](https://github.com/ZisIsNotZis/hypermaker) | 待验收 | — | 验收一个可追溯的节点产物切片 | Local-first node canvas where an agent turns connected cards into inspectable text, image, audio and video artifacts |
| [aps](https://github.com/ZisIsNotZis/aps) | 待验收 | — | 用代表性流程订单验收建模到可执行排程 | Turn item flows, resources, rules, and orders into an executable production plan — model, solve, and inspect schedules locally. |
| [vibeos](https://github.com/ZisIsNotZis/vibeos) | 待验收 | — | 验收一次从缺失应用到可用发布的完整流程 | A browser-hosted operating system that grows on demand: missing apps and pages are generated, validated and published into a world tree |

## 历史归档、暂缓和已被替代

| 仓库 | 状态 | 工作区路径 | 目标或下一步 | GitHub 简介 |
|---|---|---|---|---|
| [sys_gal_rt](https://github.com/ZisIsNotZis/sys_gal_rt) | 暂缓 | — | 等 Sys Gal 的叙事效果得到验证，再推进实时版 | Real-time narrative simulation engine where world time is a function of wall time: model latency and fast-forward become in-world physics. Design-stage; ships its first story pack. |
| [expyssion](https://github.com/ZisIsNotZis/expyssion) | 暂缓 | — | 暂缓；先明确与普通 Python 的兼容边界及实际用户 | Everything is an expression; everything is a call. A Python-hosted language with no keywords, where yield and return cross lambda boundaries. |
| [wafer-thermal-calibration](https://github.com/ZisIsNotZis/wafer-thermal-calibration) | 历史归档 | — | `disk` 的早期材料，保留采集数据与未完成的 Jacobian 搜索。 | Archived bench study of wafer thermal calibration: 47 actuators, 34 IR sensors, measured transitions and an unfinished Jacobian search. |
| [disk](https://github.com/ZisIsNotZis/disk) | 历史归档 | — | 后续闭环热控实验，早期采集和未完成搜索另见 wafer-thermal-calibration | A real closed-loop thermal-control experiment: 47 heater set-points, 34 IR channels, and the inverse models that learned to steer one from the other. |
| [ideas](https://github.com/ZisIsNotZis/ideas) | 暂缓 | — | 作为想法库保存 | Speculative idea notebook: time-series foundation models, implicit world models for RL, cache-native LLM memory, and a token language |
| [TokenQR](https://github.com/ZisIsNotZis/TokenQR) | 暂缓 | — | 设计验证待排期；明确派生凭据、撤销与额度的信任边界 | Open, client-first token authorization protocol: scan a one-time QR, confirm on your provider, keep the token end-to-end encrypted. |
| [agent-policy](https://github.com/ZisIsNotZis/agent-policy) | 已被替代 | — | 已并入 Praxis 与 Praxis2 的工作方式，保留历史 | One hand-written law becomes every agent role's instructions: Goal, roadmap, review and release in one place. |

## 其余公开仓库

| 仓库 | 状态 | 工作区路径 | 目标或下一步 | GitHub 简介 |
|---|---|---|---|---|
| [agent.js](https://github.com/ZisIsNotZis/agent.js) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A coding agent that runs in the browser tab: your own key, the workspace in OPFS, a tree of agents whose every step is a git commit — and it survives the tab being killed. |
| [agent.sh](https://github.com/ZisIsNotZis/agent.sh) | 待核 | — | 待核对 README、入口和最后一份交付证据 | An agent with no tools: the model's reply is run by one long-lived bash, and what that shell printed is the next message. |
| [asyncs7.py](https://github.com/ZisIsNotZis/asyncs7.py) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A minimal (but modern) async implementation of certain parts of S7 protocol in python |
| [bark.cpp](https://github.com/ZisIsNotZis/bark.cpp) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | Suno AI's Bark model in C/C++ for fast text-to-speech generation |
| [beam](https://github.com/ZisIsNotZis/beam) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Eight hand-written beam-search decoding experiments for llama.cpp, archived with the KV-cache trade-offs annotated. |
| [causalmlp](https://github.com/ZisIsNotZis/causalmlp) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A usable prediction at every hidden size from one forward pass — a small PyTorch study of causal hidden units. |
| [cept](https://github.com/ZisIsNotZis/cept) | 待核 | — | 待核对 README、入口和最后一份交付证据 | My programming language (not named) and compiler/transpiler implementation |
| [cppBorrow](https://github.com/ZisIsNotZis/cppBorrow) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Compile-time C++ borrowing mechanism like what's in Rust |
| [cppChan](https://github.com/ZisIsNotZis/cppChan) | 待核 | — | 待核对 README、入口和最后一份交付证据 | C++ channel implementation like what's in Go |
| [cppTest](https://github.com/ZisIsNotZis/cppTest) | 待核 | — | 待核对 README、入口和最后一份交付证据 | C/C++ unit test tool to make the compiler support unit testing |
| [cuda](https://github.com/ZisIsNotZis/cuda) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Hand-written tensor-core and warp-level CUDA experiments — a measurement-first lab. |
| [cvorat](https://github.com/ZisIsNotZis/cvorat) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Byte-level language-model architecture experiments: windowed/grouped attention, dynamic convolution, cumulative-state layers, LoRA and RoPE variants. |
| [cz_bert](https://github.com/ZisIsNotZis/cz_bert) | 待核 | — | 待核对 README、入口和最后一份交付证据 | cz_bert |
| [cz_einn](https://github.com/ZisIsNotZis/cz_einn) | 待核 | — | 待核对 README、入口和最后一份交付证据 | EINN: write a neural network as an Einstein-summation string and build it with PyTorch einsum. A 2020 fastai research archive on Chinese character modelling. |
| [cz_noidea](https://github.com/ZisIsNotZis/cz_noidea) | 待核 | — | 待核对 README、入口和最后一份交付证据 | cz_noidea |
| [cznn](https://github.com/ZisIsNotZis/cznn) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Point-free layer composition for PyTorch research — build neural networks as expressions, not Module subclasses. |
| [danmaku](https://github.com/ZisIsNotZis/danmaku) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Bilibili-style scrolling comments over any X11 desktop — transparent, always on top, click-through. |
| [DataEditorX](https://github.com/ZisIsNotZis/DataEditorX) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | YGOPRO Cards Editor |
| [dcg](https://github.com/ZisIsNotZis/dcg) | 待核 | — | 待核对 README、入口和最后一份交付证据 | GitHub 暂无简介 |
| [dino.py](https://github.com/ZisIsNotZis/dino.py) | 待核 | — | 待核对 README、入口和最后一份交付证据 | DINOv2 and DINOv3 vision features on ggml — no PyTorch at inference. |
| [dinoseg](https://github.com/ZisIsNotZis/dinoseg) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Click a few pixels to segment a whole batch: interactive segmentation on frozen DINOv3 features for industrial machine vision. |
| [dinov2.cpp](https://github.com/ZisIsNotZis/dinov2.cpp) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | DINOv2 inference engine written in C/C++ using ggml and OpenCV. |
| [drive](https://github.com/ZisIsNotZis/drive) | 待核 | — | 待核对 README、入口和最后一份交付证据 | drive project |
| [fring](https://github.com/ZisIsNotZis/fring) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Three hand-written io_uring event loops in Python: raw CQEs, an asyncio bridge, and a from-scratch coroutine scheduler. |
| [ggml-python](https://github.com/ZisIsNotZis/ggml-python) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | Python bindings for ggml |
| [ghtest](https://github.com/ZisIsNotZis/ghtest) | 待核 | — | 待核对 README、入口和最后一份交付证据 | GitHub 暂无简介 |
| [goSeamCarve](https://github.com/ZisIsNotZis/goSeamCarve) | 待核 | — | 待核对 README、入口和最后一份交付证据 | GitHub 暂无简介 |
| [grammar](https://github.com/ZisIsNotZis/grammar) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Masked-token (denoising) U-Net experiments over a 90-symbol tokenised Python-source corpus — pure convolution, no recurrence, no attention |
| [greenlet_fiber](https://github.com/ZisIsNotZis/greenlet_fiber) | 待核 | — | 待核对 README、入口和最后一份交付证据 | fiber with greenlet |
| [gu](https://github.com/ZisIsNotZis/gu) | 待核 | — | 待核对 README、入口和最后一份交付证据 | The best card game ever |
| [hfget](https://github.com/ZisIsNotZis/hfget) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Find and download the right GGUF quantizations from Hugging Face. |
| [horse_video](https://github.com/ZisIsNotZis/horse_video) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A 15-second cinematic horse gallop: a low-poly horse and its straw-hat rider at sunset, drawn frame by frame in TypeScript with React, Three.js, SVG and Remotion. |
| [http_mock](https://github.com/ZisIsNotZis/http_mock) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Can a GRU learn to be a server? Synthetic HTTP and key-value traces plus a character-level seq2seq trained from scratch to imitate them. |
| [huaqiang_game](https://github.com/ZisIsNotZis/huaqiang_game) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Game-design lab for 《一斤八两》: a social-stealth prototype where observation, preparation, and consequences decide the encounter. |
| [huaqiang_video](https://github.com/ZisIsNotZis/huaqiang_video) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A 70-second Remotion short that rebuilds the classic "Huaqiang buys a melon" scene in React — dialogue, camera and sound on one code timeline. |
| [imagen-pytorch](https://github.com/ZisIsNotZis/imagen-pytorch) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | Implementation of Imagen, Google's Text-to-Image Neural Network, in Pytorch |
| [InfluxDBStudio](https://github.com/ZisIsNotZis/InfluxDBStudio) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | InfluxDB Studio is a UI management tool for the InfluxDB time series database. |
| [io_uring-echo-server](https://github.com/ZisIsNotZis/io_uring-echo-server) | 待核 | — | 待核对 README、入口和最后一份交付证据 | io_uring-echo-server |
| [jpi.fe](https://github.com/ZisIsNotZis/jpi.fe) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Edit arbitrary JSON as a recursive tree of editable tables — a Vue 3 single-page app |
| [knowledge_net](https://github.com/ZisIsNotZis/knowledge_net) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Attention-read, gate-written key-value memory bank for sequence models: 11 PyTorch notebooks exploring it on tasks with exactly computable answers (unmaintained research sketch). |
| [llama-cpp-python](https://github.com/ZisIsNotZis/llama-cpp-python) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | Python bindings for llama.cpp |
| [llama.cpp](https://github.com/ZisIsNotZis/llama.cpp) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | llama.cpp fork with a live plain-text server dashboard: llama-server --tui N prints a tagged per-sequence status stream (phases, KV memory, cache hits, speeds, live tails, GPU/CPU utilization) every second. |
| [lm_paper_test](https://github.com/ZisIsNotZis/lm_paper_test) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Vibe coding project: lm_paper_test |
| [lmchk](https://github.com/ZisIsNotZis/lmchk) | 待核 | — | 待核对 README、入口和最后一份交付证据 | GitHub 暂无简介 |
| [lmlayer](https://github.com/ZisIsNotZis/lmlayer) | 待核 | — | 待核对 README、入口和最后一份交付证据 | OpenAI-compatible proxy that adds safety, sessions, RAG, tools, quotas, and fair scheduling to any LLM server. |
| [misc](https://github.com/ZisIsNotZis/misc) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A flat drawer of one-off scripts, notebooks and notes: a from-scratch ANSI terminal, asyncio servers, industrial-vision config munging and llama.cpp builds |
| [mux](https://github.com/ZisIsNotZis/mux) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Vibe coding project: mux |
| [mycar](https://github.com/ZisIsNotZis/mycar) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A 4.46 m shape-shifting camper car: a 1.75 m person sleeps flat and stands upright, purely mechanically. Parametric blueprint engine in one HTML file. |
| [myideaplugin](https://github.com/ZisIsNotZis/myideaplugin) | 待核 | — | 待核对 README、入口和最后一份交付证据 | GitHub 暂无简介 |
| [myminio](https://github.com/ZisIsNotZis/myminio) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A hand-rolled object store: XOR erasure coding, versioned reads, quota-aware placement, and on-read shard repair in Python and NumPy. |
| [myminio2](https://github.com/ZisIsNotZis/myminio2) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Hand-rolled object store: asyncio HTTP/1.1 file server plus a 2+1 XOR erasure-coded gateway over three backends |
| [myygo](https://github.com/ZisIsNotZis/myygo) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A compact, lambda-driven DSL sketch that turns Yu-Gi-Oh! card effects into uniform, auditable data. |
| [myzcopy](https://github.com/ZisIsNotZis/myzcopy) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Zero-copy file/RAID toolkit in one C binary (copy_file_range, splice, io_uring) — archived experiment |
| [neuronloop](https://github.com/ZisIsNotZis/neuronloop) | 待核 | — | 待核对 README、入口和最后一份交付证据 | neuronloop |
| [nn](https://github.com/ZisIsNotZis/nn) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Fifty throwaway PyTorch notebooks (2021-2022) hand-rolling attention, trainers and PageRank from primitives — sanitised archive |
| [npchallenge](https://github.com/ZisIsNotZis/npchallenge) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Pure-NumPy causal attention and 2D convolution, written to be read: full vs. blocked kernels, im2col/einsum/FFT dispatch, benchmark harnesses. |
| [omniserve](https://github.com/ZisIsNotZis/omniserve) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | [MLSys'25] QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving; [MLSys'25] LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention |
| [retnet](https://github.com/ZisIsNotZis/retnet) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Byte-level RetNet experiments: a from-scratch, softmax-free retention layer and a 28-notebook research archive. |
| [ringsvr](https://github.com/ZisIsNotZis/ringsvr) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A single-threaded HTTP/1.1 file server built entirely on io_uring. |
| [send_teams](https://github.com/ZisIsNotZis/send_teams) | 待核 | — | 待核对 README、入口和最后一份交付证据 | # send_teams |
| [seq_autoenc](https://github.com/ZisIsNotZis/seq_autoenc) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Multi-scale sequence autoencoders: one convolutional encoder-decoder reconstructs a sequence at every down-sampling scale, next to n-gram and suffix-array baselines that measure how predictable the data is. |
| [sp](https://github.com/ZisIsNotZis/sp) | 待核 | — | 待核对 README、入口和最后一份交付证据 | GitHub 暂无简介 |
| [thcupd](https://github.com/ZisIsNotZis/thcupd) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | GitHub 暂无简介 |
| [tok](https://github.com/ZisIsNotZis/tok) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Bounded-vocabulary n-gram tokenizer experiments: count every gram, shrink the overflow by dropping or halving the cheapest — C++17, CUDA, NumPy |
| [treui](https://github.com/ZisIsNotZis/treui) | 待核 | — | 待核对 README、入口和最后一份交付证据 | treui — a node-graph chat canvas you can branch, drag and rewire |
| [TTS.cpp](https://github.com/ZisIsNotZis/TTS.cpp) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | TTS support with GGML |
| [uv](https://github.com/ZisIsNotZis/uv) | 待核 | — | 待核对 README、入口和最后一份交付证据 | One dumb HTTP handler across nine event loops: Python asyncio/uvloop/uvicorn vs C on raw liburing |
| [vision.cpp](https://github.com/ZisIsNotZis/vision.cpp) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | Computer Vision ML inference in C++ |
| [XNOR-popcount-GEMM-PyTorch-CPU-CUDA](https://github.com/ZisIsNotZis/XNOR-popcount-GEMM-PyTorch-CPU-CUDA) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | The PyTorch implemenation of real XNOR-popcount (1-bit op) GEMM Linear PyTorch extension support both CPU and CUDA |
| [ydkgen](https://github.com/ZisIsNotZis/ydkgen) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Transformer-Based Yu-Gi-Oh! Deck Generator (Pure PyTorch) |
| [ydkskill](https://github.com/ZisIsNotZis/ydkskill) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A skill that generates mastered Yu-Gi-Oh! deck (need ygopro files) |
| [ygo](https://github.com/ZisIsNotZis/ygo) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Yu-Gi-Oh! deck and card-art experiments: DINOv2 on hand-written ggml/GGUF from Python, PCA card-art autocrop, video shot selection, n-gram deck naming, torch deck models |
| [ygocli](https://github.com/ZisIsNotZis/ygocli) | 待核 | — | 待核对 README、入口和最后一份交付证据 | GitHub 暂无简介 |
| [ygodoc.py](https://github.com/ZisIsNotZis/ygodoc.py) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Generate Ygopro/ocgcore Lua skeleton by parsing ocgcore/lib*.cpp |
| [ygoDocGen](https://github.com/ZisIsNotZis/ygoDocGen) | 待核 | — | 待核对 README、入口和最后一份交付证据 | Generate YGOPro Lua Documentation by automatically inspecting C++ source file |
| [ygopro-core](https://github.com/ZisIsNotZis/ygopro-core) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | ygopro script engine. |
| [ygopro-scripts](https://github.com/ZisIsNotZis/ygopro-scripts) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | scripts of official cards for ygopro. |
| [ygopromcp](https://github.com/ZisIsNotZis/ygopromcp) | 公开派生仓库，待核 | — | 待核对 README、入口和最后一份交付证据 | A ygopro GUI instance with an MCP (Model Context Protocol) control plane — an AI agent reads the board and plays Yu-Gi-Oh! through the client. |
| [ygoskill](https://github.com/ZisIsNotZis/ygoskill) | 待核 | — | 待核对 README、入口和最后一份交付证据 | A generalized skill for Yu-Gi-Oh! |
