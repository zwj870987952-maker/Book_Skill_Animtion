## R — 原文 (Reading)

> “Walking is an efficient exchange between kinetic energy and gravitational potential energy, functioning mechanically like an inverted pendulum. The body’s center of mass is highest and moving slowest at the passing position, and lowest and moving fastest at the contact position. To conserve angular momentum, the shoulders twist in the opposite direction of the hips.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 6, pp. 201–205

## I — 方法论骨架 (Interpretation)

双足行走是人类最高效的能量循环系统，其机械本质是“受控的前跌与倒单摆势能转换”：
1. **倒单摆动能与势能转换**:
   - **接触点 (Contact)**: 双腿跨度最大，重心最低，此时前进速度最快（动能处于峰值）；
   - **过路点 (Passing)**: 身体以单侧支撑腿为轴向上翻滚，骨盆和重心抬至全周期最高点，前进速度降至谷底（重力势能处于峰值）；
   - 随重心向前翻过支撑腿，重力势能再次转化为向前下跌的动能；
2. **反向力矩守恒 (Counter-Rotation)**:
   - 单侧腿向前迈步时，骨盆向前挺出产生绕垂直轴的转矩；为保持角动量守恒，胸腔与肩甲骨必须朝反方向旋转，手臂向前摆动以抵消转动惯量，保证身体沿直线前进而不发生偏航打转。

## A1 — 案例 (Application Example)

### 书中例题: 24 帧标准写实行走重心起伏与肩髋扭转调校 (worked_example)
- **任务**: 制作一段 24 帧（双步全循环，24fps）的成人自然行走循环。
- **执行过程**:
  1. 设定关键时间帧：
     - 第 1 帧与第 13 帧为左/右脚 Contact 触地点（重心 Y 轴处于最低点，前进速度最快）；
     - 第 4 帧与第 16 帧为 Down 受压缓冲帧（前膝吸收冲击，保持低位）；
     - 第 7 帧与第 19 帧为 Passing 过路帧（重心 Y 轴处于最高点，前进速度最慢）；
     - 第 10 帧与第 22 帧为 Up 蹬踏推力帧；
  2. 调节肩髋反向扭转：
     - 在第 1 帧，左腿向前迈，左侧骨盆向前旋转 $+6^\circ$；左侧肩部向后旋转 $-8^\circ$（反向互锁）；
     - 右侧手臂向前摆动 $+25^\circ$，左臂向后摆动 $-15^\circ$；
  3. 在第 13 帧对称互换角度。
- **结果**: 步态极其沉稳自然，能量交换平滑，彻底消除木偶平移感。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作高写实度角色行走、跑步、竞走与负重行进步态；
2. 纠正角色行走时“上身僵死像木头”、“下半身平移像滑冰”的动画缺陷；
3. 检查肩甲骨与骨盆在行走中的三轴扭转耦合。

### 语言信号 (Triggers)
- "行走循环重心起伏怎么定 / 倒单摆模型"
- "Inverted pendulum model for character walking"
- "行走中肩部和胯部怎么反向扭转 / 消除走路上半身僵硬"
- "触地点与过路点的速度与高度关系"

### 与相邻能力的区分
- 与 `walk-run-cycles` (Timing 领域) 的区别: 本能力从经典物理能量守恒（势能/动能倒单摆）与三轴角动量反向力矩深度建模；`walk-run-cycles` 侧重四相位脚掌时间分配与滑步排障。
- 与 `center-of-gravity-balance` 的区别: 本能力处理行进中的动态能量流；`center-of-gravity` 处理静态或单步跨越的支撑多边形失衡。

## E — 可执行步骤 (Execution)

1. **确立步态时间轴节奏 (以 24 帧全循环为例)**:
   - 帧 1: 左脚 Contact（重心高度低，速度快）；
   - 帧 4: 左脚 Recoil/Down（冲击吸收，深度微屈）；
   - 帧 7: 左腿支撑 Passing（重心高度达到波峰，前进速度慢）；
   - 帧 10: 左脚 Up（足跟抬起向前推）；
   - 帧 13: 右脚 Contact（对称切换）。
2. **调校重心 Y 轴高度曲线与前进位移曲线**:
   - Y 轴高度曲线在 Passing 帧达到波峰，在 Down 帧达到波谷；
   - X/Z 轴前进速度曲线在 Passing 帧设置缓入，在 Contact 帧保持斜率平直。
3. **设置肩髋反相旋转键**:
   - 骨盆（Hips）水平旋转（Yaw）：前迈腿侧向前转动 $4^\circ–8^\circ$；
   - 胸部（Spine/Chest）水平旋转（Yaw）：与骨盆方向严格相反，反向转动 $6^\circ–10^\circ$；
   - 骨盆侧倾（Roll）：悬空摆动腿侧骨盆轻微向下倾斜 $3^\circ–5^\circ$。
4. **输出标准交付契约**:
   - 输出完整的 4 个相位重心波形数据与肩髋扭转极限角度表。

## B — 边界与反模式 (Boundary)

### 失效边界
- 机器人、外骨骼装甲或机械行进底盘不依赖重力势能与肌腱弹性蓄能，其机电推杆可以实现纯水平直线平移，不遵循倒单摆能量转换。

### 常见反模式
- **水平切片行走**: 重心高度全程保持绝对水平一条直线，双腿像圆规在下方剪刀式滑动；
- **同向顺拐扭转**: 骨盆向前转动时，肩膀也跟着向前转动，角色走姿怪异如机械人偶。
