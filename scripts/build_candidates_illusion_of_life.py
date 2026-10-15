import json
from pathlib import Path

cand_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\illusion-of-life\candidates")
cand_dir.mkdir(parents=True, exist_ok=True)

# 1. frameworks.md
frameworks_md = """# 框架候选池 (Frameworks Candidates)

## 1. 迪士尼动画十二黄金法则体系 (The 12 Basic Principles of Animation)
- **定义**: 迪士尼动画黄金九老（Frank Thomas, Ollie Johnston 等）在数十年生产实践中确立的现代角色动画工业标准体系：
  1. 挤压与拉伸 (Squash and Stretch)
  2. 动作预备 (Anticipation)
  3. 舞台调度 (Staging)
  4. 连续画法与姿态对应法 (Straight Ahead Action and Pose to Pose)
  5. 跟随动作与动作重叠 (Follow Through and Overlapping Action)
  6. 慢入与慢出 (Slow In and Slow Out)
  7. 圆滑弧线 (Arcs)
  8. 次级动作 (Secondary Action)
  9. 时间掌握 (Timing)
  10. 戏剧夸张 (Exaggeration)
  11. 纯熟绘图 (Solid Drawing)
  12. 终极吸引力 (Appeal)
- **来源**: Frank Thomas & Ollie Johnston, The Illusion of Life, Chapter 3 'The Principles of Animation', pp. 47–69.

## 2. 动画制作管线双轨模型 (Straight Ahead vs. Pose to Pose Hybrid Engine)
- **定义**:
  - 连续画法 (Straight Ahead): 从第一张画顺次画到最后一张，充满自发的狂放灵感、意外生机与流动感，但极难控制空间比例与关键时间点；
  - 姿态对应法 (Pose to Pose): 先确立核心关键帧与极值姿态，再计算中割帧，具备极强的几何构图、体积守恒与时间精准性；
  - 迪士尼大师混合流: 关键大动作与表演使用 Pose to Pose 锁定框架，打斗特效、流体烟雾与狂奔段落使用 Straight Ahead 注入狂野生机。
- **来源**: The Illusion of Life, pp. 56–58.

## 3. 角色心理与次级动作共振框架 (Primary Intent & Secondary Emotional Amplifier)
- **定义**: 主动作（Primary Action）承载剧情的主要位移（如走路、奔跑、开门）；次级动作（Secondary Action）必须依附并丰富主动作，作为情感的放大器（如边走路边瑟瑟发抖、开门前手腕剧烈颤抖抹冷汗）。如果次级动作抢夺了主动作的焦点，则属于舞台调度失败。
- **来源**: The Illusion of Life, pp. 64–65.
"""
(cand_dir / "frameworks.md").write_text(frameworks_md, encoding="utf-8")

# 2. principles.md
principles_md = """# 原则候选池 (Principles Candidates)

1. **绝对体积守恒原则 (Law of Constant Volume)**:
   - 挤压（Squash）时形体在垂直方向缩短，必须在水平与径向方向相应膨胀展平；拉伸（Stretch）时形体变长，径向必须相应变细收拢。任何无故增减容积的变形都会摧毁物体的实体可信度。

2. **动作意图先行预备律 (The Law of Anticipation)**:
   - 任何强力做功发生之前，生命肌肉必然向反方向拉伸蓄力。预备动作越深越充分，随后的爆发动作显得越迅猛强大。

3. **舞台调度唯一焦点律 (Staging Singular Focus)**:
   - 银幕舞台在同一瞬间只能讲清楚一件事。多重动作必须在时间上错开，确保观众的视线焦点绝对不被次要细节干扰。

4. **自然圆滑弧线律 (Arcs of Natural Locomotion)**:
   - 生命骨骼绕关节转动，运动轨迹必然呈现连续圆润的弧线。直线移动是机械零件的专利。

5. **夸张服务于真理原则 (Exaggeration Magnifies Truth)**:
   - 夸张绝非丑陋怪诞变形，而是提炼现实背后的本质核心特征并将其主观放大 150%-200%，令观众无法忽视。

6. **至高吸引力第一心法 (Appeal is King)**:
   - 吸引力绝不局限于“漂亮美丽”。可爱角色需要温暖脆弱感，邪恶反派需要宏伟优雅的几何纯度与震撼力场。
"""
(cand_dir / "principles.md").write_text(principles_md, encoding="utf-8")

# 3. cases.md
cases_md = """# 案例候选池 (Cases Candidates)

1. **经典面团袋挤压拉伸形变 (The Flour Sack Life Test)**:
   - 一个装满面粉的布袋，没有五官、没有四肢。
   - 仅凭底部落地的横向挤压膨胀、起跳时的纵向拉伸拉长、悲伤时的弯曲蜷缩和傲慢时的挺直充气，完全展现出人类的喜怒哀乐与重力重量感。

2. **《白雪公主》邪恶王后变身巫婆的夸张与舞台调度 (The Queen to Witch Transformation)**:
   - 极度强烈的顶光与侧光阴影；
   - 变身前的优雅高贵（正立三角形稳固几何）在雷电中剧烈扭曲，夸张下弯为鹰钩鼻、驼背与如枯枝般的尖锐指节（倒立不稳定几何）；
   - 动作预感与次级药水翻滚完美对齐，成为动画史上表演调度的最高丰碑。

3. **《小鹿斑比》初学步行的次级动作与吸引力 (Bambi’s First Steps on Ice)**:
   - 主动作: 在冰面上挣扎保持站立；
   - 次级动作: 四条细腿各自分开向不同方向打滑、尾巴恐慌甩动、耳朵紧贴后脑、大眼睛中泛起惊恐泪花；
   - 极致的脆弱感与生理真实性赋予角色无可抗拒的至高吸引力（Appeal）。
"""
(cand_dir / "cases.md").write_text(cases_md, encoding="utf-8")

# 4. counter-examples.md
counter_examples_md = """# 反例与常见病灶候选池 (Counter-Examples & Anti-Patterns)

1. **吹气球体积失真病 (Ballooning Volume Defect)**:
   - 病灶: 拉伸时形体变大变粗，挤压时形体变小缩水，违背物理守恒定律。
   - 治愈: 严格执行常数体积公式，拉伸必变细，压缩必展平。

2. **机械木偶同步僵直病 (Twin-Framing Robot Syndrome)**:
   - 病灶: 身体各部位同时起跑、同时刹车，缺乏跟随与重叠动作。
   - 治愈: 施加多级重叠延迟（Overlapping Action），主动力源先行，柔性部件滞后跟随。

3. **杂乱失焦舞台调度病 (Cluttered Staging Bug)**:
   - 病灶: 背景里三个角色同时做剧烈动作，主画面角色也在说话，观众眼球不知所措。
   - 治愈: 净化舞台！一次只让一个主要动作发生，次要角色保持定格或微小呼吸，视线焦点唯一化。
"""
(cand_dir / "counter-examples.md").write_text(counter_examples_md, encoding="utf-8")

# 5. glossary.md
glossary_md = """# 术语候选池 (Glossary Candidates)

1. **Squash and Stretch (挤压与拉伸)**: 表现生命组织柔韧性与弹性形变的核心法则，必须严格遵循常数体积守恒。
2. **Anticipation (动作预备)**: 强力动作前向相反方向进行的生理肌肉蓄力与视觉引导动作。
3. **Staging (舞台调度)**: 将一个想法、动作或情绪以绝对清晰明了、毫无歧义的构图与剪影呈现在银幕上的艺术。
4. **Straight Ahead Action (连续画法)**: 从起点顺次逐帧向前绘制的自发式动画方法。
5. **Pose to Pose (姿态对应法)**: 先确立关键姿态再进行过渡中割计算的结构化动画方法。
6. **Follow Through (跟随动作)**: 主体停止运动后，受惯性驱动的次级附着物继续向前运动直至制动的现象。
7. **Overlapping Action (动作重叠)**: 身体各部件以不同步调、不同速率参差启动和停止的时间延迟现象。
8. **Slow In and Slow Out (慢入与慢出)**: 动作在起止极值点附近密集缓冲、中间高速位移的物理加减速现象。
9. **Arcs (圆滑弧线)**: 生物骨骼关节旋转时自然形成的圆滑运动轨迹。
10. **Secondary Action (次级动作)**: 附属于主动作并进一步放大和丰富主动作情感意图的附属微动作。
11. **Timing (时间掌握)**: 决定动作物理速度、重量感与生命质感的绝对帧数分配。
12. **Exaggeration (戏剧夸张)**: 主观提炼事物本质真理并将其戏剧性放大的美学原则。
13. **Solid Drawing (纯熟绘图)**: 在二维画纸上赋予形体真实三维体积、重量、透视厚度与空间深度的能力。
14. **Appeal (终极吸引力)**: 赋予角色令人着迷的视觉魅力、个性温度与深层人性共鸣的终极品质。
"""
(cand_dir / "glossary.md").write_text(glossary_md, encoding="utf-8")

print("Created all 5 candidate files for Illusion of Life successfully!")
