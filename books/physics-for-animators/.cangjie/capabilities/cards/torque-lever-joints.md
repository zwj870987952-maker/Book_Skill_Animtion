## R — 原文 (Reading)

> “Torque is the rotational equivalent of force, equal to force times the lever arm: $\tau = F \times r$. Most human joints are third-class lever systems where the muscle attaches very close to the joint, giving high speed at the limb tip at the expense of force. In airborne rotations, conservation of angular momentum means that pulling limbs inward drops rotational inertia, causing the character to spin dramatically faster.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 3, pp. 88–98; Chapter 5, pp. 179–181

## I — 方法论骨架 (Interpretation)

旋转运动与生物关节动作由转矩（Torque）与转动惯量（Rotational Inertia）主导：
1. **转矩与力臂最大化**:
   - 产生旋转的有效力量取决于力臂垂直距离（$\tau = F \cdot r \sin\theta$）。推门在把手边缘最省力，击拳引臂拉开最大半径能产生最大角动量；
2. **生物三类解剖杠杆**:
   - 第一类（颈部仰俯平衡）：支点在中间；
   - 第二类（踝关节提踵）：阻力在中间，动力臂大于阻力臂（省力）；
   - 第三类（屈肘、屈膝）：动力点在中间，动力臂极短（速度杠杆）。肌肉仅收缩 1 厘米，手腕末端便能以数倍初速度挥舞爆发；
3. **角动量守恒与空中转动惯量调速**:
   - 空中自由旋转时，$L = I\omega = \text{const}$。转动惯量 $I = \sum m r^2$；
   - 角色将展开的双臂双腿向身体旋转轴紧抱团身，半径 $r$ 减小，转动惯量暴跌，旋转角速度 $\omega$ 必须成倍急剧飙升。

## A1 — 案例 (Application Example)

### 书中例题: 空中团身空翻与展开落地的角速度调校 (worked_example)
- **任务**: 跑酷角色从跳台跃起完成空中后空翻 360 度，并在落地前展开四肢平稳踩地。
- **执行过程**:
  1. 起跳离地初期（帧 1–3）：身体伸展，旋转角速度较慢（约 $15^\circ/\text{帧}$）；
  2. 团身加速阶段（帧 4–10）：角色双膝紧抱胸口，双臂抱小腿，旋转半径由 0.9m 缩减为 0.35m，转动惯量降为原本的约 $1/6$，角速度瞬时飙升至 $40^\circ/\text{帧}$，在极短滞空期内飞速翻转度过核心旋转角度；
  3. 展开制动阶段（帧 11–15）：角色在转过 $300^\circ$ 后双腿猛烈向外蹬开伸展，力臂增大，$I$ 恢复高位，角速度骤降回 $10^\circ/\text{帧}$，为精准踩地争取平稳微调时间。
- **结果**: 空翻节奏张弛有度、爆发力与落地控制感完美统一。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作花样滑冰自转、体操空翻、跳水转体、跑酷空中技巧；
2. 调校挥棒、出拳、踢腿等四肢关节动作的末端速度突变；
3. 排查空中翻滚动作为什么看起来像“匀速烤肉串”，缺乏身体姿态对旋转速度的驱动。

### 语言信号 (Triggers)
- "空中翻滚怎么调加速和减速 / 团身旋转"
- "Conservation of angular momentum in airborne spins"
- "肘关节/膝关节发力速度杠杆计算"
- "挥拳击打力臂与转矩调校"

### 与相邻能力的区分
- 与 `center-of-gravity-balance` 的区别: 本能力处理角加速度、转动惯量与关节局部杠杆；`center-of-gravity` 处理整体质心在支撑面内的静态与步进稳定。
- 与 `character-jump-mechanics` 的区别: 本能力用于空中的旋转姿态调速；`character-jump` 用于整体垂直起跳滞空高度与落地缓冲时间。

## E — 可执行步骤 (Execution)

1. **识别旋转阶段与转动惯量变化**:
   - 标记姿态形态：展开期（大半径 $r_{max}$，大 $I$） vs 团身期（小半径 $r_{min}$，小 $I$）；
   - 估算半径压缩比：$k = \frac{r_{min}}{r_{max}}$（通常成人团身为 $0.4–0.5$）。
2. **计算角速度倍率**:
   - 根据角动量守恒，角速度倍率 $\frac{\omega_{spin}}{\omega_{open}} \approx \frac{1}{k^2} \approx 4–6$ 倍。
3. **在动画曲线编辑器 (Graph Editor) 中排布旋转曲线**:
   - 起跳初帧保持平缓倾斜；
   - 抱膝团身帧（时间中段）旋转曲线切线必须瞬间拔高变陡（4–6 倍斜率）；
   - 落地前展开四肢帧切线平滑放缓，平稳过渡到地面。
4. **输出标准交付契约**:
   - 输出展开角速度、团身峰值角速度与对应关键帧旋转切线参数。

## B — 边界与反模式 (Boundary)

### 失效边界
- 在地面有支撑接触或受到持续外力驱动（如冰刀在地面持续蹬冰加速）时，系统受外力矩作用，角动量不守恒，不可盲目假定转速与肢体半径成严格平方反比。

### 常见反模式
- **匀速烤肉串陷阱**: 无论角色在空中是展开大字型还是缩成一团，旋转角度在时间轴上呈一条绝对匀速的斜直线；
- **反物理展开加速**: 角色在空中伸展四肢时旋转反而越来越快。
