# 能力卡: 拉链嘴唇渐进粘连绑定 (Zipper Lips Sticky Rig)

## Rationale (核心原理)
在写实与风格化角色动画中，嘴唇闭合与轻微张开的过渡阶段最容易出现“死板纸片感”。
当真实人类微微张嘴时，由于嘴唇表面黏膜（Moist Mucosa）的表面张力与黏附性，嘴角两侧并不会立刻分开，而是保持贴合；随着下巴进一步下沉拉大距离，贴合点由内向外呈“拉链式（Zipper Effect）”逐级撕开剥离。
如果不做粘连绑定，嘴巴一旦张开，嘴角两侧立刻呈现生硬直线的锐角开口，内部黑洞直接暴露，严重缺乏生物肉感。
Osipa 在第 11 章系统提出了利用成对顶点距离测量与余弦衰减驱动的**拉链唇绑定系统（Zipper / Sticky Lips Rig）**。

## Instruction (拉链唇解耦与距离衰减算法)

### 1. 唇部关键成对受控顶点拓扑分组
沿上下唇红缘从嘴角（Corner）向中央（Center）依次选取 $M$ 对成对顶点（通常 $M = 3 \sim 5$ 对）：
- Pair 0: 最靠近嘴角的第 1 对上下顶点（粘连最强，最后分开）；
- Pair 1: 距离嘴角次近的第 2 对顶点；
- Pair 2: 距离嘴角中等距离的第 3 对顶点；
- Pair $M-1$: 最靠近唇峰的受控边界点（粘连最弱，最早分开）。

### 2. 距离测量与衰减分离公式
在三维空间中实时计算上下唇几何对的全局空间距离 $d$（或下颌骨张开旋转角度 $\theta$）。
为每一对顶点 $i \in [0, M-1]$ 设定独立的分离距离阈值 $D_{\text{threshold}}(i)$：
$$D_{\text{threshold}}(i) = D_{\text{min}} + i \cdot \Delta D$$
对于第 $i$ 对顶点，计算其粘连权重 $W_{\text{sticky}}(i) \in [0.0, 1.0]$：
- 当 $d \le D_{\text{threshold}}(i)$ 时：完全粘连，
  $$\vec{V}_{\text{upper}}(i) = \vec{V}_{\text{lower}}(i) = \frac{\vec{V}_{\text{upper}} + \vec{V}_{\text{lower}}}{2}$$
- 当 $d > D_{\text{threshold}}(i)$ 且 $d < D_{\text{threshold}}(i) + \Delta S$ 时（平滑剥离过渡区）：
  使用 Smoothstep 或余弦函数将粘连权重平滑从 $1.0$ 衰减至 $0.0$；
- 当 $d \ge D_{\text{threshold}}(i) + \Delta S$ 时：完全脱离约束，$W_{\text{sticky}}(i) = 0.0$。

### 3. Maya 节点网络构建架构
- 使用 `distanceBetween` 节点测量上下唇基准 Locator 距离；
- 连接到 `remapValue` 或 `setRange` 节点，输出非线性衰减浮点值；
- 驱动上唇与下唇骨骼的 `PointConstraint` 混合权重（Weight 0 / Weight 1），或驱动特定粘连混合形的权重通道。

## Actionable Example (Python/Maya 粘连节点网络构建脚本)
```python
def create_zipper_lip_pair(upper_vtx_loc, lower_vtx_loc, driver_attr, threshold_val, range_val=0.5):
    """
    为单对唇部顶点构建基于距离衰减的拉链式驱动网络
    """
    import maya.cmds as cmds
    
    remap = cmds.createNode("remapValue", name="remap_zipper")
    cmds.setAttr(f"{remap}.inputMin", threshold_val)
    cmds.setAttr(f"{remap}.inputMax", threshold_val + range_val)
    cmds.setAttr(f"{remap}.outputMin", 1.0) # 1.0 为完全粘连
    cmds.setAttr(f"{remap}.outputMax", 0.0) # 0.0 为完全分离
    
    # 连接驱动属性 (如下巴张开度或局部距离)
    cmds.connectAttr(driver_attr, f"{remap}.inputValue")
    
    # 将输出连接至局部混合约束权重
    return remap
```

## Constraints (约束与禁止)
- **极限张口防拉花**: 当角色大声叫喊（Open > 0.8）时，粘连权重必须被彻底切断为 0，防止嘴角网格被错误向内拉扯产生细长面条状拉花；
- **左右对称独立控制**: 左右嘴角必须分别设立独立的计算网络与总开关（`Zipper_Lips_Left` / `Zipper_Lips_Right`），支持角色做出单侧嘴角撇嘴说话、单侧粘连的不对称生动表情。

## Verification (验收标准)
- **逐级撕开视觉检验**: 极其缓慢地从 0.0 到 0.5 增加下巴开合度，观察嘴角顶点：最中央先分离，随后逐对向外展开，最后在嘴角处分离，全程无生硬跳变；
- **微张对白自然度**: 在微张状态下说对白（如 "ssss", "mmmm"），嘴角保持紧致封闭，避免口腔侧面产生突兀空隙。
