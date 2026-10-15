# 《Stop Staring: Facial Modeling and Animation Done Right》工程边界与审视清单 (Needs Review)

## 1. 软件环境与工具演进映射
- **原书背景**: 原书案例基于 Autodesk Maya 经典版本及 MEL 脚本（如 `ss2_blend_taper.mel`）。
- **现代审视与适配**:
  - 原书核心在于**数学逻辑与拓扑哲学**而非绑定工具绑定；
  - 渐变衰减脚本的数学本质是余弦空间渐变（Cosine Weight Falloff），在现代 Python/PyMEL、OpenMaya 或 Blender 几何节点中均可 1:1 无损迁移；
  - 2D 滑块控制器理念在当代已演变为现代游戏引擎标准（Unreal Engine MetaHuman Control Rig, Apple ARKit 52 Face Tracking 标准映射）。本技能包提炼其底层控制论，兼容任意现代 DCC。

## 2. FACS (面部动作编码系统) 与 Osipa 体系的关系界定
- **审视要点**: FACS 是纯粹基于解剖学生理肌肉单元（Action Units, AUs）的医学/心理学分类系统（包含 AU1, AU2, AU4...）。
- **工程界定**: FACS 适合面部捕捉数据采集，但直接用于手工关键帧动画极其痛苦（容易出现维度灾难与滑块冲突）。Osipa 体系是**为动画师直觉与高效操作而生的正交解耦体系**。能力卡将清晰指出两者异同，帮助开发者在动捕重定向与手工精修之间建立桥梁。

## 3. 极速发音与吞音连读的阈值处理
- **审视要点**: 在超高速对白（如说唱、急促辩论，发音周期短于 4 帧）中，视素开合与宽窄极值可能来不及完全拉满。
- **工程解**: 引入“振幅阻尼补偿公式”，当音节持续时间小于 3 帧时，开合度自动衰减至额定值的 40%-60%，确保视觉连贯性且不产生机械抽搐。
