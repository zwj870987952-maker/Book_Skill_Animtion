# 《数字动画制作管线与透视速写工程手册》（digital-animation-pipeline-and-perspective）项目概述

## 一、文献源与大师谱系
本技能包系统性萃取并熔铸了世界数字动画制作工业管线、绘画透视空间几何学、艺用人体运动学与经典动画史论的 11 部权威经典：
1. **托尼·怀特（Tony White）** ——《从铅笔到像素：数字动画经典教程》（*How to Make Animated Films: From Pencil to Pixels*）
   - 传统胶片逐帧手绘向无纸数字动画与 2D/3D 混合制作的跨越；
   - 动画生产管线全生命周期：概念设计 $\rightarrow$ 分镜 Layout $\rightarrow$ 原画清线 $\rightarrow$ 数字上色 $\rightarrow$ 合成特效；
2. **Autodesk Maya 工业管线专家群** ——《Maya动画师MEL脚本编程全攻略》
   - 自动化动画工具开发、UI 界面搭建、属性连接、曲线插值批量控制、资产导出与管线集成；
3. **透视几何学大师经典** ——《透视学 + 绘画透视设计透视》
   - 视平线（Horizon Line）、心点（Center of Vision）、一点/两点/三点透视、斜面透视、圆弧椭圆透视与极坐标超广角鱼眼透视网格；
4. **艺用人体结构与人体运动学群** ——《[动画师必备]艺用人体结构运动学》、《1584个姿势》、《人体动态6000例》、《Pose to Pose 之后的生活》、《pose设计基础篇》
   - 脊柱三轴曲率、骨盆与胸腔相对反向扭转、动力学重心投影面；
   - Pose-to-Pose 关键姿态工程设计：动势线（Line of Action）、极限张力与黄金剪影瞬时可读性；
5. **数字资产与镜头工程** ——《Pro Shot Builder》
   - 摄像机视差匹配、资产命名空间（Namespace）、层级搭建与布景集成；
6. **世界动画史论与知识工程** ——《世界动画史》、《如何阅读一本书》
   - 世界动画流派演变（古典全动画 vs 日本有限动画 vs 欧洲作者定格 vs 三维CG革命）；
   - 艾德勒四层次阅读法（基础/检视/分析/主题阅读）在视觉工程知识提取与 Agent 建模中的落地。

---

## 二、架构决策：Single 模式与 12 大能力卡

本技能包采用统一的 `single` 架构，包含 12 项高内聚能力卡：
1. `pencil-to-pixel-digital-pipeline` (从传统手绘逐帧到无纸数字动画全流程)
2. `maya-mel-and-python-scripting` (Maya 动画师自动化脚本编程与管线工具开发)
3. `perspective-geometry-and-focal-grids` (透视学几何法则与空间网格系统)
4. `human-locomotion-kinesiology` (艺用人体结构运动学与骨骼关节力矩)
5. `dynamic-posing-and-pose-to-pose-staging` (关键姿态设计与 Pose-to-Pose 阶段化工作流)
6. `pose-library-and-gesture-atlas` (1584/6000例人体极限姿态速写索引图谱)
7. `digital-cleanup-inking-and-color-styling` (数字动画修型清稿与色彩上色工艺)
8. `shot-builder-and-scene-layout-assembly` (镜头搭建工程与场景空间布局集成)
9. `world-animation-history-and-stylistic-paradigms` (世界动画史流派演化与美学范式)
10. `syntopic-reading-and-knowledge-engineering` (动画知识工程与主题阅读心智模型)
11. `rigging-interfacing-and-animation-caching` (三维角色绑定接口与动画缓存导出管线)
12. `pipeline-troubleshooting-and-asset-audit` (数字动画管线排障与资产审计流水线)
