# 能力卡: 头部整体 Squoosh 挤压拉伸多层变形绑定 (Squoosh Multi-Layer Rig)

## Rationale (核心原理)
在风格化卡通及高表现力三维动画中，角色需要进行剧烈的头部挤压拉伸（Squash & Stretch）与受击倾斜扭曲（Squoosh），以表达冲击力、弹力与重力感。
然而，绑定工业中极其恶劣的痛点是：
**如果在雕刻具体面部表情目标体时把头部的整体拉伸混合进去，目标体数量将呈指数级爆炸，且无法与全身骨骼动画解耦；反之，若在骨骼蒙皮上直接做头部缩放，眼球和牙齿等内部刚体又会穿透脱离。**
Jason Osipa 在第 13 章首创了 **“Squoosh 多层变形绑定分层架构（Local Expression vs. Global Squoosh Layering）”**：
将面部微表情解耦在“局部网格求值层”，而将头颅整体挤压拉伸解耦在“全局变形器层”，并在变形链中通过包裹变形（Wrap）或次级晶格（Lattice）严格遵守**三维体积守恒定律（Volume Conservation）**。

## Instruction (分层架构与体积守恒工程规程)

### 1. 三层变形流架构设计 (3-Tier Evaluation Pipeline)
```
  [ 层级 1: 局部表情评估层 (Local Mesh Layer) ]
     - 包含眼、口、眉的所有加算目标体 (Blendshapes)
     - 包含眼球转向、牙齿下颌铰链
     - 在局部静止空间评估面部肌肉位移
                 |
                 v
  [ 层级 2: 全局头颅变形层 (Global Squoosh Layer) ]
     - 通过 4x4x4 变形晶格 (Lattice Deformer) 或低模包裹 (Wrap Deformer)
     - 统管头颅整体的挤压、拉伸、侧向倾斜与梯形变 (Taper)
     - 局部表情在变形器内部继续自由播放，互不干涉
                 |
                 v
  [ 层级 3: 全身骨骼蒙皮层 (Skeletal Motion Layer) ]
     - 颈部与躯干骨骼挂载头颅全局变换矩阵 (Head Joint)
```

### 2. 体积守恒数学公式 (Volume Conservation Formula)
当头部沿主拉伸轴（通常为垂直 $Y$ 轴）发生挤压或拉伸时，设纵向缩放因子为 $S_y$：
为了保持头颅总几何体积 $V \approx \frac{4}{3} \pi \cdot r_x r_y r_z = \text{常数}$：
横向两轴（$X$ 轴与 $Z$ 轴）的缩放因子 $S_x$ 和 $S_z$ 必须严格满足平方根反比：
$$S_x = S_z = \frac{1}{\sqrt{S_y}} = S_y^{-0.5}$$
- **纵向拉伸 (Stretch, $S_y = 1.4$)**:
  $$S_x = S_z = \frac{1}{\sqrt{1.4}} \approx 0.845 \quad (\text{横向收窄 } 15.5\%)$$
- **纵向压扁 (Squash, $S_y = 0.7$)**:
  $$S_x = S_z = \frac{1}{\sqrt{0.7}} \approx 1.195 \quad (\text{横向膨胀 } 19.5\%)$$

### 3. 眼球与牙齿的自适应跟随约束
- **眼球形变隔离**: 写实角色中眼球不随头部晶格拉伸，眼球中心约束在晶格对应的局部基准点（Local Pivot）上；
- **极端卡通形变**: 极端卡通角色中眼球与牙齿一同受 Squoosh 包裹变形器驱动，确保在被平底锅拍扁成薄饼时，所有五官严丝合缝依附在压扁面上。

## Actionable Example (Python/Maya 晶格体积守恒绑定构建)
```python
def setup_squoosh_volume_lattice(head_mesh: str):
    """
    为头部构建严格遵守体积守恒反比缩放的 Squoosh 控制器
    """
    import maya.cmds as cmds
    
    # 1. 创建围绕头部的晶格
    lattice_nodes = cmds.lattice(head_mesh, dv=(4, 5, 4), oc=True, n="squoosh_lattice")
    ffd = lattice_nodes[0]
    lattice_geom = lattice_nodes[1]
    
    # 2. 创建主 Squoosh 控制器
    ctrl = cmds.circle(n="squoosh_ctrl", nr=(0, 1, 0), r=1.5)[0]
    cmds.addAttr(ctrl, ln="stretch", at="double", min=-0.5, max=1.0, dv=0, k=True)
    
    # 3. 建立体积守恒表达式
    expr = """
    float $s = 1.0 + {ctrl}.stretch;
    if ($s < 0.1) $s = 0.1;
    float $comp = 1.0 / sqrt($s);
    
    {lat}.scaleY = $s;
    {lat}.scaleX = $comp;
    {lat}.scaleZ = $comp;
    """.format(ctrl=ctrl, lat=lattice_geom)
    
    cmds.expression(s=expr, n="expr_squoosh_volume")
    return ctrl
```

## Constraints (约束与禁止)
- **变形历史节点顺序律 (History Order)**: 面部 Blendshape 节点在变形历史列表中必须**严格位于 Squoosh 晶格/包裹变形器之前**（`Input Order: Blendshape -> Lattice -> SkinCluster`），否则会导致表情形变在变形空间中发生剧烈漂移错位；
- **缩放极值保护**: 纵向缩放因子 $S_y$ 不可小于 0.1，防止晶格矩阵行列式为零导致网格顶点翻转坍塌。

## Verification (验收标准)
- **多层并发测试**: 让角色在保持龇牙说话（局部表情激活）的同时，将 Squoosh 控制器推至极端压扁（Squash = -0.4），角色整体变矮变胖，且嘴角和牙齿依然能清晰清晰发音，无任何几何面穿插或断裂；
- **体积守恒测量**: 计算变形前后网格闭合多边形的总空间体积，体积波动绝对值不超过 $\pm 3\%$。
