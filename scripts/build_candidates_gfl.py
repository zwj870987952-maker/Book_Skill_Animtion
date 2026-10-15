import json
from pathlib import Path

cand_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\grammar-of-film-language\candidates")
cand_dir.mkdir(parents=True, exist_ok=True)

# 1. frameworks.md
frameworks_md = """# 框架候选池 (Frameworks Candidates)

## 1. 180° 轴线守恒与空间坐标系统 (The 180-Degree Action Axis Matrix)
- **定义**: 在任意两个发生相互作用的被摄主体之间，连接其视线或运动矢量的无形几何线即为“轴线”（Line of Action / Line of Sight）。
- **几何规则**: 所有摄影机机位必须严格布置在该轴线同一侧的半圆弧内（180° 区域）。只要机位不跨越这条轴线，角色 A 在银幕上永远朝向右看，角色 B 永远朝向左看，保证受众大脑内部建立的三维空间方位坐标绝对稳定。
- **合法越轴四种手法**:
  1. 摄影机在单一连续镜头中横向平移推拉滑过轴线；
  2. 角色自身走位穿过轴线，自然确立新轴线；
  3. 插入正中无方向的过轴中性镜头（Neutral Shot，如完全正视脸部）；
  4. 插入主观视点镜头（POV）重置空间感知。
- **来源**: Daniel Arijon, Grammar of the Film Language, Chapter 2 'The Triangle Principle', pp. 18–35.

## 2. 三角形机位布局系统 (The Triangle Principle / Three-Camera Setup)
- **定义**: 拍摄双人对话与冲突最经典、最具普适性的几何母体。
- **三个顶点**:
  - 机位 1 (Base / Master): 位于轴线同侧正前方，同时收纳 A 和 B 的全景/双人中景，确立空间地理；
  - 机位 2 (Reverse A): 拍摄 A 的单人近景/特写；
  - 机位 3 (Reverse B): 拍摄 B 的单人近景/特写。
- **来源**: Grammar of the Film Language, Chapter 3 'Dialogue Between Two Players', pp. 36–78.

## 3. 经典三步 POV 主观视点工程 (The 3-Step Point-of-View Architecture)
- **定义**:
  - 第一步 (The Looking Shot): 拍摄角色看向画外某处（中景/特写，确立视线方向与专注神情）；
  - 第二步 (The POV / Target Shot): 摄影机模拟角色的双眼视角，拍摄其所看到的物体或景象；
  - 第三步 (The Reaction Shot): 镜头切回角色面部特写，捕捉其看到景象后的心理震惊、恐惧或喜悦微表情。
- **来源**: Grammar of the Film Language, Chapter 8 'Point of View', pp. 142–165.
"""
(cand_dir / "frameworks.md").write_text(frameworks_md, encoding="utf-8")

# 2. principles.md
principles_md = """# 原则候选池 (Principles Candidates)

1. **屏幕方向绝对守恒律 (Law of Consistent Screen Direction)**:
   - 角色从左向右走，切入下一个镜头时必须继续从左向右移动；从画右出画（Right Exit），下一镜必须从画左入画（Left Entrance）。违背此法则会导致角色看起来像突然掉头撞向自己。

2. **视线角度互补对撞原则 (Eyeline Match & Complementary Angles)**:
   - 角色 A 仰望 20°，角色 B 的反打镜头必须俯视 20°；二者在画框水平位置上的留白（Nose Room / Lead Room）必须互补对称，使观众在潜意识中深信二人的目光在空间中精准交汇。

3. **动量掩盖动作剪辑法则 (Cutting on Action)**:
   - 剪切点永远落在角色发力动作的最高潮中间帧（起立到一半、手掌刚碰到门把手、刀刃挥出瞬间）。利用人类大脑对动量惯性的视觉追踪，无缝掩盖镜头画格切换的物理硬切。

4. **主镜头空间锚定与重置律 (Master Shot Spatial Re-anchoring)**:
   - 在密集的近景与特写交锋之后，当剧情发生转折、新角色加入或动作暂告一段落时，必须切回主镜头（Master Shot）重新锚定全场地理空间。

5. **机位景别与角度跳跃双重法则 (The 30-Degree & Scale Shift Rule)**:
   - 同一角色的两个连续镜头之间，景别必须至少改变一级（如中景切特写），机位角度必须至少旋转 30° 以上。严禁机位与景别几乎相同的偷懒跳切（Jump Cut）。
"""
(cand_dir / "principles.md").write_text(principles_md, encoding="utf-8")

# 3. cases.md
cases_md = """# 案例候选池 (Cases Candidates)

1. **经典双人过肩外反打对话调度 (Classic Over-The-Shoulder Reverse Dialogue)**:
   - A 与 B 隔桌谈判。
   - 机位 1: Master Shot，双人侧面全景，确立桌子长度与光线方向；
   - 机位 2: 机位越过 B 的右肩，拍摄 A 的正面胸上近景（OTS，B 的黑肩膀占据画面左下 15% 面积）；
   - 机位 3: 机位越过 A 的左肩，拍摄 B 的正面胸上近景（OTS，A 的黑肩膀占据画面右下 15% 面积）；
   - 双方视线精准对撞，肩部框架确立无可动摇的空间连结。

2. **利用角色自然走位完成合法越轴 (Legitimate Axis Shift via Actor Blocking)**:
   - 角色 A 与 B 对话，机位在右侧半圆。
   - 谈话进入激烈冲突，角色 A 愤怒地从座位上站起，从 B 身后大步走到房间左侧端起水杯；
   - 摄影机摇镜头跟随 A 走动，随着 A 的物理位移，二人连线构成的动作轴线自然在画面中完成旋转；
   - 轴线重置后，摄影机合法进入原本禁止的左侧区域，无需任何跳切破坏连贯性。

3. **银行劫匪拔枪冲锋动量剪辑 (Cutting on Action Gun Draw)**:
   - Shot 1 (中景): 劫匪右手猛烈伸向腰后拔枪，枪拔出一半；
   - Shot 2 (特写): 在枪口猛烈挥向空中的瞬间切入特写，枪口火光在特写中炸开；
   - 观众的大脑追踪拔枪的强动能，完全感知不到剪切点的存在，带来丝滑硬朗的动作冲击。
"""
(cand_dir / "cases.md").write_text(cases_md, encoding="utf-8")

# 4. counter-examples.md
counter_examples_md = """# 反例与常见病灶候选池 (Counter-Examples & Anti-Patterns)

1. **粗暴越轴跳轴病 (Crossing the Line / Jump Axis Bug)**:
   - 病灶: 摄影机无预兆地从轴线一侧跳到了另一侧，导致原本面朝右看的角色在下一格突然面朝左看，两个对话的角色看起来在望向同一个方向，空间逻辑瞬间崩溃。
   - 治愈: 严守 180° 半圆，或通过移动镜头、走位与中性视点合法过轴。

2. **抽搐跳切病 (Lazy Jump Cut / Sub-30-Degree Glitch)**:
   - 病灶: 两个连续镜头机位几乎完全一样，只是把角色的一句废话剪掉，导致角色在屏幕上瞬间抽搐位移。
   - 治愈: 严格执行机位旋转 30° 以上或改变至少一级景别（中景切近景）。

3. **视线落差错位病 (Eyeline Mismatch)**:
   - 病灶: 站立的成人与坐着的孩子说话，反打镜头中两人的视线都平视前方，观众无法感知二人在看着彼此。
   - 治愈: 严格匹配仰俯视夹角（成人俯视 30°，孩子仰视 30°）。
"""
(cand_dir / "counter-examples.md").write_text(counter_examples_md, encoding="utf-8")

# 5. glossary.md
glossary_md = """# 术语候选池 (Glossary Candidates)

1. **180-Degree Rule (180度轴线法则)**: 影视摄影机机位必须锁定在被摄主体连线同一侧半圆区域内的几何铁律。
2. **Axis of Action (动作轴线)**: 两个角色之间的视线连线或运动主体的位移方向矢量线。
3. **Triangle Principle (三角形机位原理)**: 由一个建立全景主镜头与两个反打单人镜头构成的经典机位几何布局系统。
4. **Over-The-Shoulder Shot / OTS (过肩镜头 / 外反打)**: 越过前景角色的肩膀拍摄背景角色的镜头。
5. **Clean Single / Internal Reverse (纯净单人镜头 / 内反打)**: 画框内仅有单一角色，完全排除对方身体部件的单人反打镜头。
6. **Cutting on Action (动量动作剪辑)**: 在被摄主体动作最高潮的运动过程中执行镜头切换的剪辑技术。
7. **Eyeline Match (视线匹配)**: 确保两个反打镜头中角色的注视角度与水平方向在几何空间中精确交汇的规则。
8. **Screen Direction (屏幕方向)**: 物体在画框中从左到右或从右到左运动的矢量方向。
9. **POV / Point-of-View Shot (主观视点镜头)**: 模拟画中特定角色的双眼直接观察世界的镜头。
10. **Master Shot (主镜头)**: 涵盖整个场景完整动作与所有参与者空间地理关系的建立镜头。
11. **Blocking (场面走位)**: 导演对演员在物理场景中的站位、移动轨迹与停顿点的精心编排。
12. **Sequence Shot (长镜头 / 镜头即场景)**: 用一个不间断的连续移动镜头完整呈现一段复杂剧情的场面调度。
"""
(cand_dir / "glossary.md").write_text(glossary_md, encoding="utf-8")

print("Created all 5 candidate files for Grammar of Film Language successfully!")
