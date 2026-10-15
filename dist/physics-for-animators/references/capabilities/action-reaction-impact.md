## R — 原文 (Reading)

> “Newton’s third law states that for every action, there is an equal and opposite reaction. In fight scenes and collisions, the impulse-momentum theorem ($F \Delta t = \Delta p$) dictates that the peak force of impact depends directly on the duration of contact. Shortening contact time creates explosive, destructive blows, while extending contact time absorbs impact with soft recoil.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 3, pp. 98–100; Chapter 6, pp. 210–214

## I — 方法论骨架 (Interpretation)

格斗打击、碰撞反弹与后坐力（Recoil）由动量守恒与冲量定理决定：
1. **作用力与反作用力**:
   - 击出重拳时，施力者自身肩膀与骨盆必须承受等大反向的后坐力矩；没有地面的反向摩擦支撑，出拳者自身将被推向后方；
2. **冲量-动量定理与接触时间 $\Delta t$**:
   - 碰撞受力：$F_{impact} = \frac{m \Delta v}{\Delta t}$；
   - **硬硬刚体碰撞（Hard impact）**: 接触时间极短（$\Delta t = 1–2$ 帧，约 0.04–0.08 秒）。受击物体几乎瞬间改变速度，受力峰值极大，产生剧烈的镜头震动、受击硬直与火星碎屑；
   - **柔性缓冲碰撞（Soft cushion）**: 接触时间延长（$\Delta t = 6–12$ 帧）。受击物体产生大幅度挤压凹陷或膝盖屈曲，受力平缓均匀分布。

## A1 — 案例 (Application Example)

### 书中例题: 重拳击中下巴的受击后坐力与接触时序 (worked_example)
- **任务**: 制作主角一记重拳正面击中反派下巴的受击反应。
- **执行过程**:
  1. 击中接触帧（第 1 帧）：拳头与下巴接触；
  2. 极短挤压停顿（第 2 帧）：下巴肉体被挤压变形，维持接触仅 1 帧（高爆发硬撞击）；
  3. 动量瞬间传递（第 3–5 帧）：拳头速度急剧衰减刹停，反派头部以极高角速度猛烈后仰并甩出汗水；
  4. 躯干延迟跟随（第 6–10 帧）：由于颈椎多级关节延迟，反派胸腔和骨盆滞后 2–3 帧才被带动向后平移；
  5. 地面制动（第 11–18 帧）：反派双脚在地面倒退滑行，动摩擦力逐渐将反派身体停稳。
- **结果**: 打击感沉重、爆裂，后坐力与全身受击链条层次极其丰富。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作动作格斗、枪战射击后坐力、车辆撞击、巨石砸地等高能量碰撞镜头；
2. 调校打击感与硬直时间（Hit-stop）；
3. 排查动作为什么看起来像“打在棉花上无力”或“受击角色像无质量充气娃娃”。

### 语言信号 (Triggers)
- "打击感怎么做 / 击中瞬间停几帧"
- "Impulse momentum theorem in fight scenes"
- "枪械后坐力 recoil 与角色身体后仰时序"
- "车祸撞墙碰撞时间排布"

### 与相邻能力的区分
- 与 `character-jump-mechanics` 的区别: 本能力用于外部外力撞击与动量冲量传递；`character-jump` 专用于角色双腿蹬地与自由落体缓冲。
- 与 `fast-action-troubleshooting` 的区别: 本能力用于物理受力接触时长与后坐力分配；`fast-action` 用于消除视网膜频闪的残影变形张。

## E — 可执行步骤 (Execution)

1. **确定碰撞材质刚度与接触时间 $\Delta t$**:
   - 金属撞金属 / 石头撞石头 ➔ 接触时间 $\Delta t = 1$ 帧；
   - 拳击面部 / 木棍抽打 ➔ 接触时间 $\Delta t = 2$ 帧；
   - 击中沙袋 / 身体撞海绵垫 ➔ 接触时间 $\Delta t = 5–8$ 帧。
2. **分配施力端后坐力 (Recoil)**:
   - 击中瞬间，攻击端手臂必须产生 1–2 帧的受阻顿挫（或反弹 1 帧）；
   - 攻击者后脚脚后跟必须深踩地面以体现反作用力传导。
3. **分配受击端链式动力学**:
   - 受击点（头部/受力点）在 $\Delta t$ 结束后以最大速度爆发位移；
   - 躯干和重心滞后 2–4 帧启动（次级惯性）；
   - 给予地面滑动制动时间（通常 8–16 帧）。
4. **输出标准交付契约**:
   - 输出接触帧数、击中定格（Hit-stop）帧数、受击后退总位移与衰减帧数清单。

## B — 边界与反模式 (Boundary)

### 失效边界
- 魔法光束、激光武器等无质量高能光子打击，没有牛顿力学经典质量动量转移，不可盲目按实物质量动量守恒公式计算反冲。

### 常见反模式
- **棉花拳陷阱**: 重拳打在下巴上，接触过程持续了 6 帧慢慢推过去，毫无爆发冲击破坏力；
- **全身同时后退**: 拳头打在脸上，受击者整个人像一块实心木板平行向后平移，头部没有率先折颈后仰。
