## R — 原文 (Reading)

> “Whenever an object moves with constant acceleration from a standing start, the distance it travels in each successive unit of time follows the Odd Rule: 1, 3, 5, 7, 9, and so on. This simple mathematical rule gives animators a precise way to calculate keyframe spacing for any object starting from rest under a constant force.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 2, pp. 50–52

## I — 方法论骨架 (Interpretation)

凡受恒定外力（如恒定发动机推力、重力或稳定推力）作用从静止开始加速的物体，其加速度为常数（$a = \text{const}$），位移与时间的平方成正比（$s = \frac{1}{2}at^2$）。
将连续时间划分为等长的离散时间段（如逐帧），每一段内所走过的位移增量严格遵循奇数数列：$1u, 3u, 5u, 7u, 9u, \dots, (2n-1)u$。
而在各时间点上的累计总位移，则遵循平方数列：$1u, 4u, 9u, 16u, 25u, \dots, n^2u$。
利用奇数定律，动画师只需知道加速总距离 $S$ 与总帧数 $n$，即可在 1 秒内算准每一个中间帧的精确空间位置，彻底告别凭空猜测与线性滑冰感。

## A1 — 案例 (Application Example)

### 书中例题: 赛车 6 帧起步加速间距排布 (worked_example)
- **任务**: 制作一辆赛车从起跑线起步，用 6 帧时间加速行驶 36 米。
- **执行过程**:
  1. 设定时间步数 $n = 6$ 帧，总位移 $S = 36$ 米；
  2. 计算基础单元步长：$u = \frac{S}{n^2} = \frac{36}{6^2} = \frac{36}{36} = 1.0$ 米；
  3. 计算每帧位移增量：第 1 帧走 $1\times 1 = 1$ 米；第 2 帧走 $3\times 1 = 3$ 米；第 3 帧走 $5$ 米；第 4 帧走 $7$ 米；第 5 帧走 $9$ 米；第 6 帧走 $11$ 米；
  4. 计算累计关键帧坐标：第 0 帧 = 0m；第 1 帧 = 1m；第 2 帧 = 4m；第 3 帧 = 9m；第 4 帧 = 16m；第 5 帧 = 25m；第 6 帧 = 36m。
- **结果**: 赛车呈现出极其逼真的强大马力推背起动感，加速度曲线平滑无瑕。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 汽车、卡车、雪橇等运载工具从完全静止开始起步加速；
2. 角色用恒力推箱子、推巨石从静止开始滑动；
3. 检查与排查 3D 动画中起步动作为什么看起来像传送带匀速移动。

### 语言信号 (Triggers)
- "帮我算一下汽车起步加速每一帧的位置"
- "恒力加速关键帧间距怎么排 / 奇数定律怎么用"
- "Odd rule calculation for uniform acceleration"
- "起跑加速曲线怎么调才不滑冰"

### 与相邻能力的区分
- 与 `gravity-projectile-timing` 的区别: 本能力用于一维恒力加速的一般代数分配；`gravity-projectile` 专用于带有特定重力加速度常数（$9.8\text{m/s}^2$）与下落/抛物线正交分解。

## E — 可执行步骤 (Execution)

1. **输入已知参数**:
   - 确定加速总帧数 $n$（或总时间步数）；
   - 确定加速终点与起点的总位移差 $S$。
2. **计算单位基准步长 (Base Unit $u$)**:
   - 套用公式：$u = \frac{S}{n^2}$；
   - 判停条件：若 $u \le 0$ 或 $n < 2$，报错并要求重新确认输入。
3. **生成位移坐标序列**:
   - 对 $k = 1, 2, \dots, n$：
     - 单步增量 $\Delta s_k = (2k - 1) \cdot u$；
     - 累计位置 $s_k = k^2 \cdot u$。
4. **输出标准交付契约**:
   - 输出逐帧时间-位置数据表与 Graph Editor 切线参考。

## B — 边界与反模式 (Boundary)

### 失效边界
- 当施加的外力随时间急剧变化（如活塞往复冲击力、风力剧烈抖动）时，奇数定律失效，必须采用变加速度动力学数值积分；
- 当速度接近终端阻力阈值时，空气阻力导致加速度衰减，后程不能继续使用纯奇数递增。

### 常见反模式
- **线性增量陷阱**: 每帧让物体等距移动（1, 1, 1, 1），造成机械滑冰；
- **盲目二分法**: 在起点与终点间反复二分打中点，破坏了二次方抛物线的物理曲率。
