## R — 原文 (Reading)

> “In animating four-legged animals, study their footfalls carefully. In a standard walk, the four feet touch the ground in a rotary sequence: left hind, left fore, right hind, right fore. In the trot, diagonal pairs of legs move together. In the gallop, the horse reaches out in full extension, leaps entirely off the ground, and bunches up its legs under the body for the next powerful leap.”
> 
> —— Preston Blair, *Cartoon Animation*, Chapter 2, pp. 106–114

## I — 方法论骨架 (Interpretation)

四足动物（马、狗、猫、鹿）的解剖结构与步态规律具有极其严格的生物学几何逻辑：
1. **慢步行走 (The Animal Walk)**:
   - 永远遵循稳定的四拍旋转步序：**左后足 ➔ 左前足 ➔ 右后足 ➔ 右前足**；
   - 在任意瞬间，地面上始终保持 3 只脚接触支撑，重心转移平缓稳定；
2. **快步小跑 (The Trot)**:
   - 对角线肢体成对同步运动：**左前 + 右后** 同步向前，紧接着 **右前 + 左后** 同步向前；
   - 具有两个对称的短暂空中腾空期，躯干起伏平稳，节奏轻快；
3. **飞奔步态 (The Gallop)**:
   - 依靠脊椎的强力弓起与伸展产生巨大弹性推力；
   - **双重悬空期 (Double Suspension)**:
     1. 完全舒展腾空（Full Extension）：四蹄完全向外拉伸，身体在空中如直线飞箭；
     2. 完全团身腾空（Full Contraction）：四蹄在腹部下方收缩交错抱团；
   - 后腿先行蹬地释能，前腿先后落地缓冲支撑。

## A1 — 案例 (Application Example)

### 书中例题: 16 帧经典马匹飞奔 (Gallop) 全循环排布 (worked_example)
- **任务**: 制作一匹矫健马匹全速飞奔的 16 帧经典循环动画（24fps）。
- **执行过程**:
  1. 帧 1–3 (Rear Push & Lift): 双后腿先后落地蹬出最后一波推力；
  2. 帧 4–6 (Extended Flight): 核心伸展腾空期—脊椎反向拉直，双前腿向前全力刺出，双后腿向后平直拉伸，四蹄全部离开地面悬空飞驰；
  3. 帧 7–9 (Front Landing): 左前蹄率先着地受力，紧接着右前蹄在第 9 帧向前落地支撑并拉动身体；
  4. 帧 10–12 (Gathered Flight): 核心团身腾空期—腹部肌肉急剧收缩，双后腿从外侧向前抽射穿越腹下，四蹄在空中团聚；
  5. 帧 13–16 (Rear Touchdown): 双后腿准备触地，进入下一轮循环。
- **结果**: 马匹飞奔极具英姿飒爽的力量感，脊椎弹簧般的波动活灵活现。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作狗、猫、马、狼、鹿、狮子等四足动物行走、小跑与飞奔；
2. 制作奇幻四足怪兽（如龙、半人马、坐骑）的基础移动步态；
3. 排查四足动物走姿出现“同侧前后腿顺拐”或“左右对称青蛙跳”的严重错误。

### 语言信号 (Triggers)
- "四足动物走步先后顺序 / animal walk sequence"
- "马匹飞奔 gallop 几帧一个循环 / 脊椎伸展与团身"
- "小跑 Trot 对角线步态排布"
- "狗/猫跑步步态动画制作"

### 与相邻能力的区分
- 与 `quadruped-locomotion` (Timing 领域) 的区别: 本能力融汇了普雷斯顿·布莱尔针对四足动物骨骼解剖（肩胛骨、肘、飞节、掌骨）的手绘原画造型与动态姿态库；`quadruped-locomotion` 侧重时钟律表对齐。
- 与 `cartoon-run-locomotion` 的区别: 本能力处理四足生物多支点步态；`cartoon-run` 专用于人类/双足拟人角色奔跑。

## E — 可执行步骤 (Execution)

1. **确定四足步态类型**:
   - 慢步漫游 ➔ **Walk (四拍轮转)**；
   - 节奏轻快赶路 ➔ **Trot (对角线双拍)**；
   - 全力追逐逃命 ➔ **Gallop (脊椎伸缩双重腾空)**。
2. **按照刚性触地顺序排布关键帧**:
   - 若为 Walk：严格分配时差（左后 $\to$ 左前 $\to$ 右后 $\to$ 右前）；
   - 若为 Trot：左前+右后同帧，右前+左后同帧；
   - 若为 Gallop：必须包含帧 5（完全伸展大悬空）与帧 11（完全团身小悬空）。
3. **调校脊柱与头尾起伏**:
   - 前肢落地受压时，头部被迫向下沉降缓冲；
   - 前肢蹬离地面时，头部自然向上抬起；尾巴随脊椎做次级延迟波浪运动。
4. **输出标准交付契约**:
   - 输出四足触地律表矩阵、脊椎屈伸角度表与关键姿态线稿图。

## B — 边界与反模式 (Boundary)

### 失效边界
- 昆虫（六足三角步态）与爬行动物（鳄鱼、蜥蜴的水平 S 形侧身扭动爬行），不遵循哺乳动物的垂直屈伸飞奔动力学。

### 常见反模式
- **左右顺拐**: 同侧前腿与后腿同时向前迈出，生物学上严重失衡；
- **青蛙对称跳**: 奔跑时双前腿同时落地、双后腿同时落地，将优雅飞奔画成了蛤蟆蹦跶。
