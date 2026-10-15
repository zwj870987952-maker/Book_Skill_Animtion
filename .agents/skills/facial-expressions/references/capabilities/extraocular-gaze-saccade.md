---
id: cap.facial-expressions.extraocular-gaze-saccade
title: 眼外肌与视线扫视协同注视机制（AU 61-64）
type: technique
tier: high
status: verified
sources:
  - book: Anatomy of Facial Expression
    chapter: Extraocular Muscles & Gaze Dynamics (P62-73)
summary: 基于四直肌与双斜肌矢量合成实现极速 1 帧扫视跳跃（Saccade）、双眼聚焦注视与斜睨微表情。
requirements:
  - 眼球转动必须符合四直肌与双斜肌矢量运动学，并带动上眼睑跟随滑移
  - 视线目标转移必须采用极速扫视跳跃（Saccade），严禁平滑缓动慢入慢出
antirequirements:
  - 严禁眼球匀速慢速移动（漂浮死眼）
  - 严禁下视或上视时上眼睑边缘保持静态不动
keywords:
  - extraocular-muscles
  - gaze-direction
  - saccade
  - au61
  - au62
  - au63
  - au64
  - eyeball-rotation
also_read:
  - cap.facial-expressions.orbicularis-oculi-eyelid-mechanics
  - cap.facial-expressions.seven-universal-emotions-facs
---

# 眼外肌与视线扫视协同注视机制（AU 61-64）

## 1. 原理与解剖动力学模型

眼球注视方向与视线微运动是揭示角色心理潜台词（思考、说谎、警惕、倾慕、轻蔑）的灵魂所在。眼球的运动由眼眶深部附着的 6 块外在眼肌（Extraocular Muscles）精确控制：

1. **四条直肌（Rectus Muscles）**：
   - **上直肌（Superior Rectus - AU 63 Up）**：向上转动眼球。
   - **下直肌（Inferior Rectus - AU 64 Down）**：向下转动眼球。
   - **内直肌（Medial Rectus - AU 61/62 Inward）**：向鼻梁方向内收眼球（控制双眼聚焦点对焦）。
   - **外直肌（Lateral Rectus - AU 61/62 Outward）**：向太阳穴方向外展眼球。
2. **两条斜肌（Oblique Muscles）**：
   - **上斜肌（Superior Oblique）** 与 **下斜肌（Inferior Oblique）**：控制眼球的扭转（Torsion）以及在内收状态下的下转与上转。
3. **眼球扫视生理学（Saccadic Eye Movement）**：
   - 人类视觉在转换目标时，并非连续平滑旋转，而是以极高的角速度（高达 400°-900°/秒）在 **1-2 帧（约 30-50毫秒）** 内完成瞬间跳跃（Saccade）；跳跃完成后在目标落点进行微小震颤并锁定。只有在持续跟踪平滑移动目标（Smooth Pursuit）或前庭眼反射（VOR）头部旋转时，眼球才呈现连续逆向转动。

---

## 2. 核心量化指标与运动学参数

### 视线运动单元 (FACS AU 61-64) 规范

| 动作单元 | 驱动肌群 | 最大生理转角 | 上眼睑伴随位移率 | 典型心理微表情 |
| :--- | :--- | :--- | :--- | :--- |
| **AU 61 (向左看)** | 左眼外直肌 + 右眼内直肌 | $\pm 35^{\circ}$ | 无显著纵向位移 | 侧向打量、警惕周遭、余光探查 |
| **AU 62 (向右看)** | 右眼外直肌 + 左眼内直肌 | $\pm 35^{\circ}$ | 无显著纵向位移 | 侧向打量、警惕周遭、余光探查 |
| **AU 63 (向上看)** | 双眼上直肌 + 下斜肌 | $+25^{\circ} \sim +30^{\circ}$ | 上眼睑跟随上提 3 - 5 mm | 回忆、无聊、白眼挑衅、祈祷 |
| **AU 64 (向下看)** | 双眼下直肌 + 上斜肌 | $-30^{\circ} \sim -35^{\circ}$ | 上眼睑跟随下垂 5 - 7 mm | 羞怯、内疚、沉思、极度悲痛 |
| **双眼会聚 (Vergence)** | 双眼内直肌协同收缩 | 鼻侧倾角 $5^{\circ} \sim 15^{\circ}$ | 眼睑微窄 | 近距离特写聚焦（看鼻尖、读信） |

---

## 3. 眼睑伴随滑移法则（Lid-Follow Mechanics）

- **垂直跟随公式**：
  上眼睑边缘在纵向上的位移量 $\Delta Y_{\text{lid}}$ 必须与眼球垂直俯仰角 $\theta_{\text{pitch}}$ 保持强耦合关系：
  $$\Delta Y_{\text{lid}} = K_{\text{follow}} \cdot R \cdot \sin(\theta_{\text{pitch}})$$
  其中 $R \approx 12\text{mm}$，$K_{\text{follow}} \approx 0.65 - 0.75$。
  - 当眼球向下旋转 $30^{\circ}$ 时，上眼睑必须自然滑落约 $6\text{mm}$，完全遮蔽角膜大半部分；若上眼睑不跟随下落，角膜上方将出现巨大的不自然巩膜露白（Graefe's Sign 病态眼）。

---

## 4. 工业级执行步骤与落地流水线

1. **第 1 步：双眼视线独立控制与对焦目标（Gaze Aim Rig）**
   - 设置单个世界空间注视目标（`gaze_target_ctrl`），双眼通过 Aim 约束锁定目标；
   - 提供双眼独立微调轴（`eye_L_offset`, `eye_R_offset`），用于实现斜视、斗鸡眼（对焦近物）或角色特定眼神偏斜。
2. **第 2 步：上眼睑自动跟随驱动器（Eyelid Driver Setup）**
   - 将眼球关节的 $X$ 轴旋转（Pitch）通过 Set Driven Key 或表达式连接至上眼睑主骨骼或 `lid_follow` BlendShape；
   - 确保眼球向上翻时上眼睑自动退缩，眼球向下看时上眼睑平滑滑落。
3. **第 3 步：关键帧扫视曲线阶跃化（Stepped Saccade Curve）**
   - 在眼神转移的关键帧中，严禁给眼神属性打平滑的 Bezier 缓动曲线；
   - 转移过程压缩至 1-2 帧（阶跃式直线快速到位），并在到达目标后的下一帧施加幅度 0.5-1 度的微弱惯性回弹（Micro-overshoot）。

---

## 5. 典型案例与对比

- **思考时的扫视跳跃 vs 追踪飞行物**：
  - **角色陷入沉思**：视线在斜上方（AU 63+61，视觉回忆）瞬间跳跃停留 12 帧，随后 1 帧极速下落至地面（AU 64，内省自省），上眼睑顺势滑下半掩眼球，眼神涣散失去对焦；
  - **平滑追踪**：视线平缓跟随空中飞虫旋转，此时眼球呈现平滑连续转动（Smooth Pursuit），且伴随头部小幅度同向旋转。

---

## 6. 常见反模式与纠偏排障

- **反模式 1：死水浮游眼（Floating Dead Eyes）**
  - *现象*：角色眼球慢悠悠地在两秒内从左滑到右，像是在泥浆中漂流。
  - *纠偏*：将转动时间压缩至 1-2 帧，前一帧还在看左侧，后一帧已牢牢锁死在右侧目标点。
- **反模式 2：下视露白（Lower Gaze White Stare）**
  - *现象*：角色低头看地板，但上眼睑高高挂在上方，角膜上方露出一大片眼白，宛如僵尸。
  - *纠偏*：强制激活眼睑跟随驱动，确保角膜被上眼睑自然覆盖 50% 以上。

---

## 7. 质量验收硬门

- [ ] 视线跳跃转移在 1-2 帧内瞬时完成，无不合生理的慢速滑行漂移。
- [ ] 眼球向下俯视时，上眼睑跟随下落位移率达到眼球转角的 65%-75%。
- [ ] 双眼具备近距离注视时的内收对焦（Vergence）能力，无双眼平行的出戏木偶感。
- [ ] 上视（AU 63）与下视（AU 64）时眼眶组织形变平滑贴合眼球球冠曲面。
