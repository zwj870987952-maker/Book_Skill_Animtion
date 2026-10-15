import json
import shutil
from pathlib import Path

fi_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\framed-ink")
cap_dir = fi_dir / ".cangjie" / "capabilities"
book_dir = cap_dir / "book"
book_dir.mkdir(parents=True, exist_ok=True)

# 复制 overview.md 和 glossary.md
shutil.copy(fi_dir / "BOOK_OVERVIEW.md", book_dir / "overview.md")
shutil.copy(fi_dir / "candidates" / "glossary.md", book_dir / "glossary.md")

# 12 项能力映射
caps = [
    ("horizon-line-psychology", "视平线高度、仰俯视夹角与镜头心理学 (Horizon Line, Eye Level & Viewpoint Psychology)", "以视平线垂直位置与仰角俯角掌控受众心理投射，确立压迫、主导或脆弱情感基调。"),
    ("black-white-value-distribution", "黑白纯明度分布、深沉暗调与剪影可读性 (Black & White Value Structure & Silhouettes)", "确立 60-30-10 黑白两极明度结构，依托深黑硬边阴影与纯黑剪影实现 0.1 秒故事可读性。"),
    ("dynamic-geometric-tension", "对角斜线、尖锐三角形与几何张力构图 (Diagonals, Triangles & Visual Tension)", "打破平庸水平垂直对称，运用倾斜对角线与锐角三角形在画面中注入失衡动能与危险悬念。"),
    ("eye-leading-focal-paths", "环境线条引导、视线牵引与黄金焦点流线 (Eye Leading Lines & Focal Path Architecture)", "利用阴影边缘、地表透视反光与角色视线构建连续无形轨道，将瞳孔精准牵引至核心叙事靶点。"),
    ("three-layer-spatial-depth", "前景压迫、中景叙事与远景空气纵深 (Foreground, Midground & Background 3-Layer Depth)", "以前景暗部框架制造代入与压迫感，中景展开角色冲突，远景大气透视制造无垠空间纵深。"),
    ("aspect-ratio-framing-psychology", "画幅比例、银幕宽高比与画框心理压迫 (Aspect Ratios & Psychological Framing)", "驾驭 4:3 幽闭压迫、16:9 经典平衡与 2.39:1 宽银幕宏大对峙，让画框本身成为叙事施压者。"),
    ("visual-continuity-eye-trace", "分镜头连续视线轨迹守恒与剪辑流线 (Visual Continuity & Eye-Trace Cadence)", "在画格切换间维持受众瞳孔物理落点平滑滑动，严格遵循动作轴线守恒与视觉动量对撞。"),
    ("chiaroscuro-lighting-mood", "明暗对照法、戏剧光斑与光影情感基调 (Chiaroscuro, Dramatic Lighting & Mood)", "运用极度深沉阴影与锐利切割光斑雕刻形态，顶光审判、底光诡谲与逆光孤独的情感控制。"),
    ("scale-contrast-dominance", "尺度悬殊对比、环境吞噬与角色威严霸气 (Scale Contrast, Dominance & Vulnerability)", "以 5% 渺小个体对抗 95% 浩瀚吞噬环境，或以前景庞然大物衬托远景微小猎物制造绝对支配。"),
    ("lens-perspective-wide-vs-telephoto", "广角透视冲击 vs 长焦空间压缩窒息感 (Lens Perspective: Wide vs. Telephoto)", "广角拉伸纵深距离强化爆发冲撞与孤立感，长焦压缩空间让追击者紧贴猎物制造窒息绝望。"),
    ("negative-space-graphic-economy", "留白力量、纯粹极简与负空间引力场 (Negative Space, Subtraction & Graphic Gravity)", "以大面积空旷留白释放深沉心理引力，剔除视觉杂质，赋予叙事纯粹而锋利的情感重力。"),
    ("storyboard-cadence-editorial-flow", "故事板节拍编排、景别交替与动作分镜流水线 (Storyboard Cadence, Shot Hierarchy & Action Flow)", "全景建立、中景推进与特写爆破的戏剧节拍交替，编排具有电影呼吸感的视觉连环画卷。")
]

destinations = {
    "book_slug": "framed-ink",
    "book_title": "Framed Ink: Drawing and Composition for Visual Storytellers",
    "author": "Marcos Mateu-Mestre",
    "target_pack_slug": "framed-ink",
    "capabilities": []
}

for slug, title, desc in caps:
    destinations["capabilities"].append({
        "capability_id": f"cap.framed-ink.{slug}",
        "display_name": title,
        "target_skill_slug": "framed-ink",
        "action": "create",
        "description": desc
    })

(cap_dir / "destinations.json").write_text(json.dumps(destinations, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Created destinations.json with {len(caps)} capabilities and initialized book overview/glossary for Framed Ink!")
