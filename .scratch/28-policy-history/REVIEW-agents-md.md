I have all the evidence I need. Writing the report.

---

# 评审报告：AGENTS.md 作为 agent 操作规则

评审对象（版本锁定，只读，未做任何改动）
- `/home/z/vibe/AGENTS.md`，245 行，md5 `37b6aefaf45941502b3fccce2639806f`（哈希未独立核验，见"未能验证"）
- 真相源 `/home/z/vibe/AGENTS.yaml`（669 行，中英双语），md5 `402ab36d9c3f400cbb792d7412295a85`
- 渲染器 `/home/z/vibe/scripts/render_policy.py`，Schema `/home/z/vibe/AGENTS.schema.yaml`
- 判据来源：`/home/z/.agents/skills/writing-for-agents/SKILL.md`（no-op 判据、leading word、negation、单一真相源、co-location、disclosure/sprawl）、`SKILL-MECHANICS.md`、以及**文件自己的规则**（L184 cut_repetition、L175 one_home_per_fact、L176 structured_source、L195 policy_change_record、L76 一名一物）和 schema 对 `@` 的定义（`AGENTS.schema.yaml:5-8`："次要因果在正文里用 @key 内联，仅作注意力连接，不参与程序解析"）。

统计基线（后文引用）
- 顶层 5 个：`intent` `resources` `attention` `change` `proof`；非叶子 33 个、叶子 178 条、内容行 244（含 33 条 `_base`），无空行无注释。
- 带 `@` 记号的**行 55 条**（叶子 43/178、`_base` 12/33）；`@` 的目标**只有 5 个顶层键**（intent/resources/attention/change/proof），无死引用。
- 隐藏键只有 1 个：`attention.emphasis_by_evidence*`（`AGENTS.yaml:456`）。它正是本次第 5 项（no-op）的**文件自带标准**："应只强调'模型不会自发做对'的部分"。

---

## 结论

这份文件在同类 AGENTS.md 里属于**可执行度很高**的一类：178 条叶子几乎每条都带动作、边界或判据（"至少两个方案"、"五到十条"、"跑范围内的 `git diff --check`"、"baseline-to-worktree diff 与 hash"），树形与 `_base` 语义严格，`@` 无死引用，渲染与 SSOT 在静态核对下一致。**但作为"每次会话都会读到的操作规则"，有 2 处阻塞缺陷必须先修**：一个未定义术语承担了评审门的豁免，一个动作指向不存在的"家"。此外有一批非阻塞缺陷，其中三类值得整体处理：**对立极性**（同一件事在不同段被写成相反动作）、**三处一意**（同一规则在三个地方各写一遍，正好是 leading word 该收的地方）、**政策自身 SSOT 不满足政策自己下的强制条款**。

---

## 阻塞缺陷

### B1（阻塞）未定义的"急切"阶段承担了评审门的豁免
- 位置：AGENTS.md L182（`change.docs.write_rules.all_phases`）、L230（`proof.execution.review.eager_exempt_from_review`）；树的阶段定义只有 L120 `discuss` / L130 `advance`。
- 证据：
  - L182："SSOT 在所有阶段都执行，**急切阶段**也不免除。"
  - L230："**急切工作**除非用户要求，不做独立评审。@resources"
  - 全文出现"急切"仅这 2 处（grep 计数 2），`attention.phases` 下没有该键，也没有任何一条定义它。
- 违反判据：第 8 项（SMART——不可判定）与第 9 项（自洽性）。这是**双输**的：若"急切"是自造术语，它没有定义就承担判定；若它来自运行时/系统提示（例如某种 eager 模式），则与本文件 L177 `policy_standalone`"政策不依赖模型平台、可选工具或假设的运行时保证"直接冲突，而且没有给出任何指针让 agent 去查。
- 反例（会造成错误动作）：一个推进期的 worker 读到 L230，只要把"用户催得紧"读成"急切"，就能跳过 L227 要求的"每个工作包都要有对应的全新独立评审"，而 L231 又禁止把未验证的验收当 PASS——两条正相反，agent 只能猜。
- 最小修法：把 L230 的触发换成已有键描述的具体情形（例如 act_now 的"用户要求立即完成的临时工作"），把 L182 写成"讨论与推进两个阶段都不免除"；或新增一个 `eager` 键并在 `attention.phases` 下定义它。

### B2（阻塞）`persist_split` 指向不存在的"家"
- 位置：AGENTS.md L86 `resources.split.persist_split`。
- 证据：L86"动态拆分立即写入 **workplan SSOT**，否则与事实脱节。@change"；全文出现 "workplan" 仅此 1 处。而家（home）在文件里已被 L174/L175/L176 枚举完："docs/ 全是 SSOT… .scratch/ 全是 append-only（ticket、research、证据与台账）"、"README 给人看；AGENTS 是 agent 边界；docs 是已确认的产品决策；工作记录是临时契约与证据"、"结构化 YAML 是唯一真相源"。
- 违反判据：第 3 项（过期：引用了一个不在本文件词汇表里的家）+ 第 9 项（`one_home_per_fact` L175：一个事实只在一个家）。
- 反例：agent 在推进期动态拆分后必须"立即写入 workplan SSOT"，它要么把计划塞进 ticket（与 L198 那套车票机制重复），要么自己发明第五个家——两条路都直接违反 L175。同一条规则里的 `@change` 又把因果指到 change 段，而 change 段的家清单里没有 workplan。
- 最小修法：把 "workplan SSOT" 改成已有家（如"当前 ticket 与 `docs/` 里的计划文档"），或在 `change.docs.single_home` 下补一个 `workplan` 键，写明它的文件与路径。若仓库里真存在一个叫 workplan 的 SSOT，那问题变成"指针太弱"（没有任何路径或键指向它），同样必须修。

---

## 非阻塞缺陷

### 对立极性（第 2 项：冲突）

**P1-1 `attention.phases.discuss` 内部对"要不要开 ticket"给出相反动作**
- 位置：L126 `travel_light` × L128 `announce_long`（同为 L120 `discuss` 的兄弟）。
- 证据：L126"轻装——不加流程：**不开 ticket**、不拉分支、不派 subagent"；L128"长活先报——大工作量且没被要求立即完成，就**记 ticket 延后**"。
- 违反判据：第 2 项。文件没有 carve-out，只能靠 L15 `specificity` 现场仲裁，而"记 ticket 延后"恰恰要新开一个 ticket。
- 最小修法：L126 加限定"为当前讨论本身不加流程"，或 L128 改成"记一条待办（不另开 ticket）"。

**P1-2 是否"预告将来的动作"两段极性相反，且只有一侧带阶段限定**
- 位置：L160 `silent_advance`、L164 `act_dont_announce` × L128 `announce_long`。
- 证据：L164"直接执行已授权的工作，**不要预告将来的动作**"（无阶段限定，属 `attention.communication`，对讨论期也成立）；L128"长活先报"（明确要求先报）。
- 违反判据：第 2 项。
- 最小修法：给 L164 补"推进期"限定，或在 L128 里点明它是 L164 的例外。

**P1-3 `lossless` 与 `conclusion_only` 对"给用户多少信息"给出同级相反要求**
- 位置：L157 × L159（同属 `attention.communication`）。
- 证据：L157"**不丢信息，包括细节**；但要用可读的呈现，不甩一大段文字墙"；L159"**只给用户可见的结论**——相关的体验或结果、实质变更与权衡、具体决策；不给内部标识符与过程 dump"。
- 违反判据：第 2 项；两者不是"更具体 vs 一般"，L15 `specificity` 裁不了。
- 最小修法：给 L157 划界（"结论内部的细节不丢；内部过程不算信息"），或在 L159 里点明它压过 L157 的那一部分。

**P1-4 `self_evidence` 把评审者的深度压到"快速复核"，与同段的评审标准相反**
- 位置：L213 × L221（`falsify`）、L227（`review_each_package`）、L231（`unverified_is_not_pass`）。
- 证据：L213"评审者只在最后拿证据**快速**复核"；L221"**主动**从缺失的范围、安全、回归与过期证据上找反例"；L231"未知验收不是 PASS"。
- 违反判据：第 2 项（"快速复核"给了派发者压低评审深度的许可，随后被 L231 否定）。
- 最小修法：删掉 L213 的"快速"。

（经我核对后认为**可由文件自身裁决、不需要修**的冲突候选：L97 `single_writer` × L98 `isolate_writers`（串行 vs 并发两分支）、L225 `review_does_not_commit` × L214 `hash_bound`（工作树 hash 合法）、L125 `wait_for_yes` × L127 `act_now`（用户没提就没动作，act_now 无对象）、L149 `size_the_gate` × L227（用户 gate vs 内部评审，但见 P1-9 的"门"歧义会放大这处）、L233 `report_incomplete_at_limit` × L227（预算上限已被显式处理）。）

### 冗余：同一意思出现多次（第 1 项）

**P1-5 "修根"一条规则写了三遍（leading word 缺失）**
- 位置：L57 `roles.reconsider_first`"失败时先回头质疑父目标、方法与拆分，而不是原地打补丁"；L77 `fix_the_root`"修本质不修表象，否则同一个错会换个形式再来"；L78 `amend_upward`"追到最初的假设与决策，改最高必要层的已确认需求与原则，再改下游"。
- 违反判据：SKILL.md《Pruning》"keep each meaning in a single source of truth… duplication inflates a meaning's prominence on the ladder past its real rank"；以及文件自己的 L184 `cut_repetition`"删掉重复…的文字"。
- 最小修法：留 L78 为唯一规范句（它最具体：改到"最高必要层"），L57/L77 压成 `@intent` 链接或删（SKILL.md 的 leading word 正是为这种"三处展开"准备的）。

**P1-6 `roles.reviewer` 是 `fresh_reviewer` 的近照抄**
- 位置：L61 × L220。
- 证据：L61"用全新上下文，只看最终产物与证据，不看完成声明"；L220"用全新上下文，绝不继承执行者的上下文；检查最终范围的产物与证据，不检查完成声明"。差异只有"绝不继承执行者的上下文"。
- 最小修法：L61 只留指针（"评审者：见 @proof"），规范句留在 L220。

**P2 其余冗余（各一处，最小修法都是"留一处 + 指针")**
- L17 `shared_vocabulary` × L152 `blunt_words`：同一条禁令（不自造词 / 不写 Chinglish / 不用 A1/B1 代号）在两段各说一遍；L165 `match_user` 是第三条（用词与专业度跟用户一致）。
- L94 `preflight` × L237 `baseline_first`：两次"动手前抓 scoped baseline"；理由"分不清既有失败与你引入的失败"在 L217 是第三次。
- L124 `mark_uncertainty` × L38 `provenance`：同一条"不把推断当确认"。
- L65 `high_risk` × L46 `autonomy_bounded`：同一份"需征得同意"清单列两遍（安全/法务/隐私/花钱）。
- L54 `delegate` × L55 `blocked_not_fallback`："主 agent 不自己上手"说两遍。
- L202 `compare_on_resume` × L214 `hash_bound`："重跑过期的检查"说两遍。

### 必要性 / no-op（第 5 项；用 SKILL.md 的判据与文件自带标准）

判据：SKILL.md"an instruction the model already obeys by default pays load to say nothing… the test is model-relative"；文件自带标准见 `AGENTS.yaml:456`（隐藏键）：AGENTS.md 只该强调"模型不会自发做对"的部分。

- **P2 `roles.user`（L52）**："提供信息、描述自己、描述想做的产品与设计；他的时间与注意力不可再生。"前半句是 L51 `roles._base`"用户是信息与意图的来源"的重复，后半句是 L72 `resources._base`"时间最贵"与 L117 `attention._base`"注意力是有限、会衰减的预算"的重复，整条不含任何 agent 动作。最小修法：删，或改成对 agent 的指令（如"只取他自愿给出的信息，不为省事让他重复"）。
- **P2 `small_defect_surface`（L75）**："最小缺陷面、错误左移、自动化、配置驱动，**都是同一件事**——降低犯错的概率与代价。"全句是名词归并 + 一句模型默认就会追求的目标，没有动作。按 SKILL.md《Leading words》，这正是"`fast, deterministic, low-overhead` → `tight`"那一类该收成一个词的位置。最小修法：收成一个 leading word（例如"缺陷面"），把四个名词丢进它的定义。
- **P2 `attention._base`（L117）**："人和 agent 的注意力与上下文都是有限、会衰减的预算。"是前提陈述而非指令，且与 L72 是同一前提的第二次表述；五个顶层 `_base` 中只有它不是祈使句。最小修法：改成可执行的（如"预算会衰减：随进展重估剩余注意力，不靠一次估算吃到底"）或并入 L72。

### SMART / 不可判定（第 8 项）

- **P1-9 `门` 与 `gate` 一物三名**：L216"跑目标项目的**门**与风险驱动的检查"（CI/检查门）vs L91"用户 gate"、L148 `ship_at_gate`、L163 `gates_hold`（用户批准门）vs L149"绕过**评审**"。违反文件自己的 L76"一名一物…名字从 A 变 B 再变 C 是最大的认知陷阱"。反例：agent 可能把 CI 门当用户 gate 去请示，或把用户 gate 当 CI 门自己放行。最小修法：L216 写"目标项目的检查门（CI / 测试）"。
- **P2 `handoff_contract`（L91）"每个派发都 SMART"**：缩写未展开（SMART 有多套展开，且与"smart=聪明"同形），同句随后已逐项列出契约字段 → 既不可执行又与后文重复。最小修法：删掉这半句，或换成"每个派发都写明验收与判据"。
- **P2 `phases._base`（L119）**："阶段由'用户能不能被打断'决定"——判据给了主语，没给可观察输入（agent 从哪读到这一点）。最小修法：点明来源（会话开头的模式说明 / 用户上一句）。
- **P2 `evidence_not_insults`（L45）**："说一个设计'蠢'，或只说花了很多小时，都不是理由。"纯禁止句，没有正面目标；正面目标在 L44（"要有验证过的理由、代表性的尝试与成本收益"）与 L58（"改需求或阈值必须有证据与理由"）已存在。按 SKILL.md《Leading words·Negation》："steering by prohibition drags the forbidden behaviour into context… prompt the positive"。最小修法：改成正面句"理由是证据、验证过的成本收益与具体损失"，或删。

### 逻辑自洽 / 父子关系（第 6 项）

- **P2 `intent.precedence`（L11-18）不是 `intent` 的后果**：L3 `intent._base` 讲"质量由用户意图定义"，L12 `precedence._base` 讲跨信息源的裁决，二者无蕴含关系；其子节点（authority/implication/specificity）是文档集的结构规则。按文件自己的 L14 `implication`"低层违背高层即失效"，父子关系不成立时子规则会被静默判为不可采。最小修法：把 `precedence` 提到顶层，或挂到 `change.docs.single_home` 下。
- **P2 `@` 与所在位置在 4 处互相矛盾**（`@` 按 schema 是"次要因果"标记，即主因果由所在位置给出）：L77 `fix_the_root`、L78 `amend_upward` 的唯一因果说明都指向 `@intent`，却挂在 `resources.efficiency` 下；L244 `model_cost`、L245 `external_compute`（付费模型反向委派、外部算力）把因果指向 `@resources`，却挂在 `proof.execution.process` 下；L79 `explain_conflicts`（约束冲突要说清）无 `@`，主因果被声明为 resources.efficiency，但文本里没有任何资源内容。违反 SKILL.md 的 co-location 判据（"grouped material reads as documentation; scattered material does not"）。最小修法：这四条各归其位，或补一条 `@` 说明主因果。
- **P2 `@` 过密，且精确度只有"段"**：55/244 行带记号（`proof.execution.process` 11 条全带）；目标是 5 个顶层段，因此链接无法指到具体规则（"次要因果"只到段）。L81 `resources.split._base`"错位的拆分是设计缺陷的警报。@attention"是明显反例：该句没有任何与注意力有关的因果。最小修法：只保留跨顶层的、正文能读出因果的标记；句子内部的因果从段内位置就能看出（schema 说 @ 只作注意力连接，段内不需要它）。
- **P2 `TLDR` 一词两极**：L152"先 TLDR"（对用户的消息）× L137"不是 TLDR，不是剧场文本"（对交付物）。词同义反、两段相邻，建议统一（例如 L137 改成"不是摘要替代品"）。

### 完备性 / 遗漏（第 4、7 项）

- **P1-10 权威序缺两个位次**：L13 `authority` 只列"用户 > 已确认 > 本文件 > docs > agent 推断"。而 L15 `specificity` 明说"内层目录胜过外层目录"（承认存在外层/内层指令文件），L91 `handoff_contract` 让父派发自带"权威输入"。系统/平台提示与父派发契约都不在序里。反例：系统提示要求 X、本文件要求 Y 时无裁决；子 agent 的派发契约与项目 AGENTS 冲突时无裁决。最小修法：在 L13 补两个位次（平台/系统提示、父派发契约），或写明未列出的信息源如何归层。
- **P1-11 提交/推送没有任何规则，而证据链默认它会发生**：L214"证据绑 commit 或工作树 hash"、L225"评审不授权提交；未提交的用 baseline-to-worktree diff 与 hash"、L113"清理前确认未提交或未推送的工作安全"、L100/L206（分支与 Git 历史是档案）——四处提到 commit/推送，却没有一条说谁提交、何时提交、提交信息带什么、能否自行 push。反例：worker 拿到包评审结论后不知能否自己 commit（L225 只说评审不授权提交，没说谁授权）。最小修法：在 `roles.worker` 或 `proof.execution` 补一条（worker 在自己分支提交、集成者合并、推送需授权或按 L65 高风险处理）。
- **P2 "改 SSOT 后必须重渲染并校验"没有活规则**：L176 说渲染产物"只读、可重生成"，L1 banner 说手工改动会被覆盖，但全文没有一条要求"改 SSOT 后重跑渲染并确认产物一致"；仓库里恰好有这个检查（`scripts/render_policy.py --check`，且不通过会退出 1），政策却没要求跑，也没给出脚本名。最小修法：在 `change.docs.write_rules` 补一句"改 SSOT 后重渲染并跑一致性检查"。
- **P2 `open_it_for_them`（L154）× `model_cost`（L244）张力**：L154 指示"远端用户就上传到图床之类可访问处"，L244 禁止"悄悄去找服务来上传、付款或算力"。两者只在"披露即合规"的读法下相容，文件没写这句。最小修法：L154 补"并告知用户上传到了哪里"。
- **P2 无披露：178 条规则全部常驻，从不分层**：按 SKILL.md《Progressive disclosure》"inline what every branch needs, and push behind a pointer what only some branches reach"，只有部分分支才用的整块（`change.docs.schema` 的 7 条迁移/schema 规则、`environment.desktop_courtesy`、`proof.execution.process.model_cost`/`external_compute`）与每次会话都要的规则同权常驻。文件**自带**隐藏机制（`*` 键，`AGENTS.schema.yaml:2-4`）却只用了 1 次。声明为弱证据：判断哪些块是"分支专属"需要 `AGENTS.yaml:456` 提到的 append-only 台账，本次未取。

### 自洽性：本文件违反自己的规则（第 9 项）

- **P2 `policy_standalone`（L177）被本文件正文证伪**：L177"政策不依赖项目事实、docs、模型平台、可选工具或假设的运行时保证"；而 L54（主 agent / sub agent 分工）、L104（推理预算沿主 agent 继承）、L106/L220（全新上下文 / 绝不继承执行者上下文）、L132（全新上下文交付）、L241（"不编造上下文百分比"）、L243（"自行派 subagent 接手"）都只在"有父子会话、有上下文预算、可派发 subagent"的运行时里成立。最小修法：把 L177 收窄为"不依赖项目事实与 docs"，或明确它约束的是内容而非运行模型。
- **P2 `layer_and_source`（L189）/`field_admission`（L190）对本文件自身的 SSOT 不成立**：L189"**每个事实**必须声明 layer 与 source"，L190 要求"标生产者与消费者；枚举每值都有说明"。而政策 SSOT 的 schema（`AGENTS.schema.yaml` 的 `$defs.node`）只要求 `_zh`/`_en`，`AGENTS.yaml` 全文无 layer/source/生产者字段。最小修法：在这两条里点明适用范围（项目 SSOT），或接受它并给政策 SSOT 加最小标注。
- **干净项**（对照第 9 项检查，未发现违反）：L195"本文件不写自己的变更史"——AGENTS.md 无日期、无 changelog；L183 `facts_not_log`——无"曾经是 A 后来是 B"；L176 `structured_source`——L1 banner 与"Markdown 是只读渲染产物"一致；L17/L152 的用语禁令针对**对用户的输出**，本文件是给模型读的，用英文键名与专业缩写不构成违反。

---

## 已检查且干净的项

- **渲染忠实性**：33 个非叶子行（含 `_base`）与 33 条 `_base` 一一对应（逐行核对，父节点行 +1 即 `_base`，33/33 命中）；叶子无 `_base`；`_en` 与唯一隐藏键 `attention.emphasis_by_evidence*`（`AGENTS.yaml:456`）按 `render_policy.py:62-79` 的规则剔除；无空行、无注释；key 清单目视核对无重名；`@` 目标全部落在 5 个真实存在的顶层键上，无死引用（脚本的三项检查我在静态层面全部复核，执行验证见"未能验证"）。
- **结构**：顶层 5 个、层级 3-4 层，父节点与 `_base` 的语义（"有子节点才写自己那句话"）在 33 处无一例外，符合 `AGENTS.schema.yaml`（`required: [_zh,_en]`、`additionalProperties: false`）。
- **判据面（本文件最强处）**：绝大多数叶子带可判定的动作与边界，例如 L122（"至少两个方案"）、L31（"五到十条"）、L85（两个否条件）、L182/L216（门与命令）、L225（diff/hash 形式）、L233（上限时怎么办）。这类具体度远超一般 AGENTS.md。
- **我核对后认为站得住的父子关系**：`attention`（预算→阶段/交付/沟通）、`change`（变化→文档）、`proof`（可证明→执行/评审/过程）、`resources`（资源→效率/拆分/环境）四个顶层的子节点确实是其后果；只有 `intent` 下的 `precedence`（另见 P2）是明显例外。
- **看似冲突但可由文件自身裁决、无需修**：L97/L98、L214/L225、L125/L127、L149/L227、L227/L233（逐条理由见"对立极性"节末）。
- **SKILL-MECHANICS.md 的条款不适用**：它管的是 skill 的 frontmatter、模型/用户调用与 router；AGENTS.md 不是 skill，因此我没有据它出任何缺陷，只借用了它与 SKILL.md 共用的 leading word / no-op 判据。

## 未能验证

- **哈希**：无 shell 权限，无法独立计算或比对 `AGENTS.md` / `AGENTS.yaml` 的 md5；若与任务给的版本不同，本报告的结论依然成立，但"版本锁定"只有任务侧的单方声明。
- **`python3 scripts/render_policy.py --check` 未执行**：脚本的三项机械检查（key 形状与全局唯一、`_zh`/`_en` 齐全、未知 `@` 引用）我只做了静态核对；"AGENTS.md 与 AGENTS.yaml 一致"是按逐行比对判断的，不是跑出来的。
- **"急切"是否由运行时定义**：按任务的排除条款，我没有审仓库其它内容，因此无法确认它是否来自系统提示；两种可能（自造术语 / 运行时术语）在本报告里都已按缺陷处理。
- **no-op 筛选的分母**：判断"哪些规则是模型默认就会做对的"需要 `AGENTS.yaml:456` 所说的 append-only 失误台账（有分母才能区分"不知道"与"没做"），本次未取，故第 5 项的结论只对上面点名的三类句子负责。
- **分支频率（用于披露建议）**：同上，无台账则无法量化哪些整块只在部分分支触发。

## 合并裁决

**BLOCK** —— 修掉 B1（未定义"急切"承担评审豁免）与 B2（`workplan SSOT` 指向不存在的家）后可接受；P1 组（对立极性 4 处、冗余 2 处、`门/gate` 一物三名、权威序缺位、提交权限缺失）建议随下一次策略改动一起修，P2 组按 `AGENTS.yaml:456` 的强调度机制排期。修法一律通过 `AGENTS.yaml` 改并重渲染，不改 AGENTS.md（L1、L176）。