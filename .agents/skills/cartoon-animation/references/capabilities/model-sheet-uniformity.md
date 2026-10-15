## R — 原文 (Reading)

> “A model sheet is a reference sheet containing drawings of an animated character from different angles, with notes on proportion, construction, and facial expressions. Its primary purpose is to ensure uniformity throughout a production, so that all animators and cleanup artists draw the character identically from scene to scene.”
> 
> —— Preston Blair, *Cartoon Animation*, Chapter 5, pp. 216–224

## I — 方法论骨架 (Interpretation)

动画团队工业化协同生产的基石，在于标准化造型表（Model Sheet）规范：
1. **多视角旋转图 (The Turnaround / 5-View Guide)**:
   - 包含角色正对镜头（Front）、正侧面（Side）、3/4 正侧面（3/4 Front）、3/4 背面（3/4 Back）以及正背面（Back）；
   - **绝对水平基准线法则 (Grid Alignment)**: 必须在同一水平网格下绘制，确保所有视角的头顶、眼睛中心、下巴、腰带、膝盖与足底处于绝对水平高度，严禁侧视图比正视图矮半截；
2. **体块剖解图 (Construction Breakdown)**:
   - 在成稿旁边必须附带剥离毛发与服装的裸几何体块图（显示内部正圆球体、蛋形、梨形及经纬十字线），向原画师明示骨骼结构；
3. **比例标尺与相对比例表 (Scale & Comparative Size)**:
   - 标注头身比网格（如 4 头高）；
   - 提供角色与主角、配角、主要道具（如汽车、房屋）并排站立的“相对尺度对照图”（Comparative Size Sheet），防止不同镜头中角色忽大忽小；
4. **标志性表情与经典姿态 (Expression & Action Sheet)**:
   - 囊括大喜、大悲、吃惊、愤怒等极端表情与奔跑、跳跃的标准剪影，锁定角色神韵。

## A1 — 案例 (Application Example)

### 书中例题: 卡通小狗 4 视角旋转造型表与网格标尺构建 (worked_example)
- **任务**: 为外包团队制作一套用于 50 人协同动画生产的标准小狗角色 Model Sheet。
- **执行过程**:
  1. 比例标尺：画出 4 个头长的垂直标尺网格，拉出 8 条贯通全画面的水平辅助红线（头顶、眉线、鼻尖、下巴、肩线、腰带、膝关节、地面）；
  2. 绘制正面图：确认面部完全对称，两耳展开；
  3. 绘制 3/4 侧面图：利用蛋形十字经纬线弯曲透视，近处眼睛大、远处眼睛小且紧贴头部边缘轮廓；五官水平高度严格咬合辅助红线；
  4. 绘制正侧面图：口吻部突出长度为 0.8 个头宽，下巴和后脑勺水平对准；
  5. 绘制背面图：标注尾巴根部插槽与背部斑纹位置；
  6. 附注说明：注明“无论任何角度，鼻子永远为圆球形，不可画成尖角；双耳转动跟随头骨倾斜”。
- **结果**: 团队交出的数百张画稿完全保持一致，彻底杜绝了角色忽胖忽瘦的生产事故。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 动画前期角色设定定稿、三视图设计与团队设计资产交接；
2. 3D 角色高精建模导入参考图（Image Planes）对齐；
3. 排查镜头切换时角色“长相忽胖忽瘦”、“不同画师画得不像同一个人”。

### 语言信号 (Triggers)
- "角色标准造型表 Model sheet 怎么规范绘制"
- "角色三视图 turnaround 怎么对齐比例和高度"
- "如何保证动画团队协同绘制角色不走形"
- "角色相对尺度对照图 Comparative size sheet"

### 与相邻能力的区分
- 与 `character-construction-proportions` 的区别: 本能力是将体块与比例规范化为工业级生产蓝图交付物；`character-construction` 侧重单个角色的几何体块绘画步骤。
- 与 `exposure-sheet-field-charts` 的区别: 本能力是角色美术造型契约；`exposure-sheet` 是逐帧拍摄生产调度律表。

## E — 可执行步骤 (Execution)

1. **建立水平标尺网格 (Alignment Grid)**:
   - 建立画布，拉出不少于 6 条贯通画面的水平线（头顶、眼线、下巴、腰、膝、地面）。
2. **绘制核心多视角旋转 (Turnaround)**:
   - 依次绘制 Front（正面）、3/4 Front（3/4侧面）、Profile（正侧面）与 Back（背面）；
   - 严格核验：每一视角的五官与关节必须精准落在对应水平线上。
3. **添加体块几何剖解示意**:
   - 绘制裸体块结构（圆形头骨、蛋形透视十字线、梨形躯干、关节插槽）。
4. **制作相对尺度对照表 (若有多个角色)**:
   - 将所有角色放置在同一地平线上，标注彼此头顶相对高度。
5. **输出标准交付契约**:
   - 输出三视图/五视图工程规范图、体块结构解剖图与美术红线禁忌批注。

## B — 边界与反模式 (Boundary)

### 失效边界
- 纯个人自由艺术实验短片，追求随心所欲的形变流体画风（Morphing animation），无需恪守严苛的工业级三视图一致性约束。

### 常见反模式
- **侧视图身高塌陷**: 侧视图下角色比正视图矮了半个头或腰部错位，导致 3D 建模师在三维空间中无法对齐空间顶点；
- **缺乏透视经纬线**: 只有漂亮描边线稿，没有内部球体透视线，其他画师在绘制旋转过渡时不知道五官该如何贴合。
