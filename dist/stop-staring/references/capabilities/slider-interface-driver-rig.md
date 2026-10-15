# 能力卡: 二维滑块面部控制器界面与驱动键约束 (2D Slider Interface Rig)

## Rationale (核心原理)
无论底层的面部解剖骨骼和目标体雕刻得多么完美，如果绑定师留给动画师的是 80 多个散乱在视口中或属性通道栏里的单一浮点属性滑块，动画师的工作效率与创作欲望将瞬间崩溃。
动画师在赶工期时，根本没有时间去逐个测试“滑块 A 开到 0.3、滑块 B 开到 0.7 会不会冲突”。
Jason Osipa 颠覆性地发明了 **“二维盒子滑块控制面板（2D Box Slider Interface）”**：
将相互关联且具物理互斥边界的面部自由度，投射至位于正方形平面线框内移动的物理控制器手柄（Handle Control）；通过线框几何边界（Bounding Limits）直接在硬件交互层物理阻断一切非法组合，并利用驱动键（Set Driven Key, SDK）实现高度线性的正交能量映射。

## Instruction (二维界面布局与驱动键拓扑规范)

### 1. 标准二维滑块控制器几何结构
- **外框 (Boundary Box)**: 由 NURBS 曲线构建的边长为 2 单位（$[-1.0, 1.0] \times [-1.0, 1.0]$ 或 $[0.0, 1.0] \times [0.0, 1.0]$）的正方形平面；
- **控制手柄 (Puck / Handle)**: 置于方框内的圆形小控制器，其平移属性 `translateX` 与 `translateY` 设置硬性边界限制（Limit Information）：
  $$\text{minX} \le X \le \text{maxX}, \quad \text{minY} \le Y \le \text{maxY}$$
  锁定并隐藏除平移以外的全部旋转、缩放通道。

### 2. 三大核心二维滑块拓扑布局
```
  [ 口型控制面板 (Mouth Box) ]          [ 左眉面板 (L Brow) ]          [ 右眉面板 (R Brow) ]
         +1.0 (Open 张嘴)                      +1.0 (Inner Up)                +1.0 (Inner Up)
               |                                     |                              |
 -1.0 ---------+--------- +1.0         -1.0 ---------+--------- +1.0  -1.0 ---------+--------- +1.0
(Wide 展唇)    |       (Narrow 噘嘴) (Squeeze 挤压)  |        (Relax)(Relax)        | (Squeeze 挤压)
               |                                     |                              |
          0.0 (Closed 闭合)                    -1.0 (Inner Down)              -1.0 (Inner Down)
```
1. **口型主滑块**: 
   - $X$ 轴映射 `Wide` (向左) 到 `Narrow` (向右)；
   - $Y$ 轴映射 `Closed` (底部 0.0) 到 `Open` (顶部 1.0)；
2. **眉毛主滑块 (双侧对称独立)**:
   - $X$ 轴映射 `Squeeze` (向中线滑动为挤压) 到 `Relax` (向外滑动为舒展)；
   - $Y$ 轴映射 `Inner Brow Up` (向上) 到 `Inner Brow Down` (向下)；
   - 手柄的 `rotateZ` 通道映射 `Outer Brow Up / Down`，实现单个控制器统管一整根眉毛的所有自由度；
3. **眼睑滑块**:
   - $Y$ 轴正向映射 `Upper Lid Open`，负向映射 `Blink`；
   - $X$ 轴映射 `Squint`（下眼睑紧绷挤压）。

### 3. 驱动键 (Set Driven Key, SDK) 设置范式
- **驱动者 (Driver)**: 控制手柄的归一化平移通道（如 `mouth_ctrl.translateY`）；
- **被驱动者 (Driven)**: 目标体的权重属性（如 `blendShape1.mouth_open`）；
- **关键帧映射**:
  - Driver $= 0.0 \implies$ Driven $= 0.0$；
  - Driver $= 1.0 \implies$ Driven $= 1.0$；
  - 切线模式（Tangents）统一设置为 **Linear（线性）**，严禁使用非线性平滑切线，确保手柄位移与面部形变在触感上绝对同步。

## Actionable Example (Python/Maya 快速生成标准 2D 滑块面板)
```python
def create_2d_slider(name="mouth_slider", x_range=(-1.0, 1.0), y_range=(0.0, 1.0)):
    """
    快速生成带有精准位移限制的 Osipa 风格 2D 控制界面
    """
    import maya.cmds as cmds
    
    # 创建边界线框
    box = cmds.curve(d=1, p=[(x_range[0], y_range[0], 0), (x_range[1], y_range[0], 0),
                             (x_range[1], y_range[1], 0), (x_range[0], y_range[1], 0),
                             (x_range[0], y_range[0], 0)], k=[0,1,2,3,4], n=f"{name}_box")
    # 创建控制手柄
    handle = cmds.circle(r=0.15, nr=(0, 0, 1), n=f"{name}_ctrl")[0]
    
    # 设置限制
    cmds.transformLimits(handle, etx=(True, True), tx=x_range)
    cmds.transformLimits(handle, ety=(True, True), ty=y_range)
    cmds.transformLimits(handle, etz=(True, True), tz=(0, 0))
    
    # 锁定不相关通道
    for attr in ["tz", "rx", "ry", "rz", "sx", "sy", "sz", "v"]:
        cmds.setAttr(f"{handle}.{attr}", l=True, k=False)
        
    cmds.parent(handle, box)
    return box, handle
```

## Constraints (约束与禁止)
- **控制器视口位置隔离**: 2D 滑块面板必须放置在摄像机侧方或上方不遮挡角色头部的独立展示区，严禁将二维滑块直接浮动在角色五官正面；
- **回零归一化 (Zero Pose)**: 当所有控制器归零 $(0, 0, 0)$ 时，角色网格必须 100% 回复至绝对中性脸（Neutral Pose），无任何残余应变。

## Verification (验收标准)
- **边界防脱轨测试**: 用鼠标用力将控制手柄拖拽向任意对角线极端方向，手柄牢牢锁定在方框角落，底层目标体不发生溢出破面；
- **触感线性度审查**: 动画师在 0.0 到 1.0 之间匀速推动手柄，模型形变均匀展开，无停顿后突变的不适阻尼。
