import json
from pathlib import Path

cand_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\animators-survival-kit\candidates")
cand_dir.mkdir(parents=True, exist_ok=True)

# 1. frameworks.md
frameworks_md = """# 框架候选池 (Frameworks Candidates)

## 1. 时空双轴标尺 (Timing & Spacing Duality)
- **定义**: 动画工程的核心两端。时间 (Timing) 是完成一个动作所消耗的绝对物理帧数 (Frames / Seconds)；空间 (Spacing) 是在两张关键帧之间，相邻中割帧之间的距离差 (Distance / Spacing)。
- **核心公式**: 匀速运动 (Equal Spacing)、慢入 (Slow-In / Ease-In)、慢出 (Slow-Out / Ease-Out)、偏心轨目 (Favored Breakdowns)。
- **来源**: Richard Williams, The Animator's Survival Kit, Chapter 'Timing and Spacing', pp. 35–45.

## 2. 动画帧分级四层架构 (Hierarchy of Animation Drawings)
- **定义**:
  1. 关键帧 (Keys / Key Drawings): 决定叙事故事点、剧情转折与核心概念的关键姿态；
  2. 极值帧 (Extremes): 动作在几何空间位移中的最高点、最低点、最远点；
  3. 过渡原画 (Breakdowns / Passing): 决定两张极值帧之间身体各部分位移路径与形态倾向的核心中间画；
  4. 中割帧 (Inbetweens): 按照轨目表纯机械或半机械插值的补间画。
- **来源**: Richard Williams, The Animator's Survival Kit, Chapter 'Keys, Extremes, Breakdowns', pp. 47–69.

## 3. 人类标准行走四大黄金帧 (The Four Golden Poses of Walk Locomotion)
- **定义**:
  1. 接触位 (Contact Position): 双脚同时着地，前脚跟触地，后脚尖蹬地，重心处于两脚之间；
  2. 下沉缓冲位 (Down / Recoil Position): 前腿膝盖弯曲吸收落地冲击，角色重心降至全周期最低点；
  3. 越过位 (Passing Position): 摆动腿抬起掠过承重腿，骨盆与胸廓产生侧向倾斜，重心回升；
  4. 抬起最高位 (High / Reach Position): 承重腿脚后跟离地蹬直，摆动腿向前探出，角色重心升至全周期最高点。
- **来源**: Richard Williams, The Animator's Survival Kit, Chapter 'Walks', pp. 102–155.

## 4. 奔跑腾空与受力全周期 (The Running Engine & Airborne Flight)
- **定义**: 奔跑与行走的本质分水岭是“双脚完全离地的腾空悬浮期 (Airborne Float)”。标准奔跑包含单脚受压接触位、反冲下沉位、后蹬释能推离位与双脚悬空腾空位。
- **来源**: Richard Williams, The Animator's Survival Kit, Chapter 'Runs, Jumps and Skips', pp. 176–210.

## 5. 动作预感、反冲与超量阻尼 (Anticipation, Overshoot & Settle)
- **定义**: 任何强力动作必须具备方向相反的预备蓄力 (Anticipation)；当动作到达极值时，由于惯性作用身体会冲过目标位置 (Overshoot)，随后在阻尼反弹中恢复平稳 (Settle)。
- **来源**: Richard Williams, The Animator's Survival Kit, Chapter 'Anticipation', pp. 256–284.

## 6. 对白口型视素 2-4 帧超前量法则 (Dialogue Phoneme Advance Rule)
- **定义**: 人类大脑在看见说话者的口型动作时，神经处理速度比听到声音慢几个毫秒；同时声带振动发出声音之前，嘴唇与下颌必须先形成该发音的物理共鸣腔。因此动画中的关键嘴型视素必须比声带音频提前 2 到 4 帧开启。
- **来源**: Richard Williams, The Animator's Survival Kit, Chapter 'Dialogue', pp. 304–326.
"""
(cand_dir / "frameworks.md").write_text(frameworks_md, encoding="utf-8")

# 2. principles.md
principles_md = """# 原则候选池 (Principles Candidates)

1. **时空双轴绝对分离原则 (Separation of Timing & Spacing)**:
   - 增加帧数改变的是时间速度；改变帧与帧之间的距离分布改变的是重量感与力感。两者严禁混淆。

2. **过渡原画决定一切法则 (Breakdowns Dictate the Action)**:
   - 两个极值帧完全相同的动作，仅凭过渡原画 (Breakdown) 的不同（走上弧、走下弧、头部滞后或先行），就能创造出自信、沮丧、轻盈或沉重完全相反的动作质感。

3. **人类行走重心中轴高低波动律 (Center of Gravity Wave in Walks)**:
   - 行走不是水平滑行，而是倒单摆的交替跌落与抬升：下沉位 (Down) 最低，最高位 (High) 达到波峰，形成连续的正弦波起伏。

4. **奔跑必有腾空悬浮期 (Running Mandates Airborne Flight)**:
   - 没有任何一帧双脚同时离地的“奔跑”只是快步走。真正的奔跑至少有 1-3 帧完全悬空，且身体前倾角度与奔跑速度成正比。

5. **圆滑弧线轨迹原则 (The Law of Arcs)**:
   - 除了机械活塞与激光束，所有活生生的生命关节运动轨迹都是圆滑弧线。直线移动会导致动作机械、僵硬、穿模。

6. **多级重叠延迟法则 (Overlapping Succession)**:
   - 骨盆与躯干主动力源先动，头部与四肢滞后跟随，松弛皮肤、长发、衣物等末端附属物最后拖尾并发生正弦波甩动。全身体块同帧起止是动画的致命缺陷。

7. **口型超前 2-4 帧声学感知原则 (Dialogue 2-4 Frames Advance)**:
   - 口型与发音同帧播放会导致视觉上的“口型滞后迟钝感”。嘴巴必须在声音爆破前 2-4 帧张开到位。
"""
(cand_dir / "principles.md").write_text(principles_md, encoding="utf-8")

# 3. cases.md
cases_md = """# 案例候选池 (Cases Candidates)

1. **经典 24 帧标准写实行走循环 (24-Frame Standard Walk Cycle)**:
   - 步频: 1 秒走 2 步 (每步 12 帧，循环为 24 帧)。
   - 第 1 帧: 右脚向前脚跟接触 (Contact)；
   - 第 4 帧: 右腿受力弯曲下沉 (Down)；
   - 第 7 帧: 左腿跨过右腿越过位 (Passing)；
   - 第 10 帧: 右腿蹬直最高位 (High)；
   - 第 13 帧: 左脚向前脚跟接触 (Contact，完成半个循环)；
   - 第 16 帧: 左腿受力下沉 (Down)；
   - 第 19 帧: 右腿越过位 (Passing)；
   - 第 22 帧: 左腿最高位 (High)；
   - 第 25/1 帧: 闭环重回右脚接触位。

2. **4 帧爆发性极速狂奔 (4-Frame Fast Run)**:
   - 第 1 帧: 右脚着地蹬地受力；
   - 第 2 帧: 身体向前剧烈前倾，右腿后蹬推离；
   - 第 3 帧: 全身完全腾空，双腿如飞轮般在空中大跨度拉伸；
   - 第 4 帧: 左脚向前着地冲击。全循环仅需 8 帧，呈现超强动能。

3. **重型铁球 vs. 弹性橡胶球受力挤压 (Bowling Ball vs. Rubber Ball)**:
   - 铁球从高处落下：由于刚性与极重重量，触地几乎无挤压变形，在地面发生微小反冲后在 2 帧内迅速沉降制动；
   - 橡胶球从高处落下：触地时发生 150% 横向挤压展平，随后以超快初速度反弹腾空，经历多次衰减后平稳。

4. **蹑手蹑脚潜行步态 (The Sneak Walk)**:
   - 步频拉长至 16-24 帧每步。
   - 角色重心极度压低，前脚向前探出时使用脚尖轻轻试探接触地面，确认无声后再缓慢转移重心承重，伴随夸张的左右顾盼眼神视线。
"""
(cand_dir / "cases.md").write_text(cases_md, encoding="utf-8")

# 4. counter-examples.md
counter_examples_md = """# 反例与常见病灶候选池 (Counter-Examples & Anti-Patterns)

1. **机械节拍器均等轨目病 (Equal Spacing / Metronome Bug)**:
   - 病灶: 中割帧完全等距离均分，导致挥臂、行走毫无轻重缓急，动作像发条玩具或传送带零件。
   - 治愈: 绘制非对称轨目表，施加明确的慢入慢出 (Slow-in / Slow-out) 或偏心倾向 (Favors)。

2. **滑步太空漫步漂浮病 (Moonwalking / Foot Sliding)**:
   - 病灶: 行走接触位与下沉位中，着地脚的水平位移与摄像机/地面速度不匹配，导致脚底在地面打滑摩擦。
   - 治愈: 严格锁定接触脚在世界空间中的 X/Z 轴绝对坐标，直到后蹬帧脚尖离地前严禁发生水平位移。

3. **无腾空假奔跑 (Flightless Fake Run)**:
   - 病灶: 角色双脚在全周期内始终有一只脚踩在地上，却企图通过快速摆动手臂伪造奔跑。
   - 治愈: 在推离帧与落地帧之间插入 1-3 帧完全离地的腾空悬浮帧 (Airborne Frames)，拉大双腿跨度。

4. **口型同步迟钝滞后 (Late Mouth / Sound Delay)**:
   - 病灶: 听到爆破音时嘴唇才刚刚开始动作，观者感知严重脱节。
   - 治愈: 将所有口型关键帧整体向左平移 2 到 4 帧，确保嘴型在发声前提前就位。
"""
(cand_dir / "counter-examples.md").write_text(counter_examples_md, encoding="utf-8")

# 5. glossary.md
glossary_md = """# 术语候选池 (Glossary Candidates)

1. **Timing (时间)**: 完成一个动作所消耗的物理帧数或秒数。
2. **Spacing (空间幅度)**: 连续帧之间在屏幕物理空间中的位移跨度与加减速分布。
3. **Spacing Chart (轨目表)**: 动画师在原画纸边缘或摄影表上绘制的图示，标明关键帧之间中割帧的插值距离分配（如 1/2 切分、慢入慢出）。
4. **Key Drawing (关键帧)**: 决定动作情节转折与叙事意图的核心姿态。
5. **Extreme (极值帧)**: 角色动作在物理空间位移轨迹上的最高、最低、最左、最右等几何极值点。
6. **Breakdown (过渡原画 / 原画中割)**: 连接两张极值帧的核心过渡帧，决定动作的弧线走向、身体重叠与优先倾向。
7. **Contact Position (接触位)**: 行走步态中双脚同时着地、前后分开的最大跨步姿态。
8. **Down / Recoil Position (下沉缓冲位)**: 行走步态中前腿膝盖弯曲吸收重力冲击的最低重心姿态。
9. **Passing Position (越过位)**: 行走步态中摆动腿经过承重腿时的单腿支撑姿态。
10. **High Position (抬起最高位)**: 承重腿脚后跟蹬离地面、身体重心升至顶点的姿态。
11. **Anticipation (动作预感)**: 动作爆发前向相反方向进行的蓄力预备动作。
12. **Overshoot & Settle (超量过冲与缓冲沉降)**: 惯性导致动作冲过目标位置后的阻尼回弹稳定过程。
13. **Airborne / Flight (腾空悬浮)**: 奔跑与跳跃中双脚完全离开地平面的滞空时间。
14. **Phoneme (视素 / 口型音素)**: 对应特定声学发音的视觉嘴部形态。
15. **Smear Drawing (残影涂抹画)**: 为表现极速运动而在一帧内拉伸出的模糊长残影或多重肢体。
"""
(cand_dir / "glossary.md").write_text(glossary_md, encoding="utf-8")

print("Created all 5 candidate files for Animators Survival Kit successfully!")
