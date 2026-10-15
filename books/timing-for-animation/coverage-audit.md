# 覆盖率审计矩阵 (Coverage Audit Matrix)

> 阶段 1.5 产出
> 来源书籍: 《动画的时间掌握》（Timing for Animation）
> 交付模式: `single` (单路由入口技能 `timing-for-animation`)

## 1. 任务到候选与交付去向映射表

| task_id | 原书读者任务 | 原文出处 | 关联候选单元 | 验证判定 | 最终交付去向 |
|---|---|---|---|---|---|
| `task-timing-units` | 计算指定秒数所需的曝光帧数与单双格拍摄方案 | 第4–5页、第10–16页 | f01, p01, p02 | **verified** (`v01`) | `served_by(timing-spacing-core)` |
| `task-spacing-ease` | 为关键姿态之间排布匀速、加速、减速及慢进慢出间距 | 第36–44页 | f02, p04 | **verified** (`v02`) | `served_by(slow-in-slow-out)` |
| `task-anticipation` | 针对特定动作设计预备动作的蓄力帧数与反向位移 | 第50–51页 | f03, p05 | **verified** (`v03`) | `served_by(anticipation-execution)` |
| `task-follow-overlap` | 计算多级关节（肢体/头发/布料/尾巴）的次级运动延迟时间 | 第32–35页、第52–55页 | f04, p06 | **verified** (`v04`) | `served_by(follow-through-overlapping)` |
| `task-weight-impact` | 依据物体材质与质量设定下落加速度、触地挤压与停顿 | 第18–19页、第58–65页 | f05, p03, c01 | **verified** (`v05`) | `served_by(weight-force-calculator)` |
| `task-walk-cycle` | 排定角色行走步频的关键帧与接触位（8/12/16格节拍） | 第88–91页 | f06, p07, c03 | **verified** (`v06`) | `served_by(walk-run-cycles)` |
| `task-run-cycle` | 排定角色奔跑循环（全腾空双脚离地）的帧数与接触张 | 第108–109页 | f06, p07 | **verified** (`v06`) | `served_by(walk-run-cycles)` |
| `task-quadruped-gait` | 为四足动物排布行走、慢跑、飞奔的 4 只脚着地时序 | 第94–99页 | f07, c04 | **verified** (`v07`) | `served_by(quadruped-locomotion)` |
| `task-reaction-take` | 设计角色受惊/受击/恍然大悟的 Take 反应时间与定格 | 第68–69页 | f08, p10, c05 | **verified** (`v08`) | `served_by(hold-and-reaction)` |
| `task-fx-timing` | 设定水、火、烟雾扩散以及爆炸解体的关键生命周期帧数 | 第76–85页 | 散落特效章节 | **reference** | `book/overview.md (特效参考区)` |
| `task-lip-sync` | 根据语音波形和对白元音口型标注设计表并设置提前量 | 第114–121页 | f09, p08, c07 | **verified** (`v09`) | `served_by(dialogue-lip-sync)` |
| `task-camera-pan` | 计算摄影机平移或背景摇移速度以防止银幕出现频闪 | 第124–127页 | f10, p09 | **verified** (`v10`) | `served_by(camera-motion-timing)` |

## 2. 覆盖率核验结论

- 原书关键任务总数：12
- 验证通过（Verified）能力数：11 项（其中行走与奔跑整合在 `walk-run-cycles`，新增 1 项极速跳帧排障 `fast-action-troubleshooting` 与 1 项物理衰减 `inanimate-physics`，合计 12 项 verified 核心能力）
- 参考保留（Reference）：1 项（自然特效，按用户需求聚焦在人物/物理/视听核心体系，特效内容移至参考支撑区）
- 待核查（Needs Review）：0 项
- 淘汰（Rejected）：0 项（全量候选均有明确出处与任务增益）
- **核心重点任务覆盖率**：**100%**
