## R — 原文 (Reading)

> “Light intensity falls off with the square of distance, a fundamental property known as the inverse-square law: $E \propto 1/d^2$. A point source produces razor-sharp shadows with pure umbra, while any light source with physical size creates a soft penumbra. Moving the shadow-casting object further from the receiving surface expands this penumbra, softening the shadow edge naturally.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 4, pp. 121–134

## I — 方法论骨架 (Interpretation)

三维场景与手绘光影的真实感与物理景深，由平方反比衰减与几何投影半影决定：
1. **照度平方反比衰减定律 (Inverse-Square Law)**:
   - 物理真实光源的光子在三维空间中向球壳扩散，表面积与半径平方成正比。受光物体的光照强度严格满足 $E = \frac{I}{d^2}$；
   - 距离每增加 1 倍，照度暴跌为原本的 $25\%$；距离增加 2 倍，照度降为原本的 $11.1\%$；
   - 严禁在物理渲染中使用线性衰减（$1/d$）或无衰减，否则室内场景将发生严重的近景欠曝或远景惨白过度曝光；
2. **本影与半影光学几何 (Umbra and Penumbra)**:
   - **本影 (Umbra)**: 光源发光面被遮挡物完全遮蔽的纯黑核心区域；
   - **半影 (Penumbra)**: 仅遮挡了光源一部分面积的渐变柔和阴影边缘；
   - **半影宽度定理**: 半影宽度与光源发光面直径 $D_{source}$ 及遮挡物到投影墙面的距离 $d_{shadow}$ 成正比。脚踩地面处的脚底阴影极硬极实（$d_{shadow} \to 0$），而头部投射在远端地面的影子极软极虚。

## A1 — 案例 (Application Example)

### 书中例题: 走廊漫步角色阴影边缘柔和度渐变调校 (worked_example)
- **任务**: 角色在侧面有大型窗户柔光箱照射的走廊上行走，需精确调校角色投在地面与墙壁上的阴影虚实度。
- **执行过程**:
  1. 识别光源属性：窗户为大型面光源（发光面直径约 1.5 米），必然产生宽广的半影；
  2. 调校角色脚底触地点：脚底贴紧地面，遮挡距离 $d_{shadow} \approx 0$，此处半影宽度接近于 0，投射出锐利浓黑的接触阴影（Contact shadow / Ambient occlusion）；
  3. 调校角色头部投影：角色身高 1.8 米，头部离地面垂直距离较大，半影边缘宽度扩展至 15–20 厘米，阴影边缘呈现出极其自然的渐变羽化软影；
  4. 调校远离灯光衰减：沿走廊远离窗户 4 米处，角色照度相比 2 米处自然衰减至四分之一亮度（严格匹配 Quadratic 衰减）。
- **结果**: 场景光影通透、空间景深层次分明，完全消除了粗糙手绘或简陋引擎常见的“全身硬边黑剪影”劣质感。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 三维动画软件（Maya / Blender / Unreal）中物理灯光参数与阴影贴图/射线追踪调校；
2. 手绘动画与概念设计中人物投影边缘的羽化虚实过渡决策；
3. 排查场景光照为什么显得“塑料平淡”、“近处过暗远处过亮”或“阴影边缘死黑失真”。

### 语言信号 (Triggers)
- "灯光平方反比衰减怎么调 / inverse square decay"
- "阴影本影和半影 umbra and penumbra 几何关系"
- "为什么脚底影子是硬的头顶影子是虚的 / 阴影羽化"
- "线性工作流与物理光照强度计算"

### 与相邻能力的区分
- 与 `camera-motion-timing` 的区别: 本能力用于场景空间光照强度衰减与阴影边缘几何；`camera-motion` 用于摄影机摇镜头平移防频闪。
- 与 `inanimate-physics` 的区别: 本能力专用于物理光学与电磁辐射；`inanimate-physics` 用于机械力学摆动与阻尼振荡。

## E — 可执行步骤 (Execution)

1. **设置光源衰减类型**:
   - 在灯光属性中强制勾选 **Quadratic Decay (平方反比)**；
   - 严禁勾选 None 或 Linear（除非追求非真实卡通纯平光渲染）。
2. **计算阴影半影宽度 (Penumbra Width)**:
   - 提取光源物理直径 $D_{source}$、光源到遮挡物距离 $d_1$、遮挡物到受影面距离 $d_2$；
   - 套用半影宽度公式：$W_{penumbra} = D_{source} \times \frac{d_2}{d_1}$；
   - 规则：当 $d_2 \to 0$（贴近物体根部）时，$W_{penumbra} \to 0$，阴影呈现锐利边缘；随 $d_2$ 增大，阴影边缘半径等比例羽化扩散。
3. **输出接触阴影 (Contact Shadow) 闭环**:
   - 检查角色双足与地面接触点，必须带有最浓烈的纯黑遮蔽（AO 接触闭环），锁定角色接地感。
4. **输出标准交付契约**:
   - 输出灯光 Decay 模式确认、不同受影距离处的阴影柔和度参数与接触阴影标准。

## B — 边界与反模式 (Boundary)

### 失效边界
- 在强阳光直射的户外晴天环境下，太阳虽然直径巨大但离地球有 1.5 亿公里，光线呈绝对平行光，遮挡物在几十米范围内的半影扩展极其微弱（阳光阴影普遍偏硬）。

### 常见反模式
- **全身硬边影子**: 无论角色脚底还是数米高的头部，投影在远方地面上的影子边缘全部一样锋利如同剪纸；
- **线性衰减室内光**: 使用线性衰减打光，造成灯光像探照灯直通走廊尽头，缺乏自然衰退的物理层次感。
