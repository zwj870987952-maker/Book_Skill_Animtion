# 候选原则与规则池 (Candidate Principles)

> 提取器: `principle-extractor`
> 来源书籍: 《动画的时间掌握》（Timing for Animation）- 哈罗德·威特克 & 约翰·哈拉斯
> 说明: 包含确定性原则、计算公式、操作清单、时间判断规则与阈值指标。

```yaml
- id: p01
  title: 动画帧率时基换算规则 (24fps Timing Conversion Standard)
  type: principle
  source_chapter: 第 10–15 页
  source_quote: |
    "电影的标准放映速度是每秒 24 格（电视为每秒 25 格）。1 秒的动作占 24 格，半秒占 12 格，1/3 秒占 8 格，1/4 秒占 6 格。"
  summary: |
    动画制作的一切时间计算必须以电影 24fps（或电视 25fps）为绝对时间基准。
    计算公式与标准模数映射表：
    - 1 秒 = 24 帧（格）
    - 3/4 秒 = 18 帧
    - 1/2 秒 = 12 帧（人类正常单步基准）
    - 1/3 秒 = 8 帧（快速步频 / 转身基准）
    - 1/4 秒 = 6 帧（奔跑单步 / 快速反应起步）
    - 1/6 秒 = 4 帧（极速击打 / 眨眼闭眼）
    - 1/8 秒 = 3 帧（动作预备极限）
    - 1/12 秒 = 2 帧（双格曝光单张极限）
    - 1/24 秒 = 1 帧（闪光 / 受击最高峰值）
  inputs:
    - 现实期望秒数 (秒)
  formula: |
    总帧数 N = 秒数 t × 24 (电影标准)
  units: "帧 (Frames)"
  output: "整数帧数 (四舍五入或向上取偶)"
  tags: [standard, 24fps, time-conversion, dope-sheet]

- id: p02
  title: 单格与双格拍摄选择判定树 (Shooting on 1s vs 2s Decision Rule)
  type: principle
  source_chapter: 第 46–47 页、第 124 页
  source_quote: |
    "双格拍摄不是偷工减料，慢速动作拍双格往往比拍单格更稳定；但当动作极快、弧度极大或摄影机横移时，必须强制拍单格。"
  summary: |
    单双格选择的核心判断规则：
    1. 默认准则：角色的慢速动作、正常行走、对话表演，优先使用双格（Shooting on 2s，每画拍2帧），既节省 50% 成本，又避免线条细微颤抖；
    2. 强制单格条件（必须 On 1s）：
       - 动作极快且位移巨大（如高速挥剑、出拳位移）；
       - 空间运动弧线（Arc）曲率半径极小且转折剧烈；
       - 摄影机执行推拉摇移（Pan / Zoom）时，前景角色与背景必须同步单格拍摄，否则背景平移与角色会产生剧烈错位颤抖。
  inputs:
    - 动作速度 (像素/帧)
    - 运动轨迹曲率
    - 摄影机是否运动
  tags: [shooting-on-ones, shooting-on-twos, camera-sync, cost-optimization]

- id: p03
  title: 自由落体二次方间距公式 (Gravity Acceleration Quadratic Spacing)
  type: principle
  source_chapter: 第 24–27 页
  source_quote: |
    "物体由于重力作用自由下落时，其下落位移与时间的平方成正比。间距不是等距增加，而是呈几何级数扩大。"
  summary: |
    真实落体或跳跃下坠的中间画间距严禁均匀分配，必须遵循重力加速度平方率：
    距离公式：$S_n = k \times n^2$（其中 $n$ 为帧序号，$k$ 为基础位移常数）。
    空间位移增量比例严格呈奇数比序列：
    - 第 1 格位移：1 单位
    - 第 2 格位移：3 单位（累计 4）
    - 第 3 格位移：5 单位（累计 9）
    - 第 4 格位移：7 单位（累计 16）
    - 第 5 格位移：9 单位（累计 25）
    若忽略此规则采用线性等距中间画，物体将呈现出“在粘稠液体中缓缓滑落”的严重失重感。
  inputs:
    - 下落总高度 H
    - 期望下落帧数 N
  formula: |
    第 i 帧位移占比 = (i / N)^2
  units: "相对高度百分比"
  output: "各帧在垂直轨道上的 Y 轴坐标值"
  tags: [gravity, acceleration, physics-formula, quadratic-spacing]

- id: p04
  title: 慢进慢出对半空间切分法则 (Halving Principle for Ease In/Out)
  type: principle
  source_chapter: 第 36–41 页
  source_quote: |
    "要使动作平滑停顿，最经典实用的画法是不断对半切分：在原画与中间画的二分之一处再加一张，在四分之一处再加一张。"
  summary: |
    中间画空间分布经典黄金切分规则：
    - 慢入（Slow-in，减速进站）：
      目标原画为 100%。第一中间画定在 50%，第二张定在 75%，第三张定在 87.5%，第四张定在 93.75%。越靠近终点越密集；
    - 慢出（Slow-out，加速起步）：
      起始原画为 0%。第一中间画定在 6.25%，第二张定在 12.5%，第三张定在 25%，第四张定在 50%。
    现代应用：在三维动画曲线编辑器中，此规则对应贝塞尔切线的非对称拉伸（Ease Weight 75%–85%）。
  inputs:
    - 关键姿态 A 与 B 的距离
    - 缓动张数
  formula: |
    位移残差 = 初始跨度 × (1/2)^k
  units: "空间坐标"
  output: "Spacing chart 刻度线位置"
  tags: [ease-in, ease-out, halving-principle, spacing-chart]

- id: p05
  title: 动作预感时空配比黄金律 (Anticipation Timing & Amplitude Ratio)
  type: principle
  source_chapter: 第 50–51 页
  source_quote: |
    "如果一个快速动作需要 4 格完成，那么用于预备动作的时间至少需要 8 到 12 格。动作越猛烈，预备时间越长。"
  summary: |
    动作预感（Anticipation）的量化参数规则：
    1. 时间比例法则：预感蓄力帧数通常是主动作位移帧数的 2 至 3 倍（蓄力 6–12 帧 ➔ 释放 2–4 帧）；
    2. 反向位移比例：预备姿态的反向位移幅度，通常为主动作主要行程的 15% 至 30%（反向拉伸过大会喧宾夺主，反向过小观众视线无法聚焦）；
    3. 加速度特征：预备动作自身必须采用“慢入（Slow-in）”，在极值姿态处轻微定格 1–2 帧，随后瞬间如弹簧松脱般爆发。
  inputs:
    - 主动作释放时间 Action_Frames
  formula: |
    Anticipation_Frames = Action_Frames × 2.5 (范围: 2.0 ~ 3.5)
  units: "帧数"
  output: "预备阶段建议曝光格数"
  tags: [anticipation, golden-ratio, spring-load, staging]

- id: p06
  title: 多级关节时序延迟差参数表 (Joint Offset Frame Delay Rules)
  type: principle
  source_chapter: 第 32–35 页、第 52–55 页
  source_quote: |
    "上臂带动小臂，小臂带动腕部。腕部比小臂慢 1 到 2 格到达最高点，手指比手腕再慢 1 格。"
  summary: |
    人体与角色肢体运动的骨骼延迟参考参数（在 24fps 下）：
    - 躯干/肩部（Root / Shoulder）：基准时间 0 帧
    - 大臂/肘部（Elbow）：延迟 +1 至 +2 帧
    - 小臂/手腕（Wrist）：延迟 +2 至 +3 帧
    - 手指/末端掌指（Fingers）：延迟 +3 至 +5 帧
    - 软体挂件/长头发/松弛长裙（Secondary Cloth）：延迟 +4 至 +6 帧
    此参数表彻底消除角色机械运动，是构建自然布料、长发飘动与肢体挥动的量化标准。
  inputs:
    - 关节层级深度 (0 到 4 级)
  units: "帧偏移量 (Frame Offset)"
  output: "各层级关键帧的向后偏移帧数"
  tags: [joint-offset, delay-rules, overlapping-action, animation-rig]

- id: p07
  title: 人类步态与情绪速度对照标准表 (Human Walk/Run Pacing Standard)
  type: principle
  source_chapter: 第 88–91 页、第 108–113 页
  source_quote: |
    "步频直接反映人物的性格、体量与情绪状态。正常走每步 12 格，快跑每步 6 格，慢步拖行每步 16 格。"
  summary: |
    人类单步（一步，半个循环）曝光帧数对照标准（24fps 下）：
    - 极速冲刺奔跑（Sprinting）：单步 4 帧（每秒 6 步）
    - 正常奔跑（Running）：单步 6 帧（每秒 4 步）
    - 欢快跳跃步伐（Skipping / Jogging）：单步 8 帧（每秒 3 步）
    - 急促快走（Brisk Walk / Agitated）：单步 9–10 帧
    - 正常自然漫步（Normal Walk）：单步 12 帧（每秒 2 步，标准基准）
    - 沉重缓慢/疲惫拖步（Tired / Heavy Walk）：单步 16 帧
    - 极度苍老/潜行匿踪（Sneak / Frail）：单步 18–24 帧
  inputs:
    - 角色心理状态与体能特征
  units: "格/单步 (Frames per step)"
  output: "步频节拍模数"
  tags: [walk-speed, run-speed, pacing-table, emotion-timing]

- id: p08
  title: 声画对齐视听提前量法则 (Visual Lead Rule for Lip Sync)
  type: principle
  source_chapter: 第 114–121 页
  source_quote: |
    "必须牢记的黄金铁律：在设计表上，口型姿态必须比录音带上的发音点提前 1 到 2 格出现。"
  summary: |
    动画声画同步的生理时间补偿法则：
    1. 闭唇音（B, P, M）：在音轨波形爆破点前 2 帧，嘴唇必须完全闭合并微压紧；在音轨发音瞬间（第 0 帧），嘴唇爆破微张；
    2. 开口元音（AH, OH, EE）：嘴型张开的最大极值姿态，必须设定在音轨波形峰值前 1 帧；
    3. 视听重音动作：强调性拍桌子、挥拳、点头等表演重音，必须在关键单词发音前 2–4 帧触及极限位。
    反向警告：同帧对齐在视觉上必定显得滞后拖沓。
  inputs:
    - 音频事件帧号 Sound_Frame
  formula: |
    Mouth_Peak_Frame = Sound_Frame - 1 (元音)
    Mouth_Closed_Frame = Sound_Frame - 2 (爆破辅音)
  units: "帧号"
  output: "口型原画在律表上的放置帧号"
  tags: [lip-sync-rule, visual-lead, audio-alignment, phonetics]

- id: p09
  title: 摄影机摇移防频闪安全速度阈值 (Camera Panning Strobing Limits)
  type: principle
  source_chapter: 第 124–127 页
  source_quote: |
    "摄影机平移每格位移若在 6 至 10 毫米之间，最容易引发严重频闪。必须避开该临界速度区间。"
  summary: |
    摄影机移动防频闪判定准则：
    1. 慢速安全区：每格位移极小，允许双格平移；
    2. 危险共振区：当每格移动距离等于背景中竖向栅栏、树干等周期性条纹间距的 30%–60% 时，会产生强烈的视网膜停滞和反向倒流频闪（Strobing），严禁使用；
    3. 修复决策：要么将摇移速度降低 40% 进入慢速平稳区，要么提速并强制叠加运动模糊（Motion Blur），或者将摇镜头拆分为“快速甩镜头（Whip pan，仅需 3–5 帧）”。
  inputs:
    - 平移位移增量
    - 背景纹理重复周期
  tags: [camera-pan, strobing-threshold, safe-speed, panning-rules]

- id: p10
  title: 受惊受击定格吸收时长法则 (Take and Hold Duration Principle)
  type: principle
  source_chapter: 第 68–69 页
  source_quote: |
    "极端的反应姿势（Take）出现后，必须保持静止停留至少 8 到 16 格，否则观众的视线甚至来不及辨别角色的面部表情。"
  summary: |
    动画受击、受惊反应的生理吸收时间下限：
    - 冲击瞬间（Impact / Hit）：仅需 1–2 帧极限变形；
    - 缓冲微震（Vibration）：3–5 帧递减小震荡；
    - 绝对停顿（Freeze Hold）：
      - 快速反应：维持 8 帧（约 1/3 秒）
      - 标准喜剧反应：维持 12 帧（0.5 秒）
      - 重大震撼/目瞪口呆：维持 18–24 帧（0.75 ~ 1 秒）
    低于 8 帧的停顿在视觉上会被误认为是“卡顿了一下”，失去戏剧表演的观赏性。
  inputs:
    - 刺激事件的戏剧量级（轻微/中等/重大）
  units: "帧数"
  output: "Hold 持续曝光帧数下限"
  tags: [hold-duration, reaction-timing, take-rule, perception-threshold]

- id: p11
  title: 简谐阻尼振动等时性定律 (Isochronism of Damped Oscillation)
  type: principle
  source_chapter: 第 56–57 页
  source_quote: |
    "许多初学者常犯的错误是随着摆动幅度变小而减少画稿帧数。实际上，哪怕幅度减小到只有一毫米，往返的周期时间仍然保持不变。"
  summary: |
    物理定律在动画中的严格映射：
    单摆与弹簧振动的周期 $T$ 仅由摆长或质量刚度决定，与振幅大小无关（在小角度近似下恒定）。
    - 规则：如果第 1 次往返摆动消耗 16 帧，那么第 2 次、第 3 次、第 4 次衰减摆动也必须严格消耗 16 帧！
    - 严禁错误：不可在振幅减半时将周期减为 8 帧或 4 帧，否则物体将呈现“越摆越快、神经质抽搐”的伪物理现象。
  inputs:
    - 单摆物理周期 T (帧数)
  formula: |
    Period_n = Period_0 (恒定不变)
    Amplitude_n = Amplitude_0 × (Damping_Factor)^n
  units: "帧数 / 振幅百分比"
  output: "各振荡周期的起止帧号与振幅极值"
  tags: [isochronism, oscillation, pendulum, harmonic-motion, physics]
```
