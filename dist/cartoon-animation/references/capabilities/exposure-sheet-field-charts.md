## R — 原文 (Reading)

> “The exposure sheet (or dope sheet) is the blueprint of the animated film. It shows every frame of the scene, what drawing is on each level, where camera moves occur, and where dialogue sounds fall. The field chart establishes the dimensions of the scene. Camera moves, truck-ins, and pans must be planned with mathematical accuracy on these charts to prevent jarring jumps.”
> 
> —— Preston Blair, *Cartoon Animation*, Chapter 5, pp. 196–203, 204–215

## I — 方法论骨架 (Interpretation)

动画制作绝非画家的单兵作战，而是一套严丝合缝的工业工程体系，其核心技术中枢由两件工具构成：
1. **规格框网格系统 (The Field Chart System)**:
   - 动画摄影台以 12-Field（或 16-Field）为通用基准。中心为 12-Center；
   - 每一个 Field 单位对应固定的毫米/英寸宽度；
   - **平移摇镜头 (Pan Background)**: 背景长图纸在摄影台上的移动，必须在规格框上标注严格的每帧增量刻度（如每格移动 $1/4$ 吋），确保速度绝对均匀或带有精准加减速；
2. **摄影表/律表设计 (The Exposure Sheet / Dope Sheet)**:
   - 每一页包含 72 帧（即整整 3 秒，在 24fps 下）；
   - **纵向列结构**:
     - Column 1: 对白录音轨（Dialogue Track），精确到每帧的音素音标；
     - Column 2–5: 动画图层分层（Levels：如背景 BG、角色身体 A 层、眼球与口型 B 层、前景遮挡 C 层）；
     - Column 6: 摄影机运动与转场指示（Camera Instructions / Field / Pan / Fade / Dissolve）；
3. **图层上下逻辑 (Layering & Peg Registration)**:
   - 依靠定位尺（Pegs）保证几十层赛璐珞片/数字图层在数千帧内像素级重合，严禁图层穿插穿模。

## A1 — 案例 (Application Example)

### 书中例题: 角色在平移背景上奔跑的 12-Field 对位律表设计 (worked_example)
- **任务**: 制作一段 3 秒（72 帧）的镜头：角色居中奔跑，背景向后快速平移（Pan）。
- **执行过程**:
  1. 摄影机与画幅：设定为 10-Field Center，摄影机固定不动；
  2. 图层划分：
     - Level 1 (BG): 宽长背景画，在律表标注“PAN EAST 24 inches in 72 frames, 1/3 inch per frame on 1s”；
     - Level 2 (Body): 角色身体奔跑循环（8 帧循环，在律表依次填入 1, 2, 3, 4, 5, 6, 7, 8 并重复 9 次）；
     - Level 3 (Dust): 脚底扬尘烟团循环；
  3. 平移速度验证：每帧移动 $1/3$ 吋，24fps 播放，背景移动速度平滑，强制拍单格（On 1s）以防竖线频闪。
- **结果**: 背景平移与角色奔跑速度完美契合，毫无滑步与画面撕裂。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 规划动画分层绘制（身体、口型、道具、背景分层制作与合成）；
2. 二维动画/定格动画摄影表 Dope Sheet 与律表软件（如 Toon Boom Harmony, TVPaint, Clip Studio）工程设置；
3. 排查背景平移抖动、图层上下穿插错误或摄影机运镜不均。

### 语言信号 (Triggers)
- "动画律表 Exposure sheet / Dope sheet 怎么填"
- "规格框 12-Field chart 网格怎么看"
- "背景平移 pan 速度刻度计算"
- "多图层分层动画合成对位"

### 与相邻能力的区分
- 与 `camera-motion-timing` (Timing 领域) 的区别: 本能力用于传统/数字动画工业级摄影表填表格式、图层层级（Levels）与 Field Chart 坐标系工程规范；`camera-motion` 侧重频闪视网膜生理限制。
- 与 `acting-poses-staging` 的区别: 本能力是技术工单与图层数据契约；`acting-poses` 是镜头表演调度。

## E — 可执行步骤 (Execution)

1. **确立镜头 Field 规格与安全框**:
   - 设定画幅大小（如 12-Field）；
   - 标出摄影机中心（Center）与边界裁切安全区。
2. **绘制多图层划分表 (Layer Stacking Order)**:
   - 从下到上明确编号：BG(背景) $\to$ Layer A(主干) $\to$ Layer B(次级/五官) $\to$ FG(前景遮蔽)。
3. **填写摄影律表时间轴 (Dope Sheet 72 帧格点)**:
   - 将对白波形逐帧抄录在音轨列；
   - 将各图层画稿编号填入对应列（拍单格每行填号，拍双格隔行填号）；
   - 标注摄影机平移距离与起始/结束帧。
4. **输出标准交付契约**:
   - 输出完整的 72 帧标准律表表格、图层堆叠结构图与 Field 平移刻度清单。

## B — 边界与反模式 (Boundary)

### 失效边界
- 三维现代 3D 摄像机自由轨道拍摄（无固定 Field 规格限制），依赖 Maya/Blender 虚拟相机 Transform 曲线，但图层时间轴与律表对齐逻辑依然通用。

### 常见反模式
- **背景平移双格频闪**: 背景平移却按双格（On 2s）拍摄，导致背景背景线在播放时剧烈抖动频闪；
- **图层编号混乱**: 身体和口型画在同一张图层上，导致每一次换口型都要重画整套身体，大幅增加工作量。
