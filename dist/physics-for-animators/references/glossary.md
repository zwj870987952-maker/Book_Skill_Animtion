# 核心术语词典 (Glossary) — 《动画师物理学》

| 术语 (Term) | 物理定义与动画用法 | 和常见直觉的差异 | 关联能力卡 (Capability ID) |
|---|---|---|---|
| **The Odd Rule (奇数定律)** | 物体在恒定加速度下，连续等长离散时间段内的位移增量比必为 $1:3:5:7:9\dots$ | 常人以为加速是每步多走固定距离，实际上位移增量是等差奇数数列 | `odd-rule-acceleration` |
| **Fourth Down at Half Time (四分之一半时定理)** | 自由落体运动中，当下落时间进行到总时间的一半时，物体仅下落了总高度的四分之一（$25\%$） | 初学者常误以为时间过半高度过半（$50\%$），导致下落像带降落伞般漂浮失重 | `gravity-projectile-timing` |
| **Line of Gravity & Base of Support (重力垂线与支撑面)** | 质心引向地面的铅垂线（LOG）必须穿过双足（或多接触点）构成的凸多边形支撑面（BOS），角色方可平衡 | 站立稳定与否不取决于肢体对称，仅取决于 LOG 是否在 BOS 内；迈步是主动失衡 | `center-of-gravity-balance` |
| **Terminal Velocity (终端速度)** | 下落物体重力与向上的空气阻力相平衡时的恒定沉降速度极限（人类约 54m/s） | 现实中下落不是无限持续加速，超过 3 秒的高空跳伞必须进入匀速沉降 | `friction-drag-resistance` |
| **Biomechanical Lever Classes (生物杠杆分类)** | 人体骨骼构成的三类杠杆：第一类平衡支点、第二类踝关节省力、第三类肘/膝速度杠杆 | 大多数肢体关节属于第三类“速度杠杆”，肌肉微小收缩放大为四肢末端超高速爆发 | `torque-lever-joints` |
| **Rotational Inertia (转动惯量)** | 刚体绕轴旋转的惯性量（$I = mr^2$），角动量守恒下与自转角速度成反比 | 质量离旋转轴越近自转越快；空中抱膝团身使旋转角速度瞬间飙升 4–6 倍 | `torque-lever-joints` |
| **Impulse-Momentum Theorem (冲量-动量定理)** | 打击平均受力与碰撞接触时长成反比（$F\Delta t = \Delta p$） | 打击威力不仅取决于拳头速度，更取决于受击点接触压缩耗时；硬撞 1 帧，软撞 6 帧 | `action-reaction-impact` |
| **Push Time (起跳推地时间)** | 角色从深蹲预备姿态蹬伸双腿至脚尖脱离地面的时间（通常 4–6 帧） | 跳跃不仅包含空中抛物线，推地做功产生的反作用力才是决定跳跃高度的源头 | `character-jump-mechanics` |
| **Stop Time (落地制动缓冲时间)** | 角色双足接触地面至膝盖深屈吸收下落动能至静止的耗时（通常 3–8 帧） | 落地并非单帧静止，必须通过受压行程延长碰撞时间以避免骨骼震颤假象 | `character-jump-mechanics` |
| **Inverted Pendulum Model (行走倒单摆模型)** | 双足行走中身体以单侧支撑腿为轴翻滚，动能与重力势能交替转换的动力学模型 | 行走重心并非匀速平移，过路点势能最高速度最慢，触地点动能最高速度最快 | `character-walk-energy` |
| **Secondary Drag & Pendulum Law (次级阻力与单摆定律)** | 次级结构摆动周期与悬挂长度平方根成正比（$T = 2\pi\sqrt{L/g}$），风阻与截面积成正比 | 次级结构严禁一刀切延迟；长发/长斗篷延迟 6–8 帧，短发/小配饰延迟 1–2 帧 | `drag-follow-through-physics` |
| **Vortex Torus (环形涡流蘑菇云)** | 热浮力驱动高温气体极速上升，顶部卷吸周围冷空气向外翻卷形成的闭合环形涡旋 | 爆炸蘑菇云不是简单的二维贴图放大，而是自内向外翻卷的流体力学闭合涡环 | `fire-explosion-fracture` |
| **Radial & Concentric Cracks (辐射与同心环裂纹)** | 脆性刚体受冲击碎裂时，先产生从中心向外的直线辐射裂纹，随后产生相连的同心圆裂纹 | 碎裂纹理绝非杂乱无章，严格遵循张力释放的几何拓扑级联 | `fire-explosion-fracture` |
| **Inverse-Square Law & Penumbra (平方反比与半影几何)** | 照度按距离平方反比衰减（$E \propto 1/d^2$）；半影宽度与光源发光面直径及遮挡距离成正比 | 真实光线必须设为 Quadratic 衰减；近地面脚底阴影极硬，远端头部阴影极软 | `light-shadow-optics` |
