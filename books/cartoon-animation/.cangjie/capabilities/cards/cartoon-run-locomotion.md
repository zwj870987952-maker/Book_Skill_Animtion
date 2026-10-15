## R — 原文 (Reading)

> “A cartoon run is faster than a walk, usually timed at two, four, or six frames per step. The body leans forward into the action. In very fast cartoon runs, the legs often dissolve into a blur or complete wheel shape, with speed lines trailing behind. This wheel-leg effect gives the illusion of impossible, supersonic speed while keeping the silhouette readable.”
> 
> —— Preston Blair, *Cartoon Animation*, Chapter 2, pp. 100–105

## I — 方法论骨架 (Interpretation)

卡通奔跑（Cartoon Run）是好莱坞黄金时代动画的核心视觉奇观，其动力学具有极高的夸张自由度：
1. **步频与前倾角度**:
   - 快速跑 (Fast Run): 单步 4–6 帧（全循环 8–12 帧），躯干向前倾斜 $45^\circ–60^\circ$；
   - 极速冲刺 (Dash): 单步 2–3 帧（全循环 4–6 帧），躯干几乎平行于地面贴地飞驰；
2. **腾空期与飞奔跨度**:
   - 奔跑与行走的本质区别在于**漫长的空中腾空期（Flight Phase）**；双足完全离开地面，前后腿在空中几乎劈叉拉开成 $180^\circ$；
3. **飞轮腿轮式残影法则 (The Wheel Effect)**:
   - 当速度超过单帧视网膜追踪极限时，写实腿部绘制会导致跳帧脱节；
   - 普雷斯顿·布莱尔提出了“飞轮腿”解决方案：将双腿合成一个持续旋转的半透明圆环/椭圆飞轮，沿切线方向拖出多条平行速度线（Speed lines），并在圆环外缘绘制 3–4 个不同相位的模糊鞋掌；
4. **原地蓄力打滑 (Start-Up Burnout)**:
   - 奔跑起动前通常先在原地发生飞轮腿高速打滑 6–12 帧（冒烟升空），随后如离弦之箭向前爆射。

## A1 — 案例 (Application Example)

### 书中例题: 8 帧高速奔跑循环与前倾姿态排布 (worked_example)
- **任务**: 制作兔子角色被猎犬追捕的高速狂奔循环（单步 4 帧，双步全循环 8 帧）。
- **执行过程**:
  1. 帧 1 (Right Foot Contact): 右脚在前触地，前膝深屈承重；躯干向前剧烈倾斜 $50^\circ$；
  2. 帧 2 (Push): 右脚猛烈蹬地向后推，脚尖伸直如箭；
  3. 帧 3 (Flight / Airborne): 核心腾空帧—双脚完全离地，左腿向前大幅劈开，右腿向后平直拉伸，身体在空中如导弹般飞行；
  4. 帧 4 (Reach): 左脚向前伸展准备触地；
  5. 帧 5–8: 换左腿触地与右腿腾空对称完成循环。
- **结果**: 动作轻盈飞快、速度感与破空感极强。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作卡通追逐、逃跑、百米冲刺与超音速狂奔；
2. 制作动漫/游戏角色起跑前的原地打滑蓄力动效；
3. 排查奔跑动作为什么看起来“沉重拖沓像慢动作”或“动作脱节闪烁”。

### 语言信号 (Triggers)
- "卡通奔跑循环几帧一步 / cartoon run timing"
- "飞轮腿 wheel leg 效果怎么画 / 腿部画成车轮"
- "原地打滑蓄力起跑 burnout dash 动效"
- "极速奔跑前倾角度与腾空滞空帧排布"

### 与相邻能力的区分
- 与 `cartoon-walk-types` 的区别: 本能力用于高速奔跑与飞轮残影；`cartoon-walk` 用于低速性格走姿。
- 与 `animal-quadruped-cycles` 的区别: 本能力专用于双足角色奔跑；`animal-quadruped` 用于四足动物奔跑飞奔。

## E — 可执行步骤 (Execution)

1. **根据速度选择奔跑模式**:
   - 戏剧性中速跑 ➔ 单步 6 帧（全循环 12 帧）；
   - 快速冲刺跑 ➔ 单步 4 帧（全循环 8 帧）；
   - 极速漫画飞轮跑 ➔ 单步 2 帧，采用 **Wheel-Leg (飞轮腿)** 模式。
2. **调校身体前倾动作线**:
   - 绘制从蹬地脚尖穿过胸口向前俯冲的水平低平主动作线；
   - 下巴向前探出，双耳或长发水平向后平行拉伸。
3. **绘制飞轮腿几何结构 (若开启极速模式)**:
   - 在骨盆下方绘制一个倾斜椭圆形圆环；
   - 沿圆环外缘等距排布 3 个鞋底足尖；
   - 在后方绘制 3–5 条水平向后延伸的速度风线与尘土烟团。
4. **输出标准交付契约**:
   - 输出奔跑帧数预算表、腾空帧标注与速度线残影示意图。

## B — 边界与反模式 (Boundary)

### 失效边界
- 严谨奥运田径跑步仿真，受人体生理极限限制（步频约 4–5 步/秒），躯干前倾不得超过 $20^\circ$，不可套用水平贴地或飞轮腿。

### 常见反模式
- **直立奔跑**: 身体直挺挺呈 $90^\circ$ 奔跑，缺乏向前的势能驱动感；
- **无腾空期**: 奔跑中双脚始终有一只在地面，导致奔跑退化为滑稽快步走。
