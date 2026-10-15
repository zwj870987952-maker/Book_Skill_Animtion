import yaml
import json
from pathlib import Path
import jsonschema
from referencing import Registry, Resource

caps_data = [
    {
        "slug": "character-construction-proportions",
        "title": "基础几何体块与比例公式",
        "importance": "critical",
        "importance_rationale": "卡通角色设计与三维建模的基础底座，以头长比例与球形/梨形结构保障造型立体感与一致性",
        "one_liner": "以头高为单位标尺锁定头身比，用球形头骨与大端朝下的梨形躯干构建稳固重心与立体感",
        "intents": ["设计卡通角色头身比与基本体型", "用球形和梨形体块构建角色骨骼与躯干", "排查角色看起来扁平如纸片贴纸的造型缺陷"],
        "keywords": ["头身比", "Head Unit", "梨形体块", "Pear shape", "球形结构", "蛋形模型", "立体体块"],
        "also_read": ["line-of-action-rhythm", "model-sheet-uniformity"],
        "desc": "基于头长比例标尺与球形/梨形几何体块构建卡通角色三维立体骨架。不适用于高精复杂写实人体解剖雕塑。",
        "tags": ["cartoon", "character-design", "proportion", "construction"],
        "loc": "第 1 章，第 10–16 页"
    },
    {
        "slug": "line-of-action-rhythm",
        "title": "动作线穿透与清晰剪影",
        "importance": "critical",
        "importance_rationale": "赋予动作姿态生命力与视觉张力的决定性法则，消除面条软弱姿态并保障剪影瞬间可读",
        "one_liner": "用单一流畅的 C/S 形动作线贯穿全身三大体块，四肢外扩留出负空间确保纯黑剪影一目了然",
        "intents": ["寻找并绘制角色姿态的核心动作线", "优化关键帧姿态的爆发力与动态势能", "执行动作纯黑剪影测试消除肢体重叠混乱"],
        "keywords": ["动作线", "Line of Action", "剪影测试", "Silhouette", "负空间", "Negative Space", "姿态张力"],
        "also_read": ["character-construction-proportions", "acting-poses-staging"],
        "desc": "利用单一连续主导动作线穿透头部、胸部与骨盆，并优化负空间剪影清晰度。不适用于蜷缩防御特意闭合姿态。",
        "tags": ["cartoon", "line-of-action", "silhouette", "poses"],
        "loc": "第 1 章，第 11 页；第 3 章，第 128–132 页"
    },
    {
        "slug": "facial-expressions-squash-stretch",
        "title": "面部表情极值与容积守恒",
        "importance": "high",
        "importance_rationale": "卡通极端表情夸张戏剧性的核心法则，在下颌大尺度开合中严格保持头颅体量恒常性",
        "one_liner": "拉伸下颌时脸颊等比收窄变细，挤压下颌时脸颊横向扩张外凸，严格维持头部容积守恒",
        "intents": ["绘制狂喜、惊恐、愤怒等夸张卡通表情", "调校面部挤压拉伸时的脸颊与五官联动", "消除表情变形像气球充气变大或缩水消失的缺陷"],
        "keywords": ["面部表情", "Facial Expressions", "挤压与拉伸", "Squash and Stretch", "容积守恒", "Volume Conservation"],
        "also_read": ["dialogue-viseme-mouth-shapes", "exaggerated-takes-reactions"],
        "desc": "利用下颌铰链开合与五官连锁反应制作夸张面部表情，并严格执行挤压拉伸体积守恒。不适用于微表情写实电影。",
        "tags": ["cartoon", "expressions", "squash-and-stretch", "facial-animation"],
        "loc": "第 1 章，第 24–28 页"
    },
    {
        "slug": "cartoon-walk-types",
        "title": "经典卡通个性步态库",
        "importance": "critical",
        "importance_rationale": "好莱坞黄金时代角色性格步态宝库，涵盖潜行、昂首阔步、跳跃与标准喜剧走姿",
        "one_liner": "潜行步高抬膝盖脚尖轻点脚跟悬空，昂首阔步挺胸反弓高弹跳踢腿，跳跃步单脚双重连续点地起伏",
        "intents": ["制作角色鬼鬼祟祟的经典潜行步态 The Sneak", "设计骄傲霸道角色的昂首阔步 The Strut", "排布欢快童趣的跳跃步态 The Skip"],
        "keywords": ["卡通走姿", "The Sneak", "潜行步", "The Strut", "昂首阔步", "The Skip", "跳跃步", "性格步态"],
        "also_read": ["cartoon-run-locomotion", "animal-quadruped-cycles"],
        "desc": "排布经典好莱坞个性步态关键帧清单、重心起伏波形与脚部触地姿态。不适用于正规军队仪仗写实齐步走。",
        "tags": ["cartoon", "walk-cycles", "sneak", "strut", "locomotion"],
        "loc": "第 2 章，第 90–99 页"
    },
    {
        "slug": "cartoon-run-locomotion",
        "title": "卡通奔跑冲刺与飞轮腿残影",
        "importance": "high",
        "importance_rationale": "极速狂奔与喜剧逃跑的核心动效，解决高速步态视网膜脱节跳帧并营造风驰电掣速度感",
        "one_liner": "躯干低平前倾并带有大幅空中腾空期；超高速狂奔双腿合成旋转椭圆飞轮并拖出平行速度线",
        "intents": ["制作 4-6 帧高速奔跑与冲刺循环", "绘制经典飞轮腿 Wheel-leg 轮式旋转残影", "设计起跑原地打滑冒烟蓄力动效"],
        "keywords": ["卡通奔跑", "Cartoon Run", "飞轮腿", "Wheel leg", "速度线", "Speed lines", "腾空期", "冲刺逃跑"],
        "also_read": ["cartoon-walk-types", "animal-quadruped-cycles"],
        "desc": "构建身体低平前倾高速奔跑循环，并使用飞轮腿残影与速度线合成超音速狂奔。不适用于奥运短跑生理写实仿真。",
        "tags": ["cartoon", "run-cycles", "wheel-run", "dash", "speed-lines"],
        "loc": "第 2 章，第 100–105 页"
    },
    {
        "slug": "animal-quadruped-cycles",
        "title": "四足动物经典步态循环",
        "importance": "high",
        "importance_rationale": "马、犬、猫四足动物生物学解剖与行走、小跑、飞奔的经典手绘循环动画规范",
        "one_liner": "慢步严格遵循左后-左前-右后-右前四拍旋转顺序，小跑对角肢体同步，飞奔包含伸展与团身双重悬空期",
        "intents": ["制作马匹、猎犬、猫咪的四足行走步态", "调校马匹全速飞奔 Gallop 的脊椎伸展与团身双重腾空", "纠正四足动物左右顺拐与同侧肢体同步错误"],
        "keywords": ["四足动物", "Animal Locomotion", "马匹飞奔", "Gallop", "小跑", "Trot", "四拍慢步", "双重悬空"],
        "also_read": ["cartoon-walk-types", "wave-action-flexibility"],
        "desc": "根据四足动物解剖排布慢步四拍轮转、小跑对角线与马匹双悬空飞奔律表。不适用于爬行动物水平波状爬行。",
        "tags": ["cartoon", "animals", "quadruped", "horse-gallop", "dog-walk"],
        "loc": "第 2 章，第 106–126 页"
    },
    {
        "slug": "wave-action-flexibility",
        "title": "波浪运动与皮鞭鞭梢传递",
        "importance": "critical",
        "importance_rationale": "柔性多关节结构灵动运动的精髓，解决尾巴、皮鞭、丝带像硬木棍机械摆动的僵硬缺陷",
        "one_liner": "柔性链条逐级骨骼相对上一级产生 1-2 帧延迟滞后，在空间中形成 S 弯翻转并在末梢产生高速抽打过冲",
        "intents": ["制作动物尾巴、长发辫、丝带的柔性波浪运动", "调校皮鞭抽打的逐级延迟与末端过冲 Overshoot", "排查多关节次级动画全骨骼同步摆动的木棒失真"],
        "keywords": ["波浪运动", "Wave Action", "鞭梢效应", "Whip snap", "多级延迟", "S形弯曲", "过冲", "次级柔韧"],
        "also_read": ["animal-quadruped-cycles", "acting-poses-staging"],
        "desc": "利用骨骼层级阶梯时间偏移构建柔性链条 S 弯波动与末梢抽打动力学。不适用于高刚度金属杆或实心木棍。",
        "tags": ["cartoon", "wave-action", "flexibility", "whip-snap", "secondary-motion"],
        "loc": "第 3 章，第 140–145 页"
    },
    {
        "slug": "exaggerated-takes-reactions",
        "title": "卡通吃惊反应与 Double-Take",
        "importance": "critical",
        "importance_rationale": "好莱坞黄金时代最具标志性的喜剧表演核武器，以极致时序反差与悬停定格引爆笑点",
        "one_liner": "经历下蹲预备蓄力、1-2帧极速冲顶暴退、顶点8-12帧悬空定格发抖与回落的五阶段戏剧闭环",
        "intents": ["制作眼球暴突、下巴砸地的经典特克斯·艾弗里大 Take", "排布双重吃惊反应 Double-take 的呆滞中介定格时序", "消除吃惊反应平淡如水或无预备干拔瞬移的缺陷"],
        "keywords": ["吃惊反应", "The Take", "双重反应", "Double-Take", "眼球暴突", "Eye-pop", "下巴砸地", "悬空定格", "Shiver"],
        "also_read": ["facial-expressions-squash-stretch", "acting-poses-staging"],
        "desc": "按照五阶段闭环时序排布极度夸张的受惊、眼球暴突与双重反应定格。不适用于严肃写实正剧或真人实拍。",
        "tags": ["cartoon", "takes", "double-take", "comedy", "reactions"],
        "loc": "第 3 章，第 150–155 页"
    },
    {
        "slug": "dialogue-viseme-mouth-shapes",
        "title": "对白口型视素与身体重音",
        "importance": "high",
        "importance_rationale": "将语音音素转化为清晰嘴唇视素的标准工程系统，消除逐字母死板拼读与声画脱节",
        "one_liner": "抓取闭唇、咬唇、舌齿、宽狭元音等核心视素并提前发音1-2帧对准，身体动作在重音发音帧精准下击",
        "intents": ["根据录音音频扒波形制作角色对白口型", "映射标准英语/通用音素口型视素 Visemes", "排布角色讲话时的点头与手势身体重音 Body Accents"],
        "keywords": ["口型动画", "Lip-Sync", "视素", "Viseme", "音素", "Phonetics", "身体重音", "Body Accents", "声画对齐"],
        "also_read": ["facial-expressions-squash-stretch", "exposure-sheet-field-charts"],
        "desc": "依据核心音素视素表绘制对白口型形态，提前 1-2 帧对准声波并绑定肢体重音。不适用于超高语速饶舌逐字拼读。",
        "tags": ["cartoon", "dialogue", "lip-sync", "visemes", "speech"],
        "loc": "第 4 章，第 182–190 页"
    },
    {
        "slug": "acting-poses-staging",
        "title": "角色表演姿态与舞台调度",
        "importance": "high",
        "importance_rationale": "动画镜头视听叙事清晰度的最高准则，通过单一视觉焦点、动作弧线与视线向量掌控全局",
        "one_liner": "同一时刻仅保留一个主导动作，动作轨迹严格沿优美圆弧展开，眼神与手指精准引导观众视线穿透画面",
        "intents": ["规划镜头分镜中角色的舞台调度与表演节奏", "排布四肢摆动与转头的自然动作弧线 Arcs", "避免多角色同时抢戏造成的视觉信息混乱"],
        "keywords": ["舞台调度", "Staging", "表演姿态", "Acting", "动作弧线", "Arcs", "视线引导", "Eyeline", "单一焦点"],
        "also_read": ["line-of-action-rhythm", "exposure-sheet-field-charts"],
        "desc": "规划镜头单一视觉焦点、自然运动抛物弧线与角色眼球视线引导链条。不适用于特意制造信息混乱的大全景群戏。",
        "tags": ["cartoon", "staging", "acting", "arcs", "storytelling"],
        "loc": "第 3 章，第 136–139 页；第 5 章，第 204–212 页"
    },
    {
        "slug": "exposure-sheet-field-charts",
        "title": "摄影表设计与 Field 镜头规格",
        "importance": "medium",
        "importance_rationale": "动画工业生产与摄影台合成的技术调度中枢，规范 72 帧律表填写与 Field Chart 坐标运镜",
        "one_liner": "以 72 帧律表纵向排布对白、多图层画稿与运镜指令，利用 12-Field 网格精确控制平移背景速度与安全框",
        "intents": ["填写标准动画摄影表 Dope Sheet / Exposure Sheet", "使用 12-Field 网格换算摄影机平移 Pan 速度与刻度", "规划角色身体、口型、道具的分层绘制与合成对位"],
        "keywords": ["摄影表", "Exposure Sheet", "Dope Sheet", "律表", "规格框", "Field Chart", "12-Field", "背景平移", "Pan"],
        "also_read": ["dialogue-viseme-mouth-shapes", "model-sheet-uniformity"],
        "desc": "建立多图层层级对位规则与 72 帧标准律表工单，并在 Field 网格上精确计算运镜平移刻度。不适用自由3D无轨相机。",
        "tags": ["cartoon", "technical", "exposure-sheet", "field-chart", "production"],
        "loc": "第 5 章，第 196–215 页"
    },
    {
        "slug": "model-sheet-uniformity",
        "title": "标准造型表规范与多视角统一",
        "importance": "medium",
        "importance_rationale": "保障多人团队与外包协同制作不走形的技术蓝图，统筹三视图水平对齐与相对尺度对照",
        "one_liner": "在同一水平网格下绘制正面、3/4侧面、侧面与背面旋转图，附带裸体块透视解剖与角色间相对尺度对照表",
        "intents": ["制作标准角色造型表 Model Sheet 与三视图 Turnaround", "对齐多角度旋转下的头身比、五官与关节绝对水平高度", "制定角色造型美术规范防止团队协同绘制走形"],
        "keywords": ["标准造型表", "Model Sheet", "三视图", "Turnaround", "比例标尺", "网格对齐", "相对尺度", "造型统一"],
        "also_read": ["character-construction-proportions", "exposure-sheet-field-charts"],
        "desc": "绘制多视角水平对齐标准三视图、裸体块解剖结构与相对尺度对照表。不适用于个人自由变形流体艺术短片。",
        "tags": ["cartoon", "model-sheet", "turnaround", "character-design", "uniformity"],
        "loc": "第 5 章，第 216–224 页"
    }
]

capabilities = []
destinations_map = {}

for c in caps_data:
    cap_id = f"cap.cartoon.{c['slug']}"
    destinations_map[cap_id] = {"served_by": "cartoon-animation"}
    capabilities.append({
        "capability_id": cap_id,
        "revision": 1,
        "status": "active",
        "aliases": [],
        "supersedes": [],
        "merged_into": None,
        "split_into": [],
        "slug": c["slug"],
        "title": c["title"],
        "importance": c["importance"],
        "importance_rationale": c["importance_rationale"],
        "one_liner": c["one_liner"],
        "intents": c["intents"],
        "keywords": c["keywords"],
        "also_read": c["also_read"],
        "card": f"cards/{c['slug']}.md",
        "frontmatter": {
            "description": c["desc"],
            "tags": c["tags"]
        },
        "source_evidence": [{"source_id": "src-main-book", "location": c["loc"]}],
        "promotion": {
            "destination": "router",
            "gate": {
                "independent_intent": False,
                "independent_contract": True,
                "independent_run": True,
                "independent_reuse": False,
                "independent_eval": True
            },
            "notes": "Single 模式下归入主入口统一路由"
        }
    })

bundle = {
    "schema_version": 1,
    "bundle_id": "bundle.cartoon-animation",
    "book": {
        "title": "卡通动画制作",
        "source_pack": "books/cartoon-animation",
        "edition": "1st Edition",
        "authors": ["Preston Blair"],
        "year": 1994,
    },
    "entry": {
        "name": "cartoon-animation",
        "description": "经典卡通角色设计、个性步态、夸张表演与动画制作黄金法则工程手册。涵盖头身比与球形/梨形体块构建、单一动作线与剪影可读性、面部五官容积守恒挤压拉伸、经典卡通潜行步/阔步/跳跃步态库、飞轮腿极速狂奔残影、四足动物步态与马匹飞奔、多级骨骼波浪运动、经典特克斯·艾弗里吃惊反应与双重吃惊反应、标准对白口型音素视素与身体重音同步、镜头舞台调度与视线引导、摄影表 Dope Sheet 设计与标准造型表 Model Sheet 规范。",
        "core_principles": [
            "卡通角色由三维几何实心体块构建；以头长为单位标尺，梨形躯干大端在下提供稳固重心。",
            "每个姿态必须由单一主导动作线（Line of Action）贯通；纯黑剪影测试必须在 0.1 秒内清晰辨识动作。",
            "挤压与拉伸必须严格保持总体积（容积）恒定，严禁只拉长不收窄导致角色充气膨胀变形。",
            "波浪运动遵循多级骨骼逐级延迟传导，每一级关节产生 1-2 帧滞后，在空间中形成优雅 S 弯与末梢抽打过冲。",
            "吃惊反应（Take）必须遵循严格五阶段闭环：下蹲预备 ➔ 1-2帧极速冲顶暴退 ➔ 顶点8-12帧悬空定格发抖 ➔ 回落平复。",
            "对白口型绝非逐字母机械拼读，必须抓取核心音素视素并提前 1-2 帧对准声波，配合身体动作重音。"
        ],
        "out_of_scope": [
            "真人实拍写实电影长篇剧本文学写作与分镜头脚本台词创作",
            "写实解剖医学人体器官微观生理模拟与手术三维仿真",
            "纯非物理无重力意识流抽象实验美术色彩理论研究"
        ],
        "stop_conditions": [
            "用户仅咨询纯文本剧本创作或解剖医学图谱，不涉及卡通角色设计与动画运动时判停",
            "已输出明确的角色体块参数、个性步态时序律表或关键姿态动作线分析时判停"
        ]
    },
    "router_entry": {
        "name": "cartoon-animation",
        "description": "经典好莱坞卡通角色设计、性格步态、夸张表演与制作技术工程手册。提供头身比与体块构建、动作线与剪影测试、表情容积守恒、潜行步/昂首阔步/飞轮跑、四足步态、波浪运动、吃惊大 Take、对白口型视素与标准造型表设计支持。"
    },
    "promotion_budget": 8,
    "capabilities": capabilities
}

schemas_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\schemas")
registry = Registry()
for s in schemas_dir.glob("*.schema.json"):
    data = json.loads(s.read_text(encoding="utf-8"))
    res = Resource.from_contents(data)
    schema_id = data.get("$id", f"https://cangjie-skill.org/schemas/{s.name}")
    registry = registry.with_resource(schema_id, res)
    registry = registry.with_resource(f"https://cangjie-skill.org/schemas/{s.name}", res)

bundle_schema = json.loads((schemas_dir / "capability-bundle.schema.json").read_text(encoding="utf-8"))
validator = jsonschema.Draft202012Validator(bundle_schema, registry=registry)
validator.validate(instance=bundle)
print("Schema validation with offline registry: PASS 100%!")

out_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\cartoon-animation\.cangjie\capabilities\verified.yaml")
out_path.write_text(yaml.safe_dump(bundle, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
print(f"Written verified.yaml successfully: {out_path}")

dest_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\cartoon-animation\.cangjie\capabilities\destinations.json")
dest_path.write_text(json.dumps({
    "bundle_id": bundle["bundle_id"],
    "destinations": destinations_map
}, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated destinations.json successfully: {dest_path}")
