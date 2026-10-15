# 能力卡: 口型正交解耦与视素矩阵 (Orthogonal Viseme Matrix)

## Rationale (核心原理)
在三维面部动画中，按拼写字母逐个雕刻口型（如对 A, E, I, O, U, W, F, M 单独做混合形）会导致连续发音时形状互相干涉，引发俗称的“假面具抽搐”与“恐怖谷口型冲突”。
Jason Osipa 提出将口型空间在笛卡尔坐标系中正交解耦为两个最基础的物理自由度：
1. **开合主轴 (Open / Closed Axis, $Y$ 轴)**: 由下颌骨绕下颌关节铰链旋转驱动下巴下降与上升；
2. **宽窄主轴 (Wide / Narrow Axis, $X$ 轴)**: 由降口角肌、笑肌（向外拉宽）与口轮匝肌（向前撅起聚拢）驱动。
任意连续发音均可由二维矢量 $(X_{\text{wide}}, Y_{\text{open}})$ 在该平面内的连续轨迹表达，再辅以硬性辅音物理接触形状（闭唇 MBP、唇齿接触 FV）以及舌尖状态，从而将数十种混乱的发音映射压缩为高度优雅且无冲突的参数空间。

## Instruction (工程规范与参数矩阵)

### 1. 基础正交四极坐标定义
在二维滑块空间中定义归一化坐标 $X \in [-1.0, 1.0], Y \in [0.0, 1.0]$：
- $(0.0, 0.0)$: **Neutral (中性静止)**，双唇微闭放松，下巴处于静息位；
- $(0.0, 1.0)$: **Open (纯开度)**，下巴下落，嘴唇不横向拉宽也不纵向撅起；
- $(-1.0, 0.0)$: **Wide (纯宽嘴)**，嘴角横向向外、向后拉伸，露出上下门牙，下巴不下降；
- $(+1.0, 0.0)$: **Narrow (纯窄嘴/聚拢)**，嘴唇向前突起收缩成小圆孔，嘴角向中心靠拢；
- $(-1.0, 1.0)$: **Wide + Open (大张宽口)**，如下巴大幅下沉的大笑或“AH”音；
- $(+1.0, 1.0)$: **Narrow + Open (大张圆口)**，如下巴下沉的大喊“OH”或惊讶“WHOA”。

### 2. 核心发音视素矩阵映射表
| 视素代码 | 包含发音音标 | 正交坐标 $(X, Y)$ | 辅音接触/附加通道 | 生理视觉特征 |
| :--- | :--- | :--- | :--- | :--- |
| **MBP** | /m/, /b/, /p/ | $(0.0, 0.0)$ | `Mouth_Closed = 1.0` (覆盖开度) | 双唇向内扣合挤压，下颌微抬 |
| **FV** | /f/, /v/ | $(-0.3, 0.2)$ | `LowerLip_Bite = 1.0` | 下唇上卷抵住上门牙切缘，上唇微抬 |
| **EE** | /i:/, /I/, /eI/ | $(-0.8 \sim -1.0, 0.1 \sim 0.2)$ | 上下门牙接近咬合对齐 | 嘴角横向极大拉伸，露齿笑形 |
| **AH** | /A:/, /\ae/, /aI/ | $(-0.4 \sim -0.6, 0.7 \sim 0.9)$ | 舌平铺于口底 | 下巴大幅下垂，咽喉部通畅 |
| **OH** | /\textscripta/, /\textopeno:/ | $(+0.2 \sim +0.4, 0.6 \sim 0.8)$ | 唇周肌肉微内扣 | 纵向椭圆形开度，牙齿微隐 |
| **OO/W** | /u:/, /w/, /\textupsilon/ | $(+0.8 \sim +1.0, 0.2 \sim 0.3)$ | 双唇向前突出喇叭口 | 极小圆形孔径，脸颊横向凹陷 |
| **L/TH** | /l/, /\theta/, /\eth/ | $(-0.2, 0.3 \sim 0.4)$ | `Tongue_Up = 1.0` | 舌尖伸出上下齿列之间或抵住上牙龈 |

## Actionable Example (Python/Maya 正交映射评估伪代码)
```python
def evaluate_viseme_pose(open_val: float, wide_narrow_val: float, is_mbp: bool, is_fv: bool):
    """
    根据正交坐标与接触掩码计算最终口部目标体权重
    open_val: 0.0 ~ 1.0
    wide_narrow_val: -1.0 (Wide) ~ +1.0 (Narrow)
    """
    weights = {}
    
    if is_mbp:
        # 硬性闭唇覆盖一切开度
        weights["Mouth_Open"] = 0.0
        weights["Mouth_MBP_Press"] = 1.0
        weights["Mouth_Wide"] = max(0.0, -wide_narrow_val * 0.3)
        weights["Mouth_Narrow"] = max(0.0, wide_narrow_val * 0.3)
        return weights

    # 基础正交分解
    weights["Mouth_Open"] = max(0.0, min(1.0, open_val))
    if wide_narrow_val < 0.0:
        weights["Mouth_Wide"] = -wide_narrow_val
        weights["Mouth_Narrow"] = 0.0
    else:
        weights["Mouth_Wide"] = 0.0
        weights["Mouth_Narrow"] = wide_narrow_val
        
    if is_fv:
        weights["Mouth_FV_Bite"] = 1.0
        # FV 时开度自动钳制至舒适咬合距离
        weights["Mouth_Open"] = min(weights["Mouth_Open"], 0.25)
        
    return weights
```

## Constraints (约束与禁止)
- **绝对禁止全脸字母形**: 严禁雕刻名为 `Shape_Letter_A`、`Shape_Letter_O` 的全量形变体；
- **开合轴独立性**: `Mouth_Open` 目标体严禁包含横向拉嘴角顶点位移；
- **宽窄轴互斥性**: `Mouth_Wide` 与 `Mouth_Narrow` 在底层滑块映射上必须单向互斥，二者权重乘积在任意瞬时帧必须为 0。

## Verification (验收标准)
- **插值平滑性**: 当控制器从 $(-1.0, 1.0)$ 平滑滑移至 $(+1.0, 0.0)$ 时，网格顶点位移轨迹呈平滑空间圆弧，无折角畸变或反向穿透；
- **音素覆盖率**: 使用该正交矩阵驱动标准对白时，能够自然还原包括双元音连读（如 /aU/, /OI/）在内的任意口型平滑形变。
