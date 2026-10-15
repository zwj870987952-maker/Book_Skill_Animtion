import yaml
import json
import hashlib
from pathlib import Path
import jsonschema
from referencing import Registry, Resource

caps_data = [
    {
        "slug": "viseme-ortho-matrix",
        "title": "口型正交解耦与视素矩阵",
        "importance": "critical",
        "importance_rationale": "口型动画基石，将发音空间降维解耦为开合与宽窄正交轴，从根本上杜绝全脸目标体叠加冲突",
        "one_liner": "将发音口型在笛卡尔坐标系中正交解耦为开合 (Open/Closed) 与宽窄 (Wide/Narrow) 核心坐标，辅以接触辅音与视素发音动力学",
        "intents": ["设计无冲突的口型动画目标体系统", "将语音音标转换为三维角色口型状态矢量", "解决多音素连续发音时的嘴角穿插冲突"],
        "keywords": ["视素", "Viseme", "开合轴", "Open-Closed", "宽窄轴", "Wide-Narrow", "正交矩阵", "Orthogonal"],
        "also_read": ["lip-sync-pipeline", "slider-interface-driver-rig"],
        "desc": "基于 Jason Osipa 正交双轴系统，将发音口型解耦为开合与宽窄坐标。不适用于全自动黑盒音频深度学习直驱模型。",
        "tags": ["facial", "lip-sync", "viseme", "blendshape"],
        "loc": "第 1 章与第 4 章，第 3–20 页与第 47–74 页"
    },
    {
        "slug": "lip-sync-pipeline",
        "title": "工业级对白口型动画流水线",
        "importance": "critical",
        "importance_rationale": "消除口型按帧乱调与抽搐混乱的工业生产规程，确立开合、宽窄、硬接触与细调四步法及视错觉超前量法则",
        "one_liner": "按开合主干、宽窄过渡、硬接触帧锁定、细调与 2-4 帧视错觉超前量补偿的四步流水线制作对白动画",
        "intents": ["制作长段角色台词对白口型动画", "排查口型滞后于声音的视听不同步缺陷", "规范口型关键帧的分层打标流程"],
        "keywords": ["口型流水线", "Lip Sync", "超前量", "Advance Rule", "分层动画", "接触辅音", "MBP", "FV"],
        "also_read": ["viseme-ortho-matrix", "blink-dynamics-thought-break"],
        "desc": "工业级对白口型分层四步制作法与视错觉超前量补偿。不适用于无口型纯肢体哑剧表演。",
        "tags": ["facial", "animation", "lip-sync", "workflow"],
        "loc": "第 4 章与第 14 章，第 47–74 页与第 311–344 页"
    },
    {
        "slug": "facial-edge-flow-topology",
        "title": "面部环形循环布线与形变拓扑",
        "importance": "critical",
        "importance_rationale": "面部网格几何骨架，同心环形布线保障极限表情形变下的光影连续性与曲率平滑度，杜绝三角面破面伪影",
        "one_liner": "沿口轮匝肌、眼轮匝肌和八字鼻唇沟构建同心四边形循环边流，将五星极点隔离至平坦骨骼区",
        "intents": ["构建支持高精度面部形变的三维头部拓扑", "排查嘴角与眼周在拉伸时的光影撕裂缺陷", "布置眼口鼻三大表情区域的同心环形布线"],
        "keywords": ["边流", "Edge Flow", "同心环", "Loops", "口轮匝肌", "眼轮匝肌", "鼻唇沟", "极点隔离"],
        "also_read": ["additive-blendshape-math", "mouth-cavity-teeth-tongue"],
        "desc": "基于肌肉收缩方向的面部环形循环边流与极点拓扑规范。不适用于硬表面机械面具或非生物刚体模型。",
        "tags": ["facial", "modeling", "topology", "edge-flow"],
        "loc": "第 5、8、10 章，第 75–100、177–192、227–242 页"
    },
    {
        "slug": "additive-blendshape-math",
        "title": "无冲突加算目标体与权重渐变算法",
        "importance": "critical",
        "importance_rationale": "表情绑定数学核心，差分加算架构与余弦空间平滑衰减算法杜绝全脸混合形叠加冲突，实现完美左右分离",
        "one_liner": "以纯净差分矢量构建加算目标体，并通过 ss2_blend_taper 余弦空间平滑衰减实现对称目标体的无缝左右解耦",
        "intents": ["编写表情绑定目标体的差分权重计算脚本", "将对称雕刻的完整表情拆分为独立的左右半脸目标体", "消除微笑与张嘴同时激活时的顶点超调撕裂"],
        "keywords": ["加算目标体", "Additive Blendshapes", "差分矢量", "Delta", "余弦衰减", "Taper", "中线分离"],
        "also_read": ["facial-edge-flow-topology", "slider-interface-driver-rig"],
        "desc": "差分矢量加算目标体架构与空间余弦衰减渐变算法。不适用于骨骼蒙皮独占的刚体机械绑定。",
        "tags": ["facial", "rigging", "blendshape", "math"],
        "loc": "第 6 章，第 101–146 页"
    },
    {
        "slug": "mouth-cavity-teeth-tongue",
        "title": "口腔结构工程：牙弓与舌头多段变形",
        "importance": "high",
        "importance_rationale": "消灭口腔内廉价感与穿帮，构建抛物线牙弓、刚体上下颌铰链对齐与舌尖多段形变系统",
        "one_liner": "构建抛物线牙弓与上颅/下颌刚体铰链，搭配舌根、舌身、舌尖三段变形体与暗色遮光口腔壁",
        "intents": ["绑定三维角色牙齿与下巴旋转关节", "制作舌头在发 L/TH/S 音时的卷曲变形", "构建暗色防漏光的封闭口腔壁几何体"],
        "keywords": ["牙弓", "Dental Arch", "下颌铰链", "Jaw Joint", "舌头三段变形", "Tongue Rig", "口腔壁"],
        "also_read": ["viseme-ortho-matrix", "facial-edge-flow-topology"],
        "desc": "解剖学抛物线牙弓、颌骨铰链对齐与舌头三段变形体工程。不适用于无牙齿舌头的抽象低模角色。",
        "tags": ["facial", "anatomy", "teeth", "tongue"],
        "loc": "第 5 章，第 75–100 页"
    },
    {
        "slug": "brow-emotion-mechanics",
        "title": "眉毛三轴情绪解剖学与形态构建",
        "importance": "high",
        "importance_rationale": "面部复杂微表情发生器，将眉毛解耦为内眉、外眉与眉心挤压三轴，联动额头横纵表情折痕",
        "one_liner": "将左眉与右眉分别解耦为内眉升降、外眉升降与眉心聚拢挤压三轴，联动前额高精动态折痕贴图",
        "intents": ["设计表达悲伤、惊讶、狂怒或怀疑的眉毛形态", "绑定单侧独立挑眉与眉心纵向皱纹挤压", "解决双眉聚拢时的中线顶点相撞穿插"],
        "keywords": ["眉毛解耦", "Inner Brow", "Outer Brow", "眉心挤压", "Brow Squeeze", "额头折痕", "Wrinkle Maps"],
        "also_read": ["eyelid-expression-tension", "slider-interface-driver-rig"],
        "desc": "内眉/外眉升降与眉心聚拢三轴解耦运动控制及额头折痕联动。不适用于无眉毛平滑生物体。",
        "tags": ["facial", "acting", "eyebrows", "emotion"],
        "loc": "第 2 章与第 9 章，第 21–30 页与第 193–224 页"
    },
    {
        "slug": "eyelid-expression-tension",
        "title": "上下眼睑情绪张力与注视感知",
        "importance": "high",
        "importance_rationale": "眼神灵魂核心，确立上眼睑主导警觉与清醒度、下眼睑主导心理紧张与真笑挤压的解耦控制法则",
        "one_liner": "以上眼睑控制角膜露白标尺表达警觉与清醒，以下眼睑水平紧绷与隆起表达心理张力与真笑挤压",
        "intents": ["制作真笑时的眼周微表情挤压 (Duchenne Smile)", "调配狐疑、蔑视、惊恐等细微眼神状态", "校准摄影机视角下的角膜高光与真实注视线偏差"],
        "keywords": ["上眼睑", "Upper Lid", "下眼睑", "Lower Lid", "真笑挤压", "Squint", "视线感知", "Eyeline"],
        "also_read": ["brow-emotion-mechanics", "eye-rig-lid-follow-saccades"],
        "desc": "上眼睑主导警觉与生理清醒、下眼睑主导心理张力与真笑挤压的解耦控制。不适用于无眼睑外凸眼球。",
        "tags": ["facial", "acting", "eyelids", "gaze"],
        "loc": "第 2 章与第 7 章，第 21–30 页与第 149–176 页"
    },
    {
        "slug": "eye-rig-lid-follow-saccades",
        "title": "眼球追踪眼睑跟随与扫视跳跃绑定",
        "importance": "critical",
        "importance_rationale": "根治三维死鱼眼与假面具感，结合眼睑自动联动跟随算法与 1 帧眼动扫视微跳机制",
        "one_liner": "眼球俯仰时上眼睑以 25%-35% 比例自动随动跟随，眼球注视点在 1 帧内瞬时扫视跳跃到位并定格",
        "intents": ["构建眼球 Aim 约束与眼睑自动跟随联动网络", "制作自然生动、拒绝平滑漂移的眼球注视动画", "消除眼球向下看时露白严重的死鱼眼穿帮"],
        "keywords": ["眼球追踪", "Eye Aim", "眼睑跟随", "Lid Follow", "扫视", "Saccades", "视线微跳", "Eye Darts"],
        "also_read": ["eyelid-expression-tension", "blink-dynamics-thought-break"],
        "desc": "眼球 Aim 约束追踪、眼睑联动随动算法与 1 帧眼动扫视微跳机制。不适用于复眼昆虫或机械传感器镜头。",
        "tags": ["facial", "rigging", "animation", "eyes"],
        "loc": "第 7 章与第 11 章，第 149–176 页与第 243–264 页"
    },
    {
        "slug": "blink-dynamics-thought-break",
        "title": "眨眼动力学与思维顿悟阻断机制",
        "importance": "high",
        "importance_rationale": "面部表演的呼吸感与标点符号，确立非对称极速闭合时序与思维转折/视线跳跃同步法则",
        "one_liner": "眨眼采用 2 帧极速下落与 4-5 帧慢出回弹的非对称曲线，并作为思维顿悟与视线跳跃的节点顿挫编排",
        "intents": ["制作富有呼吸感与生命力的自然眨眼动画", "在角色思考、下定决心或视线转移节点编排眨眼", "排查机械对称节拍器眨眼的动画缺陷"],
        "keywords": ["眨眼动力学", "Blink Timing", "非对称曲线", "思维句号", "Mental Punctuation", "视线同步"],
        "also_read": ["eye-rig-lid-follow-saccades", "lip-sync-pipeline"],
        "desc": "非对称极速闭合动力学时序与思维转换/视线跳跃节点顿挫编排。不适用于机械无睫毛摄像头。",
        "tags": ["facial", "animation", "blink", "acting"],
        "loc": "第 7 章，第 149–176 页"
    },
    {
        "slug": "zipper-lips-sticky-rig",
        "title": "拉链嘴唇渐进粘连绑定",
        "importance": "high",
        "importance_rationale": "赋予嘴唇逼真黏膜弹性，基于成对顶点距离阈值衰减实现嘴角由内向外逐级剥离的拉链效果",
        "one_liner": "通过嘴角内外侧成对顶点距离阈值衰减网络，实现微张嘴时嘴角粘连、由内向外渐进分离的拉链力学",
        "intents": ["绑定逼真的写实嘴角黏膜粘连效果", "解决角色微张嘴说话时嘴角边缘呈现生硬折角的缺陷", "构建单侧独立撇嘴粘连控制网络"],
        "keywords": ["拉链唇", "Zipper Lips", "嘴角粘连", "Sticky Lips", "距离衰减", "Distance Remap"],
        "also_read": ["viseme-ortho-matrix", "facial-edge-flow-topology"],
        "desc": "基于嘴角成对顶点距离阈值衰减的拉链式渐进剥离粘连绑定。不适用于鸟类硬喙或无唇结构。",
        "tags": ["facial", "rigging", "lips", "sticky"],
        "loc": "第 11 章，第 243–264 页"
    },
    {
        "slug": "slider-interface-driver-rig",
        "title": "二维滑块面部控制器界面与驱动键约束",
        "importance": "critical",
        "importance_rationale": "解放动画师生产力的直觉控制面板，以带边界限制的 2D Box 控制器手柄阻断非法形状组合",
        "one_liner": "在 2D Box 正方形平面内映射正交面部自由度，通过位移边界物理阻断非法组合并以线性驱动键输出",
        "intents": ["搭建直观高效的 Osipa 风格 2D 面部控制面板", "使用 Set Driven Key (SDK) 连接控制器与底层目标体", "限制控制器位移范围以避免非法目标体超调破面"],
        "keywords": ["二维滑块", "2D Slider", "控制面板", "Interface", "驱动键", "Set Driven Key", "边界限制"],
        "also_read": ["viseme-ortho-matrix", "brow-emotion-mechanics"],
        "desc": "2D Box 平面手柄滑块控制器、归一化位移映射与 Set Driven Key 正交驱动拓扑。不适用于纯物理模拟面部驱动。",
        "tags": ["facial", "rigging", "ui", "controller"],
        "loc": "第 12 章，第 265–288 页"
    },
    {
        "slug": "squoosh-head-squash-stretch",
        "title": "头部整体 Squoosh 挤压拉伸多层变形绑定",
        "importance": "high",
        "importance_rationale": "解决局部微表情与全局卡通拉伸的兼容冲突，通过分层变形链与平方根反比保持体积守恒",
        "one_liner": "将局部表情目标体与全局头部 Squoosh 晶格解耦分层，沿纵向挤压拉伸时依平方根反比补偿横向体积守恒",
        "intents": ["为角色头部添加夸张的卡通挤压拉伸变形器", "保证头部剧烈形变时面部微表情与口型仍可正常播放", "计算头颅挤压拉伸时的横向体积守恒补偿因子"],
        "keywords": ["Squoosh", "挤压拉伸", "Squash and Stretch", "分层变形", "晶格绑定", "Lattice", "体积守恒"],
        "also_read": ["additive-blendshape-math", "slider-interface-driver-rig"],
        "desc": "局部表情目标体与全局头部 Squoosh 分层解耦架构与体积守恒公式。不适用于刚性机械头盔。",
        "tags": ["facial", "rigging", "deformation", "squash-stretch"],
        "loc": "第 13 章，第 289–310 页"
    }
]

capabilities = []
destinations_map = {}

for c in caps_data:
    cap_id = f"cap.stop-staring.{c['slug']}"
    destinations_map[cap_id] = {"served_by": "stop-staring"}
    
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
    "bundle_id": "bundle.stop-staring",
    "book": {
        "title": "面部建模与动画表情绑定：Stop Staring 实战精粹",
        "source_pack": "books/stop-staring",
        "edition": "2nd/3rd Edition",
        "authors": ["Jason Osipa"],
        "year": 2007,
    },
    "entry": {
        "name": "stop-staring",
        "description": "三维角色面部建模、表情绑定、对白口型与眼神演技工业级工程手册。涵盖 Osipa 视素双轴正交解耦（开合 vs 宽窄）、分层四步对白流水线与 2-4 帧超前量、口轮眼轮匝肌同心环循环布线与五星极点隔离、差分加算目标体架构与 ss2_blend_taper 余弦衰减、抛物线牙弓与舌头三段变形、内眉外眉挤压三轴解耦与额头动态折痕、上下眼睑张力解耦与角膜露白标尺、眼球追踪眼睑跟随算法与 1 帧扫视跳跃、非对称极速闭合眨眼动力学与思维顿悟同步、拉链嘴唇渐进粘连绑定、带边界限制的 2D Box 面部滑块控制器界面设计、头部整体 Squoosh 挤压拉伸多层变形分层与体积守恒算法。",
        "core_principles": [
            "发音口型在笛卡尔坐标系中正交解耦为开合 (Open/Closed) 与宽窄 (Wide/Narrow)，杜绝全脸字母混合形叠加冲突。",
            "对白口型严格遵循分层四步法；关键辅音接触（MBP 闭唇、FV 咬唇）必须提前 2-4 帧闭合以补偿视觉感知超前量。",
            "面部拓扑严格服从口轮匝肌与眼轮匝肌同心环形边流（Edge Loops），五星极点严禁落在形变边缘与折痕处。",
            "目标体仅记录差分矢量（Delta）；对称分离应用余弦平滑衰减，在中线严格满足 W_L + W_R ≡ 1.0 互补守恒律。",
            "上眼睑主导生理清醒度与警觉，下眼睑主导心理张力与真笑挤压（Squint）；眼球上下旋转必须带动上眼睑 25%-35% 联动跟随。",
            "眼球转动遵循 1 帧扫视跳跃（Saccades）并保持定格；眨眼作为思维句号与视线跳跃同步，采用 2 帧极速下落与 4-5 帧慢出回弹。",
            "局部表情目标体与全局头部 Squoosh 挤压拉伸解耦分层，横向缩放严格按纵向缩放平方根反比维持三维体积守恒。"
        ],
        "out_of_scope": [
            "真人实拍写实电影文学剧本台词剧本文学创作",
            "医学头面部神经外科微观解剖手术仿真",
            "纯非生物刚体机械金属外壳硬表面零件数控加工编程"
        ],
        "stop_conditions": [
            "用户仅咨询纯文本剧本创作或解剖医学手术，不涉及角色面部建模、表情绑定与动画时判停",
            "已输出明确的面部拓扑布线规范、2D 控制器映射参数、口型对白时序律表或加算目标体算法时判停"
        ]
    },
    "router_entry": {
        "name": "stop-staring",
        "description": "三维角色面部建模、表情绑定、对白口型与眼神表演工业级工程手册。提供视素双轴正交解耦、四步口型流水线、同心环拓扑布线、加算目标体余弦衰减、牙弓与三段舌、眼眉情绪三轴、眼睑跟随与 1 帧扫视微跳、思维阻断眨眼、拉链唇粘连、2D 滑块界面与 Squoosh 体积守恒绑定支持。"
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

out_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\stop-staring\.cangjie\capabilities\verified.yaml")
out_path.write_text(yaml.safe_dump(bundle, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
print(f"Written verified.yaml successfully: {out_path}")

dest_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\stop-staring\.cangjie\capabilities\destinations.json")
dest_path.write_text(json.dumps({
    "bundle_id": bundle["bundle_id"],
    "destinations": destinations_map
}, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated destinations.json successfully: {dest_path}")
