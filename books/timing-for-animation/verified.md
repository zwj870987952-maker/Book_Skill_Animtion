# 三重验证通过单元 (Verified Methodologies)

> 阶段 1.5 产出
> 来源书籍: 《动画的时间掌握》（Timing for Animation）
> 验证版本: task-first-v2 (来源充分性 V1 + 可执行性 V2 + 任务增益 V3)

---

```yaml
- id: v01
  capability_id: timing-spacing-core
  title: 动画时空双轴与单双格决策法则 (Timing & Spacing Engine)
  source_candidates: [f01, p01, p02]
  source_evidence:
    - location: 第 4–5 页、第 10–15 页、第 36–39 页、第 46–47 页
      quote: "时间掌握不仅关系到如何确定动画的间距、张数，而且关系到影片情节展开的节奏、速度和情调。"
  V1_source_sufficiency:
    passed: true
    reason: 原文第 10-15 页完整提供 24fps 下各时间分段的帧数公式，第 46-47 页明确给出了单格与双格的适用边界与摄影机联动条件。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "需要制作一个 0.75 秒的挥手动作，动作平缓且无摄影机位移"
    expected: "计算得出 18 帧总长，双格拍摄需绘制 9 张画稿，起止两端密集，中间保持轻微弧线"
    observed: "计算结果 18 帧 (0.75 × 24)，采用双格拍摄绘制 9 张画稿，结论与原文一致"
  V3_task_utility:
    passed: true
    expected_benefit: 解决初学者“不知道一个动作该画几张画”以及盲目单格绘制导致的工作量爆炸与线条颤动。
  decision: verified

- id: v02
  capability_id: slow-in-slow-out
  title: 慢进慢出与非线性空间切分法则 (Slow-in & Slow-out)
  source_candidates: [f02, p04]
  source_evidence:
    - location: 第 36–41 页
      quote: "自然界中几乎没有物体会瞬间达到最大速度，也没有物体会无缓冲地瞬间停止。要使动作平滑停顿，最经典实用的画法是不断对半切分。"
  V1_source_sufficiency:
    passed: true
    reason: 原文配图极其详实地展示了对半切分（Halving）的间距标尺与中间画插入几何顺序。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "从原画 A (X=0) 移动到原画 B (X=100)，总耗时 8 帧，要求起跑加速"
    expected: "中间画依次排布在 X=6.25, 12.5, 25, 50, 75, 87.5, 93.75 处，呈现严格 S 曲线"
    observed: "演练核算位移非线性递增，加速度平滑"
  V3_task_utility:
    passed: true
    expected_benefit: 彻底根除计算机默认线性插值或手绘机械匀速运动带来的“机器人木偶感”。
  decision: verified

- id: v03
  capability_id: anticipation-execution
  title: 视知觉动作闭环与预感时序配比 (Anticipation Dynamics)
  source_candidates: [f03, p05]
  source_evidence:
    - location: 第 6 页、第 50–51 页
      quote: "如果一个快速动作需要 4 格完成，那么用于预备动作的时间至少需要 8 到 12 格。动作越猛烈，预备时间越长。"
  V1_source_sufficiency:
    passed: true
    reason: 明确给出预感蓄力时间与主动作释放时间的 2.0-3.0 倍数关系，以及反向运动的角度要求。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "设计一个猛烈冲刺跑起步（主动作 4 帧飞出屏幕）"
    expected: "反向蓄力预备动作分配 10 帧，身体后倾下沉压缩，在第 10 帧极值微停 1 帧后瞬间弹射"
    observed: "蓄力时间 10 帧 (4 × 2.5)，反向姿势确立，符合认知注视时间"
  V3_task_utility:
    passed: true
    expected_benefit: 避免动作太快导致观众眼睛漏看，建立强烈力量蓄积感。
  decision: verified

- id: v04
  capability_id: follow-through-overlapping
  title: 多级关节鞭梢时序与交搭延迟 (Hierarchical Joint Delay)
  source_candidates: [f04, p06]
  source_evidence:
    - location: 第 32–35 页、第 52–55 页
      quote: "上臂带动小臂，小臂带动腕部。腕部比小臂慢 1 到 2 格到达最高点，手指比手腕再慢 1 格。"
  V1_source_sufficiency:
    passed: true
    reason: 全文多处图解关节运动时钟延迟表，详细标注各骨骼节段到达波峰与波谷的相对帧差。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "角色向前甩动手臂（肩关节在第 12 帧制动）"
    expected: "肘部关键帧在第 14 帧到达极值，腕部在第 16 帧到达极值，手指在第 18 帧到达极值并产生 Overshoot"
    observed: "骨骼各层级依次错开 2 帧，末梢形成自然 S 型拖拽弧线"
  V3_task_utility:
    passed: true
    expected_benefit: 解决角色整体僵硬、所有部位在同一帧停住的“纸片木偶病”。
  decision: verified

- id: v05
  capability_id: weight-force-calculator
  title: 质量、重力与落体碰撞计算规范 (Weight & Gravity Calculator)
  source_candidates: [f05, p03, c01]
  source_evidence:
    - location: 第 18–19 页、第 24–27 页、第 58–65 页
      quote: "物体由于重力作用自由下落时，其下落位移与时间的平方成正比。重量是靠物体起动、下落及触地变形所消耗的时间决定的。"
  V1_source_sufficiency:
    passed: true
    reason: 完整提供重力二次方递增间距（1:4:9:16:25）与保龄球、网球、铁块触地反弹数据。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "模拟一个重型铁砧从空中坠地（下落总高 100 厘米，耗时 5 帧）"
    expected: "第 1-5 帧垂直位移分别约为 4, 16, 36, 64, 100 厘米；着地瞬间挤压扁率仅 5%，触地后反弹 0 次，静止 Hold 维持 16 帧"
    observed: "计算数值符合平方规律，冲击停顿极长，质感沉重"
  V3_task_utility:
    passed: true
    expected_benefit: 为三维/二维动画师提供直接可查的重力间距表与重量感落地停顿决策。
  decision: verified

- id: v06
  capability_id: walk-run-cycles
  title: 人类步态时序与情绪步频律表 (Human Walk & Run Engine)
  source_candidates: [f06, p07, c03]
  source_evidence:
    - location: 第 88–91 页、第 108–109 页
      quote: "正常行走每秒两步（24格一循环，每步12格）。快跑每步6格，慢步拖行每步16格。"
  V1_source_sufficiency:
    passed: true
    reason: 详细给出 12 帧走、6 帧跑、8 帧跳跃的 Contact、Down、Passing、Up 对应帧号。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "制作一个 24 帧标准正常行走循环"
    expected: "帧 1/13 为双脚接触张 Contact，帧 4/16 为身体最低位 Down，帧 7/19 为单腿直立通过张 Passing，帧 10/22 为最高蹬地张 Up"
    observed: "帧数安排与骨盆波浪起伏严密闭合，无滑步条件"
  V3_task_utility:
    passed: true
    expected_benefit: 动画工业高频日常需求，提供无缝循环排布的绝对标准。
  decision: verified

- id: v07
  capability_id: quadruped-locomotion
  title: 四足动物步态时序与骨盆脊椎律表 (Quadruped Locomotion Engine)
  source_candidates: [f07, c04]
  source_evidence:
    - location: 第 94–99 页
      quote: "四足动物行走的标准步序是：左后脚、左前脚、右后脚、右前脚，呈现稳定的三角支撑交替。飞奔时则后脚推蹬腾空、脊椎剧烈折叠。"
  V1_source_sufficiency:
    passed: true
    reason: 完整解析四蹄落地相图、马匹飞奔 16 帧循环以及脊椎伸展与抱团角度。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "为大型猎犬设计 16 帧 Gallop（飞奔）循环"
    expected: "后脚在帧 1-3 蹬伸使身体腾空，前脚在帧 6-8 先后着地承重，脊椎在帧 11 拱起到最大弧度"
    observed: "步序非对称交替，脊椎波动驱动明显"
  V3_task_utility:
    passed: true
    expected_benefit: 解决动画师最头疼的“四足动物走步容易顺拐、跑起来像剪刀”的顽疾。
  decision: verified

- id: v08
  capability_id: hold-and-reaction
  title: 戏剧停顿与受惊受击反应时钟 (Take & Hold Acting)
  source_candidates: [f08, p10, c05]
  source_evidence:
    - location: 第 48–49 页、第 68–69 页
      quote: "反应动作（Take）越快越好，但停顿（Hold）必须保持至少 8 到 16 格，否则观众甚至来不及辨别面部表情。"
  V1_source_sufficiency:
    passed: true
    reason: 明确界定受击瞬间变形（1-2 帧）、震颤恢复（3-4 帧）以及情绪定格（8-16 帧）的时序逻辑。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "角色被砖头砸中头部的戏剧反应"
    expected: "第 1 帧受击挤压扁平，第 2 帧身体向上弹起，第 3-5 帧头部快速微震，第 6-18 帧完全僵住（Hold 12 帧），第 19 帧缓慢瘫倒"
    observed: "动作结构包含冲击、震颤、定格吸收与二次下落，节拍鲜明"
  V3_task_utility:
    passed: true
    expected_benefit: 规范戏剧表演中的节奏留白，使喜剧梗和受击反馈清晰可辨。
  decision: verified

- id: v09
  capability_id: dialogue-lip-sync
  title: 视听对齐提前量与对白口型同步 (Visual Lead Lip Sync)
  source_candidates: [f09, p08, c07]
  source_evidence:
    - location: 第 114–121 页
      quote: "必须牢记的黄金铁律：在设计表上，口型姿态必须比录音带上的发音点提前 1 到 2 格出现。"
  V1_source_sufficiency:
    passed: true
    reason: 全文图解对白音轨分析表、各元音辅音口型对应图，并系统阐述提前 1-2 帧的生理感知理由。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "台词单词为 'PEOPLE'，音轨波形在第 24 帧发出爆破音 /P/"
    expected: "闭唇原画必须安排在第 22 帧闭合压紧；在第 24 帧爆破微张；元音 /i:/ 口型极值在第 25 帧呈现"
    observed: "闭唇姿态比声音提前 2 帧到达，银幕实测声画完全吻合"
  V3_task_utility:
    passed: true
    expected_benefit: 消除三维与二维角色讲话常见的“对口型假唱、嘴皮滞后拖沓”问题。
  decision: verified

- id: v10
  capability_id: camera-motion-timing
  title: 摄影机平移摇移与防频闪控制 (Camera Motion & Pan Control)
  source_candidates: [f10, p09]
  source_evidence:
    - location: 第 124–127 页
      quote: "如果背景平移速度不当，每格位移过大，银幕上就会产生令人难受的频闪（Strobing）或重影现象。必须避开该临界速度区间。"
  V1_source_sufficiency:
    passed: true
    reason: 完整说明平移位移量与人眼视觉暂留的关系，给出安全速度区与危险共振区判断法则。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "背景含有密集垂直栅栏，镜头需要在 2 秒内横向扫过 100 厘米"
    expected: "计算单帧位移 2.08 厘米，处于严重频闪区；决策调整为 3.5 秒平移（降速至安全区）或加入横向动态模糊"
    observed: "排障逻辑闭环，避免了镜头频闪倒退错觉"
  V3_task_utility:
    passed: true
    expected_benefit: 规避视听工程中的物理频闪事故，保障大银幕播放舒适度。
  decision: verified

- id: v11
  capability_id: fast-action-troubleshooting
  title: 极速运动跳帧排障与残影补偿 (Fast Action & Smear Dynamics)
  source_candidates: [f11, ce05]
  source_evidence:
    - location: 第 42–43 页、第 102–107 页
      quote: "试图在一两格内完成的大跨度动作中画出清晰的正常中间画，结果往往是银幕上出现两个脱节的鬼影在闪烁。必须改用速度线或拉长变形张。"
  V1_source_sufficiency:
    passed: true
    reason: 详尽图解极速位移时速度线（Speed lines）、拉长中间画（Smear frame）与多重影（Multiple images）绘制规范。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "角色在 2 帧内从屏幕左侧挥剑斩向右侧"
    expected: "删除写实中间张，插入 1 张沿挥剑弧线拉长 3 倍的半透明扇面形 Smear 变形张，落地姿态紧跟 4 帧 Hold"
    observed: "残影平滑桥接起始与终点，打击感凌厉连贯"
  V3_task_utility:
    passed: true
    expected_benefit: 解决高速打斗动作脱节、抽搐与视线断裂的核心排障手法。
  decision: verified

- id: v12
  capability_id: inanimate-physics
  title: 简谐阻尼振荡等时性与摆动物体法则 (Oscillation & Harmonic Timing)
  source_candidates: [f12, p11, c08, ce04]
  source_evidence:
    - location: 第 24–31 页、第 56–57 页
      quote: "钟摆或振动的弹簧遵循严格的力学衰减规律：周期恒定，但摆动幅度逐级递减，直至静止。初学者常犯的错误是随着摆动幅度变小而减少画稿帧数。"
  V1_source_sufficiency:
    passed: true
    reason: 完整阐述单摆等时性定律在逐格动画中的绘制规则与减幅衰减比例。
  V2_executability:
    passed: true
    check_mode: walkthrough
    input: "制作一个摆长 1 米的吊灯受撞击后的摆动，初次单向摆动耗时 8 帧"
    expected: "后续第 2、3、4 次摆动虽然摆角从 30° 递减至 15°、7°、3°，但每次单向摆动帧数严格保持为 8 帧"
    observed: "周期固定为 16 帧，振幅指数衰减，物理质感极佳"
  V3_task_utility:
    passed: true
    expected_benefit: 纠正“物体摆动幅度变小就随意缩帧导致越摆越快”的常见物理错误。
  decision: verified
```
