## R — 原文 (Reading)

> “Liquids exhibit unique physical properties that define their appearance: cohesion, adhesion, viscosity, and surface tension. Viscosity is internal friction; water has low viscosity and splashes freely, while honey has high viscosity and coils into thick ropes. In oceans, deep-water waves move in circular orbits, but as water becomes shallower than half the wavelength, bottom friction slows the wave base, forcing the crest forward to break into a plunging wave.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 9, pp. 268–285

## I — 方法论骨架 (Interpretation)

液体特效与水体动画由流体内摩擦（黏度）、表面张力以及浅水破浪动力学决定：
1. **黏度分级与倾倒流态**:
   - **低黏度流体（如水、清酒）**: 剪切阻力极小，倾倒时下落速度极快，接触固体表面瞬间爆开成无数离散球形水滴与薄水膜（Droplets & Sheets）；
   - **中高黏度流体（如机油、糖浆、蜂蜜）**: 内部剪切阻力大，流动时呈光滑连续的厚圆柱绳状下垂；接触平面时不飞溅，而是层层堆积盘旋卷曲，形成经典的**线圈堆叠效应 (Liquid Rope Coiling Effect)**；
2. **海洋深水波与浅水碎浪 (Breaking Waves)**:
   - 深水区水质点沿闭合圆周轨道回旋，波峰向前、波谷向后，物体浮在水面上仅上下前后打转而不随波漂移；
   - 当水深 $d < \frac{1}{2}\lambda$（水深小于半波长）时，波浪触底（Feel the bottom），波底受海底地面摩擦制动急剧减速，波峰因不受摩擦继续全速狂飙，水体向上堆积变陡，最终波峰越过波底向前翻滚卷落，形成标志性的中空管浪（Plunging breaker）。

## A1 — 案例 (Application Example)

### 书中例题: 冲浪巨浪在沙滩浅滩形成的卷管翻浪调校 (worked_example)
- **任务**: 制作一段海浪涌向海滩并最终翻倒碎裂的浪花动画。
- **执行过程**:
  1. 深水行进阶段（波长 $\lambda = 10$ 米，水深 $> 5$ 米）：波形平缓呈正弦波推进，波面水分子在原地做直径 1.5 米的椭圆顺时针旋转；
  2. 浅水压缩阶段（水深减小至 3 米）：波速由 $v = \sqrt{\frac{g\lambda}{2\pi}}$ 减缓，由于后浪追赶前浪，波长被压缩收窄，波高急剧拔高至 2.5 米；
  3. 翻卷破碎阶段（水深 $< 1.5$ 米）：浪底因泥沙摩擦滞后，浪尖前倾超出波底垂线，前部凹陷形成空心水洞（Tube），波峰在 3 帧内向前凌空砸落到水面，爆裂出大量白色气泡、飞沫（Spray）与白色泡沫毯（Foam blanket）。
- **结果**: 准确捕捉到重力与海底地形摩擦对波浪形态的物理撕扯，动态极其震撼真实。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作倒水、倒牛奶、倒蜂蜜、倒熔岩等流体倾倒与飞溅动画；
2. 制作海滩冲浪、暴风雨海面大浪、拍岸碎浪的几何形变；
3. 排查水体动画看起来像“塑料假浪”或“水倒出来像果冻黏土”。

### 语言信号 (Triggers)
- "倒水/倒蜂蜜流体形态怎么排 / 线圈堆叠 coiling"
- "Viscosity and surface tension in liquid animation"
- "海浪拍岸碎浪 breaking waves 物理规律"
- "水滴飞溅与水面浮动物体回旋轨迹"

### 与相邻能力的区分
- 与 `inanimate-physics` 的区别: 本能力专用于流体形态、黏度与非刚体波形破裂；`inanimate-physics` 处理刚体单摆与悬挂结构振荡。
- 与 `fire-explosion-fracture` 的区别: 本能力处理常温液体表面张力与摩擦；`fire-explosion` 处理高温气体热浮力与爆炸冲击波。

## E — 可执行步骤 (Execution)

1. **识别流体黏度等级**:
   - 低黏度（水/果汁） ➔ 倾倒断裂为离散雨滴形态，撞击产生辐射状飞溅冠冕（Splash crown）；
   - 高黏度（蜂蜜/熔岩） ➔ 保持连续粗流柱，并在落点产生圆周盘旋堆积（Coiling）。
2. **设定海洋水波破浪时机**:
   - 提取波长 $\lambda$ 与水深 $d$；
   - 当 $d > 0.5 \lambda$ ➔ 保持平滑正弦波形（Sine wave）；
   - 当 $d \le 0.5 \lambda$ ➔ 压缩波长，垂直拉伸波高；
   - 当波前倾斜角超过 $60^\circ$ ➔ 波尖向前弯曲形成空心圆弧砸向水面（Plunging breaker）。
3. **输出飞沫与泡沫层**:
   - 碎浪砸地后立即生成漂浮白沫（Foam），泡沫在水面随回流展开网状纹理，衰减耗时 24–48 帧逐渐消失。
4. **输出标准交付契约**:
   - 输出流态类型、破浪几何分相时序表与白沫消散帧数配置。

## B — 边界与反模式 (Boundary)

### 失效边界
- 微重力太空舱环境中的液体表面张力占绝对统治地位，无论水还是油均自发收缩为漂浮球形，不存在重力下落柱与破浪翻滚。

### 常见反模式
- **果冻水滴**: 倒水时水柱像橡胶软棒一样在空中扭动而不破碎断开；
- **深水碎浪**: 在深不见底的大洋中央让平缓海浪无缘无故向前卷管翻倒碎裂。
