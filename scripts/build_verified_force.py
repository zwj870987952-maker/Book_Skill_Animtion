import yaml
import json
from pathlib import Path
import jsonschema
from referencing import Registry, Resource

caps_data = [
    {
        "slug": "directional-applied-force",
        "title": "方向力与施加力物理学",
        "importance": "critical",
        "importance_rationale": "动态速写动力学核心，区分主导推进流与碰撞转向支点，赋予线条明确的能量矢量",
        "one_liner": "分析重力与动能矢量分解，以方向力构建滑行推进，遇骨骼支点转化为施加力碰撞反弹转向",
        "intents": ["分析人体动态姿态中的受力矢量分布", "定位骨骼支点上的施加力碰撞点", "排查线条软弱无方向的被动描摹问题"],
        "keywords": ["方向力", "Directional Force", "施加力", "Applied Force", "受力矢量", "重力对抗", "能量流"],
        "also_read": ["force-rhythm-rollercoaster", "opposing-curves-torso"],
        "desc": "基于重力与动能矢量分解的方向力与施加力力学分析。不适用于静止刚体无机物透视排线。",
        "tags": ["drawing", "force", "physics", "dynamics"],
        "loc": "第 1 章，第 18–34 页"
    },
    {
        "slug": "force-rhythm-rollercoaster",
        "title": "力量节奏与过山车动能法则",
        "importance": "critical",
        "importance_rationale": "贯穿全身体态的动能闭环，运用滑雪跳台比喻实现能量从凸面到对侧凹面的连续反弹",
        "one_liner": "运用滑雪跳台比喻引导动能从一侧凸面连续顺滑反弹至对侧凹面，构建无间断的过山车能量闭环",
        "intents": ["构建全身贯通的动能流线与节奏", "排查肢体脱节散架的速写缺陷", "应用滑雪跳台比喻绘制连贯的身体动能线"],
        "keywords": ["力量节奏", "Force Rhythm", "过山车", "Roller Coaster", "滑雪跳台", "Ski Slope", "能量闭环"],
        "also_read": ["directional-applied-force", "straight-vs-curved-shapes"],
        "desc": "基于滑雪跳台比喻的动能对角反弹与连续过山车节奏法则。不适用于静止机械零件几何拆解。",
        "tags": ["drawing", "force", "rhythm", "flow"],
        "loc": "第 1 章，第 34–50 页"
    },
    {
        "slug": "opposing-curves-torso",
        "title": "躯干对抗曲线与胸腔骨盆反向扭转",
        "importance": "critical",
        "importance_rationale": "人体全身动力学核心引擎，胸腔与骨盆的反向倾斜与对抗扭矩确立全身动态姿态基石",
        "one_liner": "以楔形对立模型构建胸腔与骨盆的反向倾斜与扭矩对抗，形成挤压侧肉褶与拉伸侧长直线的张力对立",
        "intents": ["设计充满动能与扭矩张力的躯干姿态", "平衡胸腔与骨盆在运动中的反向倾斜夹角", "刻画腹部挤压与后背拉伸的楔形对立"],
        "keywords": ["胸腔骨盆对抗", "Counter-Torque", "反向倾斜", "Counter-Tilt", "挤压拉伸", "Squash-Stretch", "楔形模型"],
        "also_read": ["directional-applied-force", "wrapping-lines-cross-contour"],
        "desc": "胸腔与骨盆两大质量中心的对立扭转与反向倾斜力学。不适用于无脊椎软体流体造型。",
        "tags": ["drawing", "torso", "counter-torque", "anatomy"],
        "loc": "第 2 章，第 52–78 页"
    },
    {
        "slug": "wrapping-lines-cross-contour",
        "title": "环绕包裹线与三维透视进深",
        "importance": "critical",
        "importance_rationale": "二维平面构建三维容积的核心工具，以带有视平线朝向的横截面包裹线赋予形体厚度与深度",
        "one_liner": "利用带有明确视平线俯仰朝向的横截面环绕包裹线，在二维纸面上赋予形态以三维体积与空间厚度",
        "intents": ["在速写中快速建立肢体的三维空间进深感", "用环绕线表现四肢与躯干的圆柱体透视朝向", "处理剧烈透视缩短 (Foreshortening) 下的肢体叠压"],
        "keywords": ["环绕包裹线", "Wrapping Lines", "截面线", "Cross-Contour", "透视缩短", "Foreshortening", "空间体积"],
        "also_read": ["opposing-curves-torso", "straight-vs-curved-shapes"],
        "desc": "基于视平线朝向的横截面环绕包裹线与空间体块构建。不适用于纯平面极简扁平矢量图设计。",
        "tags": ["drawing", "form", "cross-contour", "perspective"],
        "loc": "第 2 章，第 60–85 页"
    },
    {
        "slug": "straight-vs-curved-shapes",
        "title": "直线对抗曲线造型美学",
        "importance": "critical",
        "importance_rationale": "打破死板对称的黄金造型法则，以支撑骨骼直线对抗发力肌肉曲线，驱使视觉流速飞驰",
        "one_liner": "支撑与张力侧使用刚劲直线，施力与肌肉膨胀侧使用饱满曲线，杜绝充气香肠双曲面对称",
        "intents": ["设计具备骨骼支撑感与发力张力的四肢外形", "消除人体四肢对称圆弧导致的充气香肠病", "运用直曲对立引导观众视线沿特定矢量飞速流动"],
        "keywords": ["直线对抗曲线", "Straight vs Curved", "对称破除", "骨骼支撑", "动能跑道", "形状美学"],
        "also_read": ["asymmetry-law-of-thirds", "force-rhythm-rollercoaster"],
        "desc": "支撑直线与发力饱满曲线的对立造型法则。不适用于完全对称的机械几何图纸绘制。",
        "tags": ["drawing", "shape", "design", "aesthetics"],
        "loc": "第 3 章，第 96–118 页"
    },
    {
        "slug": "asymmetry-law-of-thirds",
        "title": "黄金不对称性与三分结构法则",
        "importance": "high",
        "importance_rationale": "赋予线条动态加速度与明确方向性，将弧顶锁定在 1/3 或 2/3 处以打破 50% 几何死板",
        "one_liner": "将力量曲线最高凸起顶点锁定在 1/3 或 2/3 处，打破 50% 几何对称以制造强烈的推力加速度",
        "intents": ["赋予线条鲜明的推进方向与速度感", "排查弧顶位于 50% 中点导致的软弱无力曲线", "布局大腿、小腿与前臂的不对称肌肉顶点"],
        "keywords": ["三分法则", "Law of Thirds", "不对称性", "Asymmetry", "弧顶定位", "Apex", "加速度"],
        "also_read": ["straight-vs-curved-shapes", "line-texture-pencil-pressure"],
        "desc": "基于三分定律的曲线不对称弧顶定位与加速度控制。不适用于工业规整抛物线函数放样。",
        "tags": ["drawing", "shape", "asymmetry", "dynamics"],
        "loc": "第 3 章，第 104–124 页"
    },
    {
        "slug": "silhouette-negative-space",
        "title": "力量剪影与负空间力场",
        "importance": "high",
        "importance_rationale": "瞬间传达角色意图与戏剧张力，通过 0.1 秒黑剪影测试与负空间锐角三角形构建舞台力场",
        "one_liner": "以 0.1 秒纯黑剪影测试检验动作瞬间可读性，利用肢体间负空间锐角三角形构建充满压力的力场气场",
        "intents": ["优化角色姿态的外轮廓剪影瞬间可读性", "利用肢体间的负空间三角形强化戏剧张力", "排查肢体并拢粘连导致的泥泞混乱剪影缺陷"],
        "keywords": ["剪影", "Silhouette", "负空间", "Negative Space", "瞬间可读性", "力场三角形", "舞台调度"],
        "also_read": ["acting-drama-storytelling-pose", "straight-vs-curved-shapes"],
        "desc": "纯黑剪影可读性检验与几何负空间力场设计。不适用于微距局部五官特写。",
        "tags": ["drawing", "silhouette", "staging", "composition"],
        "loc": "第 3 章，第 124–138 页"
    },
    {
        "slug": "fabric-drape-folds-mechanics",
        "title": "服装布料重力悬挂与七类衣褶动力学",
        "importance": "high",
        "importance_rationale": "解密服装因重力下拉与骨骼支撑产生的折痕力学，掌握管状、半圆、螺旋等七大经典衣褶",
        "one_liner": "解析骨骼支撑点与重力下拉对布料的作用，运用七大经典衣褶力学精准表现服装的悬挂与运动张力",
        "intents": ["绘制符合重力与人体发力规律的真实服装衣褶", "识别管状褶、半圆褶、螺旋褶与之字褶的受力机理", "排查衣服表面无序碎乱折痕的画法缺陷"],
        "keywords": ["衣褶力学", "Fabric Folds", "管状褶", "Pipe", "半圆褶", "Swag", "螺旋褶", "Spiral", "重力悬挂"],
        "also_read": ["wrapping-lines-cross-contour", "line-texture-pencil-pressure"],
        "desc": "基于骨骼支撑点与重力牵引的七大衣褶动力学工程。不适用于无织物裸体解剖素描。",
        "tags": ["drawing", "clothing", "fabric", "folds"],
        "loc": "第 4 章，第 140–178 页"
    },
    {
        "slug": "quick-sketch-reportage",
        "title": "极限生活速写与叙事瞬间捕捉",
        "importance": "critical",
        "importance_rationale": "将速写从画室推向真实世界的实战心法，用 4-5 根主力量线在 5-30 秒内冻结鲜活生命叙事",
        "one_liner": "运用 5 秒骨架抓捕法与 30 秒叙事速写流，以极简主力量线在移动环境中捕捉真实生活的人情味与戏剧瞬间",
        "intents": ["在地铁、街头等移动场景下进行 5-30 秒极限极速速写", "用 3 到 4 笔快速确立移动中人物的重心骨架", "捕捉日常生活中人物的真实人情味与叙事情境"],
        "keywords": ["极速速写", "Quick Sketch", "现场纪实", "Reportage", "5秒抓形", "人情味", "Humanity"],
        "also_read": ["acting-drama-storytelling-pose", "directional-applied-force"],
        "desc": "5秒至30秒现场纪实速写流程与故事性瞬间抓捕。不适用于数小时精细写实超写实素描。",
        "tags": ["drawing", "sketching", "life-drawing", "reportage"],
        "loc": "第 5 章，第 180–208 页"
    },
    {
        "slug": "human-animal-comparative-force",
        "title": "人兽同源比较解剖与力量传递",
        "importance": "high",
        "importance_rationale": "破除动物画法神秘感，运用哺乳动物骨骼同源映射（手腕与飞节）打通四足动物力量过山车流",
        "one_liner": "依据哺乳动物骨骼同源性映射前膝与后飞节力学，打通后肢引擎到脊椎波浪再至前肢缓冲的动物力量流",
        "intents": ["掌握猫科、犬科与马科动物的骨骼同源解剖映射", "绘制充满爆发力与弹性的猛兽潜行与飞跃姿态", "排查四足动物前后关节弯折方向画反的严重错误"],
        "keywords": ["比较解剖", "Comparative Anatomy", "四足动物", "Quadrupeds", "飞节", "Hock", "腕关节", "脊椎波浪"],
        "also_read": ["directional-applied-force", "force-rhythm-rollercoaster"],
        "desc": "哺乳动物骨骼同源映射与四足动物力量传导分析。不适用于节肢昆虫或水生软体动物速写。",
        "tags": ["drawing", "animals", "quadrupeds", "anatomy"],
        "loc": "第 6 章，第 210–244 页"
    },
    {
        "slug": "line-texture-pencil-pressure",
        "title": "线条质感与运笔压力动力学",
        "importance": "high",
        "importance_rationale": "笔触即动能的记录仪，以大臂肩膀联动发力，通过运笔速度与深浅压感直接传达物理重量与速度",
        "one_liner": "以大臂与肩膀联动驱动长线，通过运笔速度与压感粗细变化实时映射人体内部重力与动能强弱",
        "intents": ["消除手腕手指作画导致的碎短发丝线与毛刺", "训练 40 厘米以上超长顺滑力量曲线的运笔发力法", "通过线条压感粗细对比传达肢体沉重感与轻盈感"],
        "keywords": ["线条质感", "Line Texture", "运笔压感", "Pencil Pressure", "大臂发力", "发丝线破除", "线条速度"],
        "also_read": ["directional-applied-force", "asymmetry-law-of-thirds"],
        "desc": "基于全身发力链的运笔速度、压感与线条肌理动力学。不适用于计算机辅助矢量直线钢笔勾边。",
        "tags": ["drawing", "technique", "line-weight", "pressure"],
        "loc": "第 1 章与第 4 章，第 24 页与第 140–146 页"
    },
    {
        "slug": "acting-drama-storytelling-pose",
        "title": "肢体表演戏剧性与情感主张构图",
        "importance": "critical",
        "importance_rationale": "速写的灵魂与导演主张，运用金字塔层级法确立第一核心意图，以 120%-150% 戏剧夸张让画作震耳欲聋",
        "one_liner": "遵循金字塔层级理论自顶向下提炼核心意图，以 120%-150% 主观戏剧夸张赋予每一根线条鲜明主张",
        "intents": ["为动画关键帧姿态注入强烈的情感故事与戏剧张力", "应用金字塔层级理论自顶向下排布作画优先级", "进行 120%-150% 的主观主张夸张以摆脱平庸照抄"],
        "keywords": ["戏剧性", "Drama", "金字塔层级", "Hierarchy Pyramid", "主观夸张", "Exaggeration", "表演主张"],
        "also_read": ["silhouette-negative-space", "quick-sketch-reportage"],
        "desc": "基于金字塔层级法的情感意图提炼与戏剧性主张夸张。不适用于医学解剖客观测量拓片。",
        "tags": ["drawing", "acting", "storytelling", "drama"],
        "loc": "前言与第 5 章，第 8–15 页与第 180–208 页"
    }
]

capabilities = []
destinations_map = {}

for c in caps_data:
    cap_id = f"cap.force-life-drawing.{c['slug']}"
    destinations_map[cap_id] = {"served_by": "force-life-drawing"}
    
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
    "bundle_id": "bundle.force-life-drawing",
    "book": {
        "title": "动画师力量动态速写：Force 动态人体与生命律动工程手册",
        "source_pack": "books/force-life-drawing",
        "edition": "2nd Edition",
        "authors": ["Mike Mattesi"],
        "year": 2006,
    },
    "entry": {
        "name": "force-life-drawing",
        "description": "动画角色设计、动态人体速写、力量流线与生命律动工程手册。涵盖方向力与施加力物理学、力量节奏过山车滑雪跳台比喻、躯干对抗曲线与胸腔骨盆反向扭转、环绕包裹线三维透视厚度、直线对抗曲线造型美学、黄金不对称性三分法则、纯黑剪影瞬间可读性与几何负空间力场、布料重力悬挂与七大经典衣褶力学、5-30秒极限现场纪实速写、哺乳动物骨骼同源解剖与四足力量传递、大臂肩膀运笔压力质感动力学、金字塔层级理论自顶向下意图提炼与 120%-150% 主观戏剧夸张法则。",
        "core_principles": [
            "永远画穿透形态的物理力量（Energy with Purpose），严禁毫无意识地描摹外轮廓边缘线。",
            "严禁在肢体两侧对称使用外凸圆弧（充气香肠病）；必须遵循直线对抗曲线（Straight vs Curved），支撑侧为长直线，施力侧为饱满弧。",
            "能量永不停止；顺应滑雪跳台（Ski Slope）惯性，能量从一侧凸面连续顺滑反弹至对侧凹面，形成闭环过山车力量节奏。",
            "胸腔与骨盆两大核心体块在空间中永远对立，一侧发生极限挤压（Squash），对侧必然产生极限拉伸（Stretch），反向扭转维持力矩平衡。",
            "力量曲线的最高凸起顶点必须锁定在 1/3 或 2/3 处（三分法则），打破 50% 几何对称，提供强烈的推进加速度。",
            "利用带有明确视平线俯仰朝向的横截面环绕包裹线（Wrapping Lines），在二维平面上直接确立三维厚度与空间进深。",
            "遵循金字塔层级理论（The Hierarchy Pyramid），宏观核心戏剧故事第一，主力量线第二，三维结构第三，细节最末；主观戏剧夸张 120%-150%。"
        ],
        "out_of_scope": [
            "纯医学人体神经外科手术切片微观组织学仿真",
            "工业刚体数控车床零件机械工程蓝图制图",
            "纯非生物无重力静止几何透视排线测绘"
        ],
        "stop_conditions": [
            "用户仅咨询纯医学手术解剖或工业数控零件制图，不涉及角色动态速写、力量线条与姿态设计时判停",
            "已输出明确的力量流线分析、直曲对抗造型指导、衣褶力学归类或 5-30 秒速写执行方案时判停"
        ]
    },
    "router_entry": {
        "name": "force-life-drawing",
        "description": "动画师力量动态速写与生命律动工程手册。提供方向力与施加力分析、过山车节奏滑雪跳台流、胸腔骨盆对抗扭转、环绕包裹线进深、直曲对抗造型、三分法则不对称、黑剪影与负空间、七大衣褶力学、5-30秒极限速写、人兽同源解剖、线条压感动力学与金字塔戏剧夸张指导支持。"
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

out_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-life-drawing\.cangjie\capabilities\verified.yaml")
out_path.write_text(yaml.safe_dump(bundle, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
print(f"Written verified.yaml successfully: {out_path}")

dest_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-life-drawing\.cangjie\capabilities\destinations.json")
dest_path.write_text(json.dumps({
    "bundle_id": bundle["bundle_id"],
    "destinations": destinations_map
}, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated destinations.json successfully: {dest_path}")
