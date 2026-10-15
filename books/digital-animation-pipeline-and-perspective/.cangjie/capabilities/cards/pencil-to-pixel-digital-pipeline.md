# pencil-to-pixel-digital-pipeline

从传统手绘逐帧到无纸数字动画与2D/3D混合制作全流程（托尼·怀特管线模型、生产全生命周期与阶段交接契约）。

## 核心法则与工程机制

### 1. 托尼·怀特无纸数字工业生产全流程（Pencil to Pixels Pipeline）
传统胶片逐帧动画向现代数字化无纸动画（Paperless Animation）的跨越并非单纯更换工具，而是工业生产协同逻辑的彻底重构：
1. **前期概念与视觉开发（Pre-Production）**：
   - 剧本锁定 $ightarrow$ 角色/场景设计造型表（Model Sheets） $ightarrow$ 动态故事板（Story Reel / Animatic，配齐临时对白与音效）；
2. **场景布局与摄影机设置（Layout & Camera Setup）**：
   - 确立视平线与 3D 摄像机参数，输出背景设计稿（BG Layout）与角色动势指引（Pose Layout）；
3. **关键原画与动作分解（Key Animation & Breakdowns）**：
   - 资深动画师完成关键极致姿态（Keys / Extremes）与动势中继分解帧（Breakdowns）；
4. **数字清线与矢量修型（Digital Cleanup & Vector Inking）**：
   - 助理工段将草稿转化为严密闭合的工业级整洁线条；
5. **数字上色与色盘管理（Digital Painting & Ink and Paint）**：
   - 依据统一色盘（Palette）执行无缝油漆桶平涂与明暗阴影层（Shadow Pass）分离；
6. **后期合成与最终特效（Compositing & Multiplane FX）**：
   - 多层视差摄像机运动合成、景深模糊、粒子光效与终极 4K 色彩校准。

---

## 工业实操排障与反模式

| 常见致命失误 | 缺陷诊断 | 工业标准重构法 |
| :--- | :--- | :--- |
| **未锁动态台本直接开始原画** | 剪辑台本镜头时长尚未敲定就制作原画，导致海量原画作废 | 严格执行 Animatic 签字锁定制度，镜头帧数未敲定严禁开启动画制作 |
| **色盘无版本控制** | 不同原画师使用各自拾取的颜色，导致同一角色在不同镜头中肤色跳跃 | 建立全局只读的数字调色板资产库（Digital Swatch Asset），通过脚本强制锁定 |
| **清线断线导致漏色** | 矢量清线存在 0.1 毫米微小缝隙，数字上色油漆桶直接泛滥全屏 | 开启数字绘图软件的“自动闭合缝隙（Close Gap）”算法，并由清线组执行闭合审计 |
