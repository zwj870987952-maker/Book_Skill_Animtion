---
id: cap.facial-expressions.fat-pads-soft-tissue-wrinkles
title: 面部脂肪垫、支持韧带锚点与正交皮肤张力皱纹法则
type: principle
tier: core
status: verified
sources:
  - book: Anatomy of Facial Expression
    chapter: Soft Tissues, Fat Pads & Wrinkle Mechanics (P128-135)
summary: 解析浅层颧脂肪垫、深层 SOOF/ROOF 脂肪垫、骨性韧带锚点阻隔与肌肉收缩正交垂向皮肤皱折物理。
requirements:
  - 严格遵守兰格氏线与肌肉收缩矢量的正交垂直折痕法则
  - 分离浅层可移动脂肪垫与深层固定结构，定义真骨性支持韧带的几何阻隔边界
antirequirements:
  - 严禁在三维模型表面雕刻与皮下肌纤维收缩轴平行的动态皱纹
  - 严禁将脂肪垫视为刚性整体或均匀无区隔的流体
keywords:
  - fat-pads
  - malar-pad
  - soof
  - roof
  - retaining-ligaments
  - orthogonal-wrinkles
  - langers-lines
  - skin-turgor
also_read:
  - cap.facial-expressions.cranial-landmarks-geometry
  - cap.facial-expressions.duchenne-smile-vs-social-mask
---

# 面部脂肪垫、支持韧带锚点与正交皮肤张力皱纹法则

## 1. 原理与五层软组织解剖架构

面部的生动质感、高光分布以及衰老和表情褶皱，并非由骨骼和肌肉直接与表皮贴合形成，而是取决于面部五层连续软组织系统（Soft Tissue Architecture）的剪切互动：

1. **五层解剖分层系统（Five Anatomical Layers）**：
   - **第 1 层：皮肤（Skin）**（表皮与真皮，富含弹性纤维与胶原蛋白，具有兰格氏线固有张力）。
   - **第 2 层：浅层皮下脂肪垫（Subcutaneous Fat Compartments）**：
     - 包括颧脂肪垫（Malar fat pad）、鼻唇脂肪垫（Nasolabial fat pad）、眶周浅层脂肪。这些脂肪垫是表情推挤中产生“苹果肌隆起”的直接体积来源。
   - **第 3 层：表浅肌肉腱膜系统（SMAS）**：
     - 包含所有面部表情肌（如眼轮匝肌、口轮匝肌、大颧肌、额肌），是产生收缩动力的引擎层。
   - **第 4 层：深层间隙与深层脂肪垫（Deep Spaces & Deep Fat）**：
     - 包括眼轮匝肌下脂肪（**SOOF - Sub-Orbicularis Oculi Fat**）与眼轮匝肌后脂肪（**ROOF - Retro-Orbicularis Oculi Fat**），垫在骨膜与肌肉之间，提供肌肉无摩擦滑移的生物润滑。
   - **第 5 层：骨膜与颅骨基底（Periosteum & Bone）**。
2. **真性骨性支持韧带（True Bony Retaining Ligaments）**：
   - **颧支持韧带（Zygomatic Ligament / McGregor's Patch）**：起自颧弓骨膜，穿透所有层级垂直锚定于皮肤。
   - **下颌支持韧带（Mandibular Ligament）**：起自下颌下缘前三分之一骨面，锚定下巴侧边缘。
   - *力学阻隔效应*：韧带如同牢不可破的木桩，软组织和脂肪垫在表情运动或重力下垂时，会被阻隔在韧带线上，从而形成天然的结构性分界凹槽（如鼻唇沟外侧隆起与木偶纹断裂点）。

---

## 2. 核心量化指标与正交折痕物理定律

### 正交张力折痕定律（Orthogonal Wrinkle Generation Law）
动态皮肤折痕（Dynamic Skin Creases）是表皮在皮下肌纤维向心缩短挤压下产生的几何屈曲失稳（Euler Buckling）。
折痕的方向 $\vec{T}_{\text{wrinkle}}$ 恒严格垂直于肌纤维收缩矢量 $\vec{F}_{\text{muscle}}$：
$$\vec{T}_{\text{wrinkle}} \cdot \vec{F}_{\text{muscle}} = 0$$

### 全面部正交褶皱动力学映射表

| 面部解剖区域 | 驱动肌束 | 肌肉收缩轴向 | 动态皮肤皱纹走向 | 衰老/极限静态加深表现 |
| :--- | :--- | :--- | :--- | :--- |
| **前额区** | 枕额肌额腹 | 纵向垂直 ($\vec{Y}$) | **完全水平横向 ($\vec{X}$)** | 额头横纹（抬头纹） |
| **眉间印堂区** | 皱眉肌 | 水平横向 ($\vec{X}$) | **垂直纵向 ($\vec{Y}$)** | 双侧或三侧“川字纹” |
| **鼻根鞍区** | 降眉间肌 | 纵向垂直 ($\vec{Y}$) | **水平横向 ($\vec{X}$)** | 鼻梁横纹 |
| **外眦眼角区** | 眼轮匝肌外眶环 | 环形向心切线 | **向外发散放射状** | 鱼尾纹（Crow's feet） |
| **面颊中段** | 颧大肌 / 提唇肌 | 斜向 $45^{\circ}$ 外上 | **斜向 $135^{\circ}$ 深化** | 鼻唇沟（法令纹）陡峭折叠 |
| **下唇颏沟区** | 颏肌 | 垂直向上 ($\vec{Y}$) | **水平弧形 + 点状点阵** | 颏唇沟加深与橘皮凹坑 |
| **下颌缘区** | 颈阔肌 | 垂直向下 ($\vec{Y}$) | **水平向环状项圈纹** | 颈横纹与火鸡脖折叠 |

---

## 3. 浅层脂肪垫位移与体积守恒流形

- **脂肪滑移方程**：
  浅层脂肪垫并非弹性海绵，其压缩系数趋近于不可压缩流体（Poisson's ratio $\nu \approx 0.48$）。
  当面部肌肉收缩导致沿肌肉切线方向的长度压缩 $\Delta L < 0$ 时，脂肪垫沿表面法向（法线高度 $H$）必然发生大幅度的正向隆起 $\Delta H > 0$：
  $$\frac{\Delta H}{H_0} \approx -\nu \left( \frac{\Delta L}{X_0} + \frac{\Delta W}{Y_0} \right)$$
  - 这正是微笑时颧脂肪垫从平缓分布瞬间凝聚为坚挺高光的“苹果肌”的物理原因。

---

## 4. 工业级执行步骤与落地流水线

1. **第 1 步：韧带锚点顶点遮罩绘制（Ligament Mask Painting）**
   - 在角色拓扑中，绘制颧支持韧带与下颌支持韧带的黑白权重遮罩（Ligament Mask）；
   - 设置这些顶点在次级软组织模拟中具有极高的弹簧刚度，确保脂肪滑移在此处被自然阻挡堆叠。
2. **第 2 步：正交皱纹张力贴图生成（Tension-Driven Wrinkle Maps）**
   - 使用 Maya 或 UE5 的 Tension Map / Pose Space Deformation（PSD）；
   - 当检测到特定边长的压缩率超过 15% 时，沿正交垂直方向触发微多边形细分位移或法线混合。
3. **第 3 步：深浅层脂肪垫分层雕刻**
   - 雕刻老年角色的松弛面部时，将颧脂肪垫沿颧骨斜面下垂 5-8mm 堆叠于鼻唇沟上方；
   - 青年角色则使 SOOF 和颧脂肪垫紧紧贴合眶下缘，呈现饱满连贯的中面部高光转折。

---

## 5. 典型案例与对比

- **青年真笑 vs 老年真笑的软组织堆叠**：
  - **青年角色**：皮下胶原蛋白丰富，AU 6 + AU 12 激活时，颧脂肪垫形成一颗光洁平滑、高光汇聚的半球形苹果肌，眼尾仅现浅淡生动的 2 条鱼尾纹；
  - **老年角色**：韧带与皮肤松弛，浅层脂肪垫下垂，同样激活 AU 6 + AU 12 时，鼻唇沟上方堆叠出厚重的皮肤脂肪皱褶帘，外眼角爆发出 5-6 条深邃蔓延至太阳穴的刀刻状鱼尾纹。

---

## 6. 常见反模式与纠偏排障

- **反模式 1：平行于肌肉的荒谬皱纹（Parallel Muscle Wrinkle Fault）**
  - *现象*：额头上画出了纵向竖条纹，或者外眼角画出了环绕眼眶的同心圆纹理。
  - *纠偏*：严格按照欧拉屈曲失稳公式，强制所有动态折痕旋转 $90^{\circ}$，保持与驱动肌纤维正交。
- **反模式 2：塑料充气脸（Plastic Balloon Inflation）**
  - *现象*：微笑时苹果肌向外鼓起，但法令纹一点也不加深，整个脸部像充气的硅胶娃娃。
  - *纠偏*：建立脂肪隆起与韧带折痕深化的联动，脂肪垫每隆起 1mm，其边缘的鼻唇沟必须向内下陷 0.5mm。

---

## 7. 质量验收硬门

- [ ] 所有动态生成的皮肤皱纹方向与皮下肌纤维收缩矢量严格正交（夹角误差 $< 5^{\circ}$）。
- [ ] 颧支持韧带与下颌支持韧带区域具备正确的软组织位移阻隔效应。
- [ ] 浅层脂肪垫在肌肉收缩时遵循体积守恒定律，产生自然的高光苹果肌隆起。
- [ ] 青年与老年角色在软组织松弛度与折痕深度上具有明确的解剖学梯队。
