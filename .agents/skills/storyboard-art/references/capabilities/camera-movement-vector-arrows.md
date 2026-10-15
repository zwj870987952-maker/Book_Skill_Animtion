---
id: cap.storyboard-art.camera-movement-vector-arrows
title: 摄影机运动符号学与三维箭头标注规范（Pan, Tilt, Dolly, Zoom, Crane, Track）
type: technique
tier: core
status: verified
sources:
  - book: The Art of the Storyboard
    chapter: Part 2 - Actions and Arrows & Camera Moves (P55-88)
summary: 统一摄影机空心粗箭头/框式引导线符号系统，彻底消除与角色位移箭头的工业沟通歧义。
requirements:
  - 摄影机运动必须统一使用画框外侧或跨画框的空心双线粗箭头，并附带专业英文缩写
  - 必须严格区分 Dolly In/Out（物理位移有透视视差）与 Zoom In/Out（光学变焦无透视变化）
antirequirements:
  - 严禁在画框内使用细实心箭头表示摄像机运动（会导致误判为角色走位）
  - 严禁省略摄像机运动的起止画框（Start/End Frame）标记
keywords:
  - camera-movements
  - vector-arrows
  - pan
  - tilt
  - dolly
  - zoom
  - crane
  - tracking-shot
  - storyboard-symbology
also_read:
  - subject-action-directional-arrows
  - shot-scale-visual-hierarchy
---

# 摄影机运动符号学与三维箭头标注规范（Pan, Tilt, Dolly, Zoom, Crane, Track）

## 1. 原理与工业符号契约

故事板画师与现场摄制组（导演、摄影指导 DP、移动车掌机 Dolly Grip、斯坦尼康摄影师 Steadicam Operator）之间，依赖一套极其严格的**二维图纸三维运动符号契约**。在静止的纸面或数字画布上，如果无法清晰表达机位的空间位移、旋转轴向与透视变化，整个分镜蓝图将彻底失去指导生产的工业价值。

好莱坞工业标准确立了以下铁律：
- **摄影机运动（Camera Move）**：恒定采用**空心双线大箭头（Hollow Double-lined Arrows）**，通常标注在画框外部边缘，或作为连接起始画框（Frame A）与终止画框（Frame B）的跨框对角引导线；
- **角色/道具运动（Subject Action）**：恒定采用**画框内部的细实心单线箭头（Solid Thin Arrows）**。两者在视觉重量与层级上具有绝对区分度。

---

## 2. 六大经典摄影机运动符号学规范

### 标准摄影机运动符号标注全览表

| 运动类型 | 工业标准术语 | 运动物理本质 | 标准图纸符号与箭头规范 | 透视与视差特征 |
| :--- | :--- | :--- | :--- | :--- |
| **水平摇镜** | **PAN (Left / Right)** | 机位不动，机身沿垂直轴水平旋转 | 画框外侧水平横向的空心双线箭头；若大范围摇镜，绘制相交的双画框并以弯曲水平箭头连接 | 背景与前景产生纯水平转动，无纵深透视改变 |
| **垂直俯仰** | **TILT (Up / Down)** | 机位不动，机身沿水平轴上下仰俯 | 画框外侧垂直纵向空心双线箭头，标明 `TILT UP` 或 `TILT DOWN` | 地平线在画框中上下位移，仰角产生低透视收缩 |
| **轨道车推拉** | **DOLLY (In / Out)** | 机身搭载在轨道车上沿光轴前后物理位移 | **大画框内嵌套小画框**：四角拉出向内的对角透视引导线表示 `DOLLY IN`；反之向外为 `DOLLY OUT` | **强烈的动态透视视差（Parallax）**：前景移动极快，背景移动缓慢 |
| **光学变焦** | **ZOOM (In / Out)** | 机位绝对静止，镜头机械调整焦距 | 同样使用内嵌画框，但在面板说明栏加粗标注 **`ZOOM IN`**，箭头加“Z”字标识 | **无真实三维视差**：画面像扁平贴图一样被单纯放大或缩小，前后景比例不变 |
| **横向移镜** | **TRACK / TRUCK** | 机身搭载轨道车平行于走位角色横移 | 画框底部通栏双线空心箭头，标明 `TRACK WITH CHARACTER` | 前景障碍物高速掠过，产生强烈的侧向景深飞掠感 |
| **升降摇臂** | **BOOM / CRANE** | 机身安装在大型机械臂上进行高空三维升降 | 带立体投影的垂直或弧形空心箭头，标注高度落差（如 `CRANE DOWN from 5m to 1m`） | 剧烈的三维空间俯仰与景别维度重构 |

---

## 3. Dolly（推轨）vs Zoom（变焦）的本质区别与图纸表达

- **物理与心理学本质差异**：
  - **Dolly In（物理推进）**：摄影机穿行于三维物理空间。随着镜头逼近，角色鼻子和耳朵的透视角度发生剧烈变化，背景向两侧迅速退去（强视差）。受众在潜意识中感觉“我也跟着走进了房间”，产生强烈的临场感与代入感；
  - **Zoom In（光学放大）**：摄影机像狙击手透过望远镜看目标。背景没有被剥离，反而景深被压缩拉平。受众在潜意识中感觉“我坐在原地，被强行推近了一个偷窥视野”，产生冷静、旁观或被监视的疏离感。
- **图纸表示法**：
  在面板上表示推进时，必须在框内小画框四角引出虚线，并在动作栏明确写出：
  - `DOLLY IN to CU of Jack (Real Camera Move)` 或
  - `ZOOM IN to Jack's eyes (Optical Move, Static Tripod)`。

---

## 4. 工业级执行步骤与落地流水线

1. **第 1 步：起始画框与终止画框设定（Frame A to Frame B）**
   - 凡是包含大幅度摄影机运动的镜头，严禁只画一个静态面板；
   - 必须绘制两联或三联面板：面板 A（运动起点）与面板 B（运动终点），中间用空心箭头跨框贯通。
2. **第 2 步：运动时长与平滑度技术参数注明**
   - 在面板下方技术说明栏必须规范书写：
     - `Camera: DOLLY IN (Frame A: MS -> Frame B: ECU)`；
     - `Duration: 3.5 seconds`；
     - `Grip/Support: Track on floor / Steadicam`。
3. **第 3 步：机位辅助顶视图绘制（Overhead Diagram）**
   - 在复杂场面调度（如围绕角色的 360° 环绕 Track 或长距离 Crane 升降）中，在分镜页空白处绘制场景俯视图，标明机位运动导轨弧线与镜头朝向。

---

## 5. 典型案例与对比

- **惊悚片经典“希区柯克变焦 / 眩晕镜头”（Dolly Zoom / Vertigo Effect）**：
  - **物理原理**：摄影机一边向后推轨（Dolly Out），一边镜头同步向前光学变焦放大（Zoom In），保持主体人物在画框中大小恒定不变；
  - **分镜图纸表达**：
    - Panel 1（起点）：男主 MS 居中，身后走廊透视正常；
    - Panel 2（终点）：男主依然是 MS 且大小完全未变，但背景走廊墙壁被疯狂压缩、拉伸扭曲；
    - 箭头标注：画框四角标注向外的双线箭头（`DOLLY OUT`），同时在人物周围标注向内挤压的变焦箭头（`ZOOM IN`），说明栏大写高亮：`VERTIGO EFFECT: DOLLY OUT & ZOOM IN SIMULTANEOUSLY`。

---

## 6. 常见反模式与纠偏排障

- **反模式 1：黑箭头乱飞（The Stray Black Arrow Trap）**
  - *现象*：画面里画了三四个黑色实心单线箭头，既指着汽车，又指着天空，又指着画框边缘。
  - *纠偏*：彻底清洗符号层。机位运动全部移至画框边缘外侧做成空心粗箭头；框内仅保留 1 个指向汽车行进方向的实心细箭头。
- **反模式 2：把横摇画成推拉（Pan Confused with Dolly）**
  - *现象*：镜头本该是机位固定的水平 Pan，画师却画了四个对角线内收线。
  - *纠偏*：纠正为纯水平贯穿的横向双线箭头，标明 `PAN RIGHT`。

---

## 7. 质量验收硬门

- [ ] 摄影机运动箭头严格采用画框外侧或跨框的空心双线粗箭头，与框内角色位移完全绝缘。
- [ ] 所有推拉与变焦镜头明确标注为 Dolly（物理移位）还是 Zoom（光学变焦）。
- [ ] 复合运动（如 Pan + Tilt 或 Crane Down）标明了起止画框（Frame A/B）与运动时长秒数。
- [ ] 复杂长镜头配齐了俯视机位路线图（Overhead Setup），满足现场摄影组布轨需求。
