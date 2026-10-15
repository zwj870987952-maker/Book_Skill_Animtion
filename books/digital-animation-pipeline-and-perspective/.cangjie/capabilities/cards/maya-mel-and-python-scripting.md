# maya-mel-and-python-scripting

Maya动画师自动化脚本编程与管线工具开发（MEL/mayapy批量处理、动画曲线操作、Undo原子块与UI搭建）。

## 核心法则与工程机制

### 1. Maya 自动化脚本工业架构规范
在工业三维管线中，动画师必须具备通过 MEL / Python 脚本解放双手、批量解决机械操作的能力：
1. **命名空间安全原则（Namespace Safety）**：
   - 严禁硬编码裸节点名（如 `select -r "hand_CTRL"`），必须动态解析当前角色的命名空间（`namespace:hand_CTRL`）或抓取完整 DAG 路径；
2. **撤销队列原子性（Undo Chunk Atomic Enforcement）**：
   - 任何批处理脚本必须被包含在 Undo Chunk 中，确保按一次 `Ctrl+Z` 能够完整回滚全部操作，不产生残留脏节点：
   ```python
   import maya.cmds as cmds
   cmds.undoInfo(openChunk=True)
   try:
       # 批量操作逻辑：遍历动画控制器、镜像关键帧、对齐约束等
       pass
   finally:
       cmds.undoInfo(closeChunk=True)
   ```
3. **动画曲线批处理（Anim Curve Manipulation）**：
   - 掌握通过 `keyframe`、`copyKey`、`pasteKey` 与 `setInfinity` 脚本化批量修剪周期循环曲线、清理冗余关键帧（Euler Filter）与批量调整切线类型（Spline/Linear/Clamped）。

---

## 工业实操排障与反模式

| 常见致命失误 | 缺陷诊断 | 工业标准重构法 |
| :--- | :--- | :--- |
| **未加 Undo 导致回滚灾难** | 脚本生成了 200 个约束节点后报错，按 Ctrl+Z 无法回滚，场景彻底损坏 | 在脚本首尾必须使用 `try...finally` 块严格包裹 `undoInfo -openChunk` |
| **选择集硬编码失效** | 脚本写死 `character_rig:spine_ctrl`，场景导入第二个角色时脚本全部崩溃 | 自动读取当前鼠标选中的任意控制器并自动剥离其前缀命名空间作为作用域 |
| **主线程阻塞假死** | 批量处理 1000 帧动画时在主线程循环刷新视口，导致 Maya 假死崩溃 | 在大循环中调用 `cmds.refresh(suspend=True)` 暂停视口重绘，执行完毕后恢复 |
