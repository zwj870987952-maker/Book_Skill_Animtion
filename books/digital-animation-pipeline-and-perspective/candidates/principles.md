# 数字动画管线与透视速写核心原则与工程铁律

## 1. 动势线与关键姿态设计铁律（Line of Action & Pose-to-Pose Rules）
- **单一连贯动势线（Single Unbroken Line of Action）**：
  - 优秀的关键姿态（Key Pose）必须由贯穿脚踝、骨盆、脊柱直到头顶或指尖的单一“C型”或“S型”平滑弧线统治；
  - 严禁出现折断、对抗无秩序的僵硬线条碎块。
- **纯黑剪影瞬时可读性（Silhouette Test First）**：
  - 姿态必须在剥离一切肌肉细节与色彩后，纯黑轮廓仍能在 0.1 秒内清晰辨识角色的重心、动作意图与空间朝向；
  - 核心关节与道具必须从躯干主轮廓向外伸展（负空间留白）。

---

## 2. 空间透视绝对一致性原则（Spatial Perspective Consistency）
- **全场视平线锁死（Horizon Line Lock）**：
  - 同一镜头内所有角色、道具与建筑背景必须共享完全相同的视平线高度与镜头焦距；
  - 角色站在地面上，其眼睛、肩膀或膝盖与视平线的相对高低位置，严格由摄像机真实物理高度决定，严禁随意漂移。
- **圆弧与椭圆长短轴垂直律（Minor Axis Rule）**：
  - 任何放置在地面或透视面上的圆柱、车轮、盘子，其透视椭圆的短轴必须**严格垂直于该圆所在平面的主轴线**，严禁倾斜歪曲。

---

## 3. Maya 脚本工具开发健壮性铁律（Pipeline Scripting Robustness）
- **命名空间与DAG路径隔离（Namespace & Full DAG Path）**：
  - 所有 MEL/Python 工具必须通过命名空间（`namespace:node`）或完整 DAG 路径处理节点，严禁使用裸节点名导致多角色场景节点重名冲突；
- **撤销队列原子性（Undo Chunk Atomic Enforcement）**：
  - 任何自定义脚本工具的执行过程必须被完整包裹在 `undoInfo -openChunk` 与 `undoInfo -closeChunk` 之间，确保用户按 `Ctrl+Z` 能一次性完整回滚全部操作，不留下半吊子脏节点。
- **缓存优先与不可逆烘焙解耦（Alembic/USD Decoupling）**：
  - 动画环节完成后，向下游布光与渲染输出交付的必须是烘焙后的点缓存（Alembic / USD Cache），严禁带复杂重型骨骼绑定进入渲染农场。
