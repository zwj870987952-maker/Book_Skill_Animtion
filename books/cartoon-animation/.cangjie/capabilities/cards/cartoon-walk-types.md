## R — 原文 (Reading)

> “A walk can express any emotion or character type. In the classic sneak, the character moves with great caution, knees bent, body crouching low, and the foot raised high before touching down quietly on tiptoe. The strut, on the other hand, is full of swagger—the chest thrown out, the head held high, and the legs kicking outward with high bounce and rhythm.”
> 
> —— Preston Blair, *Cartoon Animation*, Chapter 2, pp. 90–99

## I — 方法论骨架 (Interpretation)

行走不仅是位移工具，更是直接揭示卡通角色性格、心境与戏剧地位的核心舞台语言。普雷斯顿·布莱尔奠定了经典卡通四大个性步态：
1. **潜行步 (The Sneak, 16–24 帧/步)**:
   - 展现鬼祟、小偷潜入、捕猎或恶作剧；
   - 核心力学：身体极度下蹲压低（Low center of gravity），过路位置（Passing）摆动腿提至胸口高度悬停，**脚尖轻触地面而脚后跟悬空至少 4–8 帧**，重心滞后缓慢转移；
2. **昂首阔步 (The Strut / Rooster Walk, 8–12 帧/步)**:
   - 展现骄傲自大、得胜游行、霸道张扬；
   - 核心力学：胸膛外挺成盾牌，头颅后仰，双臂外扩弯曲如公鸡翅膀；触地脚后跟重重磕地并伴随强烈下压反弹（Squash & Stretch），摆动腿以大弧度外踢甩出；
3. **轻快跳跃步 (The Skip, 12–16 帧/步)**:
   - 展现天真无邪、童趣狂喜；
   - 核心力学：单脚着地后在同一只脚上进行二次点地小跳，产生高空滞空的双重弹性起伏；
4. **标准卡通步 (The Basic Comic Walk, 12 帧/步)**:
   - 四大经典相位（Contact 触地、Down 受压、Passing 过路、Up 蹬踏），强调上下波形夸张度。

## A1 — 案例 (Application Example)

### 书中例题: 24 帧潜行步全循环极值与时序排布 (worked_example)
- **任务**: 制作反派角色在侦探背后蹑手蹑脚逼近的 24 帧无缝潜行循环（单步 12 帧，24fps）。
- **执行过程**:
  1. 帧 1 (Contact): 右脚尖轻触地面，脚跟翘起，重心位于左腿后方；
  2. 帧 4 (Down): 双膝弯曲深压，角色双手抱胸紧张缩颈，高度降至最低；
  3. 帧 7 (Passing): 核心高张力姿态—左大腿高高抬起贴紧腹部，膝盖尖朝上，左脚尖绷直下垂，身体停顿蓄势；
  4. 帧 10 (Up): 左脚尖凌空伸向前探路，悬空摸索；
  5. 帧 13 (Contact): 左脚尖轻点地面，右脚脚后跟仍保持悬空；
  6. 帧 14–24: 对称完成另一半循环。
- **结果**: 戏剧悬疑感与滑稽效果极为出众，步态充满张力。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作经典卡通角色特定性格走姿（鬼鬼祟祟、得意忘形、欢快跳跃）；
2. 游戏角色潜行状态（Stealth mode）与胜利庆祝步态；
3. 排查角色行进步态千篇一律、缺乏戏剧表演性格。

### 语言信号 (Triggers)
- "经典卡通潜行步 The Sneak 怎么调帧数和动作"
- "昂首阔步 The Strut / Rooster walk 步态循环"
- "如何让角色走路看起来鬼鬼祟祟 / 骄傲自大"
- "卡通欢快跳跃步态 The Skip 姿态排布"

### 与相邻能力的区分
- 与 `walk-run-cycles` (Timing 领域) 的区别: 本能力聚焦经典好莱坞卡通性格表演与肢体极端造型（Sneak, Strut）；`walk-run-cycles` 侧重写实双足物理时间计算与防滑步。
- 与 `cartoon-run-locomotion` 的区别: 本能力处理常速与慢速行走步态；`cartoon-run` 专用于高速冲刺与极速飞轮跑。

## E — 可执行步骤 (Execution)

1. **选定性格步态类型**:
   - 鬼祟/偷盗/暗中观察 ➔ **The Sneak (潜行步)**；
   - 骄傲/炫耀/反派自得 ➔ **The Strut (昂首阔步)**；
   - 孩童/欢喜/雀跃 ➔ **The Skip (轻快跳跃步)**。
2. **排布节奏律表 (以 24 帧全循环为例)**:
   - 确定 Contact 帧（通常帧 1 与帧 13）；
   - 确定 Passing 极值帧（通常帧 7 与帧 19）。
3. **注入关键特征姿态**:
   - 若为 Sneak：Passing 帧大腿膝盖必须提到胸口，Contact 帧脚跟严格悬空，双手置于胸前轻微抖动；
   - 若为 Strut：Passing 帧胸膛必须挺到最高点并拉伸，脚后跟重击地面，头部反弓；
   - 若为 Skip：在单侧脚上插入连续两次着地蹬起帧。
4. **输出标准交付契约**:
   - 输出步态分类、关键帧清单（Contact/Down/Passing/Up）与重心 Y 轴高度曲线图。

## B — 边界与反模式 (Boundary)

### 失效边界
- 严谨军事写实步操或纪录片数字人，要求脚跟率先着地与标准军姿，不可套用卡通高抬腿潜行或反弓挺胸阔步。

### 常见反模式
- **潜行脚跟触地**: 画潜行步时让脚后跟先砸地，完全丧失了蹑手蹑脚的轻柔感；
- **阔步胸部僵硬**: 画昂首阔步时胸膛和后背没有起伏反弓，仅双腿外摆，显得动作油腻机械。
