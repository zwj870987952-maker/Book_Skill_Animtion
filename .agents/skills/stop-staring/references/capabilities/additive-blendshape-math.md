# 能力卡: 无冲突加算目标体与权重渐变算法 (Additive Blendshapes & Tapering)

## Rationale (核心原理)
在面部表情目标体（Blendshapes）系统中，如果每个形状都记录整个面部的绝对位置（Absolute Mesh Replacement），当多个表情（如“左挑眉”与“右挑眉”，或“微笑”与“张嘴”）同时开启时，目标体之间会发生全量覆盖或双倍位移冲突，导致顶点飞出、嘴唇撕裂。
Osipa 创立的加算目标体体系（Additive Shapes）遵循差分矢量叠加原理：
$$\vec{V}_{\text{final}} = \vec{V}_{\text{base}} + \sum_{i=1}^{N} w_i \cdot \Delta \vec{V}_i$$
其中 $\Delta \vec{V}_i = \vec{V}_{\text{target}_i} - \vec{V}_{\text{base}}$。同时，为了避免手工左右拆分时在中线处产生硬接缝或不对称撕裂，Osipa 发明了著名的余弦平滑衰减渐变算法（`ss2_blend_taper`），实现无缝的半边脸目标体分离。

## Instruction (差分加算与中线渐变规程)

### 1. 目标体纯净差分约束
- 雕刻特定目标体（如 `Mouth_Smile`）时，未受该表情影响的区域（如眼部、额头、耳朵）其顶点位移量 $\Delta \vec{V}$ 必须严格归零；
- 避免全脸连带抖动，保证每个目标体的差分稀疏性。

### 2. 空间余弦平滑渐变算法 (`ss2_blend_taper`)
为了将一个居中对称雕刻的形状拆分为“左半边（Left）”与“右半边（Right）”，在沿面部对称轴（通常为世界坐标 $X$ 轴，$X=0$ 为中线）应用平滑余弦衰减权重：
设渐变缓冲区半宽为 $T$（通常设为鼻梁到内眼角的距离，例如 $T = 0.5 \sim 1.0 \text{ cm}$）：
对于任意顶点坐标 $x$：
- 当 $x > T$ 时（纯左侧）：权重 $W_{\text{left}}(x) = 1.0$；
- 当 $x < -T$ 时（纯右侧）：权重 $W_{\text{left}}(x) = 0.0$；
- 当 $-T \le x \le T$ 时（中线过渡区）：
  $$W_{\text{left}}(x) = 0.5 \cdot \left[1.0 + \sin\left(\frac{\pi \cdot x}{2T}\right)\right]$$
对应右侧权重严格满足互补守恒律：
$$W_{\text{right}}(x) = 1.0 - W_{\text{left}}(x)$$
这保证了在任何位置：
$$W_{\text{left}}(x) + W_{\text{right}}(x) \equiv 1.0$$
当左右两边同时激活为 1.0 时，能够 100% 完美复原原始中央对称形状，在中线绝无折角或凹槽。

## Actionable Example (Python 实现 Osipa 余弦渐变拆分)
```python
import math

def calculate_taper_weight(x_coord: float, taper_width: float) -> float:
    """
    根据顶点 X 坐标与过渡半宽计算左侧权重 (0.0 ~ 1.0)
    """
    if taper_width <= 0:
        return 1.0 if x_coord >= 0 else 0.0
        
    if x_coord >= taper_width:
        return 1.0
    elif x_coord <= -taper_width:
        return 0.0
    else:
        # 正弦/余弦平滑过渡
        norm_val = x_coord / taper_width # -1.0 ~ 1.0
        return 0.5 * (1.0 + math.sin(norm_val * (math.pi / 2.0)))

def split_blendshape_left_right(base_mesh_verts, target_verts, taper_width=0.8):
    """
    将对称目标体顶点差分矢量拆分为纯净的 Left 与 Right 目标体
    """
    num_verts = len(base_mesh_verts)
    left_target = []
    right_target = []
    
    for i in range(num_verts):
        bx, by, bz = base_mesh_verts[i]
        tx, ty, tz = target_verts[i]
        dx, dy, dz = tx - bx, ty - by, tz - bz
        
        w_left = calculate_taper_weight(bx, taper_width)
        w_right = 1.0 - w_left
        
        # 加算生成分离目标体
        left_target.append((bx + dx * w_left, by + dy * w_left, bz + dz * w_left))
        right_target.append((bx + dx * w_right, by + dy * w_right, bz + dz * w_right))
        
    return left_target, right_target
```

## Constraints (约束与禁止)
- **禁止线性割裂 (Linear Step Split)**: 严禁以 $X=0$ 为硬分界线简单按面拆分（会导致中线法线断裂产生黑线）；
- **拓扑点序恒定**: 生成的所有目标体必须与基础模型（Base Mesh）具备完全一致的顶点数量与点序号（Vertex ID Order）；
- **权重归一保证**: 拆分出的左形与右形在 $w_{\text{left}}=1, w_{\text{right}}=1$ 叠加时，中线上任意顶点的绝对位移误差必须小于 $10^{-5}$。

## Verification (验收标准)
- **中线完美重合测试**: 在 Maya/Blender 中同时将 `Shape_L` 与 `Shape_R` 设为 1.0，比对生成的几何体与原始对称雕刻目标体，顶点法线与空间坐标 100% 重合；
- **单侧独立测试**: 仅激活 `Shape_L = 1.0`，右半张脸保持绝对静止（位移为 0），中线过渡区柔和顺滑无突变台阶。
