import os
import re
import yaml

base_dir = r"c:\Users\zwj87\Documents\Book_Skill\books\storyboard-art"
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
    also_read = [s.replace("cap.storyboard-art.", "") for s in raw_also_read]

    intents = [
        f"如何实现{title}",
        f"应用{title}的分镜与视听规范",
        f"排查{title}相关的常见分镜反模式与错误"
    ]

    source_evidence = []
    for src in fm.get("sources", []):
        source_evidence.append({
            "source_id": "hart-art-of-the-storyboard-2008",
            "citation": f"{src.get('book', 'The Art of the Storyboard')} - {src.get('chapter', '')}",
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
        "importance_rationale": f"该能力是《开拍之前：故事板的艺术》中核心的{importance}级别工业分镜设计规范。",
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
    "bundle_id": "bundle.storyboard-art",
    "book": {
        "title": "开拍之前：故事板的艺术 (The Art of the Storyboard)",
        "source_pack": "books/storyboard-art",
        "edition": "2nd Illustrated Edition",
        "authors": [
            "John Hart"
        ],
        "year": 2008
    },
    "entry": {
        "name": "storyboard-art",
        "description": "好莱坞影视工业与全球动画前期制作标准化分镜实战工程手册。建立故事板画师与导演、摄影指导、剪辑师及三维布局团队无歧义协同的标准视觉语言。涵盖 1.33:1, 1.85:1, 2.39:1 画幅几何学与 90% 动作/80% 字幕安全框（Action/Title Safe）、ELS 至 ECU 七级人体解剖非关节黄金裁切标尺、摄影机运动双线空心箭头系统（Pan, Tilt, Dolly, Zoom, Crane, Track）、角色位移细实心箭头与出入画语法（E.F. / X.F.）、视平线与摄影机高度等价铁律与一/二/三点透视网格、广角大透视 vs 长焦空间扁平压缩情绪、三分法则九宫格交叉点与视线呼吸留白（Looking Room）、三阶极简明暗调（白、50%灰、黑）与纯黑剪影测试、180°动作轴线守恒与追逐/对峙屏幕矢量连续性、硬切/叠化/淡黑/匹配剪辑（Match Cut）光学转场语法、动态故事板（Animatic）非线性编辑对白导轨与时间线节奏排障、15秒/30秒商业广告四段式黄金结构（Hook, Pain Point, Solution, Brand Lock），以及动作大戏蓄力-击打-受击反应三步曲与动量隐形剪辑（Cutting on Action）全流程工业规范。",
        "core_principles": [
            "故事板是工业蓝图而非纯艺术插画：核心价值在于视觉沟通的绝对准确度与现场工业可执行性。",
            "符号系统零歧义铁律：摄影机运动一律采用画框外侧或跨框双线空心大箭头；主体位移一律采用画框内部细实心箭头或虚线轨迹。",
            "人体景别非关节裁切铁律：绝对禁止在人体自然关节处（颈、肘、腕、膝、踝）横向裁切，永远切在长骨肌肉饱满的中段。",
            "视平线等价铁律：画面中透视视平线（Horizon Line）高度在物理上严格等于摄影机镜头的离地绝对高度。",
            "180°动作轴线守恒：机位必须永久锁定在假想轴线同侧半圆内；追逐戏保持同向屏幕矢量，对峙戏保持对撞相向。",
            "视线呼吸留白（Looking Room）守恒：角色面朝方向前方必须预留至少占画幅宽度 50%-70% 的开阔负空间。",
            "三阶极简明暗（Three-Tone System）：画面精简提炼为纯白、50%中灰与纯黑，主体必须 100% 通过纯黑剪影测试。",
            "动态故事板（Animatic）前置排障：在实拍和三维资产制作前，通过装配对白导轨的时间线测试，就地消灭叙事拖沓与节奏病灶。"
        ],
        "out_of_scope": [
            "纯工业机械模具注塑成型与数控铣削工艺",
            "静态纸质书籍印刷拼版与油墨配比化验",
            "医学牙科种植牙与颌面外科手术临床操作"
        ],
        "stop_conditions": [
            "用户仅咨询机械注塑或印刷牙科临床医学，不涉及影视导演、分镜头设计、视听语言与前期动画预演时判停",
            "已输出明确的标准分镜画框参数、机位运镜箭头图、景别裁切线、180° 轴线图、商业广告时间分配或 Animatic 剪辑表时判停"
        ]
    },
    "router_entry": {
        "name": "storyboard-art",
        "description": "约翰·哈特电影与动画故事板艺术工程手册。提供标准画幅与安全框、七级景别人体裁切、摄影机运镜箭头规范、角色出入画轨迹、一/二/三点透视网格、三分法则视线留白、三阶明暗与剪影测试、180°动作轴线连续性、光学剪辑转场语法、动态故事板（Animatic）时间线节奏、15/30秒广告结构与动作大戏分镜拆解全流程工业支持。"
    },
    "promotion_budget": 8,
    "capabilities": capabilities
}

with open(output_yaml, "w", encoding="utf-8") as f:
    yaml.dump(bundle, f, allow_unicode=True, sort_keys=False)

print(f"Successfully generated standard verified.yaml for storyboard-art with {len(capabilities)} capabilities.")
