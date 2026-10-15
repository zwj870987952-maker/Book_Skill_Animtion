# 《Stop Staring: Facial Modeling and Animation Done Right》章节覆盖度审计 (Coverage Audit)

| 章节索引 | 原书章节名称 | 核心主题 | 映射能力卡 (Capability ID) | 覆盖状态 |
| :--- | :--- | :--- | :--- | :--- |
| **Part I: Ch 1** | Learning the Basics of Lip Sync | 视素基础、发音循环、开合与宽窄正交轴 | `cap.stop-staring.viseme-ortho-matrix` | 完全覆盖 (100%) |
| **Part I: Ch 2** | What the Eyes and Brows Tell Us | 眉毛两大运动、上下眼睑情绪表达、视线偏差 | `cap.stop-staring.brow-emotion-mechanics`<br>`cap.stop-staring.eyelid-expression-tension` | 完全覆盖 (100%) |
| **Part I: Ch 3** | Facial Landmarking | 面部地标定位、鼻唇沟折痕、头部姿态旋转 | `cap.stop-staring.facial-edge-flow-topology`<br>`cap.stop-staring.lip-sync-pipeline` | 完全覆盖 (100%) |
| **Part II: Ch 4** | Visimes and Lip Sync Technique | 视素进阶、四步口型制作流水线、视素超前量 | `cap.stop-staring.lip-sync-pipeline`<br>`cap.stop-staring.viseme-ortho-matrix` | 完全覆盖 (100%) |
| **Part II: Ch 5** | Constructing a Mouth and Nose | 嘴鼻拓扑布线、口轮匝肌边流、牙齿舌头构造 | `cap.stop-staring.facial-edge-flow-topology`<br>`cap.stop-staring.mouth-cavity-teeth-tongue` | 完全覆盖 (100%) |
| **Part II: Ch 6** | Mouth Keys | 加算混合形、`ss2_blend_taper` 余弦渐变脚本 | `cap.stop-staring.additive-blendshape-math` | 完全覆盖 (100%) |
| **Part III: Ch 7** | Building Emotion: The Basics of the Eyes | 上脸情绪系统、Box Head 极简练习、眨眼与扫视 | `cap.stop-staring.blink-dynamics-thought-break`<br>`cap.stop-staring.eye-rig-lid-follow-saccades` | 完全覆盖 (100%) |
| **Part III: Ch 8** | Constructing Eyes and Brows | 眼球眼眶拓扑、眼睑内翻厚度、额头布线 | `cap.stop-staring.facial-edge-flow-topology`<br>`cap.stop-staring.eye-rig-lid-follow-saccades` | 完全覆盖 (100%) |
| **Part III: Ch 9** | Eye and Brow Keys | 写实与风格化眉毛目标体、额头折痕贴图联动 | `cap.stop-staring.brow-emotion-mechanics` | 完全覆盖 (100%) |
| **Part IV: Ch 10** | Connecting the Features | 耳朵建模、面部各子模块缝合与五星极点规避 | `cap.stop-staring.facial-edge-flow-topology` | 完全覆盖 (100%) |
| **Part IV: Ch 11** | Skeletal Setup, Weighting, and Rigging | 头部骨骼蒙皮、眼球跟随联动、拉链唇粘连绑定 | `cap.stop-staring.eye-rig-lid-follow-saccades`<br>`cap.stop-staring.zipper-lips-sticky-rig` | 完全覆盖 (100%) |
| **Part IV: Ch 12** | Interfaces for Your Faces | 二维滑块控制器界面设计、驱动键约束管理 | `cap.stop-staring.slider-interface-driver-rig` | 完全覆盖 (100%) |
| **Part IV: Ch 13** | Squash and Stretch and Squoosh | 全局 Squoosh 头部挤压拉伸与晶格/包裹分层绑定 | `cap.stop-staring.squoosh-head-squash-stretch` | 完全覆盖 (100%) |
| **Part IV: Ch 14** | A Shot in Production | 生产实战全流程整合、台词分层与情绪表演 | `cap.stop-staring.lip-sync-pipeline`<br>`cap.stop-staring.blink-dynamics-thought-break` | 完全覆盖 (100%) |

**审计结论**: 全书 14 个核心章节均已实现 100% 结构化工程映射，无技术盲区或遗漏。
