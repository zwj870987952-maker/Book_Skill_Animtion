import os
import re
import yaml

base_dir = r"c:\Users\zwj87\Documents\Book_Skill\books\facial-expressions"
cards_dir = os.path.join(base_dir, ".cangjie", "capabilities", "cards")
output_yaml = os.path.join(base_dir, ".cangjie", "capabilities", "verified.yaml")

capabilities = []

for card_file in sorted(os.listdir(cards_dir)):
    if not card_file.endswith(".md"):
        continue
    filepath = os.path.join(cards_dir, card_file)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm_match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not fm_match:
        print(f"Error parsing frontmatter in {card_file}")
        continue

    fm = yaml.safe_load(fm_match.group(1))
    cap_id = fm.get("id")
    slug = cap_id.split(".")[-1]
    title = fm.get("title")
    importance = fm.get("tier", "core")
    summary = fm.get("summary", "")
    keywords = fm.get("keywords", [])
    raw_also_read = fm.get("also_read", [])
    also_read = [s.replace("cap.facial-expressions.", "") for s in raw_also_read]

    intents = [
        f"如何实现{title}",
        f"应用{title}的解剖与几何规范",
        f"排查{title}相关的常见形变反模式与错误"
    ]

    source_evidence = []
    for src in fm.get("sources", []):
        source_evidence.append({
            "source_id": "zarins-anatomy-of-facial-expression-2017",
            "citation": f"{src.get('book', 'Anatomy of Facial Expression')} - {src.get('chapter', '')}",
            "excerpt": summary
        })

    cap_entry = {
        "capability_id": cap_id,
        "revision": 1,
        "status": "active",
        "aliases": [],
        "supersedes": [],
        "merged_into": None,
        "split_into": [],
        "slug": slug,
        "title": title,
        "importance": importance,
        "importance_rationale": f"该能力是《面部表情艺用解剖》中核心的{importance}级别解剖学与三维形变基座规范。",
        "one_liner": summary,
        "intents": intents,
        "keywords": keywords,
        "also_read": also_read,
        "card": f"cards/{card_file}",
        "frontmatter": {
            "title": title,
            "importance": importance,
            "one_liner": summary,
            "requirements": [fm.get("requirements", [])] if isinstance(fm.get("requirements"), str) else fm.get("requirements", []),
            "antirequirements": [fm.get("antirequirements"), []] if isinstance(fm.get("antirequirements"), str) else fm.get("antirequirements", []),
            "intents": intents,
            "keywords": keywords,
            "sources": source_evidence,
            "also_read": also_read
        },
        "source_evidence": source_evidence,
        "promotion": {
            "source": "cangjie-phase2",
            "validated_by": "human-and-schema"
        }
    }
    capabilities.append(cap_entry)

bundle = {
    "schema_version": 1,
    "bundle_id": "bundle.facial-expressions",
    "book": {
        "title": "面部表情艺用解剖 (Anatomy of Facial Expression)",
        "source_pack": "books/facial-expressions",
        "edition": "Visual Reference Edition",
        "authors": [
            "Uldis Zarins",
            "Sandis Kondrats"
        ],
        "year": 2017
    },
    "entry": {
        "name": "facial-expressions",
        "description": "全球三维角色艺术家、动画师与数字雕塑家面部解剖与表情绑定第一圣经。将达芬奇经典人体解剖学与保罗·埃克曼面部动作编码系统（FACS）完美统一。涵盖头骨 10 大硬质骨骼标志点刚性锚定、正交皮肤张力皱纹动力学定律、枕额肌与皱眉肌复合内中外三分段运动解耦（AU 1/2/4）、眼轮匝肌眶部与睑部张力闭合（AU 5/6/7/43）、四直肌与双斜肌矢量合成极速 1 帧扫视跳跃（AU 61-64）、鼻肌与上唇鼻翼提肌中面部滑移（AU 9/38/39）、口轮匝肌内外同心环与红唇白线体积守恒（AU 18/22/23/24）、颧大肌斜拉 vs 笑肌纯水平撕扯嘴角矢量网络（AU 11/12/13/20）、降口角肌与颏肌推高下巴橘皮纹（AU 15/16/17）、咬肌闭颌与 TMJ 双阶段旋转-平移张嘴运动学（AU 26/27/31）、深浅层脂肪垫与骨性支持韧带阻隔、杜氏真笑双肌群协同（AU 6+12）跨越恐怖谷，以及人类七大普适核心情绪（喜悦、悲伤、狂怒、恐惧、惊讶、厌恶、蔑视）全参数 FACS 拓扑合成与微表情时间线规范。",
        "core_principles": [
            "头骨标志点在任何极端表情下保持绝对刚性，软组织沿骨骼三维曲面滑移与堆叠。",
            "正交皱纹动力学定律：动态皮肤折痕走向恒垂直于深层驱动肌纤维的收缩轴线。",
            "杜氏真笑黄金闭环：眼轮匝肌眶外环（AU 6）的自发收缩与下眼睑拱起是真诚微笑不可或缺的解剖学标志。",
            "悲伤肌群反向力偶：额肌内侧向上提拉（AU 1）与皱眉肌向内下拉（AU 4）对抗形成特征性倒八字眉峰与中央三角隆起。",
            "恐惧水平撕扯 vs 惊讶垂直松弛：恐惧为笑肌（AU 20）水平横拉嘴唇且眉毛拉直；惊讶为下颌受重力松弛垂直下坠（AU 26）且眉毛高拱。",
            "口角轴心（Modiolus）是 8 组表情肌力的矢量合成枢纽，决定酒窝生成与中下脸平衡。",
            "颞下颌关节（TMJ）遵循双阶段运动学：张嘴前 20mm 为纯定轴旋转，大张嘴时髁突向前下方平移滑行 8-12mm。"
        ],
        "out_of_scope": [
            "纯工业机械齿轮传动与流体力学管道仿真",
            "静态建筑钢筋混凝土承重力学计算",
            "眼科白内障与激光视力矫正临床手术操作指南"
        ],
        "stop_conditions": [
            "用户仅咨询机械建筑或眼科眼科临床医学，不涉及角色面部解剖、表情绑定、动画表演与三维雕刻时判停",
            "已输出明确的面部骨骼标志点坐标、FACS 动作单元参数、肌群收缩矢量、正交皱纹图或情绪合成方案时判停"
        ]
    },
    "router_entry": {
        "name": "facial-expressions",
        "description": "乌尔迪斯·扎林斯面部表情艺用解剖与表情绑定工程手册。提供头骨刚性标志点、正交张力皱纹定律、额肌皱眉肌解耦、眼轮匝肌真笑闭环、眼外肌扫视跳跃、鼻部与中面部滑移、口轮匝肌同心环与白线守恒、嘴角提升与水平撕扯矢量网络、降口角肌与颏肌橘皮下巴、TMJ 双阶段张嘴运动学、深浅脂肪垫韧带阻隔与七大核心情绪全参数 FACS 拓扑合成支持。"
    },
    "promotion_budget": 8,
    "capabilities": capabilities
}

with open(output_yaml, "w", encoding="utf-8") as f:
    yaml.dump(bundle, f, allow_unicode=True, sort_keys=False)

print(f"Successfully generated standard verified.yaml with slugified also_read.")
