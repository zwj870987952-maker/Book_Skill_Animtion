# 候选案例池 (Candidate Cases)

> 提取器: `case-extractor`
> 来源书籍: 《动画的时间掌握》（Timing for Animation）- 哈罗德·威特克 & 约翰·哈拉斯
> 说明: 包含书中真实案例、长片工程实操与标准例题演算（worked_example）。

```yaml
- id: c01
  title: 保龄球与网球自由下落对比演练
  type: case
  example_kind: worked_example
  source_chapter: 第 18–19 页、第 58–63 页
  source_quote: |
    "如果让一个网球和一个同样大小的铁保龄球从相同高度下落，两者的下落时间相差无几，但着地瞬间的表现却截然不同。"
  summary: |
    原书经典重力与材质例题：
    网球下落 8 帧，着地瞬间产生 50% 挤压变形（Squash），随后在 6 帧内反弹至原高度的 70%，经历 5 轮衰减反弹才静止；
    保龄球同样下落 8 帧，着地瞬间自身几乎不发生变形，但直接砸裂木地板并在第 9 帧瞬间停死（0 反弹），伴随长达 18 帧的绝对静止（Heavy Hold）。
  bound_to:
    - "质量与重量感判定换算框架 (Weight & Force Heuristics)"
    - "自由落体二次方间距公式"
  outcome: |
    证明了物体的重量感不是靠外部轮廓造型表现，而是靠触地瞬间的变形比率与反弹时间决定的。
  tags: [case, weight, bouncing-ball, impact, worked-example]

- id: c02
  title: 拔出陷入深泥之脚的阻力反弹演练
  type: case
  example_kind: worked_example
  source_chapter: 第 22–23 页
  source_quote: |
    "当角色用力把深陷泥潭的脚拔出来时，外力持续增加但没有位移，直到克服吸力的瞬间爆发。"
  summary: |
    原书关于静摩擦力与爆发反冲的经典例题：
    角色向上用力拔腿，身体向后拉伸长达 12 帧，但脚部在泥中完全纹丝不动（蓄势积累）；
    在第 13 帧，脚掌脱离泥浆，仅用 1 帧瞬间飞跃大半个屏幕；
    第 14–16 帧因惯性冲过头（Overshoot），角色由于反冲力失衡一屁股摔坐在地上，泥点在第 17–24 帧滞后落下。
  bound_to:
    - "视知觉与动作闭环机制 (Anticipation-Action-Reaction Loop)"
    - "慢进慢出非线性缓动机制"
  outcome: |
    生动展示了“长时间蓄力 ➔ 瞬时位移 ➔ 惯性失衡摔倒”的物理因果链条。
  tags: [case, resistance, tension-release, anticipation, worked-example]

- id: c03
  title: 12格标准人类行走循环工程演算
  type: case
  example_kind: worked_example
  source_chapter: 第 88–91 页
  source_quote: |
    "在标准的每秒两步（24格一循环）行走中，第1格与第13格为前后脚接触位，第4格与第16格为身体最低下沉位。"
  summary: |
    原书给出的 24fps 下 12 格单步（24 格完整循环）工业基准：
    - 帧 1：右脚向前触地，左脚在后蹬地，双脚全开（Contact，高度中等）
    - 帧 4：右脚全掌承重，右膝弯曲，身体沉至最低谷（Down，吸收冲击）
    - 帧 7：左脚抬起经过右腿侧面，身体回升（Passing，单腿承重）
    - 帧 10：右脚尖用力后蹬，身体升至最高峰（Up，重心最高）
    - 帧 13：左脚向前触地，右脚在后（相反对称的 Contact）
  bound_to:
    - "人类步态循环工程框架 (Human Locomotion Cycles)"
    - "人类步态与情绪速度对照标准表"
  outcome: |
    成为全球商业动画工业中通用性最强的人形角色走步施工图。
  tags: [case, walk-cycle, standard-timing, worked-example]

- id: c04
  title: 烈马飞奔（Gallop）16格步序时钟演算
  type: case
  example_kind: worked_example
  source_chapter: 第 96–99 页
  source_quote: |
    "马在飞奔时，后肢不是同时着地，而是先落下一只后脚，紧接着另一只后脚超越它着地推蹬，使身体腾空。"
  summary: |
    原书针对大型四足动物飞奔（Gallop）的 16 帧极速循环演算：
    - 帧 1–3：后脚猛烈推蹬地面，马身完全向前腾空飞跃（Suspension phase，四蹄离地，身体伸长）
    - 帧 6：前外侧单蹄首先着地承重，吸收冲击
    - 帧 8：前内侧单蹄着地，马头沉到最低位（Head drops down）
    - 帧 11：后肢收缩向前抱团，马脊椎如弹簧般剧烈拱起（Spine flexes）
    - 帧 13–15：后蹄先后着地再次蹬伸
  bound_to:
    - "四足动物步态时序模型 (Quadruped Locomotion Engine)"
    - "多级关节鞭梢时序延迟机制"
  outcome: |
    消除了四足动物奔跑时“前后肢像剪刀般机械对称开合”的业余假象。
  tags: [case, quadruped, horse-gallop, animal-timing, worked-example]

- id: c05
  title: 经典滑稽二次受惊反应（Double-Take）表演
  type: case
  example_kind: worked_example
  source_chapter: 第 68–69 页
  source_quote: |
    "角色走过一个令人吃惊的物体，起初毫无察觉地走过，随后神经系统突然反应过来，猛烈反弹。"
  summary: |
    经典动画表演时序解剖：
    - 阶段 1（轻忽）：角色眼睛扫过怪物，毫无反应继续向前漫步 6 帧；
    - 阶段 2（神经传导时延）：突然身体僵直，眼球向后看 3 帧；
    - 阶段 3（极端爆发）：整个身体向上暴起，脖子拉长 3 倍，嘴巴大张（仅占 2 帧）；
    - 阶段 4（震颤与定格）：落地振动 3 帧，随后身体呈惊恐僵硬状态完全静止 16 帧。
  bound_to:
    - "戏剧停顿与受惊受击反应模型 (Hold & Take Mechanics)"
    - "受惊受击定格吸收时长法则"
  outcome: |
    精准诠释了喜剧表演中“延迟反馈”与“夸张定格”的时间艺术。
  tags: [case, double-take, comedy-acting, cartoon-take, worked-example]

- id: c06
  title: 鞭梢效应与末端破音障时序演算
  type: case
  example_kind: worked_example
  source_chapter: 第 32–35 页
  source_quote: |
    "手腕向后抽拉鞭柄，波浪沿着皮鞭逐渐加速传递，当波浪到达末梢时，鞭头速度达到最大。"
  summary: |
    纯物理波动机制例题：
    第 1–3 帧手柄猛烈向后拉；第 4 帧鞭身中部呈巨大弧形弯曲滞后；第 5 帧前段制动，动能完全汇聚至鞭梢；
    第 6 帧鞭梢以惊人速度完成 180 度极速折返爆响（画成细长速度线）；第 7–10 帧鞭身呈阻尼波浪逐渐松弛落地。
  bound_to:
    - "多级关节鞭梢时序延迟机制"
    - "无生命物体受力与阻尼振荡模型"
  outcome: |
    奠定了角色挥剑、投掷棒球、甩尾巴等一切末端爆发动作的数学模型。
  tags: [case, whip-action, wave-motion, kinetic-transfer, worked-example]

- id: c07
  title: 《动物庄园》（Animal Farm）长片复杂对白与音乐律表
  type: case
  example_kind: firsthand
  source_chapter: 第 6–7 页、第 114–115 页
  source_quote: |
    "在英国第一部彩色动画长片《动物庄园》的制作中，为保证对白的情绪力量，整场长镜头的动画时间完全受事先录制好的演员声音支配。"
  summary: |
    约翰·哈拉斯团队在制作长篇史诗动画时的真实工程案例：
    先录制老少校（Old Major）的慷慨演讲音频，用声波分析仪将每个音节精确标注到 24fps 摄制表上；
    在配乐段落，根据 120BPM 节拍器设定每 12 格一个音乐重音；
    所有的猪只呼吸起伏与口型张闭严格遵照“提前 1 格发音、重音提前 2 格点头”的工程法则绘制，达成了极高的严肃戏剧严肃性。
  bound_to:
    - "声画对齐与视听生理时钟同步框架 (Audio-Visual Lip Sync)"
    - "声画对齐视听提前量法则"
  outcome: |
    验证了工业级动画长片必须依赖以音频律表为核心的前期时间锁死机制。
  tags: [case, animal-farm, feature-film, voice-sync, firsthand]

- id: c08
  title: 钟摆阻尼振荡等时性 16 帧往复实测
  type: case
  example_kind: worked_example
  source_chapter: 第 56–57 页
  source_quote: |
    "一个绳长固定的重锤摆动，第一次往返摆动耗时 16 格，第四次微弱摆动依然严格耗时 16 格。"
  summary: |
    单摆运动的严谨逐帧演算：
    - 轮次 1（大摆动）：摆角 ±45°，单向耗时 8 帧，回摆耗时 8 帧（周期 16 帧）；两端慢进慢出，中央间距 15 厘米；
    - 轮次 2（中摆动）：摆角 ±22°，单向耗时 8 帧，回摆耗时 8 帧（周期仍为 16 帧！）；中央间距缩减至 7 厘米；
    - 轮次 3（微摆动）：摆角 ±8°，周期依然严格为 16 帧；
    - 轮次 4：振幅低于人眼可辨阈值，直接停在垂直静止位（Hold）。
  bound_to:
    - "无生命物体受力与阻尼振荡模型 (Inanimate Physics & Oscillation)"
    - "简谐阻尼振动等时性定律"
  outcome: |
    纠正了初学者常犯的“振幅变小就随意缩减帧数”的严重错误。
  tags: [case, pendulum, damping, harmonic-timing, worked-example]
```
