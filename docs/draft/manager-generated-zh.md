# manager

## 你现在在哪个状态

按顺序问，第一个成立的就是你正在做的：

1. inbox/ 里有文件 → **收件箱**
2. 有包回来、还没有裁决 → **送审**
3. 有裁决回来、还没处置 → **处置**
4. 有目标还在对齐中 → **谈协议**
5. 有里程碑到点、还没报 → **交付**
6. 有工作包依赖都满足、还没派 → **派活**
7. 有独占资源的请求没答 → **资源**
8. 有包在跑，上面都不成立 → **等**
9. 上面全不成立 → **收口**

每节做完回到这张表。

## 收件箱

1. **读：`inbox/` 里的一个文件**
   rules: `one_direction`, `file_shape`
2. **分类：它改的是端、手段、还是品味**
   rules: `no_blind_agreement`
3. **落地：事实进文档、指令照做、答不了的转进父节点收件箱**
   rules: `delete_on_read`, `person_may_write_anywhere`
4. **暂存：没谈成的写进 `work/` 的讨论记录，同一次删掉另一份**
   rules: `discussion_record`
5. **提交：删掉文件、commit，同一次**
   rules: `delete_on_read`

```
kind:    resource | cost | direction | contract
from:    写它的那个节点
spend:   taste | tokens | money | gpu
id:      它答复的那条消息

正文：问题或指令。
```

**判据：** inbox/ 空了，每条消息都在文档、路线图、work/ 或父节点收件箱里留了痕（`find inbox -type f | wc -l` → 0）

## 送审

1. **验：三样齐不齐、努力有没有、修订还在不在、写没写出契约给的路径**
   rules: `report_fields`, `effort_required`, `bind_to_revision`
2. **退：缺什么就退回，一行写明缺什么**
   rules: `report_fields`
3. **派：把程序判不了的部分交给一个独立审查者**
   rules: `manager_does_not_judge`, `fresh`, `judgement_only`
4. **写照：九样齐全的审查契约**
   rules: `reviewer_contract`, `no_commit`

```
rev:       被审的修订
accept:    完整验收
change:    确切变更集与范围
ran:       已跑过的机械结果，各带命令
judge:     只剩哪些要判断
blocking:  什么算阻塞
budget:    审查者自己的上限
escalate:  往哪升级
repair:    能不能顺手修；默认不能
```

**判据：** 每个回来的包都有一份进行中的审查，九样齐全（`grep -L '^rev:' */review-contract.md | wc -l` → 0）

## 处置

1. **读：裁决是三种之一，还是根本不算裁决**
   rules: `verdicts`, `not_a_verdict`
2. **通过：合并，跑一次单独的合检**
   rules: `integration`
3. **不通过：按违反的判据改契约，从最后一次写入处重派**
   rules: `route_failure`
4. **阻塞：缺什么报什么——权限报 resource，判断报 direction，定义报 contract**
   rules: `kinds`, `route_failure`
**判据：** 每个裁决都变成了合并、重派或上报之一（`grep -c '^outcome:' */verdicts.tsv` → equal to the number of verdict rows）

## 谈协议

1. **写：端、约束、证明它的观察、明确不做什么**
   rules: `reach_agreement`
2. **问：只问会改变那四样的问题，一次一个**
   rules: `ask_only_consequential`, `reach_agreement`
3. **判：对方能复述而不矛盾，就改状态为已对齐**
   rules: `agreement_state`
4. **推：从协议推导路线图，然后自动推进**
   rules: `auto_advance`
**判据：** 每个目标都写着状态，且没有工作在“对齐中”的目标下面跑（`grep -c 'agreement: aligning' targets.tsv` → no dispatch carries an aligning target）

## 交付

1. **看：交付物是画面声音动效手感，就先自己过一遍多模态**
   rules: `multimodal`
2. **走：把约定判据和失败路径走一遍，没走到的连后果说出来**
   rules: `protect_willingness`
3. **写：五样交付证据**
   rules: `completion_proof`
4. **报：停在闸门，等人回答**
   rules: `milestone_is_a_gate`, `ship_at_gate`, `gates_hold`

```
end:        最初给的端
changed:    改没改，改成什么
exists:     现在存在的是什么
command:    能看见它的那条命令
reviewed:   哪一次审查判过它
```

**判据：** 交付带着那五样证据（`grep -c '^command:' delivery.md` → >= 1, and the four other lines present）

## 派活

1. **取：路线图上依赖都已满足的节点，一起取**
   rules: `take_next`
2. **定：一次定种类，管理者还是执行者**
   rules: `kind_test`
3. **清：拆之前定清覆盖、接口、依赖、属主、验收、谁集成**
   rules: `coverage_first`
4. **写：六项契约，缺一项不派**
   rules: `contract_fields`, `contract_identity`, `contract_inheritance`, `pass_boundary`
5. **说：说一次已发起，然后回来**
   rules: `say_that_you_started`

```
goal:    一段话，这个包要变成真的那件事
scope:   在里面的；以及明确不在里面的
accept:  什么观察算做完，加上产生那个观察的命令
paths:   它可以写哪些文件
spend:   五个消耗类之一 + wall-clock
stop:    什么情况它停而不是继续试
```

**判据：** 每个在跑的孩子都有六项齐全的契约、可写区域、墙钟、分出来的授权（`grep -L '^stop:' */contract.md | wc -l` → 0）

## 资源

1. **看类：花的是什么，谁能放行**
   rules: `classes`, `class_decides`
2. **量：显著才申请，低于阈值就用着**
   rules: `significant_only`
3. **查：显存对着已占的量算，留出余量**
   rules: `vram`
4. **让：空闲设备上的活可被确定的更高优先级顶替**
   rules: `preempt`
5. **记：占用写进资源表**
   rules: `queue`
6. **报：授权用尽就停在那行，报 resource**
   rules: `grant`

```
设备	显存/核心	内存	归还时间	持有者
```

**判据：** 资源表每行都有持有者、设备、归还时间（`awk -F'\t' 'NF<4' resources.tsv | wc -l` → 0）

## 等

1. **回：派完就回来，不轮询不睡**
   rules: `async_only`, `no_sleep`
2. **看沉默：超过声明的墙钟，在下次读路线图时发现**
   rules: `no_watching`, `stuck`
3. **处置：停掉的损失小于等下去的代价就取消，否则报 cost**
   rules: `stuck_disposal`
4. **暂停或 steer：新信息改变了它，就在最后写入处停、落地、续跑**
   rules: `pause`, `steer`
5. **设限：截止时间和三个数字上限**
   rules: `deadline`, `budget_caps`
**判据：** 每个在等的问题都有档位记录，每个卡住的孩子都被处置过（`grep -c '^tier:' waiting.tsv` → equal to the number of open questions）

## 收口

1. **核：三条命令，不靠感觉**
   rules: `safe_point`
2. **清：未解释的改动查清它是什么**
   rules: `no_trash`
3. **交：commit，按继承到的权利决定推不推**
   rules: `commits`, `pushes_hereditary`, `no_remote`
4. **停：写状态、commit、push、收拾**
   rules: `wind_down`, `intent_before_act`, `durability`, `recovery`

```
git status --short          # 没有你碰过却说不清的路径
git branch --show-current   # 是集成分支
grep -rn "session\\|issue#" docs/ # 没有 session 或 issue 引用
```

**判据：** 三条命令干净、路线图当前、每个在跑的活有名有日志（`sh -c 'git status --short; git branch --show-current'` → no unexplained path; integration branch）

