## R — 原文 (Reading)

> “Friction opposes the relative motion between two surfaces in contact. Static friction prevents an object from starting to slide, while kinetic friction slows down an object that is already moving. Meanwhile, for objects moving through air, air resistance creates drag that increases with the square of speed, eventually capping falling speed at terminal velocity.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 3, pp. 74–77, 85–86

## I — 方法论骨架 (Interpretation)

阻尼与阻力是动画中赋予物体材质真实质感与制动真实性的核心物理机制：
1. **静摩擦与动摩擦**:
   - 静摩擦阈值（$f_s \le \mu_s N$）：推动静止物体需要比维持滑动更大的初级爆发推力（$\mu_s > \mu_k$）。物体起步前必须有微小的挤压形变与蓄力突破；
   - 动摩擦阻力（$f_k = \mu_k N$）：在平地上滑行的物体受到恒定减速阻力（$a = -\mu_k g$），滑行位移符合反向减速抛物线，最终平稳刹停；
2. **空气阻力与终端速度**:
   - 流体阻力与相对速度的平方及迎风截面积成正比（$F_{drag} \propto v^2 A$）；
   - 当重力与向上风阻平衡时，加速度归零，达到**终端速度 (Terminal Velocity)**。人类高空下落终端速度约为 54m/s（在 24fps 下约为 2.25 米/帧），高空坠落时间超过 3 秒后严禁继续无休止加速。

## A1 — 案例 (Application Example)

### 书中例题: 木箱在粗糙木地板上滑行刹停计算 (worked_example)
- **任务**: 箱子以初速度 $v_0 = 6\text{m/s}$ 被推开，在木地板上滑行（动摩擦系数 $\mu_k = 0.3$），求刹停时间与帧数。
- **执行过程**:
  1. 计算制动加速度：$a = \mu_k \cdot g = 0.3 \times 9.8 \approx 2.94\text{m/s}^2$；
  2. 计算刹停时间：$t_{stop} = \frac{v_0}{a} = \frac{6}{2.94} \approx 2.04$ 秒；
  3. 换算 24fps 帧数：$F = \text{round}(2.04 \times 24) \approx 49$ 帧；
  4. 计算滑行距离：$S = \frac{v_0^2}{2a} = \frac{36}{2 \times 2.94} \approx 6.12$ 米；
  5. 间距排布：前快后慢（反向慢出），末端符合动摩擦匀减速抛物线。
- **结果**: 木箱在地面平稳滑出并缓缓减速沉静停下，摩擦质感极其清晰。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作物体、汽车、角色在冰面、泥地、水泥地面上的滑行与刹车动作；
2. 制作跳伞、高空跳机、超人坠落等长距离坠落的最高时速限制；
3. 排查物体滑行像永久永动机停不下来，或高空掉落速度快到画面撕裂。

### 语言信号 (Triggers)
- "算一下滑行多远会停下来 / 滑行要几帧"
- "摩擦力刹车曲线怎么调 / friction deceleration"
- "高空掉落最高速度是多少 / 终端速度 terminal velocity"
- "冰面滑行 vs 粗糙地面滑行动画"

### 与相邻能力的区分
- 与 `odd-rule-acceleration` 的区别: 本能力处理摩擦与风阻带来的匀减速与速度封顶；`odd-rule` 处理恒力驱动的起步加速。
- 与 `gravity-projectile-timing` 的区别: 本能力给自由落体设定了空气阻力与终端速度上限；`gravity-projectile` 适用于无风阻真空抛物线。

## E — 可执行步骤 (Execution)

1. **确定地面滑行刹车参数**:
   - 识别材质摩擦系数：冰面 $\mu_k \approx 0.05$；平滑木地板 $\mu_k \approx 0.3$；水泥路面 $\mu_k \approx 0.6$；草地/泥地 $\mu_k \approx 0.8$；
   - 确定物体初速度 $v_0$（m/s）。
2. **计算滑行时长与帧数**:
   - 制动减速度 $a = \mu_k \cdot 9.8$；
   - 滑行总时长 $t = \frac{v_0}{a}$；总帧数 $N = \text{round}(t \times FPS)$；
   - 滑行总距离 $S = \frac{v_0^2}{2a}$。
3. **高空坠落终端速度限制判定**:
   - 若下落高度 $h > 50$ 米（自由下落时间超过 3 秒，约 72 帧）：
   - 必须在达到 $v_t \approx 54\text{m/s}$（人类）或相应物体终端速度后，将曲线切线拉平为直线斜率（单帧位移固定为 $2.25$ 米）。
4. **输出标准交付契约**:
   - 输出刹车减速总帧数、滑行总位移以及终端速度分界帧。

## B — 边界与反模式 (Boundary)

### 失效边界
- 当摩擦表面有水膜发生水漂（Hydroplaning），或物体本身在滚动（如车轮纯滚动摩擦力远小于滑动摩擦）时，不可套用简单滑动摩擦系数。

### 常见反模式
- **永动机滑行**: 滑行时全程匀速平移，直到最后一帧突然急刹立停；
- **超光速自由落体**: 角色从一万米高空跳下，下落速度一路飙升到几千公里/小时，单帧位移跨越几十米，完全忽略大气阻力。
