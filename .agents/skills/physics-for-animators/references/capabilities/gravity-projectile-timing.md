## R — 原文 (Reading)

> “A falling object accelerates continuously due to gravity. One of the most useful rules of thumb for animators is ‘Fourth Down at Half Time’: when half the total fall time has elapsed, the object has fallen only one-fourth of the total distance. The remaining three-fourths of the distance is covered in the second half of the time.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 3, pp. 64–67

## I — 方法论骨架 (Interpretation)

地球重力加速度（$g \approx 9.8\text{m/s}^2$）决定了所有不计空气阻力的物体在下落时的普适规律：
1. **时间平方律**: 下落距离 $h = \frac{1}{2}gt^2$。下落时间仅由高度决定，与物体重量无关；
2. **四分之一半时定理**: 当下落时间进行到总时间的一半时（$t = 0.5 t_{total}$），下落距离仅为总高度的 $1/4$（$25\%$）；在剩余的一半时间里，速度急剧飙升完成剩余 $75\%$ 的路程；
3. **抛体运动正交解耦**: 投掷物体在空中飞行时，水平方向保持恒定匀速位移（$a_x = 0$），垂直方向保持重力加速度（$a_y = -g$），两轴在计算上完全独立，互不影响。

## A1 — 案例 (Application Example)

### 书中例题: 4.9 米高台坠落与半时位置验证 (worked_example)
- **任务**: 角色从 4.9 米高的屋顶跌落到地面，需在 24fps 下排布下落帧数。
- **执行过程**:
  1. 计算下落秒数：$t = \sqrt{\frac{2 \times 4.9}{9.8}} = 1.0$ 秒；
  2. 换算总帧数：$F = 1.0 \times 24 = 24$ 帧；
  3. 检验关键时间中点（第 12 帧）：角色下落高度为 $4.9 \times \frac{1}{4} = 1.225$ 米（距离地面仍有 3.675 米）；
  4. 排布关键姿态：前 12 帧呈现缓慢启动与身体失衡前倾，后 12 帧急剧加速坠落直至砸地。
- **结果**: 动作真实沉重，完全消除了下落像悬挂威亚慢慢滑下的虚假失重感。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作悬崖坠落、高楼跌落、抛物跌落的帧数与垂直位移；
2. 投掷标枪、棒球、投石机炮弹的抛物线轨迹调校；
3. 排查角色坠落为什么看起来像降落伞或塑料泡沫。

### 语言信号 (Triggers)
- "算一下从 X 米高掉下来要多少帧"
- "Fourth down at half time / 自由落体时间计算"
- "抛体运动轨迹怎么排 / 为什么抛物线两头看起来不对"
- "消除坠落时的漂浮失重感"

### 与相邻能力的区分
- 与 `odd-rule-acceleration` 的区别: 本能力专用于以 $g = 9.8\text{m/s}^2$ 为基准的地球重力场与抛体二维正交分解；`odd-rule` 是通用的一维恒力加速分配工具。
- 与 `character-jump-mechanics` 的区别: 本能力处理自由落体与纯抛体；`character-jump` 专用于角色生物主动起跳推地与落地深蹲缓冲闭环。

## E — 可执行步骤 (Execution)

1. **计算垂直下落时间与总帧数**:
   - 输入下落高度 $h$（米）与帧率 $FPS$（通常 24）；
   - 计算下落秒数：$t_{fall} = \sqrt{\frac{2h}{9.8}}$；
   - 换算垂直总帧数：$N_{fall} = \text{round}(t_{fall} \times FPS)$。
2. **锚定关键时序位置**:
   - 第 0 帧：下落位移 $0$；
   - 第 $\text{round}(N_{fall} / 2)$ 帧：下落位移 $0.25 \times h$（四分之一半时定理）；
   - 第 $N_{fall}$ 帧：下落位移 $h$（触地撞击）。
3. **处理抛体水平位移 (若是抛体运动)**:
   - 给定水平初速度 $v_x$，每帧水平位移 $\Delta x = \frac{v_x}{FPS}$（恒定常数）；
   - 水平坐标 $x_k = k \times \Delta x$，严禁在顶点处收缩水平位移。
4. **输出标准交付契约**:
   - 输出下落总时长、总帧数、时间中点垂直坐标及逐帧位置律表。

## B — 边界与反模式 (Boundary)

### 失效边界
- 当下落时间极长（超过 3 秒，下落高度超过 50 米）时，空气阻力使速度达到终端速度（Terminal Velocity，约 54m/s），此时不再加速，必须切换为匀速下落；
- 微质量物体（纸片、树叶、羽毛）受空气升力影响巨大，不可套用真空抛体公式。

### 常见反模式
- **时间过半距离过半**: 在半程时间把角色排在 $50\%$ 高度，造成严重漂浮；
- **抛体顶点水平减速**: 在抛物线最高点把水平速度也减慢，导致抛物线畸变成“尖顶倒 V 字”。
