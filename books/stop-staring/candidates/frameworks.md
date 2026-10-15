# 《Stop Staring: Facial Modeling and Animation Done Right》候选框架池 (Frameworks)

## 框架 1: 视素双轴正交解耦矩阵 (The Orthogonal Wide/Narrow & Open/Closed Viseme Matrix)
- **来源**: Chapter 1 & Chapter 4
- **核心逻辑**:
  传统口型动画常常试图为每个音素（A, E, I, O, U, W, F, M...）单独雕刻全量混合形（Blendshape），导致多音素连续过渡时形状冲突、嘴唇打架。Osipa 提出将口型空间正交解耦为两个核心主轴：
  1. **开合主轴 (Open / Closed Axis)**: 沿 Y 轴控制下巴下降、口腔开合度（0.0 至 1.0）；
  2. **宽窄主轴 (Wide / Narrow Axis)**: 沿 X 轴控制嘴角横向拉伸至微笑/宽阔（Wide, -1.0）与向前聚拢突起（Narrow/Pucker, +1.0）。
- **应用范围**: 任意发音口型均可由 `(Open, Wide)` 二维状态矢量插值合成，辅以接触辅音（MBP 闭唇、FV 咬唇）与舌尖状态，消除 90% 的混合形冲突。

## 框架 2: 无冲突加算目标体架构 (Additive Blendshape Architecture)
- **来源**: Chapter 6
- **核心逻辑**:
  传统目标体直接包含整个下半张脸的绝对位移，导致“微笑（Smile）”与“张嘴（Open）”同时激活时，嘴角受到双倍拉扯而畸变。
  加算目标体架构（Additive Blendshapes）将每个关键形定义为相对中性脸的差分向量（Delta Vectors），并通过渐变权重脚本（`ss2_blend_taper.mel`）在对称中线处施加平滑余弦衰减（Cosine Falloff），使得左/右半张脸的形状能够以独立通道完全解耦，且任意两形状叠加时不发生顶点超调。

## 框架 3: 二维滑块控制器界面系统 (2D Box Slider Interface System)
- **来源**: Chapter 12
- **核心逻辑**:
  通过在三维视图或独立控制面板中构建带有矩形边界约束的二维手柄（2D Joystick / Slider Controls），直观驱动底层 Driven Keys：
  1. **口型主滑块**: X 轴映射 Wide <-> Narrow，Y 轴映射 Open <-> Closed；
  2. **眉毛主滑块**: 区分左眉与右眉，X 轴映射 Squeeze（聚拢）<-> Relax，Y 轴映射 Up <-> Down；
  3. **眼睑滑块**: X 轴控制 Squint（下眼睑紧绷），Y 轴控制 Blink/Lid Height。
  控制器手柄在几何边界内的物理移动直接限制了非法形状的共存，极大简化动画师的心智负担。

## 框架 4: 对白口型分层四步工作流 (Layered 4-Step Lip Sync Pipeline)
- **来源**: Chapter 4 & Chapter 14
- **核心逻辑**:
  口型动画严禁“单帧单帧逐个微调全部控制器”。Osipa 制定了不可逾越的四步分层推进流程：
  1. **第一步：主节奏开合（Open/Closed Pass）**：仅依据声波振幅和元音核心，定下嘴巴开合的关键极值，忽略所有宽窄与细节；
  2. **第二步：宽窄形态贯穿（Wide/Narrow Pass）**：顺应音素的辅音与元音属性，在时间轴上铺设宽（EE/AH）与窄（OO/W）的形态过渡；
  3. **第三步：硬性接触辅音锁定（Hard Consonant Clamping）**：精确锁死 MBP 闭合与 FV 唇齿接触帧，应用“提前 2-3 帧闭合”的视错觉超前量法则；
  4. **第四步：舌头、上唇与下巴滞后微调（Finesse Pass）**：添加舌尖上挑（L/TH）及下巴相对于嘴唇的惯性延迟（1 帧 Offset）。

## 框架 5: 面部环形循环布线拓扑规范 (Facial Edge-Flow Loop Topology)
- **来源**: Chapter 5, 8 & 10
- **核心逻辑**:
  三维面部网格的布线必须严格服从表情肌肉的收缩方向：
  1. **口轮匝肌循环环（Mouth Loops）**：围绕嘴唇呈同心椭圆环状展开，确保嘴唇拉伸和收缩时几何面均匀变形；
  2. **眼轮匝肌循环环（Eye Loops）**：围绕眼眶闭合环形排布，支撑眼睑上下眨眼闭合；
  3. **八字鼻唇沟环（Nasolabial Loop）**：从鼻翼两侧向下延伸包裹口轮匝肌，形成法令纹自然折叠缓冲区，阻断嘴部运动向面颊的异常拉扯；
  4. **极点/五星点（5-Star Poles）位置约束**：五星点严禁落在唇红缘（Lip Line）或眼睑边缘，必须隐藏在颧骨平坦区或下巴后侧。

## 框架 6: 眼球追踪与眼睑联动系统 (Eye Aim & Lid-Follow Mechanics)
- **来源**: Chapter 7 & Chapter 11
- **核心逻辑**:
  “死鱼眼”和“假面具感”的根源是眼球转动与眼睑脱节。真实解剖中，眼球上下旋转会直接推挤上下眼睑：
  1. **Lid-Follow 算法**：通过表达式或驱动键，当眼球注视点向上看时，上眼睑自动跟随提升 25-35%，下眼睑跟随提升 10-15%；当眼球向下看时，上眼睑跟随下落 35-45%；
  2. **扫视跳跃（Saccades / Eye Darts）**：眼球从点 A 移动到点 B 绝不能使用线性平滑过渡（Linear Spline），而是在 1 帧内瞬时跳跃到位（Saccadic Movement），随后定格 10-30 帧，模拟人类视觉注视机制。

## 框架 7: 局部表情与全局 Squoosh 分层变形架构 (Local Expression vs Global Squoosh Layering)
- **来源**: Chapter 13
- **核心逻辑**:
  角色在做出大幅度下潜、惊吓或受击时需要整体头部 Squash & Stretch，但如果在单个 Blendshape 中混合整体头部形变，会彻底毁掉所有局部眼部和口型绑定。
  Osipa 提出解耦方案：
  - **局部层（Local Layer）**：由 Blendshapes 与骨骼蒙皮驱动面部精细表情（眼、鼻、口）；
  - **中间层（Base Mesh Evaluation）**：稳定计算局部变形后的纯几何体；
  - **全局层（Global Squoosh Layer）**：通过包裹变形器（Wrap Deformer）或次级晶格（Secondary Lattice），在局部表情之上施加整体头部的体积守恒挤压拉伸与倾斜，实现局部表演与全局卡通张力的完美共存。
