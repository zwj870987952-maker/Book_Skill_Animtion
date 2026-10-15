## R — 原文 (Reading)

> “Drag and follow-through are physical consequences of inertia and fluid resistance. Drag slows the trailing part of an object as it moves through air, directly proportional to the surface area facing the wind. Follow-through happens because mass in motion tends to stay in motion. A long appendage swings at a much slower natural frequency than a short one, following the pendulum formula $T = 2\pi\sqrt{L/g}$.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 6, pp. 217–221

## I — 方法论骨架 (Interpretation)

次级运动（Secondary Motion）、拖尾阻力（Drag）与惯性跟随（Follow-through）由惯性质量、几何迎风面积与单摆物理固有频率决定：
1. **阻力与表面积物理法则**:
   - 移动物体所受风阻与垂直于运动方向的有效截面积及速度平方成正比（$F_{drag} \propto A \cdot v^2$）；
   - 迎风展开的宽大披风比细绳受到大得多的气动阻力，产生剧烈的后翻凹陷；
2. **长度-周期单摆法则**:
   - 悬挂附庸物的自振周期与长度平方根成正比（$T = 2\pi\sqrt{\frac{L}{g}}$），与其自身质量完全无关；
   - **短附庸物**（短发、小坠饰）：摆动周期极短，紧跟主干，延迟滞后仅 1–2 帧；
   - **长附庸物**（及腰长发、长尾巴、长斗篷）：摆动周期长达数倍，具有显著的低频大振幅波动，主干停止后滞后 5–8 帧才达到过冲极值。

## A1 — 案例 (Application Example)

### 书中例题: 奔跑中长短马尾辫的次级摆动延迟对比 (worked_example)
- **任务**: 场景中两位角色同时跑步，角色 A 戴 20cm 短马尾，角色 B 戴 80cm 齐腰长马尾。
- **执行过程**:
  1. 计算物理摆动周期：
     - 短马尾（$L = 0.2$ 米）：$T_A = 2\pi \sqrt{\frac{0.2}{9.8}} \approx 0.9$ 秒（单向摆动约 10 帧）；
     - 长马尾（$L = 0.8$ 米）：$T_B = 2\pi \sqrt{\frac{0.8}{9.8}} \approx 1.8$ 秒（单向摆动约 21 帧，几乎是短发的整整 2 倍）；
  2. 匹配角色步态频率（单步 12 帧）：
     - 短马尾自然频率与单步频率高度接近，呈现出每跨一步即剧烈上下弹跳一次的活泼节奏（延迟 2 帧到达波峰）；
     - 长马尾自然频率远低于单步频率，无法跟随每一步快速颠簸，而是跨越两个完整步态周期形成优雅滞后的大 S 形波浪起伏（延迟 6 帧到达波峰）。
- **结果**: 两位角色的发丝物理质感与材料属性形成鲜明对比，动作层次极其丰富。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作角色长发、马尾、裙摆、披风、羽毛、围巾、兽耳与尾巴的次级动画；
2. 调校不同尺寸物体的惯性拖尾帧数差；
3. 排查所有次级物件像铁板一块硬邦邦，或长短物件摆动频率千篇一律的机械缺陷。

### 语言信号 (Triggers)
- "头发/衣服/尾巴摆动延迟几帧 / 怎么调次级动画"
- "Pendulum formula for secondary motion latency"
- "短发和长发摆动区别 / 表面积风阻计算"
- "Overlapping action based on length and drag"

### 与相邻能力的区分
- 与 `follow-through-overlapping` (Timing 领域) 的区别: 本能力从单摆长度方程与表面积风阻方程出发给出严格的物理周期计算；`follow-through` 侧重传统动画十二法则中的多关节错开指导。
- 与 `inanimate-physics` 的区别: 本能力处理随生物运动附着的柔性次级结构；`inanimate-physics` 处理独立悬挂的阻尼摆动衰减。

## E — 可执行步骤 (Execution)

1. **测量悬挂次级结构的等效物理长度 $L$ (米)**:
   - 提取从根部关节到末端顶点的几何长度 $L$。
2. **计算自然摆动半周期与延迟帧数**:
   - 自然半周期秒数：$t_{half} = \pi \sqrt{\frac{L}{9.8}}$；
   - 理论延迟帧数基准：$N_{delay} = \text{round}(t_{half} \times FPS \times 0.25)$（通常取周期的四分之一左右作为滞后相位差）：
     - $L \le 0.2\text{m}$（短小物件）➔ 延迟 $1–2$ 帧；
     - $0.2\text{m} < L \le 0.6\text{m}$（中等物件）➔ 延迟 $3–4$ 帧；
     - $L > 0.6\text{m}$（长条物件）➔ 延迟 $5–8$ 帧。
3. **根据迎风截面积调节弯曲曲率**:
   - 截面大、材质软（如薄纱丝绸）➔ 极速运动时加重 S 弯与 C 弯曲率；
   - 截面小、材质韧（如粗麻绳、兽尾）➔ 保持较大的弧线张力。
4. **输出标准交付契约**:
   - 输出各层级骨骼延迟偏移帧数表（Keyframe Offsets）与摆动波形振幅建议。

## B — 边界与反模式 (Boundary)

### 失效边界
- 纯刚体物件（如金属长剑、实心拐杖）虽然长度长，但由于材料刚度极大，不存在弯曲滞后，只有整体受迫摆动，不可强加软体波浪形变。

### 常见反模式
- **一刀切延迟**: 所有头发、尾巴和衣服在时间轴上统一向后偏移 3 帧，导致长发像硬塑料板，短发像泥浆；
- **无阻尼无限弹跳**: 物体停下后，次级摆动持续几十帧不衰减，像没有空气阻力。
