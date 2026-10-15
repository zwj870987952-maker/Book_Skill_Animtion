import json
from pathlib import Path

cand_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\framed-ink\candidates")
cand_dir.mkdir(parents=True, exist_ok=True)

# 1. frameworks.md
frameworks_md = """# 框架候选池 (Frameworks Candidates)

## 1. 视平线与镜头心理学坐标系 (The Horizon Line Psychological Matrix)
- **定义**: 视平线（Horizon Line / Eye Level）在画框中的垂直位置与俯仰角度直接支配观众对角色的心理投射：
  - 极低视平线 + 仰拍 (Low Angle): 赋予角色崇高、支配、恐怖或不可撼动的神圣与威权感；
  - 极高视平线 + 俯拍 (High Angle): 压缩角色垂直高度，将角色置于被困、孤独、弱小或被全知视角审判的状态；
  - 倾斜视平线 (Dutch Angle / Cant): 破坏重力平衡，传达疯狂、危机逼近与心理崩溃。
- **来源**: Marcos Mateu-Mestre, Framed Ink, Chapter 1 'Visual Narrative', pp. 12–25.

## 2. 纯黑白明度结构三层次 (The Three-Tier B&W Value Structure)
- **定义**: 优秀构图在剥离色彩后依然坚不可摧。画面由纯黑（Solid Blacks）、纯白（Solid Whites）与过渡中间灰（Mid-Tones）按主次等级构建：
  - 60% 主导色调（建立整体光影明暗氛围，如夜戏以 60% 纯黑主导）；
  - 30% 对抗次级色调（勾勒主体剪影与建筑轮廓）；
  - 10% 焦点高反差冲击点（纯白高光或纯黑剪影，锁定绝对戏剧焦点）。
- **来源**: Marcos Mateu-Mestre, Framed Ink, Chapter 2 'Light and Shadow', pp. 28–49.

## 3. 三层空间纵深架构 (The 3-Layer Spatial Depth Engine)
- **定义**:
  - 前景 (Foreground): 通常作为深暗剪影框架（Framing within a Frame），提供窥视感、纵深标尺与空间压迫；
  - 中景 (Midground): 核心叙事区域，角色动作展开与戏剧冲突发生的核心平面；
  - 远景 (Background): 环境地理与宏观世界观背景，通过大气透视（Atmospheric Perspective）与对比度衰减制造无垠进深。
- **来源**: Marcos Mateu-Mestre, Framed Ink, Chapter 3 'The Illusion of Depth', pp. 52–75.

## 4. 连续分镜视线轨迹流线 (Eye-Trace Continuity in Storyboarding)
- **定义**: 在镜头剪辑或画格切换时，观众的瞳孔焦点在屏幕上的物理坐标必须保持平滑的流动连续性（Eye-Trace）。上一格画面的视觉聚焦点与下一格画面的第一冲击点必须重合或沿引导线顺畅滑动，杜绝观众眼球在屏幕两端无序乱跳而产生视觉疲劳。
- **来源**: Marcos Mateu-Mestre, Framed Ink, Chapter 4 'Composing Shots & Flow', pp. 78–105.
"""
(cand_dir / "frameworks.md").write_text(frameworks_md, encoding="utf-8")

# 2. principles.md
principles_md = """# 原则候选池 (Principles Candidates)

1. **构图服务于情绪原则 (Composition Serves Emotion First)**:
   - 构图严禁只图“画面平衡好看”。构图的首要职责是放大剧本中的戏剧冲突、角色孤独感、恐惧或浪漫。

2. **剪影优先于细节原则 (Silhouettes Trump Detail)**:
   - 观众的大脑在 0.1 秒内仅识别黑白剪影形态。如果角色的动作与意图在纯黑剪影下模糊不清，再精细的毛发与面部纹理也毫无意义。

3. **对角线代表动能原则 (Diagonals Equals Dynamic Energy)**:
   - 水平与垂直线代表稳固、永恒与停滞；倾斜的对角线打破平衡，在画面中注入不可阻挡的下坠速度、穿透力与视觉紧迫感。

4. **环境吞噬尺度法则 (Scale Contrast & Dominance)**:
   - 将角色缩小到画面的 5%，置于占据 95% 画面面积的宏伟巨浪或巍峨城堡下，角色所承受的心理压迫感呈几何级数放大。

5. **焦距与心理空间匹配律 (Lens Perspective Psychology)**:
   - 广角拉伸距离强化速度与孤立；长焦压缩景深让追击者紧贴猎物后背制造窒息压迫。透视不仅是数学几何，更是心理距离。

6. **负空间引力法则 (Gravitational Force of Negative Space)**:
   - 巨大的空旷留白不是空无一物，而是充满情感重力的心理场域。空无一人的空旷原野本身就是一个具有压迫感的主角。
"""
(cand_dir / "principles.md").write_text(principles_md, encoding="utf-8")

# 3. cases.md
cases_md = """# 案例候选池 (Cases Candidates)

1. **阴雨巷战中逃亡者的逆光剪影构图 (Rainy Alleyway Backlit Chase)**:
   - 极低视平线；
   - 前景两侧为被深黑阴影吞噬的高耸砖墙（作为侧向压迫框架）；
   - 远景是一盏刺眼的白色路灯，逃亡者呈锐利的黑色三角形剪影飞奔冲向镜头；
   - 地面雨水泥泞的倒影形成修长的白色反射反光线，作为速度跑道将视线直引逃亡者。

2. **法庭威权受审的俯视深渊构图 (High Angle Courtroom Interrogation)**:
   - 极高俯视视平线（上帝视点）；
   - 被告孤零零站在画面右下方狭窄的微弱光斑中，缩成一团；
   - 巨大的阴影从左上方呈刀刃状斜切而下，占据画面 80% 空间，法官台如高耸绝壁压在上方，无言传达绝对的威严与无可逃遁。

3. **西部荒野牛仔终极对决双人画框 (Cinemascope 2.39:1 Gunslinger Standoff)**:
   - 2.39:1 超宽画幅；
   - 前景左侧为拔枪牛仔的腰带与枪套特写（极近景暗部剪影框架）；
   - 远景右侧中景为伫立在漫天尘土中的对手（全身中景）；
   - 画面中部留出巨大的空旷地平线负空间，冷酷视线在画格两端形成极度紧绷的对角线张力。
"""
(cand_dir / "cases.md").write_text(cases_md, encoding="utf-8")

# 4. counter-examples.md
counter_examples_md = """# 反例与常见病灶候选池 (Counter-Examples & Anti-Patterns)

1. **灰调泥泞无焦点病 (Muddy Mid-Tone Trap)**:
   - 病灶: 画面充斥着 50% 均等灰调，既没有纯正扎实的深黑阴影，也没有纯净剔透的白色高光，视觉呈现一团灰蒙蒙的视觉灰尘，无法聚焦。
   - 治愈: 确立黑白两极基准，用大面积纯黑块面锚定结构，将纯白留给核心叙事点。

2. **视线跳跃眼球疲劳病 (Eye-Fatigue Jumping Bug)**:
   - 病灶: 连续画格之间，前一格焦点在极左下角，后一格突变到极右上角，观者视网膜在画格切换时剧烈颠簸寻找焦点。
   - 治愈: 构建视线轨迹连续性（Eye-Trace），让上一格的视线引流线自然滑向下一格的第一聚焦点。

3. **平庸中心对称死板构图 (Boring Bullseye Center Composition)**:
   - 病灶: 角色永远呆板地安置在画格正中央，视平线永远卡在画面二分之一处，画面僵死毫无张力。
   - 治愈: 打破对称！推向三分线黄金分割点，施加对角线倾斜与深邃前后空间三层遮挡。
"""
(cand_dir / "counter-examples.md").write_text(counter_examples_md, encoding="utf-8")

# 5. glossary.md
glossary_md = """# 术语候选池 (Glossary Candidates)

1. **Eye Level / Horizon Line (视平线)**: 摄像机镜头的垂直高度基准，决定观众观察场景的心理视角（仰视/俯视/平视）。
2. **Chiaroscuro (明暗对照法)**: 通过极度强烈的纯黑深影与锐利强光对比雕刻立体形态与戏剧悬念的经典光影技法。
3. **Silhouette (剪影)**: 角色或物体在强背光下呈现的无内部细节的二维几何纯黑轮廓。
4. **Leading Lines (视线引导线)**: 构图中利用道路、阴影边缘、墙壁折角或角色视线构建的引导观者瞳孔移动的连续轨迹。
5. **Foreground / Midground / Background (前景/中景/远景)**: 构建画面三维纵深感的三大核心空间图层。
6. **Framing within a Frame (画中画框架构图)**: 利用前景门框、窗户、桥洞或阴影剪影将核心叙事主体框入其中的构图手法。
7. **Aspect Ratio (画幅宽高比)**: 影像画框的宽度与高度比例（如 4:3、16:9、2.39:1 Cinemascope）。
8. **Eye-Trace (视线轨迹连续性)**: 连续分镜头切换时观众视觉注意力焦点的物理空间运动流线。
9. **Negative Space (负空间 / 留白)**: 主体之外留空的无复杂细节区域，承载着强大的心理引力与构图平衡。
10. **Dutch Angle (荷兰斜角镜头)**: 摄影机地平线发生明显倾斜的构图角度，用于表达不安、疯狂或失衡。
"""
(cand_dir / "glossary.md").write_text(glossary_md, encoding="utf-8")

print("Created all 5 candidate files for Framed Ink successfully!")
