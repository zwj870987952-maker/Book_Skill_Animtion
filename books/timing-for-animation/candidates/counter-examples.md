# 候选反例与失败模式池 (Candidate Counter-Examples)

> 提取器: `counter-example-extractor`
> 来源书籍: 《动画的时间掌握》（Timing for Animation）- 哈罗德·威特克 & 约翰·哈拉斯
> 说明: 包含作者明确警告的失败模式、动画反模式与初学者常见大坑。

```yaml
- id: ce01
  title: 线性均匀间距陷阱 (Even Spacing / Mechanical Anti-Pattern)
  type: counter-example
  source_chapter: 第 36–39 页
  source_quote: |
    "初学者最常见也是最致命的毛病，就是在两张原画之间盲目画出等距离的中间画。这会立刻夺走动作的所有生命力，使其变成冰冷机械的仪器转动。"
  failure_mode: |
    在两张原画之间按固定空间距离平分放置中间画，没有任何加速或减速。
  mechanism: |
    自然界物体受力时必定伴随加速度。如果空间位移严格线性，物体就表现为合外力为零的匀速漂移，物理重力、惯性与材质弹性瞬间瓦解。
  warning_signs:
    - 角色挥臂或走动看起来像工厂流水线的机械臂
    - 动作发飘、发软，缺乏爆发力和顿挫感
    - 曲线编辑器里的动画曲线是一条笔直的折线（Linear interpolation）
  bound_to:
    - "动画时空双轴决策模型 (Timing vs Spacing)"
    - "慢进慢出非线性缓动机制"
  tags: [counter-example, even-spacing, mechanical-motion, anti-pattern]

- id: ce02
  title: 缺少动作预感导致的视知觉丢失 (Missing Anticipation Blunder)
  type: counter-example
  source_chapter: 第 6 页、第 50–51 页
  source_quote: |
    "如果一个动作发生得太突然，在观众把注意力转移到它身上之前，动作就已经结束了。创作者精心设计的动作完全被浪费掉了。"
  failure_mode: |
    角色直接执行高速动作（如突然出拳、突然逃窜、猛然跳起），省去了反方向蓄力姿态。
  mechanism: |
    人类大脑在银幕上追踪目标需要 100–200 毫秒的生理注视延迟。缺少反向蓄力（Anticipation），观众的眼球尚未聚焦，高速位移（1–3 帧）就已完成，导致观众产生“闪烁卡顿”而非“有力出击”的错觉。
  warning_signs:
    - 观众看完表示“没看清发生了什么”
    - 角色打击感软弱无力，像被看不见的线突然拽走
  bound_to:
    - "视知觉与动作闭环机制 (Anticipation-Action-Reaction Loop)"
    - "动作预感时空配比黄金律"
  tags: [counter-example, missing-anticipation, visual-blindspot, staging-error]

- id: ce03
  title: 全肢体同步到达终点的木偶病 (Simultaneous Arrival / Stiff Rig Anti-Pattern)
  type: counter-example
  source_chapter: 第 32–35 页、第 52–55 页
  source_quote: |
    "绝不要让手臂、躯干、衣角和头发在同一格画面上同时停下来。这会让角色瞬间变成一具僵死的木雕。"
  failure_mode: |
    挥臂、转身或落地时，肩膀、手臂、手腕、手指标记在完全相同的关键帧到达极值位置并同时停止。
  mechanism: |
    真实的生物由多级关节和软组织构成，力在不同质量和长度的骨骼间传递必然存在时差。所有部件同时定格违背了动量守恒与次级运动规律。
  warning_signs:
    - 角色整体呈现木偶式、纸片人般的生硬感
    - 三维动画中所有骨骼层级的 Keyframe 都在同一垂直线上对齐
  bound_to:
    - "多级关节鞭梢时序延迟机制"
    - "多级关节时序延迟差参数表"
  tags: [counter-example, simultaneous-arrival, stiff-puppet, overlapping-error]

- id: ce04
  title: 振荡衰减缩减周期帧数错误 (Damped Period Shrinkage Fallacy)
  type: counter-example
  source_chapter: 第 56–57 页
  source_quote: |
    "很多人误以为幅度变小了时间就应该变短。如果摆幅变小而帧数减少，钟摆在视觉上就会显得越变越快，产生神经质般的抽搐。"
  failure_mode: |
    在制作单摆、跳板、天线或头发的减幅振动时，随着振动幅度减小，盲目将半周期帧数从 8 帧减为 4 帧、2 帧。
  mechanism: |
    单摆等物理系统的振动周期由系统固有频率决定，具有等时性（Isochronism）。帧数缩短意味着频率虚假飙升，违背基本物理常识。
  warning_signs:
    - 钟摆在即将停下时突然像癫痫般高频抖动
    - 软体反弹失去优雅的弹性质感
  bound_to:
    - "无生命物体受力与阻尼振荡模型"
    - "简谐阻尼振动等时性定律"
  tags: [counter-example, physics-fallacy, frequency-error, pendulum-glitch]

- id: ce05
  title: 极速动作绘制写实平滑中间画的跳影灾难 (Strobing in Fast Inbetweens)
  type: counter-example
  source_chapter: 第 42–43 页、第 102–107 页
  source_quote: |
    "试图在一两格内完成的大跨度动作中画出清晰的正常中间画，结果往往是银幕上出现两个脱节的鬼影在闪烁。"
  failure_mode: |
    当角色手臂在 3 格内从左挥到右时，试图在中间画出清晰写实的手臂姿态。
  mechanism: |
    在 24fps 下，单帧曝光时间仅为 1/48 秒。当快速物体的位移超过其自身宽度数倍时，视网膜无法通过视觉暂留将两张清晰独立的图像融合成平滑路径，而是将其识别为互不相关的两个跳跃残影。
  warning_signs:
    - 画面频闪、跳动严重
    - 动作看起来“脱臼”或分裂
  bound_to:
    - "极速运动跳帧排障机制"
    - "动画时空双轴决策模型"
  tags: [counter-example, strobing-ghosts, smear-violation, fast-action-trap]

- id: ce06
  title: 口型声音同帧对齐导致的视觉滞后病 (Zero-Offset Lip Sync Lag)
  type: counter-example
  source_chapter: 第 114–121 页
  source_quote: |
    "如果动画师把口型的最大张开帧精确对准声音波形的最高峰值，在银幕上放映出来时，观众会强烈感觉到口型总是慢半拍。"
  failure_mode: |
    在摄制表上严格将音频波形的起伏峰值帧与嘴型张合极值帧放在同一格。
  mechanism: |
    人类感官对听觉反应的速度（约 10 毫秒）显著快于视觉光信号处理速度（约 50 毫秒）。同帧对齐在认知心理学上必定呈现滞后。
  warning_signs:
    - 观众感觉角色是在“对口型假唱”
    - 角色说话松散、咬字无力
  bound_to:
    - "声画对齐与视听生理时钟同步框架"
    - "声画对齐视听提前量法则"
  tags: [counter-example, lip-sync-lag, perception-delay, audio-misalignment]

- id: ce07
  title: 停顿不足导致的戏剧表演失效 (Insufficient Hold Failure)
  type: counter-example
  source_chapter: 第 48–49 页、第 68–69 页
  source_quote: |
    "如果你画出了一个绝妙的受惊表情，却只让它在银幕上停留 2 到 3 格，那么这个表情等于根本没画过。"
  failure_mode: |
    在重大戏剧转折、受惊、恍然大悟或受击后，角色仅停留 2–4 帧就立刻进入下一个动作。
  mechanism: |
    观众对复杂面部情绪的认知消化需要至少 250–500 毫秒（6–12 帧）。过短的停顿会被观众视网膜当作“镜头掉帧”或无意抽动忽略掉。
  warning_signs:
    - 喜剧包袱抖不响，观众没笑
    - 角色表演慌乱，没有任何戏剧节奏感（Pacing）
  bound_to:
    - "戏剧停顿与受惊受击反应模型"
    - "受惊受击定格吸收时长法则"
  tags: [counter-example, rushed-acting, lost-punchline, hold-deficiency]

- id: ce08
  title: 巨兽无重力纸片人灾难 (Weightless Giant Syndrome)
  type: counter-example
  source_chapter: 第 70–71 页
  source_quote: |
    "许多人把大象或恐龙的动作画得和小猫一样灵巧迅捷。这彻底毁灭了巨型怪兽的体量感与压迫感。"
  failure_mode: |
    绘制巨型角色（如巨人、恐龙、高达、大象）时，使用常规角色的 8–12 帧单步步频，且起步制动仅耗费 2–3 帧。
  mechanism: |
    平方-立方定律（Square-Cube Law）：生物体积增大为原来的 $N$ 倍，其质量将按 $N^3$ 增长，其惯性极其庞大。巨型生物必须消耗大量帧数来完成蓄力缓冲与惯性制动。
  warning_signs:
    - 几十米高的怪兽跑起来像小狗，缺乏视觉震撼与压迫感
    - 落地时无视巨大惯性，轻飘飘停下
  bound_to:
    - "质量与重量感判定换算框架"
    - "自由落体二次方间距公式"
  tags: [counter-example, scale-error, weightless-giant, inertia-violation]
```
