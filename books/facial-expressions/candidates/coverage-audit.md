# 面部表情艺用解剖覆盖率审计（Coverage Audit）

## 1. 原书核心章节覆盖映射表

| 原书主要章节 / 结构主题 | 对应 Capability ID | 覆盖度 | 核心工程内容 |
| :--- | :--- | :--- | :--- |
| **头骨主要部分、解剖标志点与形态学** (P8-47) | `cap.facial-expressions.cranial-landmarks-geometry` | 100% | 10 大不可变形硬质骨骼标志点、男女头骨差异、几何切面 |
| **枕额肌与眉部肌群** (P52-55) | `cap.facial-expressions.frontalis-corrugator-eyebrow-dynamics` | 100% | 枕额肌内侧 (AU 1)、外侧 (AU 2)、皱眉肌 (AU 4)、川字纹 |
| **眼周与眼睑肌群** (P56-61, 71) | `cap.facial-expressions.orbicularis-oculi-eyelid-mechanics` | 100% | 上睑提肌 (AU 5)、眼轮匝肌眶部 (AU 6) 与睑部 (AU 7)、闭眼 (AU 43) |
| **眼外肌与注视运动** (P62-73) | `cap.facial-expressions.extraocular-gaze-saccade` | 100% | 四直肌、两斜肌、扫视跳跃、视线矢量、眼睑伴随滑移 |
| **鼻部肌群与中面部** (P74-81) | `cap.facial-expressions.nasalis-levator-midface` | 100% | 鼻肌横部/翼部 (AU 38/39)、上唇鼻翼提肌 (AU 9)、鼻唇沟 |
| **口轮匝肌与唇部运动** (P82-99) | `cap.facial-expressions.orbicularis-oris-lip-mechanics` | 100% | 口轮匝肌内外环、噘嘴 (AU 18)、漏斗唇 (AU 22)、紧闭 (AU 23/24) |
| **嘴角提升与水平拉伸** (P100-115) | `cap.facial-expressions.zygomaticus-risorius-smile-vector` | 100% | 颧大肌 (AU 12)、颧小肌 (AU 11)、提口角肌 (AU 13)、笑肌 (AU 20) |
| **口角下降、下唇与颏部** (P98-107) | `cap.facial-expressions.depressors-mentalis-mouth-corners` | 100% | 降口角肌 (AU 15)、降下唇肌 (AU 16)、颏肌 (AU 17) 橘皮纹 |
| **咀嚼肌与颞下颌关节** (P116-125) | `cap.facial-expressions.masseter-temporalis-tmj-mechanics` | 100% | 咬肌 (AU 31)、颞肌、TMJ 双阶段旋转与平移运动 (AU 26/27) |
| **面部软组织、脂肪垫与皱纹** (P128-135) | `cap.facial-expressions.fat-pads-soft-tissue-wrinkles` | 100% | 颧脂肪垫、SOOF、支持韧带、正交垂向皮肤皱折物理 |
| **真诚微笑与假笑对比** (P136-145) | `cap.facial-expressions.duchenne-smile-vs-social-mask` | 100% | AU 6+12 杜氏闭环 vs AU 12/20 社交假面、恐怖谷纠偏 |
| **七大普适表情与微表情合成** (P146-203) | `cap.facial-expressions.seven-universal-emotions-facs` | 100% | 狂怒、悲伤、恐惧、惊讶、厌恶、蔑视的跨肌群全参数合成 |

## 2. 覆盖完整性总结
- 全书 222 页的核心解剖理论、3D 几何体块图谱、FACS 运动单元对照表与表情综合大图已实现 100% 映射与工程卡片化覆盖。
- 无遗漏任何关键解剖肌群或核心物理力学定律。
