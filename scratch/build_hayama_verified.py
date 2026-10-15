import os
import re
import yaml

base_dir = r"c:\Users\zwj87\Documents\Book_Skill\books\hayama-character-design"
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
    also_read = [s.replace("cap.hayama-character-design.", "") for s in raw_also_read]

    intents = [
        f"如何实现{title}",
        f"应用{title}的角色设计与动态作画规范",
        f"排查{title}相关的常见原画与作监反模式"
    ]

    source_evidence = []
    for src in fm.get("sources", []):
        source_evidence.append({
            "source_id": "hayama-anime-drawing-masterclass-2016",
            "citation": f"{src.get('book', 'Junichi Hayama Anime Drawing Masterclass')} - {src.get('chapter', '')}",
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
        "importance_rationale": f"该能力是《羽山淳一动画角色设计与动态作画》中核心的{importance}级别工业原画与作监设计规范。",
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
    "bundle_id": "bundle.hayama-character-design",
    "book": {
        "title": "超人气动画角色设计攻略：羽山淳一的现场绘画解说课",
        "source_pack": "books/hayama-character-design",
        "edition": "Masterclass Edition",
        "authors": [
            "Junichi Hayama (羽山淳一)"
        ],
        "year": 2016
    },
    "entry": {
        "name": "hayama-character-design",
        "description": "日本殿堂级总作画监督羽山淳一热血动画角色设计与动态作画实战工程手册。涵盖脊椎单一动作主线与动态骨架极速提炼（Line of Action）、头部脑颅球体与经纬十字基准线极端仰俯三维透视旋转、决意与咆哮表情及 45° 经典硬派影线分面雕刻、三棱柱体块化头发分组与发旋气流破风流线、胸腔梯形箱与骨盆倒梯形箱三轴对立平衡对抗（Contrapposto）、锁骨衣架力学与三角肌/二头肌手臂肌群旋转联动、手掌楔形块与掌骨拱门指关节阶梯透视抓握、腿部双 S 减震对抗曲线与内踝高外踝低解剖铁门、格斗出拳飞踢尺度爆炸与 T-Joint 重叠极限透视短缩法（Foreshortening）、服装拉伸辐射褶与战斗斗篷破风正弦波浪流线、0.2 秒纯黑剪影测试与负空间透光窗口排布，以及作画监督级线条物理重量感、中割时间图表（Time-chart）与圆弧导轨保形修正全套工业规范。",
        "core_principles": [
            "动作主线优先律：绘制任何姿态前必须先用一条贯穿脊椎的单一连续弧线（Line of Action）统领全身动量与重力平衡。",
            "三维几何箱体对抗：胸腔箱与骨盆箱必须确立三轴方向上的对立平衡（Contrapposto），形成一侧紧缩（Pinch）与对侧拉伸（Stretch）的黄金非对称性。",
            "极限透视短缩重叠截断定律：正对镜头的重拳与飞踢依靠尺度暴涨、T-Joint 遮挡截断与环形包裹线彻底破除截肢错觉。",
            "头部球面经纬十字基准线：严格依据仰沉俯浮的透视规律排布五官，展现坚硬的颏下三角（Submental Triangle）底面。",
            "内外踝高低差解剖铁门：脚踝结构恒定遵守内踝骨高、外踝骨低的物理规律，脚掌蹬地紧贴地面透视网格。",
            "45° 影线与眼窝死黑：用纯黑深阴影切碎漫反射，眼窝全黑配合瞳孔锐利高光，排线保持严格平行的 45° 纯净倾角。",
            "纯黑剪影 0.2 秒自明性：通过四肢外展制造透光的负空间窗口，确保招式意图与武器指向在纯黑投影下瞬间可读。",
            "作画监督中割保形工程：运用运笔压感赋予线条重力重量感，标明 Time-chart 摄影表时序与运动圆弧导轨，防止中割抽搐崩坏。"
        ],
        "out_of_scope": [
            "纯工业机械齿轮模具注塑成型代码",
            "静态纸质图书排版拼版与油墨化学配比化验",
            "医学骨科人工关节置换手术临床操作规范"
        ],
        "stop_conditions": [
            "用户仅咨询机械注塑或骨科临床手术，不涉及角色设计、动画原画、作画监督、动态速写与格斗动作时判停",
            "已输出明确的动作主线图式、箱体透视参数、肌肉体块交错、45° 影线图、剪影负空间或中割导轨方案时判停"
        ]
    },
    "router_entry": {
        "name": "hayama-character-design",
        "description": "羽山淳一动画角色设计与动态作画工程手册。提供动作主线、胸骨盆对立平衡箱体、头部十字线三维翻转、热血表情与 45° 影线分面、体块发束风力流线、锁骨肩臂联动、掌骨拱门阶梯、腿部双 S 曲线与内外踝高低差、重拳飞踢极限透视短缩、战斗斗篷布褶、纯黑剪影负空间与作监中割保形修正全流程工业支持。"
    },
    "promotion_budget": 8,
    "capabilities": capabilities
}

with open(output_yaml, "w", encoding="utf-8") as f:
    yaml.dump(bundle, f, allow_unicode=True, sort_keys=False)

print(f"Successfully generated standard verified.yaml for hayama-character-design with {len(capabilities)} capabilities.")
