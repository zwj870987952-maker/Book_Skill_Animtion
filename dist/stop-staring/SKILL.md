---
name: stop-staring
description: |
  三维角色面部建模、表情绑定、对白口型与眼神演技工业级工程手册。涵盖 Osipa 视素双轴正交解耦（开合 vs 宽窄）、分层四步对白流水线与 2-4 帧超前量、口轮眼轮匝肌同心环循环布线与五星极点隔离、差分加算目标体架构与 ss2_blend_taper 余弦衰减、抛物线牙弓与舌头三段变形、内眉外眉挤压三轴解耦与额头动态折痕、上下眼睑张力解耦与角膜露白标尺、眼球追踪眼睑跟随算法与 1 帧扫视跳跃、非对称极速闭合眨眼动力学与思维顿悟同步、拉链嘴唇渐进粘连绑定、带边界限制的 2D Box 面部滑块控制器界面设计、头部整体 Squoosh 挤压拉伸多层变形分层与体积守恒算法。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.stop-staring
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# 面部建模与动画表情绑定：Stop Staring 实战精粹 — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 真人实拍写实电影文学剧本台词剧本文学创作
- 医学头面部神经外科微观解剖手术仿真
- 纯非生物刚体机械金属外壳硬表面零件数控加工编程

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 发音口型在笛卡尔坐标系中正交解耦为开合 (Open/Closed) 与宽窄 (Wide/Narrow)，杜绝全脸字母混合形叠加冲突。
2. 对白口型严格遵循分层四步法；关键辅音接触（MBP 闭唇、FV 咬唇）必须提前 2-4 帧闭合以补偿视觉感知超前量。
3. 面部拓扑严格服从口轮匝肌与眼轮匝肌同心环形边流（Edge Loops），五星极点严禁落在形变边缘与折痕处。
4. 目标体仅记录差分矢量（Delta）；对称分离应用余弦平滑衰减，在中线严格满足 W_L + W_R ≡ 1.0 互补守恒律。
5. 上眼睑主导生理清醒度与警觉，下眼睑主导心理张力与真笑挤压（Squint）；眼球上下旋转必须带动上眼睑 25%-35% 联动跟随。
6. 眼球转动遵循 1 帧扫视跳跃（Saccades）并保持定格；眨眼作为思维句号与视线跳跃同步，采用 2 帧极速下落与 4-5 帧慢出回弹。
7. 局部表情目标体与全局头部 Squoosh 挤压拉伸解耦分层，横向缩放严格按纵向缩放平方根反比维持三维体积守恒。

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 设计无冲突的口型动画目标体系统；将语音音标转换为三维角色口型状态矢量；解决多音素连续发音时的嘴角穿插冲突 | references/capabilities/viseme-ortho-matrix.md | references/capabilities/lip-sync-pipeline.md、references/capabilities/slider-interface-driver-rig.md |
| 制作长段角色台词对白口型动画；排查口型滞后于声音的视听不同步缺陷；规范口型关键帧的分层打标流程 | references/capabilities/lip-sync-pipeline.md | references/capabilities/viseme-ortho-matrix.md、references/capabilities/blink-dynamics-thought-break.md |
| 构建支持高精度面部形变的三维头部拓扑；排查嘴角与眼周在拉伸时的光影撕裂缺陷；布置眼口鼻三大表情区域的同心环形布线 | references/capabilities/facial-edge-flow-topology.md | references/capabilities/additive-blendshape-math.md、references/capabilities/mouth-cavity-teeth-tongue.md |
| 编写表情绑定目标体的差分权重计算脚本；将对称雕刻的完整表情拆分为独立的左右半脸目标体；消除微笑与张嘴同时激活时的顶点超调撕裂 | references/capabilities/additive-blendshape-math.md | references/capabilities/facial-edge-flow-topology.md、references/capabilities/slider-interface-driver-rig.md |
| 绑定三维角色牙齿与下巴旋转关节；制作舌头在发 L/TH/S 音时的卷曲变形；构建暗色防漏光的封闭口腔壁几何体 | references/capabilities/mouth-cavity-teeth-tongue.md | references/capabilities/viseme-ortho-matrix.md、references/capabilities/facial-edge-flow-topology.md |
| 设计表达悲伤、惊讶、狂怒或怀疑的眉毛形态；绑定单侧独立挑眉与眉心纵向皱纹挤压；解决双眉聚拢时的中线顶点相撞穿插 | references/capabilities/brow-emotion-mechanics.md | references/capabilities/eyelid-expression-tension.md、references/capabilities/slider-interface-driver-rig.md |
| 制作真笑时的眼周微表情挤压 (Duchenne Smile)；调配狐疑、蔑视、惊恐等细微眼神状态；校准摄影机视角下的角膜高光与真实注视线偏差 | references/capabilities/eyelid-expression-tension.md | references/capabilities/brow-emotion-mechanics.md、references/capabilities/eye-rig-lid-follow-saccades.md |
| 构建眼球 Aim 约束与眼睑自动跟随联动网络；制作自然生动、拒绝平滑漂移的眼球注视动画；消除眼球向下看时露白严重的死鱼眼穿帮 | references/capabilities/eye-rig-lid-follow-saccades.md | references/capabilities/eyelid-expression-tension.md、references/capabilities/blink-dynamics-thought-break.md |
| 制作富有呼吸感与生命力的自然眨眼动画；在角色思考、下定决心或视线转移节点编排眨眼；排查机械对称节拍器眨眼的动画缺陷 | references/capabilities/blink-dynamics-thought-break.md | references/capabilities/eye-rig-lid-follow-saccades.md、references/capabilities/lip-sync-pipeline.md |
| 绑定逼真的写实嘴角黏膜粘连效果；解决角色微张嘴说话时嘴角边缘呈现生硬折角的缺陷；构建单侧独立撇嘴粘连控制网络 | references/capabilities/zipper-lips-sticky-rig.md | references/capabilities/viseme-ortho-matrix.md、references/capabilities/facial-edge-flow-topology.md |
| 搭建直观高效的 Osipa 风格 2D 面部控制面板；使用 Set Driven Key (SDK) 连接控制器与底层目标体；限制控制器位移范围以避免非法目标体超调破面 | references/capabilities/slider-interface-driver-rig.md | references/capabilities/viseme-ortho-matrix.md、references/capabilities/brow-emotion-mechanics.md |
| 为角色头部添加夸张的卡通挤压拉伸变形器；保证头部剧烈形变时面部微表情与口型仍可正常播放；计算头颅挤压拉伸时的横向体积守恒补偿因子 | references/capabilities/squoosh-head-squash-stretch.md | references/capabilities/additive-blendshape-math.md、references/capabilities/slider-interface-driver-rig.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 用户仅咨询纯文本剧本创作或解剖医学手术，不涉及角色面部建模、表情绑定与动画时判停
- 已输出明确的面部拓扑布线规范、2D 控制器映射参数、口型对白时序律表或加算目标体算法时判停
