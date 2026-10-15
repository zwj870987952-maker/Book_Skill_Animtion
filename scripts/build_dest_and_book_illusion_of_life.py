import json
import shutil
from pathlib import Path

iol_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\illusion-of-life")
cap_dir = iol_dir / ".cangjie" / "capabilities"
book_dir = cap_dir / "book"
book_dir.mkdir(parents=True, exist_ok=True)

# 复制 overview.md 和 glossary.md
shutil.copy(iol_dir / "BOOK_OVERVIEW.md", book_dir / "overview.md")
shutil.copy(iol_dir / "candidates" / "glossary.md", book_dir / "glossary.md")

# 12 项能力映射 (对应迪士尼十二黄金法则)
caps = [
    ("squash-and-stretch", "挤压与拉伸：生物组织弹性与常数体积守恒 (Squash & Stretch & Volume Conservation)", "在重力压迫与运动做功中展现极致弹性形变，严格遵循几何常数体积守恒定律。"),
    ("anticipation-physics", "动作预备与心理蓄势：反向做功与视觉引导 (Anticipation & Muscular Setup)", "在强力动作爆发前向反方向拉伸拮抗肌与调整重心蓄势，引导受众视网膜注意力。"),
    ("staging-clarity", "舞台调度与剪影清晰度：绝对瞬间可读性 (Staging & Silhouette Clarity)", "以纯黑剪影测试检验动作瞬间可读性，确立单一主视觉焦点，消除空间泥泞并拢与切线。"),
    ("straight-ahead-pose-to-pose", "连续画法与姿态对应法：动能灵感与结构控制融合 (Straight Ahead vs. Pose to Pose)", "连续画法的狂放不可预测动能与姿态对应法的严密空间时间控制在生产管线中的黄金融合。"),
    ("follow-through-overlapping", "跟随动作与动作重叠：多级滞后波浪与动能余震 (Follow Through & Overlapping Action)", "主动力源先行，柔性附属物与松弛组织多级滞后拖尾跟随，刹车时产生超量鞭打过冲。"),
    ("slow-in-slow-out", "慢入与慢出：牛顿加减速与阻尼缓冲轨目 (Slow In & Slow Out Mechanics)", "消除机械线性均分中割，在极值点编排密集加减速缓冲轨目，中间跨越大位移高速撕裂。"),
    ("arcs-of-motion", "圆滑弧线运动轨迹：关节旋转与自然律动 (Arcs of Motion)", "遵循生物骨骼绕铰链旋转运动学，运动轨迹绝对呈圆滑弧线，消除机械折线与穿模萎缩。"),
    ("secondary-action", "次级动作与情绪放大器：主次动作心理共振 (Secondary Action & Emotional Resonance)", "以附属微小动作丰富并放大主动作的情感动机与戏剧潜台词，严格服从主动作节奏。"),
    ("timing-weight-acting", "时间掌握与物理重量感：帧数控制与生命节拍 (Timing, Weight & Life Beat)", "通过绝对帧数控制展现物体的质量、密度、重力加速度与角色的心理情绪节拍。"),
    ("exaggeration-essence", "戏剧夸张与本质放大：真实背后的超真实提炼 (Exaggeration: Magnifying the Essence)", "绝非丑陋畸形变形，而是主观提炼角色精神与生理本质真理并放大 150%-200% 的艺术精髓。"),
    ("solid-drawing-volume", "纯熟绘图与三维立体空间：空间深度与体块转折 (Solid Drawing & Spatial Volume)", "在二维画纸上赋予形体真实三维体积、重量感、透视厚度与空间旋转，杜绝扁平纸片人。"),
    ("appeal-character-soul", "至高吸引力与角色灵魂：黄金比例、脆弱感与终极魔力 (Appeal & Character Soul)", "赋予角色迷人的几何比例、温暖人性脆弱感与跨越文化隔阂的迪士尼至高吸引力。")
]

destinations = {
    "book_slug": "illusion-of-life",
    "book_title": "The Illusion of Life: Disney Animation",
    "authors": ["Frank Thomas", "Ollie Johnston"],
    "target_pack_slug": "illusion-of-life",
    "capabilities": []
}

for slug, title, desc in caps:
    destinations["capabilities"].append({
        "capability_id": f"cap.illusion-of-life.{slug}",
        "display_name": title,
        "target_skill_slug": "illusion-of-life",
        "action": "create",
        "description": desc
    })

(cap_dir / "destinations.json").write_text(json.dumps(destinations, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Created destinations.json with {len(caps)} capabilities and initialized book overview/glossary for Illusion of Life!")
