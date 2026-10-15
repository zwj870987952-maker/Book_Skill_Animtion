import json
import shutil
from pathlib import Path

gfl_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\grammar-of-film-language")
cap_dir = gfl_dir / ".cangjie" / "capabilities"
book_dir = cap_dir / "book"
book_dir.mkdir(parents=True, exist_ok=True)

# 复制 overview.md 和 glossary.md
shutil.copy(gfl_dir / "BOOK_OVERVIEW.md", book_dir / "overview.md")
shutil.copy(gfl_dir / "candidates" / "glossary.md", book_dir / "glossary.md")

# 12 项能力映射
caps = [
    ("axis-of-action-180-rule", "180° 动作轴线守恒与合法越轴规程 (The 180° Action Axis & Crossing the Line)", "将机位锁定在视线连线同侧 180° 半圆内，熟练掌握移动镜头滑过、角色走位与主观视点四种合法越轴手法。"),
    ("triangle-principle-setups", "三角形机位系统与双人对话布局 (The Triangle Principle for Two Actors)", "以全景主镜头为顶点、两个单人反打为底角构建稳固三角形机位网络，统领双人对话场景。"),
    ("ots-vs-clean-single", "过肩外反打 vs 纯净内反打景别心理学 (External OTS vs. Internal Clean Singles)", "过肩外反打借由前景肩膀建立空间连结与心理博弈，纯净内反打剔除干扰强化极度孤独与情感爆破。"),
    ("parallel-screen-dialogue", "并排平行站位与车内吧台镜头调度 (Parallel Dialogue & Lateral Setups)", "调校两人肩并肩同行、车内驾驶座或吧台等并排平行站位下的侧向反打、内侧反打与潜望视线系统。"),
    ("three-character-triangles", "三人及多角色对话多边形机位重组 (Three-Character Setups & Axis Reorientation)", "在三人复杂群戏中解构主导双人轴线、次级对话轴线与外围观察者，动态切换三角形机位分组。"),
    ("eyeline-match-convergence", "视线角度对撞匹配与空间汇聚几何学 (Eyeline Matching & Convergence Geometry)", "严格匹配反打镜头中的视线水平朝向与仰俯互补夹角，留出对称视线留白，确立目光空间交汇。"),
    ("screen-direction-continuity", "屏幕运动方向守恒与出入画对齐 (Screen Direction: Clean Exit & Clean Entrance)", "保证移动主体在连续镜头间的屏幕矢量一致，右出画必左入画，防止角色掉头撞击自身的方位混乱。"),
    ("cutting-on-action-momentum", "动作剪辑点与动量惯性掩盖法则 (Cutting on Action & Momentum Match)", "在起立、坐下、开门等动作做功最高潮中间帧执行镜头切分，利用人脑动量追踪惯性掩盖剪辑硬切。"),
    ("pov-three-step-architecture", "主观视点镜头三步法与视听投射 (The 3-Step POV System: Look, Object, React)", "以看(Looking Shot) -> 视点目标(POV Shot) -> 反应特写(Reaction Shot) 三步法实现受众深度代入。"),
    ("master-shot-coverage-system", "主镜头空间建立与分切覆盖装配工程 (Master Shot Technique & Coverage)", "从 Master 全景确立空间地理，按戏剧节拍切入中近景反打，在剧情转折点切回主镜头重置空间。"),
    ("actor-blocking-camera-reposition", "角色走位引导轴线转移与机位重置 (Actor Blocking & Natural Axis Shift)", "通过演员在场景中的起立、踱步与换位自然重构动作轴线，引导摄影机机位合法平稳重置。"),
    ("sequence-shot-choreography", "一镜到底场面调度与无剪辑景别转换 (Sequence Shot & Mise-en-Scène Choreography)", "在不间断长镜头中通过角色走位与机位推拉摇移，无缝实现全景、双人中景与单人特写的流态切换。")
]

destinations = {
    "book_slug": "grammar-of-film-language",
    "book_title": "Grammar of the Film Language",
    "author": "Daniel Arijon",
    "target_pack_slug": "grammar-of-film-language",
    "capabilities": []
}

for slug, title, desc in caps:
    destinations["capabilities"].append({
        "capability_id": f"cap.grammar-of-film-language.{slug}",
        "display_name": title,
        "target_skill_slug": "grammar-of-film-language",
        "action": "create",
        "description": desc
    })

(cap_dir / "destinations.json").write_text(json.dumps(destinations, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Created destinations.json with {len(caps)} capabilities and initialized book overview/glossary for Grammar of Film Language!")
