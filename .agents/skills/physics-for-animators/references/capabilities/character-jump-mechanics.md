## R — 原文 (Reading)

> “A jump consists of three distinct physical parts: the push, the airborne arc, and the landing. During the push, the character exerts force against the ground to build up vertical velocity. Once in the air, the character behaves strictly as a projectile under gravity. Upon landing, the character must spend stop time flexing the knees to absorb the impact.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 6, pp. 189–199

## I — 方法论骨架 (Interpretation)

角色跳跃绝非简单的空中抛物线，而是完整的闭环动力学三部曲：
1. **推地阶段 (Push Phase)**:
   - 从最低深蹲蓄力点蹬伸双腿至双脚离地瞬间。肌肉向地面施加反作用力（$F_{push} > mg$），将下蹲距离 $d_{squat}$ 转化为离地初速度 $v_0 = \sqrt{2gh}$。推地耗时通常为 4–6 帧；
2. **空中滞空阶段 (Air Phase)**:
   - 双脚一旦离地，身体完全受重力控制，任何空中乱蹬腿都无法改变质心的纯抛物线轨迹；
   - 滞空时间仅取决于跳跃高度：$t_{air} = 2 \sqrt{\frac{2h}{g}}$；
3. **落地缓冲阶段 (Stop Phase)**:
   - 足尖触地瞬间速度达到最大值（$v_{impact} = v_0$），必须通过膝关节深屈距离 $d_{cushion}$ 缓冲刹停。缓冲耗时通常为 3–8 帧。落地制动时间越短，对骨骼冲击越大。

## A1 — 案例 (Application Example)

### 书中例题: 篮球运动员 0.8 米垂直起跳与落地全周期计算 (worked_example)
- **任务**: 制作一名篮球运动员垂直跳起 0.8 米争抢篮板球，求三阶段精准帧数分配（24fps）。
- **执行过程**:
  1. 计算腾空初速度：$v_0 = \sqrt{2 \times 9.8 \times 0.8} \approx 3.96\text{m/s}$；
  2. 计算空中滞空时间：上升时间 $t_{up} = \frac{3.96}{9.8} \approx 0.404$ 秒（约 10 帧）；下降时间同为 10 帧；总空中滞空帧数 $N_{air} = 20$ 帧；
  3. 计算起跳推地时间：设定下蹲预备深度 $d_{squat} = 0.4$ 米，推地时间 $t_{push} = \frac{2 \times 0.4}{3.96} \approx 0.2$ 秒，即 $N_{push} = 5$ 帧；
  4. 计算落地深蹲缓冲时间：落地膝盖弯曲吸收冲击距离 0.4 米，缓冲时间 $N_{stop} = 5$ 帧；
  5. 组装整套关键帧闭环：深蹲推地（帧 1–5） ➔ 离地上升（帧 6–15） ➔ 下落（帧 16–25） ➔ 触地深屈缓冲（帧 26–30） ➔ 挺直站起（帧 31–36）。
- **结果**: 动作力量爆发极其充沛，起飞与落地重量感极其扎实，无任何悬空失真。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作立定跳远、垂直起跳、跨步大跳、高处跳落；
2. 游戏角色跳跃动效与起跳落地前摇后摇判定；
3. 排查角色跳跃像被钢丝吊起（无起跳蹬地）或落地像木桩插入地面（无弯膝缓冲）。

### 语言信号 (Triggers)
- "跳跃动作怎么定帧数 / 起跳要几帧落地要几帧"
- "Push time and stop time calculation for character jumps"
- "跳起 1 米高空中要停留多少秒"
- "起跳无力量感 / 落地假摔排查"

### 与相邻能力的区分
- 与 `gravity-projectile-timing` 的区别: 本能力是角色全身生物力学全周期系统（推地+滞空+深蹲缓冲）；`gravity-projectile` 纯粹是刚体抛物线公式。
- 与 `odd-rule-acceleration` 的区别: 本能力把推地和缓冲具象为特定重力加速度下的跳跃模型；`odd-rule` 是通用恒力排布工具。

## E — 可执行步骤 (Execution)

1. **确定跳跃目标高度与生理参数**:
   - 目标跳跃高度 $h$（米；普通人立定跳高约 0.4–0.5m，运动员约 0.7–0.9m）；
   - 预备下蹲深度 $d_{squat}$（通常 0.3–0.45m）；
   - 落地缓冲深度 $d_{cushion}$（硬着陆 0.15m，深屈软着陆 0.4m）。
2. **计算核心力学时序**:
   - 离地初速度 $v_0 = \sqrt{2 \times 9.8 \times h}$；
   - 空中滞空总帧数 $N_{air} = \text{round}\left(2 \times \sqrt{\frac{2h}{9.8}} \times FPS\right)$；
   - 推地爆发总帧数 $N_{push} = \text{round}\left(\frac{2d_{squat}}{v_0} \times FPS\right)$（通常 4–6 帧）；
   - 落地缓冲总帧数 $N_{stop} = \text{round}\left(\frac{2d_{cushion}}{v_0} \times FPS\right)$（通常 3–8 帧）。
3. **分段排布间距与姿态**:
   - 推地阶段采用慢出（越接近离地速度越快）；
   - 空中顶点采用两端对称慢入慢出（顶点极值）；
   - 触地缓冲阶段采用慢入（触地瞬间极速，随后平滑受阻刹停）。
4. **输出标准交付契约**:
   - 输出三阶段帧数预算表、各关键姿态编号与垂直高度标注。

## B — 边界与反模式 (Boundary)

### 失效边界
- 带有喷气背包、超能力反重力飞行或水下跳跃的动作，受到持续外力驱动，空中轨迹不符合自由重力抛物线。

### 常见反模式
- **零推地跳跃**: 角色站立姿态脚底直接离地升空，没有预备下蹲与足部向后蹬踏延伸；
- **零缓冲落地**: 角色空中落下一碰到地面立刻停在直立姿态，膝盖不弯曲，骨骼受力失真。
