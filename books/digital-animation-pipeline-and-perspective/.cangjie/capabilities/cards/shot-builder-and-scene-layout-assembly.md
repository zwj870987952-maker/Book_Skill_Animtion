# shot-builder-and-scene-layout-assembly

镜头搭建工程与场景空间布局集成（Pro Shot Builder、摄像机视差与资产对齐）。

## 核心法则与工程机制

### 1. 镜头搭建工程体系（Pro Shot Builder Architecture）
在三维数字化生产中，一个镜头的建立绝非随意把模型扔进场景，必须遵循严格的工业流水线装配逻辑：
1. **资产版本化引用（Referencing & Namespace Allocation）**：
   - 所有角色、道具与场景环境必须以只读引用（Reference）模式载入，严禁直接导入（Import）；
   - 强制分配唯一命名空间（如 `CHAR_Hero01:`、`BG_CyberStreet:`），杜绝节点重名冲突；
2. **摄影机参数锁死（Camera Metric Lock）**：
   - 镜头搭建第一步导入已通过导演审批的 Layout 摄影机；
   - 焦距（Focal Length）、画幅宽高比（Film Back Aspect Ratio 2.39:1 / 16:9）、裁切平面（Near/Far Clip）严格加锁禁止改动；
3. **场景深度分层与视差校准（Parallax Depth Staging）**：
   - 明确拆分前景层（Foreground）、中景行动区（Midground Action Core）与背景远景（Background / Matte Painting）；
   - 检查摄影机推拉横移时，三层之间是否呈现严密的物理速度差视差运动（Parallax）。

---

## 工业实操排障与反模式

| 常见致命失误 | 缺陷诊断 | 工业标准重构法 |
| :--- | :--- | :--- |
| **直接 Import 资产导致文件爆炸** | 场景内资产直接导入，无法同步上游模型修形与绑定修复，文件臃肿至数个G | 全面切换为 Reference 引用机制，任何上游资产修复一键全局刷新 |
| **摄像机近裁切面穿模破面** | 摄影机过近特写时，物体前端直接被 Near Clip Plane 裁切穿透开洞 | 根据场景尺度微调 Near Clip Plane 至 0.1cm - 1.0cm，确保微距特写不破面 |
| **角色脚步地面穿透或滑步** | 场景地表高低起伏，动画师在平地上制作动画后导致角色脚深陷地下 | 镜头装配阶段优先对齐实际碰撞地表网格，严禁在脱离地表的空旷空间盲调脚步 |
