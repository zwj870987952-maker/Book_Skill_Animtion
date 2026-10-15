## R — 原文 (Reading)

> “Wave action is the basis of movement for many flexible things—ropes, whips, ribbons, and tails. When a whip is snapped, the hand moves first, starting a wave that travels down the length of the whip to the tip. By the time the tip reaches the extreme position, the handle has already started back in the opposite direction. This delay creates the classic whip snap.”
> 
> —— Preston Blair, *Cartoon Animation*, Chapter 3, pp. 140–145

## I — 方法论骨架 (Interpretation)

波浪运动（Wave Action）是赋予一切柔韧物体与次级肢体灵动生命力的物理精髓：
1. **逐级延迟与波动传递**:
   - 柔性链条（如皮鞭、丝带、松鼠尾巴、章鱼触角）受到根部主动关节驱动时，波动绝不会瞬间到达末梢；
   - 动力沿骨骼链顺次向末梢逐级传递，**每一级骨骼节点相对于上一节点产生 1–2 帧的时间滞后（Keyframe Offset）**；
2. **反向交错与“S”形弯曲**:
   - 当根部关节到达第一个方向的极值并开始折返往回运动时，中段关节才刚刚到达该极值，而末梢节点依然留在原本的相反方向；
   - 这一时差导致链条在空间中必然扭动成流畅优美的正“S”形或反“S”形多重弯曲波峰；
3. **末梢过冲与抽打爆破 (Whip Snap & Overshoot)**:
   - 随动能在末端汇聚，末梢节点最终以远超根部的高速甩过平衡位置（Overshoot），释放出如鞭梢抽响般的锐利弹性。

## A1 — 案例 (Application Example)

### 书中例题: 松鼠跳跃落地大尾巴 12 帧波浪摆动排布 (worked_example)
- **任务**: 制作松鼠跳下落地停稳后，蓬松大尾巴随之翻滚平复的 12 帧次级波浪动画。
- **执行过程**:
  1. 骨骼分段：将尾巴从根部至末梢标记为 Node-0(Root), Node-1, Node-2, Node-3(Tip) 四级节点；
  2. 帧 1–3: 松鼠身体落地停下，Node-0 顺惯性向下沉降压低；Node-1/2/3 滞后留在上方；
  3. 帧 4–6: Node-0 开始向上回弹；向上推力传导至 Node-1；Node-2 与 Node-3 受阻向下弯折，形成优雅的深 S 形大波浪；
  4. 帧 7–9: 波动冲抵 Node-3 尾尖，尾尖以极大弧线向前猛烈翻滚过冲并甩开；
  5. 帧 10–12: 尾尖在空气阻力下经历 2 帧微小摆动，平稳贴伏在松鼠后背。
- **结果**: 尾巴显得毛茸茸、极度柔韧饱满，彻底告别了硬塑料木棍感。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作皮鞭甩动、丝带舞动、跳绳、水下水草摆动；
2. 制作动物尾巴（猫尾、松鼠尾、恐龙长尾）与章鱼触手的生动次级运动；
3. 排查柔性链条看起来像“硬木棍扫地”或“全链条同步开合”的僵硬缺陷。

### 语言信号 (Triggers)
- "波浪运动 Wave action 怎么排关键帧 / 鞭梢原理"
- "如何调出柔软多关节尾巴/绳子的次级动画"
- "S形弯曲与多级骨骼延迟 offset 调校"
- "皮鞭抽打与末端过冲 overshoot"

### 与相邻能力的区分
- 与 `drag-follow-through-physics` (Physics 领域) 的区别: 本能力聚焦手绘原画经典 S 弯造型、波峰波谷曲率几何与多级骨骼手绘层级；`drag-follow-through` 侧重重力单摆公式与空气风阻数值推导。
- 与 `animal-quadruped-cycles` 的区别: 本能力用于柔性附庸物多级波动；`animal-quadruped` 关注四足刚性骨骼步态。

## E — 可执行步骤 (Execution)

1. **链条节点离散化 (骨骼链划分)**:
   - 将柔性物体沿长度等距划分为 $M$ 个节点（通常 $M = 4–6$）；
   - 明确 Node-0 为主动驱动源，Node-$(M-1)$ 为自由随动末梢。
2. **构建时序阶梯延迟 (Offset Ladder)**:
   - 确定基准半周期帧数 $T_{half}$；
   - 为各节点设置旋转关键帧时间偏移：
     - Node-0: 第 0 帧转折；
     - Node-1: 第 2 帧转折（延迟 2 帧）；
     - Node-2: 第 4 帧转折（延迟 4 帧）；
     - Node-3: 第 6 帧转折（延迟 6 帧）。
3. **校准 S 弯与 C 弯几何形态**:
   - 检查中段帧（帧 4 附近）：必须呈现出两个反向弯曲的波峰与波谷（“S”形）；
   - 检查末端到达极值时（帧 7 附近）：末端弧线必须发生明显的过冲（Overshoot $15\%–25\%$）。
4. **输出标准交付契约**:
   - 输出骨骼链层级偏移律表、中段 S 弯姿态草图与末梢过冲振幅数据。

## B — 边界与反模式 (Boundary)

### 失效边界
- 极高刚度材料（如高强度金属杆、钢管），在微观上虽有振动，但在宏观上形变不可见，绝不可强行套用 S 形波浪软体波动。

### 常见反模式
- **全节点同步摆动**: 所有关节在同一帧一起到达左端或右端，像雨刷器一样生硬；
- **过度软化成面条**: 缺乏根部主动力的有效控制，各节点相位混乱，变成失去重量形态的面条抽搐。
