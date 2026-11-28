# 项目总索引

按 2026-11-26 的固定远端提交逐仓核对。只有完成范围和可取回回执都已确认的项目进入完成清单。
未完成项目在父仓固定为子模块。暂缓项目保留固定版本，退出自动推进队列。历史归档、被替代的项目和上游参考保留在本页。

[横向比较与历史评分](docs/result/catalogue-redesign/README.md) · [工作区和验收规则](WORKSPACE.md)

共 120 项，21 项已验收完成，45 个子模块（含 3 个暂缓），其余保留历史或参考状态。

## 已验收完成


| 仓库 | 固定版本或回执 | 验收证据 | 范围说明 |
|---|---|---|---|
| [agent.js](https://github.com/ZisIsNotZis/agent.js) | [ac325672](https://github.com/ZisIsNotZis/agent.js/blob/ac325672acbb783a7ab68c5c94e8c4fc94e703db/COMPLETION.md) | 浏览器内可恢复 agent 树的 M1，有界的本地模拟 provider 路径。 | — |
| [agent.sh](https://github.com/ZisIsNotZis/agent.sh) | [9cf9c3e3](https://github.com/ZisIsNotZis/agent.sh/blob/9cf9c3e3759a6103b761fff88e7249315dbb0ab5/COMPLETION.md) | Bash 单进程执行 harness 的 M1，包含任务回执、恢复及后台任务。 | — |
| [cov7segDsp](https://github.com/ZisIsNotZis/cov7segDsp) | [3d4b3301](https://github.com/ZisIsNotZis/cov7segDsp/blob/3d4b33012ff9189a54641a09a80dde88bc9db337/COMPLETION.md) | 覆盖遮挡与有限故障的研究及离线自定义显示器工作坊；按设计器当前路线验收。 | — |
| [horse_video](https://github.com/ZisIsNotZis/horse_video) | [4217d45f](https://github.com/ZisIsNotZis/horse_video/blob/4217d45f840ee65c534df0104c8b737a1e6dd8ab/COMPLETION.md) | 已封板创意作品；远端 MP4 真解码成功，1280×720 H.264 30fps，AAC 双声道，容器全长 15.06s。 | 完成范围为该短片与其 Remotion 时间线；不纳入后续项目队列。 |
| [huaqiang_video](https://github.com/ZisIsNotZis/huaqiang_video) | [5b6045dd](https://github.com/ZisIsNotZis/huaqiang_video/blob/5b6045ddf850007e33649a46179ca7d382db2777/COMPLETION.md) | 闭合的 0.1.0 影音原型，远端 MP4 真解码成功，1280×720 H.264 30fps、AAC 双声道，70.06s。 | 只标记已完成的代码分镜实验；转载素材权利未核，不增加发布渠道或资产。 |
| [litellmgen](https://github.com/ZisIsNotZis/litellmgen) | [836efb38](https://github.com/ZisIsNotZis/litellmgen/blob/836efb389a1738631f6257462365fb887daa5e68/COMPLETION.md) | 明确工具封板；用临时 YAML、费用表和合成目录在真实 main() 生成两条路由，验证逐字段优先、名单限制、每密钥一条。 | 单脚本生成器，运行前需配置本机路径。 |
| [mux](https://github.com/ZisIsNotZis/mux) | [16326ba](https://github.com/ZisIsNotZis/mux/blob/16326ba6b57ad642b3039700c08b19eb832e693c/COMPLETION.md) | 实际是小 tmux FIFO 分流示例。隔离 tmux 会话真实看到两个 pane 的 0+/1+ 与 0-/1-，shell 检查通过。| 完成范围为终端 stdout/stderr 两窗格示例；运行会留下需要手动清理的 FIFO 目录。 |
| [npchallenge](https://github.com/ZisIsNotZis/npchallenge) | [35324294](https://github.com/ZisIsNotZis/npchallenge/blob/3532429403bbb2609db04f186b84e950563303dd/COMPLETION.md) | 仓内声明 2026-09-29 教学里程碑已闭合。独立 NumPy 对照覆盖长短因果注意力、点卷积、带步幅与膨胀的卷积及 FFT 路径，受支持的同维 Q/K/V 数值一致。 | 基准速度随硬件变化。 |
| [pelican_bike](https://github.com/ZisIsNotZis/pelican_bike) | [aaf2a215](https://github.com/ZisIsNotZis/pelican_bike/blob/aaf2a21571a8004d1dfc62eafbe3a059bafa9f67/COMPLETION.md) | 远端完成标记和离线 HTML 都在固定提交。上一轮独立 Chromium 驱动 6 档、昼夜、静音与铃铛，并重新从远端检出核对单文件摘要。 | — |
| [pi-keys](https://github.com/ZisIsNotZis/pi-keys) | [22885d90](https://github.com/ZisIsNotZis/pi-keys/blob/22885d9005342742d4f50cc3bdbc37169dac3890/COMPLETION.md) | 在固定提交的隔离副本，用 Pi 1.6.1 执行 PI_KEYS_SMOKE=1 npm test。普通单元测试和真实 CLI 接回环模拟 API 的两个凭据路径均通过，未用真实凭据。 | — |
| [pushbus](https://github.com/ZisIsNotZis/pushbus) | [05bb1479](https://github.com/ZisIsNotZis/pushbus/blob/05bb1479f81230611a9edcdd7cdb0496524c6ad0/COMPLETION.md) | 远端完成标记、实现和 13 条测试同在固定提交。上一轮从独立远端副本重跑 pytest 全通过。 | — |
| [raid_calc](https://github.com/ZisIsNotZis/raid_calc) | [39578bbe](https://github.com/ZisIsNotZis/raid_calc/blob/39578bbe37ae111f456796c6b81d1728612e7d98/COMPLETION.md) | 远端固定提交保留完成记录。上一轮 111 项测试、字节一致的单文件重建和 53 项 Chromium 检查通过，再用独立副本恢复核对。 | — |
| [resume_img_gen](https://github.com/ZisIsNotZis/resume_img_gen) | [8da436dd](https://github.com/ZisIsNotZis/resume_img_gen/blob/8da436dd22459284356adcf77b8d978899253397/COMPLETION.md) | 仓内关闭的三阶段交付已实跑：5 项渲染测试通过，样例 JSON 产出 HTML 及 1760×2400 PNG，样例 Markdown 经 Pandoc 3.11/WeasyPrint 产出 PDF 1.7；浏览器另从 HTML 导出单页 PDF。 | PNG 和 PDF 导出依赖相应浏览器或文档工具。 |
| [resume_improve_loop](https://github.com/ZisIsNotZis/resume_improve_loop) | [c451f33f](https://github.com/ZisIsNotZis/resume_improve_loop/blob/c451f33f2c6f909a8372e90265e45034e5e54129/COMPLETION.md) | 原范围是独立评委打分与聚合 CLI。固定提交 4 项自测通过；9 个评委通过本地合成子进程完成两轮，比分相同后在上限 3 轮之前按阈值停止。 | 验收范围为本地评审与打分流程，真人评审价值与实际录用效果未评估。 |
| [suzhou-drive](https://github.com/ZisIsNotZis/suzhou-drive) | [0b11c2d4](https://github.com/ZisIsNotZis/suzhou-drive/blob/0b11c2d4204dd248e8d0741626a163adee2ac171/COMPLETION.md) | 原范围 roadmap-v2 0.1.0。隔离复验 40 条单元测试与 Vite 构建通过；用现有 Chromium Headless Shell 的软件 WebGL 运行实际浏览器套件，26 条通过，缺命名地点样例的既知测试跳过。 | 硬件性能未纳入验收。 |
| [hfget](https://github.com/ZisIsNotZis/hfget) | [efdaabb7](https://github.com/ZisIsNotZis/hfget/blob/efdaabb71cf61c07793805edb50f137aaa353ee7/COMPLETION.md) | 10 项离线测试通过。真实 Hugging Face 干跑列出一个公开仓的完整文件选择，未下载权重。 | — |
| [goSeamCarve](https://github.com/ZisIsNotZis/goSeamCarve) | [4852759c](https://github.com/ZisIsNotZis/goSeamCarve/blob/4852759cac45dfb05369eaea395a74f5e5c63f4f/COMPLETION.md) | 离线 Go 缩图入口与五组合成场景；20 张 PNG 可逐字节重现，远端干净检出复验通过。 | — |
| [asyncs7.py](https://github.com/ZisIsNotZis/asyncs7.py) | [57d26f89](https://github.com/ZisIsNotZis/asyncs7.py/blob/57d26f898b3cbc80752c5b2fcb06835609656d08/COMPLETION.md) | 只读 Python 客户端、CLI 与本地模拟器。远端重建安装后，Python 3.11 和 3.14 各通过 23 项回环与功能测试。 | — |
| [cppTest](https://github.com/ZisIsNotZis/cppTest) | [9afd565d](https://github.com/ZisIsNotZis/cppTest/blob/9afd565d34f11693e0f5a5cac3beb97b1e2a5f5b/COMPLETION.md) | 独立的表驱动 C/C++ 单元测试运行器。干净远端检出通过 47 项自检，覆盖混合语言、退出状态和并发运行。 | — |
| [ygodoc.py](https://github.com/ZisIsNotZis/ygodoc.py) | [b2ba3980](https://github.com/ZisIsNotZis/ygodoc.py/blob/b2ba3980603dd83ce891b51186f8a853a6866cb1/COMPLETION.md) | 解析五个 ocgcore Lua 绑定文件，生成签名说明与 Sublime 补全。固定远端和 ocgcore 2d2e322d 实测输出 609 行 | 验收依据为固定的 ocgcore 版本，复现命令见项目 README。 |
| [ygoDocGen](https://github.com/ZisIsNotZis/ygoDocGen) | [96b34b7c](https://github.com/ZisIsNotZis/ygoDocGen/blob/96b34b7c2692ab22a0acb8719e005d0d9b1194d0/COMPLETION.md) | v2.0.0 从五份 ocgcore 绑定源码生成 DataEditorX Lua API 文档，保留中文注释并导出逐字段证据。两个上游版本与两种 Python 的四组测试均 41 项通过；独立远端检出复验通过。 | 三项源码不可推断的字段仍明确标为未知。 |

## 进行中与待验收

按本表从上往下推进。短且有明确验收入口的先做，每批最多 5 项。

| 仓库 | 固定版本或回执 | 已核对的交付范围与边界 | 下一步 |
|---|---|---|---|
| [monoploy11](https://github.com/ZisIsNotZis/monoploy11) | [97c5a499](https://github.com/ZisIsNotZis/monoploy11/tree/97c5a499e749c0f1345aa416e00af82276034024) | 街角生意可离线打完。定步按钮显示已锁定的步数，己方店铺停业时标明剩余天数和暂不收租的店。远端版在两个手机尺寸复验，晨光街茶铺到期恢复 2,800 租金。可选营业规则的实收仍计入结算。 [复验](https://github.com/ZisIsNotZis/monoploy11/blob/97c5a499e749c0f1345aa416e00af82276034024/docs/evidence/MOBILE-OPENING.md) | 试玩完整一局，检验能否顺畅形成计划、看到后果并调整，尤其关注短屏上最影响选择的地方。 |
| [monopoly12](https://github.com/ZisIsNotZis/monopoly12) | [f1010094](https://github.com/ZisIsNotZis/monopoly12/tree/f1010094f3a67d2bf111496f139ee26f5f69b2d5) | 塌路试玩可花 500 挖通公共路，或留断省下现钱。远端版用同一组骰子复验：两种选择到达不同格子，走挖通支线在该局净多花 218。离线单文件可重建，普通存档保留。 [复验](https://github.com/ZisIsNotZis/monopoly12/blob/f1010094f3a67d2bf111496f139ee26f5f69b2d5/game/story/road-response.md) | 从自然游玩验证路网应对是否足以支撑一段有趣的对局。 |
| [learn_draw](https://github.com/ZisIsNotZis/learn_draw) | [c0170171](https://github.com/ZisIsNotZis/learn_draw/tree/c0170171141a0f44b139a5a2e724e40225c1a61b) | 八幅原创画已发布。《末班以前》可通过具名部件调整狐狸与挡板、预览同区、另存和恢复。CPU 复跑两版 PNG/SVG 字节一致。局部可辨前后关系，尚未验证全图初见。 [复验](https://github.com/ZisIsNotZis/learn_draw/blob/c0170171141a0f44b139a5a2e724e40225c1a61b/.scratch/3586-edit/RESULT.md) | 用另一个小画面或关系检验编辑方法是否能复用。R1a 暂缓。 |
| [dojo](https://github.com/ZisIsNotZis/dojo) | [6bae2743](https://github.com/ZisIsNotZis/dojo/tree/6bae2743e0516a2c1e9c92c7a478d798d20987fd) | 讨论可逐版认可。会话后只读提炼清单展示认可快照、原话轮次和所缺依据，未认可草稿单列。远端用回环模型桩复验三版认可、同秒回改，以及重开不写库。 [复验](https://github.com/ZisIsNotZis/dojo/blob/6bae2743e0516a2c1e9c92c7a478d798d20987fd/docs/evidence/2026-11-28-m2-distill/README.md) | 验证真实模型的分类取舍和人是否能独立读懂、指出不当提议。 |
| [agentic-animation](https://github.com/ZisIsNotZis/agentic-animation) | [92678d89](https://github.com/ZisIsNotZis/agentic-animation/tree/92678d8951d0782c8c31f32bdf4efcffc26a0b8d) | 可重复的叙事动画工具，已发布多集展示。本地 CPU 复验确认道具交接的视线机制，尚待验证观众能否从成片看懂交接对象。 | GPU 与浏览器渲染验收暂缓；恢复时用同一短片核对动作与道具交接的可读性。 |
| [hypermaker](https://github.com/ZisIsNotZis/hypermaker) | [ad3c5694](https://github.com/ZisIsNotZis/hypermaker/tree/ad3c5694c3fc849285154c7510457f9d4271b302) | 画布可分别导入两张本地图并直接选中。远端完成手写字幕片、只换第二幕、重播并按字节恢复旧片。另复验有声轨的成片路径。 [复验](https://github.com/ZisIsNotZis/hypermaker/blob/ad3c5694c3fc849285154c7510457f9d4271b302/docs/evidence/local-picture-cut.md) | 验证带着已做好的影片隔天重开、继续编辑和导出。真实视觉模型发现与真人听感仍待验。 |
| [vibeos](https://github.com/ZisIsNotZis/vibeos) | [cf652952](https://github.com/ZisIsNotZis/vibeos/tree/cf652952580167a8f84a737b9fc6ac03fdef6040) | 公开里程碑声明已关闭。固定提交 75 个服务测试、构建通过；真实浏览器 4/6，App Shop 安装入口及设置标题断言失败 | 重新验收从缺少应用到发布恢复的用户流程，并对齐设置测试 |
| [TokenQR](https://github.com/ZisIsNotZis/TokenQR) | [622b4d08](https://github.com/ZisIsNotZis/TokenQR/tree/622b4d084afa9f5c07b12ba4fce9205eb165e3d1) | 仓内称最小授权 POC 已关闭；1440×1400 Chromium 中两个独立浏览器上下文跑通真实授权、密文中转及回环模拟上游对话。普通 1280×720 视口的授权确认按钮超出可点击区域。 | 确认授权弹层在普通桌面和窄屏都能完成全流程，限定到 POC。 |
| [mycar](https://github.com/ZisIsNotZis/mycar) | [09e4fec6](https://github.com/ZisIsNotZis/mycar/tree/09e4fec6952c125c64645ed1e7d2fb3d36e52863) | 远端状态文档只收口 v13，现行入口 v17（紧凑 4460）。点选真实页面八个预设并等待动画结束，车长为 4460，全部仍触发硬约束 C13，部分还触发 C16/C17/C20；默认布局按钮标 4870 mm，实测是 5000 mm。 | 对齐 v13 历史状态和 v17 当前检验，明确 4460 布局各模式还没满足的几何条件。 |
| [iba.py](https://github.com/ZisIsNotZis/iba.py) | [674aaeb7](https://github.com/ZisIsNotZis/iba.py/tree/674aaeb705519fdf9e62ab0e63c021a7a80d36a1) | README 双向入口已用合成两通道 JSON 往返真实 .dat，时戳、间隔和数据在容差内；尚未独立验证 IBA Analyzer 写入兼容及未支持的压缩格式。 | 补准确命名和输出边界，真实 Analyzer 读取至少一个自产文件并测试已知压缩拒绝。 |
| [lmlayer](https://github.com/ZisIsNotZis/lmlayer) | [6c1dfdec](https://github.com/ZisIsNotZis/lmlayer/tree/6c1dfdecb73bee569a7f928832527f78aa753e93) | 公开代理接入、RAG、配额调度和工具过程，状态文档记录功能版本多年未核，以公开指令实际通过导入 smoke，确认 chat/completions、embeddings、rerank 三条路由；未接数据库与推理实例。 | 先验证普通请求、数据来源和每种配额边界，再验收完整接口。 |
| [greenlet_fiber](https://github.com/ZisIsNotZis/greenlet_fiber) | [a72519a4](https://github.com/ZisIsNotZis/greenlet_fiber/tree/a72519a4b0cde50f63b0339632fce166ffdbbed6) | 在独立环境执行 README 协作调度的两个 fiber，均按顺序输出；README 对抢占/切换明确提示仍需严谨测试、可能导致解释器崩溃。 | 以协作路径为最低验收范围，明确不安全抢占的支持边界。 |
| [cppBorrow](https://github.com/ZisIsNotZis/cppBorrow) | [01f9707f](https://github.com/ZisIsNotZis/cppBorrow/tree/01f9707f55430c9a3b87bf06c631a26c9fd26dcb) | 实验性 C++ owner/borrow wrapper；尚未成为文档标榜的完整借用契约。 | 补可编译入口，验证正常借用、转移、空状态和生命周期的契约。 |
| [cppChan](https://github.com/ZisIsNotZis/cppChan) | [c89c800a](https://github.com/ZisIsNotZis/cppChan/tree/c89c800a7719c9aa660dc1f9f8124719adc9ccdd) | 试验性 C++ channel 与 pipeline；README 明称 pipeline 设计未定。 | 先为有界 channel 的传递和收尾提供可重复回执，再决定 pipeline 范围。 |
| [danmaku](https://github.com/ZisIsNotZis/danmaku) | [163502f4](https://github.com/ZisIsNotZis/danmaku/tree/163502f4639f60186b4a12b81e7e1c0bbf46176d) | X11 弹幕引擎已提供演示，仍需独立复验当前目标入口。 | 在隔离 X11 下验证透明、置顶、点击穿透行为和引擎时间线，明确 Wayland 范围。 |
| [ydkskill](https://github.com/ZisIsNotZis/ydkskill) | [69455991](https://github.com/ZisIsNotZis/ydkskill/tree/69455991d7fd49e8a253a7e2a10f2084758e3c19) | 卡组构建和分析知识技能树，包含数据与验证工作说明 | 取公开样例从起始卡组到可核验分析，明确与 ygoskill 的范围 |
| [ygoskill](https://github.com/ZisIsNotZis/ygoskill) | [12089803](https://github.com/ZisIsNotZis/ygoskill/tree/120898038d8d03dbf8dd88900e9397c279882064) | Yu-Gi-Oh! 和 YGOPro 技能树，新增卡组与历史材料，不同场景证据仍不齐 | 验收具体卡组推演和证据来源，记录可交付子范围 |
| [ygocli](https://github.com/ZisIsNotZis/ygocli) | [9ae2adf9](https://github.com/ZisIsNotZis/ygocli/tree/9ae2adf9722a363f20c15a23e6320eedc2f9f4d5) | C++ 文本决斗程序、服务器和 MCP，最新提交加入新的 headless 层；未从干净检出验收完整对局 | 记录可复现依赖后实跑一局 |
| [ygopromcp](https://github.com/ZisIsNotZis/ygopromcp) | [a05d4673](https://github.com/ZisIsNotZis/ygopromcp/tree/a05d4673145cf7d1d8cf9d70f47eb0d7ce6fe570) | 有自己的 MCP 控制面，README 仍有未验的回放与异常场景 | 以可恢复环境验收从连接到完成对局，厘清与 ygocli 的取舍 |
| [ygoimgen.sh](https://github.com/ZisIsNotZis/ygoimgen.sh) | [9cd8afa5](https://github.com/ZisIsNotZis/ygoimgen.sh/tree/9cd8afa5250712d05dd624ddd0fc7a6a4af24ec7) | 有 ImageMagick 渲染脚本和样例资源，README 声称提供 cards.cdb，但远端树没有它 | 提供合成最小卡数据或明确输入契约，验证实际输出 |
| [lmchk](https://github.com/ZisIsNotZis/lmchk) | [03153eef](https://github.com/ZisIsNotZis/lmchk/tree/03153eefeed5b2500e4f172f72c48bb0d55fc0df) | README 说明普通与流式代码评阅、源文件传输和结构化输出。远端干净检出实测内置 JSON Schema 转 BNF。完整评阅流程待验。 | 补本地模拟供应商，用仓内样例检查普通与流式路径的请求、结果和退出状态。 |
| [send_teams](https://github.com/ZisIsNotZis/send_teams) | [c2c4d0bd](https://github.com/ZisIsNotZis/send_teams/tree/c2c4d0bd430e67fbc19f351535046bfc8ac65e31) | 树包含多个 Teams 实验路径及截图。README 依赖现有机器的已登录状态，缺隔离结果和跨环境的安全验证。没有实际发送消息或读取账户材料。 | 先取得本地模拟入口与明确授权边界，人工确认后的对外发送另行验收。 |
| [agentworld](https://github.com/ZisIsNotZis/agentworld) | [00de40fd](https://github.com/ZisIsNotZis/agentworld/tree/00de40fd6e61b6e548b68ff729893bcf323f89d6) | 有成本约束的文明演化模拟。 | 用相同世界种子复验演化规则与成本收益。 |
| [aps](https://github.com/ZisIsNotZis/aps) | [3cf5b87c](https://github.com/ZisIsNotZis/aps/tree/3cf5b87c6e2007f5e08aec47415c19a2cc8089f0) | M1 工作台历史关闭，但这次未拿到可复核的完整求解入口回执，正式全流程先留待验收。 | 在有锁定依赖的环境跑一条代表性工单，从建模到甘特验收；核定完成的是关闭的工作台范围，避免重做已交付内容。 |
| [auto_maintain_bench](https://github.com/ZisIsNotZis/auto_maintain_bench) | [e6d8d0ac](https://github.com/ZisIsNotZis/auto_maintain_bench/tree/e6d8d0aca9617445089fdb2f8059b6f4cf394828) | 远端已关闭一轮 172 场景研究，当前重新推进可无人值守的维护能力。 | 把当前独有本地可发布成果先复验后入远端，再评估代表性服务维护切片。 |
| [autofe](https://github.com/ZisIsNotZis/autofe) | [05599052](https://github.com/ZisIsNotZis/autofe/tree/0559905221bd9d07da04abc11f8f090772514ed5) | 已发布意图渲染的可审阅画廊，完整业务呈现接口仍在做。 | 从一个源证据及声明生成完整用户流程并将验收与交付页面绑定。 |
| [backseat](https://github.com/ZisIsNotZis/backseat) | [596483ab](https://github.com/ZisIsNotZis/backseat/tree/596483abe13a3c08cabbab096c945013535d68d3) | 本地评论助手，评审须限于透明同意、可追溯、低负担的用户体验。 | 用受控、用户已同意的本地素材验证可追溯性和恰当干预。 |
| [dinoseg](https://github.com/ZisIsNotZis/dinoseg) | [41269cbc](https://github.com/ZisIsNotZis/dinoseg/tree/41269cbc545978e661cf07138bd0cdcf8f506976) | 用冻结 DINO 特征交互分割工业样本的研究工具。 | 用一组公开小图跑点击分割流程并核对可复现产物。 |
| [dinov23.cpp.py](https://github.com/ZisIsNotZis/dinov23.cpp.py) | [ff23ab0f](https://github.com/ZisIsNotZis/dinov23.cpp.py/tree/ff23ab0f0a92864cbff715d034d1d208cce903f5) | 依赖 ggml 的 DINOv2/v3 Python 推理，用户确认 v3 输出有疑。 | 以固定小图和小权重对照官方输出，定位 v3 数值偏离。 |
| [expyssion](https://github.com/ZisIsNotZis/expyssion) | [5871dcae](https://github.com/ZisIsNotZis/expyssion/tree/5871dcae59b49197e33a8ab04222e905b4dc235a) | v1 规格与运行时已交付；清洁检出按 README 94 过 1 失败，NumPy 未声明。临时补依赖后 95/95，expy Fibonacci 输出 55。 | 修复可重跑的 v1 依赖与推荐命令；Python 向后兼容仍按用户既定暂缓。 |
| [fat_kakeya_needle](https://github.com/ZisIsNotZis/fat_kakeya_needle) | [28cec3a5](https://github.com/ZisIsNotZis/fat_kakeya_needle/tree/28cec3a5235fb8101bfd128bcbba8d9670bb7be5) | v1 数值里程碑后已恢复证书优化。公开定位为精确有理上界与候选族；一般渐近结论未得。 | 把运行证书所需源码与证据移出仅本地产物，独立复跑并区分有限证书与渐近结论。 |
| [flashdb](https://github.com/ZisIsNotZis/flashdb) | [f7a77061](https://github.com/ZisIsNotZis/flashdb/tree/f7a77061c2ed242769f08fb61cba5c277fd0e31a) | 公开代码和 README 有单机业务请求与从工作负载学习布局的原型；单机效益对照未达标，真实发布来源链仍待验。 | 独立重建两个平台的交付并核对完整业务事务与布局收益边界。 |
| [gu](https://github.com/ZisIsNotZis/gu) | [dec67ebb](https://github.com/ZisIsNotZis/gu/tree/dec67ebbdf461c2bb9edbc9d11d10d63b4579665) | 古早卡牌游戏设计，README 明示核心、卡片类与 UI 未完成，入库的是效果草稿和样例牌。 | 先验证最小回合、一个效果和明确的输入输出，再审视是否继续。 |
| [helpagent](https://github.com/ZisIsNotZis/helpagent) | [7a73c48c](https://github.com/ZisIsNotZis/helpagent/tree/7a73c48cca53b6f7b9b06e9d89d13ca47bff26fb) | 已关闭公开测量轮，从干净远端树复跑 reproduce.py 与引文审计，506 解引用、0 缺失。Vibe 的后续小模型工作流目标仍开放。 | 封存已结束研究结论，以独立协议和合适对照验收下一项收益。 |
| [lm_paper_test](https://github.com/ZisIsNotZis/lm_paper_test) | [2653c2d9](https://github.com/ZisIsNotZis/lm_paper_test/tree/2653c2d951da7e17d0e58307b1286b8659ec1d2f) | 论文、PDF 与图存在；没有足够的实验脚本、数据和机器可读元数据可验证指标。 | 跑通一项图表从数据到稿件的可重现结果。 |
| [murderMysteryGame](https://github.com/ZisIsNotZis/murderMysteryGame) | [3a991e81](https://github.com/ZisIsNotZis/murderMysteryGame/tree/3a991e814b49c4fd848685e91aaef5e67637b58a) | 仓库有三部作品，过往《寿宴》已归档。实跑第三部 28 Markdown/64 链接/四类印件和第二部 23 Markdown/42 链接的静态验收，皆无失败；真人场次仍未验。 | 优先安排一次真实主持/六玩家体验，量出卡点和实际时长，再收口。 |
| [nomos](https://github.com/ZisIsNotZis/nomos) | [c01a97bd](https://github.com/ZisIsNotZis/nomos/tree/c01a97bdb8985e0c6c0e66fc450dab4b3d0753a7) | 公开实验已有定量结果。独立运行判分自测，6 个提取用例、30 个校验用例和 5 次流水线用例通过。路线图仍未采纳新适配器，未完成政策收益与能力退化的联合验收。 | 区分策略内化与照抄，锁定对通用能力代价的联合验收。 |
| [pathlm](https://github.com/ZisIsNotZis/pathlm) | [f37c90b5](https://github.com/ZisIsNotZis/pathlm/tree/f37c90b571e8b68a9ac95cf11dfbec3ec10f34e1) | 研究树已公开，目录指向 46 个项目定义和共享验收流程。核心范围覆盖模型计算放置与多轴实验，通过固定提交的 build_catalog --check 和 check_docs --check；46 项研究目录一致，506 个文档的 10006 处引用没有违规。最新提交的论文初稿仍写着待复核。 | 按每个实验卡推进可重复测试，保留成本和结果边界。 |
| [socraticMirror](https://github.com/ZisIsNotZis/socraticMirror) | [a132586b](https://github.com/ZisIsNotZis/socraticMirror/tree/a132586bd235918deae6ccfb37cbdb6f242ed2ae) | 固定提交的 Python 引擎 36 项测试通过。README 和路线图说明真人知识地图价值仍在验收。 | 推进真实会话的自主性与洞察，不把引擎测通过等同真人价值。 |
| [sys_gal](https://github.com/ZisIsNotZis/sys_gal) | [2e84584f](https://github.com/ZisIsNotZis/sys_gal/tree/2e84584f2854a3cd21ce616965b96e1d7ef1b13e) | 远端 v5 strict lint 通过并列出 9 个概念覆盖待补；4 个确定性回放测试通过。路线仍有三天责任追踪与十二天叙事长弧。 | 用独立轨迹验收角色选择、感知约束和长弧可重放。 |
| [tiny-llm-eval-factors](https://github.com/ZisIsNotZis/tiny-llm-eval-factors)（`local_lm_research`） | [fd568179](https://github.com/ZisIsNotZis/tiny-llm-eval-factors/tree/fd568179a60dfb6b9d82d999a22c007da62b9b32) | 固定提交跑路由检查，77/77 个引用及 27/27 个路径解析。不仅已有首版报告，STATUS 还列出综合效应账与 GPU 阻塞未测范围。 | 继续不需 GPU 的 synth 对照，并保持未测项与实证分开。 |
| [ydkgen](https://github.com/ZisIsNotZis/ydkgen) | [70d2de36](https://github.com/ZisIsNotZis/ydkgen/tree/70d2de36ceff4bf729e77ed46c57ff52f4ab86bd) | PyTorch 卡组生成与训练脚本；README 依赖外部模型和卡表，树无可复现测量及发布权重 | 恢复有出处的权重或最小离线端到端质量对照 |

## 暂缓的未完成项目


| 仓库 | 固定版本或回执 | 已核对的交付范围与边界 | 下一步 |
|---|---|---|---|
| [huaqiang_game](https://github.com/ZisIsNotZis/huaqiang_game) | [906cf1e5](https://github.com/ZisIsNotZis/huaqiang_game/tree/906cf1e544d5a1e3529f09f0562624ef7cb0b401) | README 明确无限期暂停，Phase 4 浏览器灰盒和规则原型存在，不能表述为制作完成。 | 保留暂停事实；复活前先验收「观察→准备→后果」的可玩体验。 |
| [iron-meridian](https://github.com/ZisIsNotZis/iron-meridian) | [21541c9c](https://github.com/ZisIsNotZis/iron-meridian/tree/21541c9c0a8e86111e6f7023b7d3215a61e30704) | 公开交付可玩的 V1，明确暂停后续；独立跑过确定性模拟、自带内容核对及生产构建，并在离线网络隔离的 Chromium 中启动战斗和重启画布，无页面异常。 | 保留这个已交付切片；更广目标不进入自动推进，等恢复决定。 |
| [sys_gal_rt](https://github.com/ZisIsNotZis/sys_gal_rt) | [4600a12d](https://github.com/ZisIsNotZis/sys_gal_rt/tree/4600a12deb5e2047ffeb5c520e2ebf398a6e4a87) | 2026-09-29 明确暂停。11 条树记录为文档和图标，首个故事设计保留，实时引擎没有代码。 | 等待 sys_gal 因果核心，再实现并验收实时引擎。项目本身未完成。 |

## 历史归档与已被替代


| 仓库 | 固定版本或回执 | 已核对的交付范围与边界 | 下一步 |
|---|---|---|---|
| [agent-policy](https://github.com/ZisIsNotZis/agent-policy) | [4d406582](https://github.com/ZisIsNotZis/agent-policy/tree/4d406582a85fad85b2d048726fb44b9589a5d6c6) | 独立角色规范，已由 Praxis / Praxis2 接续。 | — |
| [beam](https://github.com/ZisIsNotZis/beam) | [774ebe02](https://github.com/ZisIsNotZis/beam/tree/774ebe029757046a0f878c886a2f4e169edb39be) | llama.cpp 八个 beam-search 手稿归档。 | — |
| [causalmlp](https://github.com/ZisIsNotZis/causalmlp) | [2c66cba3](https://github.com/ZisIsNotZis/causalmlp/tree/2c66cba3fa610f8e7be8af95c0c30324ba6d9118) | 有公开结果的 PyTorch 研究归档。 | — |
| [cept](https://github.com/ZisIsNotZis/cept) | [eda1c58f](https://github.com/ZisIsNotZis/cept/tree/eda1c58f975ca3be24a5a470cae4111afdbdb686) | 历史语言/编译器探索，无可支持的现行产品。 | — |
| [cuda](https://github.com/ZisIsNotZis/cuda) | [5a4c13d6](https://github.com/ZisIsNotZis/cuda/tree/5a4c13d6ec1dcf09ca79cc5bf82e570372965123) | CUDA tensor-core/warp 测量实验归档。 | — |
| [cvorat](https://github.com/ZisIsNotZis/cvorat) | [322d69ba](https://github.com/ZisIsNotZis/cvorat/tree/322d69baefc7ba2c86775751689400deeb7f39d3) | 字节级语言模型结构实验归档。 | — |
| [cz_bert](https://github.com/ZisIsNotZis/cz_bert) | [f7eed5e5](https://github.com/ZisIsNotZis/cz_bert/tree/f7eed5e5be2da86b2885760f5d50aa5ed5110c88) | 2019–2020 弃用的深度学习笔记，含 Mixer 与注意力结构、内存映射数据内核和 fastai CNN。 | — |
| [cz_einn](https://github.com/ZisIsNotZis/cz_einn) | [2865d041](https://github.com/ZisIsNotZis/cz_einn/tree/2865d0418c43290d3b9dc914c450d3251fa216ff) | 2020 EINN 中文字符建模 notebook。 | — |
| [cz_noidea](https://github.com/ZisIsNotZis/cz_noidea) | [3272f57e](https://github.com/ZisIsNotZis/cz_noidea/tree/3272f57ed6261b58147418d9ea4de00556008475) | 2020–2021 弃用的 Python 试验笔记，含 asyncio 与套接字吞吐、稀疏数组和 NumPy、Numba、PyTorch。 | — |
| [cznn](https://github.com/ZisIsNotZis/cznn) | [6b05a2e4](https://github.com/ZisIsNotZis/cznn/tree/6b05a2e40c443c71be00ee4c71d0983b7873f8fb) | 三份分叉尚未合并的研究神经网络构件。 | — |
| [dcg](https://github.com/ZisIsNotZis/dcg) | [db9675fc](https://github.com/ZisIsNotZis/dcg/tree/db9675fc311643c8fec6adedd6b89e7b5823f743) | DIY 游戏王卡片数据和脚本归档，无独立应用。 | — |
| [dino.py](https://github.com/ZisIsNotZis/dino.py) | [f080369a](https://github.com/ZisIsNotZis/dino.py/tree/f080369a8e3d8e635deea246e2928fb51c68f1a5) | DINO ggml 推理多路径的实验参考实现。 | — |
| [disk](https://github.com/ZisIsNotZis/disk) | [b10a43cd](https://github.com/ZisIsNotZis/disk/tree/b10a43cd26923655165fea2b9fd156d07279b738) | 已失去实物台架的闭环热控研究快照。 | — |
| [fring](https://github.com/ZisIsNotZis/fring) | [542901ae](https://github.com/ZisIsNotZis/fring/tree/542901ae7a394398f14c2189f1eecc54cc64172c) | 三代 Python io_uring 实验及压测脚本，README 明确归档、无测试和包。 | 保留实现与历史说明，无待续产品承诺。 |
| [ghtest](https://github.com/ZisIsNotZis/ghtest) | [e4e4aa29](https://github.com/ZisIsNotZis/ghtest/tree/e4e4aa2989bc062977a964b35f61c3691fb81fb7) | 明确为测试 GitHub 工作流和元数据的文档样本；独立 Git clone 验证目录。 | 保留测试夹具。 |
| [grammar](https://github.com/ZisIsNotZis/grammar) | [107e710e](https://github.com/ZisIsNotZis/grammar/tree/107e710eb4f64e2dfc8617a849d1808f4aeb3921) | 已声明 notebook 归档；原始训练路径依赖仓外私有语料，暂无复现栈或维护承诺。 | 保留笔记与方法，列清私有语料缺口。 |
| [http_mock](https://github.com/ZisIsNotZis/http_mock) | [953fb149](https://github.com/ZisIsNotZis/http_mock/tree/953fb14944cbda80b52d5c2f8b43fb7f917121d4) | 明确归档的 GRU 模拟 HTTP/KV 实验；无已保存结果、评估成绩或依赖表。 | 保留 notebooks；后续研究须另定可复验目标。 |
| [ideas](https://github.com/ZisIsNotZis/ideas) | [c41c3b1f](https://github.com/ZisIsNotZis/ideas/tree/c41c3b1f4e0239a3408d07ec6f2a1ecb0ac29b7b) | 明确封存的想法笔记，每条作为机制或证伪建议，不声称已实现。 | 作为灵感索引保留。 |
| [io_uring-echo-server](https://github.com/ZisIsNotZis/io_uring-echo-server) | [ab483562](https://github.com/ZisIsNotZis/io_uring-echo-server/tree/ab483562a39de8ce1e95c4ef087b79787ddb2eb3) | C 网络基准草图。README 和简介说明接收连接后发送固定内容、零字节吞吐与阻塞式对照，保留原构建缺口。 | — |
| [jpi.fe](https://github.com/ZisIsNotZis/jpi.fe) | [a4959581](https://github.com/ZisIsNotZis/jpi.fe/tree/a495958106eb6d629579ae69ec682749232b465e) | 明确归档的 Vue JSON 网格原型，后端缺席，README 无待续路线。 | 保留前端代码和后端缺口。 |
| [knowledge_net](https://github.com/ZisIsNotZis/knowledge_net) | [c5ebd6c4](https://github.com/ZisIsNotZis/knowledge_net/tree/c5ebd6c49300c7082f4329311eaac98feb3c2889) | 已冻结的记忆槽研究草图，源和笔记在，未发布结果或包。 | 保留方法与原始笔记。 |
| [misc](https://github.com/ZisIsNotZis/misc) | [5473f0cb](https://github.com/ZisIsNotZis/misc/tree/5473f0cb66c5038d816cebfbf172a0c8e33bc775) | 明确为一次性脚本与研究笔记抽屉，没有共同入口或发布范围。 | 按档案保留，不把散件纳入一个虚构产品验收。 |
| [myideaplugin](https://github.com/ZisIsNotZis/myideaplugin) | [358bc1fe](https://github.com/ZisIsNotZis/myideaplugin/tree/358bc1fe78de25b30801dec88e4883cc86fa8c12) | IntelliJ 插件模板归档，README 链接到项目服务所用的插件清单、Gradle 配置和样例测试。 | — |
| [myminio](https://github.com/ZisIsNotZis/myminio) | [ef836607](https://github.com/ZisIsNotZis/myminio/tree/ef83660726e25ea2c913a8b78e254efc28153750) | 首代存储实验明确归档，保留纠删码验证入口与分片、版本及重建源码；Flask 包装只做了一部分。 | 保留历史来源和 S3 兼容性边界。 |
| [myminio2](https://github.com/ZisIsNotZis/myminio2) | [128d9cc3](https://github.com/ZisIsNotZis/myminio2/tree/128d9cc375103aa047b459d868376cb008fc2b40) | 归档 README 明确说明当前快照无法直接启动，保留手写 HTTP 服务器和三后端 XOR 网关源码，且无测试套件或发布清单。 | 保留说明和实验材料。 |
| [myygo](https://github.com/ZisIsNotZis/myygo) | [e8356864](https://github.com/ZisIsNotZis/myygo/tree/e83568648cad4b6d9e006f372f81057fdb617db1) | 明确归档的卡片效果 DSL。两个版本包含 11 张卡的钩子数据，依赖未包含的宿主。 | 保留样例与草图。 |
| [myzcopy](https://github.com/ZisIsNotZis/myzcopy) | [3cea27eb](https://github.com/ZisIsNotZis/myzcopy/tree/3cea27eb69eabfb6fc390a923c22b94ce42e25f6) | 归档形态保留单 C 文件的 copy_file_range/splice、RAID 与重建命令及 Linux 编译入口。没有现行支持或发布验收目标。 | 保留 Linux 工具链和存储实验边界。 |
| [neuronloop](https://github.com/ZisIsNotZis/neuronloop) | [32518901](https://github.com/ZisIsNotZis/neuronloop/tree/325189012b220f9fb48cdccaa9359ca6e9ce7f1e) | 循环式神经训练实验保存在 notebook；README 明确没有软件入口、CI 或完整可复现训练条件。 | 保存可解释的训练快照。 |
| [nn](https://github.com/ZisIsNotZis/nn) | [c3a96afa](https://github.com/ZisIsNotZis/nn/tree/c3a96afa4dbfd7b123322346b70170d636253a3a) | 说明和树均为 2021–2022 PyTorch 学习日志，有 attention、训练及 PageRank 笔记，不提供包、入口或统一测试。 | 按研究笔记存档。 |
| [retnet](https://github.com/ZisIsNotZis/retnet) | [beceb2bd](https://github.com/ZisIsNotZis/retnet/tree/beceb2bddd3c2753002e859495bc99f90a913bf0) | 研究归档展示 byte-level retention layer、模型和多个 notebook；README 点到了缺失的语料、环境记录和完整训练可重复性。 | 保留原模型探索与数据边界。 |
| [ringsvr](https://github.com/ZisIsNotZis/ringsvr) | [c753990b](https://github.com/ZisIsNotZis/ringsvr/tree/c753990b044a630f92f68af9262d5580cb1667f0) | README 明确是历史 io_uring 文件服务研究，CMake 和 C 实现可见，生产强化不属于记录范围。 | 保持档案入口。 |
| [seq_autoenc](https://github.com/ZisIsNotZis/seq_autoenc) | [dd7c7748](https://github.com/ZisIsNotZis/seq_autoenc/tree/dd7c7748470dd2024d8939123ea0fdd80c1ab145) | 多尺度自编码器和 n-gram/suffix array 比较仍可读；私有原始和派生语料及数值日志没有公开，不能复训原实验。 | 保留历时性研究数据与边界。 |
| [sp](https://github.com/ZisIsNotZis/sp) | [4b49e187](https://github.com/ZisIsNotZis/sp/tree/4b49e187f5525d582d0ba034cfa69f2687463745) | 2019 年的 C 序列预测原型。README 列出两个共享库、Python 入口、样例 notebook 和复现边界。 | — |
| [tok](https://github.com/ZisIsNotZis/tok) | [1532dc39](https://github.com/ZisIsNotZis/tok/tree/1532dc399383580c53485788a8745041d323be33) | 保留多个版本的 n-gram tokeniser 研究与备忘。README 指名 tok5.cpp 仍是中途版本且不能编译；没有统一发布或测试。 | 保留算法历史，继续研究前另起验收目标。 |
| [treui](https://github.com/ZisIsNotZis/treui) | [5d176867](https://github.com/ZisIsNotZis/treui/tree/5d176867a794aac18f5863ce7445c48694662668) | 可拖动分叉的图式对话原型；README 明确归档 | 保留原型与构建说明 |
| [uv](https://github.com/ZisIsNotZis/uv) | [58fd6f5c](https://github.com/ZisIsNotZis/uv/tree/58fd6f5c0068fe56ca42ce14d855573ff24b5ba5) | 相同 HTTP 响应在多种 Python/C 事件循环的实验；README 明确归档 | 保留基准与环境边界 |
| [wafer-thermal-calibration](https://github.com/ZisIsNotZis/wafer-thermal-calibration) | [0912389e](https://github.com/ZisIsNotZis/wafer-thermal-calibration/tree/0912389e61505da7f48bccf351ed0ae7b6227f7a) | 47 路加热、34 路红外硬件数据；采集已完成，Jacobian 控制实验未收尾，README 明确归档 | 保留历史数据与 disk 的继承关系 |
| [ygo](https://github.com/ZisIsNotZis/ygo) | [aa8ca9a4](https://github.com/ZisIsNotZis/ygo/tree/aa8ca9a4c5855ddb0c3125ef39a0fb26539c3498) | 历史卡图、裁剪、向量模型与卡组研究，以 notebooks/脚本保留多条独立实验 | 仍要推进的研究已由具体 DINO 和卡组仓库分别承担 |

## 上游派生、参考与空仓


| 仓库 | 固定版本或回执 | 已核对的交付范围与边界 | 下一步 |
|---|---|---|---|
| [bark.cpp](https://github.com/ZisIsNotZis/bark.cpp) | [eabe3d5f](https://github.com/ZisIsNotZis/bark.cpp/tree/eabe3d5fb09b98500cc04bb3500afa6c730d0632) | 外部 C++ Bark 推理仓库的 fork，未发现所有者已声明的独立交付。 | — |
| [DataEditorX](https://github.com/ZisIsNotZis/DataEditorX) | [44297061](https://github.com/ZisIsNotZis/DataEditorX/tree/442970619ba0e4c08bded9f803ae9360706e6269) | 外部 YGOPro 卡片数据库编辑器 fork，使用上游的产品声明。 | — |
| [dinov2.cpp](https://github.com/ZisIsNotZis/dinov2.cpp) | [2d522b26](https://github.com/ZisIsNotZis/dinov2.cpp/tree/2d522b2636248d2586efdb8bbc30f47b33c11ed7) | 外部 lavaman131 DINOv2 C++ 参考实现的 fork。 | — |
| [drive](https://github.com/ZisIsNotZis/drive) | 空仓，无提交 | 旧同名远端无默认分支对象。 | — |
| [ggml-python](https://github.com/ZisIsNotZis/ggml-python) | [5fecd991](https://github.com/ZisIsNotZis/ggml-python/tree/5fecd991f80bc89f49d2d302c56e3e91f3a90f32) | 公开派生仓库，README 和构建指向上游 ggml Python bindings；对比上游有 4 个独有提交、落后 79，代表有 tensor struct 修正，未形成独立验收范围。 | 按上游分支作参考，只有可核实独有目标时纳入推进。 |
| [imagen-pytorch](https://github.com/ZisIsNotZis/imagen-pytorch) | [05448bc4](https://github.com/ZisIsNotZis/imagen-pytorch/tree/05448bc479f588377d2767e716deae1663e2a10f) | 公开上游派生，包含上游 Imagen 实现；对比上游 0 个独有提交、落后 179。 | 保留为上游参考，独有目标出现后再定验收。 |
| [InfluxDBStudio](https://github.com/ZisIsNotZis/InfluxDBStudio) | [fcd67c29](https://github.com/ZisIsNotZis/InfluxDBStudio/tree/fcd67c299d346216d13c1f1acae94bfd6e1af834) | 公开派生的 InfluxDB Studio C# 客户端，对比上游默认分支为完全相同。 | 保留为上游参考。 |
| [llama-cpp-python](https://github.com/ZisIsNotZis/llama-cpp-python) | [c37132ba](https://github.com/ZisIsNotZis/llama-cpp-python/tree/c37132bac860fcc333255c36313f89c4f49d4c8d) | 公开派生的上游 Python bindings 和构建；对比上游 0 个独有提交、落后 174。 | 作为上游源码参考保留。 |
| [llama.cpp](https://github.com/ZisIsNotZis/llama.cpp) | [429dc8d2](https://github.com/ZisIsNotZis/llama.cpp/tree/429dc8d2fbf89a6f32d66599503ea00e75b32f3f) | 公开自用上游派生，快照对比为 7 个独有提交、落后 2053；专属实时 dashboard 的终端和文本输出是有意义的差异，未独立验收跨平台。 | 索引记录 fork 差异；若独立启用该 dashboard，先复跑 README 实例和测试。 |
| [omniserve](https://github.com/ZisIsNotZis/omniserve) | [02b2925a](https://github.com/ZisIsNotZis/omniserve/tree/02b2925aa6fa3b92b06316a1524b7f38922cd9c8) | GitHub 标为 fork。仓内 README 和目录是上游 QServe/LServe 研究及 CUDA 构建工具，没有此作品集自有的新交付合同。 | 保留上游出处和研究概览。 |
| [thcupd](https://github.com/ZisIsNotZis/thcupd) | [0d2df05e](https://github.com/ZisIsNotZis/thcupd/tree/0d2df05e51aad824ea5db9ddb6bedd3027a1d1e3) | GitHub 外部 fork（上游 purerosefallen/thcupd）；树由卡片/规则扩展、脚本、图片和更新材料组成，无独立 README 或自有验收目标。 | 索引保留第三方来源，README 如补应清楚注明 fork 与范围。 |
| [TTS.cpp](https://github.com/ZisIsNotZis/TTS.cpp) | [c04c77ab](https://github.com/ZisIsNotZis/TTS.cpp/tree/c04c77ab7575adf48c8af5a16e3bea179cba7dbb) | 上游 TTS C++ 派生镜像；树含上游示例与 CMake | 保留上游镜像 |
| [vision.cpp](https://github.com/ZisIsNotZis/vision.cpp) | [13d8889c](https://github.com/ZisIsNotZis/vision.cpp/tree/13d8889cadabd790f6943ee39f6ca55f4bffd492) | 视觉推理上游派生，保留一次编译修整 | 与自有 DINO 项目独立审阅 |
| [XNOR-popcount-GEMM-PyTorch-CPU-CUDA](https://github.com/ZisIsNotZis/XNOR-popcount-GEMM-PyTorch-CPU-CUDA) | [7ac12caa](https://github.com/ZisIsNotZis/XNOR-popcount-GEMM-PyTorch-CPU-CUDA/tree/7ac12caa75a0ef1adef48a42a04961e6d132b041) | XNOR GEMM 上游实验镜像，含 CPU/CUDA 源包 | 保留上游参考 |
| [ygopro-core](https://github.com/ZisIsNotZis/ygopro-core) | [2d2e322d](https://github.com/ZisIsNotZis/ygopro-core/tree/2d2e322d68c5ea7b858669605cb6dd672b0a939b) | 上游 Lua/规则核心镜像，近期为上游 CI pin | 作为决斗项目依赖保存 |
| [ygopro-scripts](https://github.com/ZisIsNotZis/ygopro-scripts) | [acc243ea](https://github.com/ZisIsNotZis/ygopro-scripts/tree/acc243ea65d4092b851e8aaa57dc1f461456e30f) | 上游规则脚本镜像，树包含 7600 路径且无根 README | 作为上游依赖保存 |
