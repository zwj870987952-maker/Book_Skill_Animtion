## R — 原文 (Reading)

> “An object is balanced if its center of gravity is supported. The line of gravity is an imaginary vertical line that extends downward from the center of gravity to the ground. If this line passes within the base of support, the object remains stable. If the line of gravity falls outside the base of support, the object tips over unless a new support is created.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 3, pp. 70–73

## I — 方法论骨架 (Interpretation)

角色姿态的物理平衡与稳定度，取决于质心（Center of Gravity, CG）、重力垂线（Line of Gravity, LOG）与支撑多边形底面（Base of Support, BOS）三者的几何相对关系：
1. **重心位置**: 成人双腿站立时，质心通常位于肚脐下方、骨盆骶骨前方约 55% 身高处；四肢展开或举重时，质心随肢体位置发生显著位移；
2. **平衡判据**: 从质心垂直向地面投影重力垂线。若投影落点严格位于双足（或手脚接触点）构成的凸多边形支撑区域内，系统力矩平衡，角色稳定；
3. **失衡与倾覆**: 一旦重力垂线越出支撑底面外缘，重力将对支撑边缘产生倾覆力矩（$\tau = mg \times d$）。角色必须在 1–3 帧内产生摔倒、前跌，或者向前大步迈腿以重建支撑底面。

## A1 — 案例 (Application Example)

### 书中例题: 角色单脚踢腿前的重心代偿平移 (worked_example)
- **任务**: 角色由双脚站立姿态转为右腿向前高踢，要求姿态真实稳定不违和。
- **执行过程**:
  1. 初始姿态：双脚着地，支撑面包括两脚掌及两脚之间的地面矩形，LOG 居中；
  2. 预备阶段（帧 1–4）：角色骨盆与上身向左侧主动平移约 15 厘米，使 LOG 准确投射在左脚掌中心；
  3. 执行踢击（帧 5–10）：右腿脱离地面向前踢出；同时左臂自然向后摆动以平衡右腿向前产生的偏心力矩；
  4. 恢复站立：右腿收回触地前，躯干重新向右侧平移复位。
- **结果**: 彻底消除了“双腿正中站立却能凭空抬起单脚不倒”的反重力悬浮假象。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 设计角色单脚独立、走钢丝、弯腰捡物、推重物等极限静止或慢速平衡姿态；
2. 制作角色被推搡失衡踉跄跌倒的过程；
3. 检查角色站立姿态看起来像“反重力魔术”或“被胶水粘在地板上”的失真。

### 语言信号 (Triggers)
- "角色站立姿态怎么摆才不倒 / 重心怎么找"
- "Base of support and line of gravity balance check"
- "角色失衡摔倒动作怎么调 / 为什么踢腿看起来很假"
- "弯腰举重物时的重心偏移与代偿"

### 与相邻能力的区分
- 与 `character-walk-energy` 的区别: 本能力用于静态或准静态姿态平衡与倾覆临界点判定；`character-walk-energy` 用于行走中倒单摆动态能量转移。
- 与 `torque-lever-joints` 的区别: 本能力聚焦质心位置与地面支撑几何；`torque-lever` 聚焦关节局部旋转力矩与角动量。

## E — 可执行步骤 (Execution)

1. **估算角色当前姿态质心 (CG)**:
   - 躯干与头部占总体重约 60%，双臂各占 5%，双腿各占 15%；
   - 根据各肢体位置加权合成整体质心坐标 $(X_{cg}, Y_{cg}, Z_{cg})$。
2. **构建触地支撑底面多边形 (BOS)**:
   - 提取所有与地面接触的顶点（如左足跟、左足尖、右足跟、右足尖）；
   - 生成包围这些接触点的二维外凸几何多边形。
3. **执行重力垂线投射判定**:
   - 投射地面点 $P = (X_{cg}, Z_{cg})$；
   - 检查 $P$ 是否在多边形 BOS 内部：
     - 若 $P \in \text{BOS}$ ➔ **稳态平衡**，计算稳定裕度（距离边缘最小距离）；
     - 若 $P \notin \text{BOS}$ ➔ **失衡状态**，计算倾覆距离 $d_{tip}$。
4. **决策动作响应**:
   - 若失衡且未倒下：必须在 1–3 帧内产生摆动腿落地（前跨步），或在 $1–4$ 帧内执行倾倒倒地动画。

## B — 边界与反模式 (Boundary)

### 失效边界
- 在高速奔跑或摩托车压弯飞驰等动态运动中，离心力（惯性力）会打破纯重力垂线平衡，此时倾斜身体是为了利用重力力矩抵消离心力矩，不可套用静态垂直投影。

### 常见反模式
- **反重力单脚独立**: 身体完全没有横向位移，直接把一只脚抬起，重力垂线悬空在两脚中间；
- **倾覆无跌倒**: 上身大幅度探出窗外超过 45 度，双脚脚后跟未翘起也未迈步，像被焊死在地面。
