# 候选术语词典池 (Candidate Glossary)

> 提取器: `glossary-extractor`
> 来源书籍: 《动画的时间掌握》（Timing for Animation）- 哈罗德·威特克 & 约翰·哈拉斯
> 说明: 提炼作者在书中具有特定技术与美学含义的关键术语，明确与常识含义的差异。

```yaml
- id: g01
  term: 时间掌握 (Timing)
  type: term
  source_chapter: 第 3–5 页、第 8–10 页
  author_definition: |
    "在固定放映速率（如 24 帧/秒）下，一个动作或情节意念从起步、发展到结束所占据的绝对银幕格数与时间长度。"
  key_distinction: |
    ≠ 常识中的“钟表时间”或“耗时多久”
    ≠ 单纯的速度（快或慢）
    = 动作的物理重量、性格情绪与观众神经系统吸收意念的生理节奏总和
  why_it_matters: |
    是全书所有技能的核心根基。在动画中，没有不带 Timing 的动作；改变帧数就是改变物理属性和戏剧意图。
  tags: [term, core-concept, timing]

- id: g02
  term: 间隔距离 (Spacing)
  type: term
  source_chapter: 第 36–39 页
  author_definition: |
    "在两张关键原画（Key Poses）之间，中间画（Inbetweens）在运动轨道几何空间上的相对位移跨度与疏密排布。"
  key_distinction: |
    ≠ 常识中的“物体间距”或“几何尺寸”
    ≠ 静态画面的布局排版
    = 加速度（Acceleration）与制动力的空间投射曲线
  why_it_matters: |
    Timing 决定总时间，Spacing 决定质感。相同 12 帧时间，均匀 Spacing 是机械运动，两端密中间疏则是弹性缓动。
  tags: [term, core-concept, spacing, acceleration]

- id: g03
  term: 单格与双格 (Shooting on 1s vs 2s)
  type: term
  source_chapter: 第 46–47 页
  author_definition: |
    "单格指每胶片格曝光一张新画稿（24fps 下画 24 张）；双格指每胶片格拍摄同一张画稿两次（24fps 下画 12 张）。"
  key_distinction: |
    ≠ “粗制滥造”与“精雕细琢”的贫富对立
    ≠ 双格必然卡顿
    = 结合人眼视觉暂留特性的工程效率与稳定性平衡策略（中慢速双格更稳，极速与运镜单格必选）
  why_it_matters: |
    直接决定制作预算与画面平滑度。滥用单格导致成本翻倍且线条微颤，滥用双格在高速运镜时引发剧烈频闪。
  tags: [term, production-technique, frame-rate]

- id: g04
  term: 慢进与慢出 (Slow-in & Slow-out / Cushion)
  type: term
  source_chapter: 第 40–45 页
  author_definition: |
    "在动作开始起步和结束停顿的位置，画稿间距极其密集、位移极小；在动作行程中央，画稿间距拉大、位移最大的非线性运动法则。"
  key_distinction: |
    ≠ 简单的“走得慢”
    = 描述物体克服静止惯性（起跑）与克服运动动量（刹车）的物理必经阶段
  why_it_matters: |
    三维动画中贝塞尔切线（Tangent Handles）的物理源头。凡是无 Slow-in/out 的动作必定呈现木偶机械感。
  tags: [term, ease-in-out, acceleration, physics]

- id: g05
  term: 动作预感 (Anticipation)
  type: term
  source_chapter: 第 50–51 页
  author_definition: |
    "角色在实施主要意图动作之前，在反方向所做的短暂蓄力、压缩或姿势准备。"
  key_distinction: |
    ≠ 常识中的“预感、第六感或心理猜测”
    = 生理蓄能机制（跳前必蹲）与引导观众视网膜提前聚焦的视知觉舞台调度工具
  why_it_matters: |
    极速动作能否被观众“看清并看懂”的决定性前置条件。
  tags: [term, anticipation, staging, body-language]

- id: g06
  term: 追随与交搭 (Follow-through & Overlapping)
  type: term
  source_chapter: 第 52–55 页
  author_definition: |
    "主动力源躯干停止后附属结构由于惯性继续运动（追随）；以及多级关节和不同肢体部分在不同时间点错落到达极值（交搭）。"
  key_distinction: |
    ≠ 简单的“尾随”或“动作重叠”
    = 表达角色材质柔软度、松弛感与消除多肢体同步到达木偶僵硬感的核心手段
  why_it_matters: |
    次级动画（Secondary Animation）的灵魂。头发、裙摆、尾巴、松弛肌肉的核心解算逻辑。
  tags: [term, overlapping, follow-through, secondary-motion]

- id: g07
  term: 停顿 (Hold)
  type: term
  source_chapter: 第 48–49 页
  author_definition: |
    "某一特定关键姿态或表情在连续曝光数格（通常为 6–24 格）中保持绝对静止不动。"
  key_distinction: |
    ≠ 播放器“卡顿”或动画师偷懒不画
    = 给予观众视网膜与大脑处理复杂信息、品味戏剧笑点和情绪共鸣的留白缓冲期
  why_it_matters: |
    节奏（Pacing）的呼吸感来源。永远不停顿的动画会让人眼花缭乱、疲惫不堪。
  tags: [term, hold, pacing, acting]

- id: g08
  term: 反应 (Take / Double Take)
  type: term
  source_chapter: 第 68–69 页
  author_definition: |
    "角色在意识到突发物理撞击或戏剧刺激时，所产生的夸张生理震颤、瞬间变形与随后的呆滞定格动作序列。"
  key_distinction: |
    ≠ 电影实拍中的“拍摄镜头单元（Take 1, Take 2）”
    = 动画特有的高度符号化、夸张化的情绪外显表演模式
  why_it_matters: |
    动画角色表演灵魂与喜剧幽默感的核心发源地。
  tags: [term, take, double-take, comedy, acting]

- id: g09
  term: 挤压与拉伸 (Squash & Stretch)
  type: term
  source_chapter: 第 18–21 页
  author_definition: |
    "物体在加速运动中沿运动方向拉长，在撞击受阻时沿冲击法线方向压扁，且始终保持体积守恒的形变法则。"
  key_distinction: |
    ≠ 随意的橡皮泥乱变形
    = 必须严格遵守质量守恒（压扁时必定变宽，拉长时必定变细），用于表现物体硬度与弹性
  why_it_matters: |
    传递冲击力与消除高速运动跳帧的最经典手段。
  tags: [term, squash-stretch, deformation, volume-preservation]

- id: g10
  term: 视听提前量 (Visual Lead)
  type: term
  source_chapter: 第 114–121 页
  author_definition: |
    "在设计表上，将视觉口型与重音动作的曝光帧数，比真实音频波形峰值向前提前 1 至 2 格绘制的补偿规则。"
  key_distinction: |
    ≠ 播放设备硬件时延或音画不同步故障
    = 针对人类视觉感知比听觉感知滞后约 40 毫秒所做出的主动感知校准
  why_it_matters: |
    声画对齐成败的生死线。同帧对齐在银幕上必定感觉口型滞后，必须提前。
  tags: [term, visual-lead, lip-sync, perception-calibration]

- id: g11
  term: 摄制表 / 律表 (Exposure Sheet / Dope Sheet)
  type: term
  source_chapter: 第 16–17 页
  author_definition: |
    "以 24 格为一秒分行纵向排列，详细记录音轨发音、层级画稿编号、摄影机指令与背景移动的施工总表。"
  key_distinction: |
    ≠ 简单的日程计划表或草稿纸
    = 整个动画制作管线唯一的、具备法律效力的工程施工蓝图
  why_it_matters: |
    三维软件时间轴（Timeline）与二维动画律表（Xsheet）的始祖原型。
  tags: [term, dope-sheet, exposure-sheet, production-pipeline]

- id: g12
  term: 接触姿态与通过姿态 (Contact & Passing Poses)
  type: term
  source_chapter: 第 88–91 页
  author_definition: |
    "接触姿态指迈出脚跟刚刚接触地面的双腿最大开合帧；通过姿态指摆动腿经过支撑腿并使其承重伸直的单腿过渡帧。"
  key_distinction: |
    ≠ 任意行走姿态的随意切片
    = 步态循环中决定步长、重心最高最低点与骨盆倾斜角的关键工程原画
  why_it_matters: |
    构建一切人类与拟人动物行走循环不可动摇的黄金骨架。
  tags: [term, contact-pose, passing-pose, locomotion-keys]
```
