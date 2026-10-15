import yaml
import json
from pathlib import Path
import jsonschema
from referencing import Registry, Resource

caps_data = [
    {
        "slug": "horizon-line-psychology",
        "title": "视平线高度、仰俯视夹角与镜头心理学",
        "importance": "critical",
        "importance_rationale": "视觉叙事心理学绝对基准，极低视平线仰角神圣威权与极高视平线俯角脆弱审视支配受众投射",
        "one_liner": "以视平线垂直位置与仰角俯角掌控受众心理投射，确立压迫、主导或脆弱等核心情感基调",
        "intents": ["在故事板分镜中设定特定视平线高度与镜头俯仰角控制角色戏剧地位", "运用极低仰视机位赋予角色压倒性的力量感、神圣威严或恐怖压迫", "运用极高俯视全景传达角色的脆弱无助、受困绝望与全知视角审判"],
        "keywords": ["视平线", "Horizon Line", "视平高度", "Eye Level", "镜头心理学", "仰视", "Low Angle", "俯视", "High Angle", "荷兰角", "Dutch Angle"],
        "also_read": ["black-white-value-distribution", "dynamic-geometric-tension"],
        "desc": "以视平线高度与镜头俯仰角度控制受众心理地位与情感投射的镜头调度规程。不适用于无透视二维平涂矢量图标。",
        "tags": ["composition", "storyboard", "horizon-line", "camera-angles", "cinematography"],
        "loc": "Chapter 1 'Visual Narrative', pp. 12–25"
    },
    {
        "slug": "black-white-value-distribution",
        "title": "黑白纯明度分布、深沉暗调与剪影可读性",
        "importance": "critical",
        "importance_rationale": "构图剥离色彩后的坚固基石，60-30-10 黑白两极结构与纯黑逆光剪影 0.1 秒故事可读性",
        "one_liner": "确立 60-30-10 黑白两极明度结构，依托深黑硬边阴影与纯黑剪影实现 0.1 秒故事瞬间可读性",
        "intents": ["构建黑白分明的 60-30-10 黄金明度层级架构，杜绝 50% 中间灰泥潭陷阱", "将散碎阴影合并为连贯深沉的纯黑块面 (Connect the Shadows) 锚定空间重量", "提炼高反差逆光剪影 (Silhouettes) 确保角色动作与叙事焦点瞬间穿透视网膜"],
        "keywords": ["明度分布", "Value Distribution", "纯黑纯白", "Black and White", "剪影可读性", "Silhouette", "明暗层级", "反差"],
        "also_read": ["horizon-line-psychology", "chiaroscuro-lighting-mood"],
        "desc": "以 60-30-10 纯黑白两极明度大块面与逆光剪影构建坚不可摧视觉结构的构图法则。不适用于全彩无明度纯色谱分析。",
        "tags": ["composition", "value-structure", "black-and-white", "silhouette", "visual-design"],
        "loc": "Chapter 2 'Light and Shadow', pp. 28–49"
    },
    {
        "slug": "dynamic-geometric-tension",
        "title": "对角斜线、尖锐三角形与几何张力构图",
        "importance": "critical",
        "importance_rationale": "打破死板水平垂直网格，倾斜对角线破坏重力平衡注入疾速动能，锐角三角形构建侵略性力场",
        "one_liner": "打破横平竖直呆板网格，运用倾斜对角线与锐角三角形在画面中注入失衡动能与危险悬念",
        "intents": ["在构图中布局对角倾斜斜线与 X 交叉对撞线注入强烈的位移动量与冲突感", "运用正倒三角形与锋利锐角构建具有方向侵略性与不稳定性的几何力场", "排查平庸的九十度直角网格导致的画面呆滞死寂与动作软弱无力缺陷"],
        "keywords": ["对角斜线", "Diagonals", "几何张力", "Geometric Tension", "锐角三角形", "Triangles", "动态能量", "失衡"],
        "also_read": ["horizon-line-psychology", "eye-leading-focal-paths"],
        "desc": "运用对角斜线与尖锐三角形打破引力平衡、构建冲突动能与侵略性力场的几何构图工程。不适用于静物对称轴测图。",
        "tags": ["composition", "geometry", "diagonals", "triangles", "visual-tension"],
        "loc": "Chapter 4 'Composing the Shot & Geometry', pp. 78–105"
    },
    {
        "slug": "eye-leading-focal-paths",
        "title": "环境线条引导、视线牵引与黄金焦点流线",
        "importance": "critical",
        "importance_rationale": "无形视觉导流铁轨，阴影边缘、地表透视与角色视线 0.1 秒精准牵引瞳孔命中核心叙事靶点",
        "one_liner": "利用阴影边缘、地表透视反光与角色视线构建连续导流轨道，将瞳孔在 0.1 秒内牵引至核心叙事靶点",
        "intents": ["在构图中布设物理透视线与明暗交界硬边作为视觉铁轨牵引观者瞳孔移动", "利用角色注视目光与指示性手势构建次级视线发射箭头 (Joint Attention)", "杜绝死胡同废线与多重高反差焦点打架，确保第一视觉入口与终极靶心明晰"],
        "keywords": ["视线引导", "Leading Lines", "焦点流线", "Focal Path", "视觉导流", "明暗交界", "视线牵引", "Eye-Tracking"],
        "also_read": ["dynamic-geometric-tension", "three-layer-spatial-depth"],
        "desc": "以环境线条、阴影边界与角色目光构建无形轨道精准控制受众注意力流向的导流工程。不适用于纯散点漫游装饰壁纸。",
        "tags": ["composition", "leading-lines", "focal-points", "visual-guidance", "storytelling"],
        "loc": "Chapter 4 'Composing the Shot & Geometry', pp. 78–105"
    },
    {
        "slug": "three-layer-spatial-depth",
        "title": "前景压迫、中景叙事与远景空气纵深",
        "importance": "critical",
        "importance_rationale": "刺穿二维画框的三维纵深幻觉，前景深暗框架压迫、中景核心交互与远景大气透视衰减",
        "one_liner": "以前景暗部框架制造代入与压迫感，中景展开角色冲突，远景大气透视制造无垠空间纵深",
        "intents": ["构建前景、中景、远景严格分层的三维纵深空间结构 (3-Layer Depth Engine)", "运用画中画框架 (Framing within a Frame) 与前景纯黑剪影制造沉浸代入感", "应用大气透视 (Atmospheric Perspective) 阶梯式衰减远景明度与对比度拉开深远距离"],
        "keywords": ["空间纵深", "Spatial Depth", "前景框架", "Foreground", "中景舞台", "Midground", "远景空气透视", "Background", "画中画"],
        "also_read": ["eye-leading-focal-paths", "lens-perspective-wide-vs-telephoto"],
        "desc": "以物理重叠遮挡、前景框架压迫与远景空气对比度衰减构建三维纵深幻象的工程规程。不适用于单层二维拼贴剪纸。",
        "tags": ["composition", "spatial-depth", "foreground", "midground", "background", "depth-cues"],
        "loc": "Chapter 3 'The Illusion of Depth', pp. 52–75"
    },
    {
        "slug": "aspect-ratio-framing-psychology",
        "title": "画幅比例、银幕宽高比与画框心理压迫",
        "importance": "high",
        "importance_rationale": "对现实的第一道暴力戏剧裁剪，4:3 垂直幽闭、16:9 经典平衡与 2.39:1 宽银幕史诗对峙心理学",
        "one_liner": "驾驭 4:3 幽闭压迫、16:9 经典平衡与 2.39:1 宽银幕宏大对峙，让画框边缘成为强有力的叙事施压者",
        "intents": ["根据剧本冲突维度（垂直禁锢 vs 水平广袤）选择最适配的银幕宽高比 (Aspect Ratio)", "在 1.33:1 封闭画框中运用逼仄空间与头顶下巴裁切强化窒息囚禁心理", "在 2.39:1 宽银幕中运用多重子框架 (Sub-Framing) 与大跨度水平负空间构建对峙"],
        "keywords": ["画幅比例", "Aspect Ratio", "银幕宽高比", "画框心理学", "Framing", "宽银幕", "Cinemascope", "幽闭感"],
        "also_read": ["horizon-line-psychology", "negative-space-graphic-economy"],
        "desc": "依据不同银幕宽高比的空间场域属性控制戏剧压迫感与自适应构图的画框工程。不适用于无边界无画框沉浸VR全景。",
        "tags": ["composition", "aspect-ratio", "framing", "cinematography", "psychology"],
        "loc": "Chapter 1 'Visual Narrative', pp. 12–25"
    },
    {
        "slug": "visual-continuity-eye-trace",
        "title": "分镜头连续视线轨迹守恒与剪辑流线",
        "importance": "critical",
        "importance_rationale": "故事板连贯流动的神经纽带，画格切换瞳孔落点平滑滑动，180° 轴线守恒与动作动量对撞",
        "one_liner": "在画格切换间维持受众瞳孔物理落点平滑滑动，严格遵循 180° 动作轴线守恒与视觉动量对撞",
        "intents": ["执行视线轨迹守恒 (Eye-Trace Continuity) 确保画格切换瞬间受众瞳孔零寻找成本", "严格遵守 180° 动作轴线规则与视线反打匹配 (Eyeline Match) 杜绝空间方位错乱", "在动作剪辑点 (Cutting on Action) 利用上一镜头的位移矢量惯性平滑掩盖剪辑痕迹"],
        "keywords": ["视线轨迹守恒", "Eye-Trace", "分镜连续性", "Visual Continuity", "180度轴线", "Axis Rule", "剪辑流线", "视线匹配"],
        "also_read": ["storyboard-cadence-editorial-flow", "eye-leading-focal-paths"],
        "desc": "在连续故事板画格切换中维持受众视线轨迹平滑流动与空间轴线严密守恒的电影语法规程。不适用于单幅孤立概念插图。",
        "tags": ["storyboard", "continuity", "eye-trace", "editing", "film-grammar"],
        "loc": "Chapter 6 'Continuity, Flow & Editorial Cadence', pp. 106–125"
    },
    {
        "slug": "chiaroscuro-lighting-mood",
        "title": "明暗对照法、戏剧光斑与光影情感基调",
        "importance": "critical",
        "importance_rationale": "用光芒雕刻阴影的悬念艺术，单一主光源锐利几何光斑，顶光审判、底光诡谲与侧光内心交战",
        "one_liner": "运用极度深沉阴影与锐利切割光斑雕刻形态，顶光审判、底光诡谲与侧光分裂的情感基调控制",
        "intents": ["运用卡拉瓦乔式明暗对照法 (Chiaroscuro) 建立单一主光源与高戏剧张力光影", "通过顶光 (Top Light) 刻画审判宿命，通过底光 (Under Light) 刻画恶魔诡异反派气场", "用伦勃朗三角光斑与锐利明暗分界线 (Terminator) 塑造角色双重人格与道德挣扎"],
        "keywords": ["明暗对照法", "Chiaroscuro", "戏剧布光", "Dramatic Lighting", "光斑雕刻", "顶光", "底光", "伦勃朗光", "情感基调"],
        "also_read": ["black-white-value-distribution", "scale-contrast-dominance"],
        "desc": "以极端单一光源、锐利明暗交界面与大面积未知暗部雕刻戏剧悬念与心理情绪的光影工程。不适用于工业平光无影照。",
        "tags": ["lighting", "chiaroscuro", "mood", "light-and-shadow", "cinematography"],
        "loc": "Chapter 3 'Light, Shadow & Chiaroscuro', pp. 28–49"
    },
    {
        "slug": "scale-contrast-dominance",
        "title": "尺度悬殊对比、环境吞噬与角色威严霸气",
        "importance": "high",
        "importance_rationale": "画框内相对比例对撞产生的心理威慑，5% 渺小个体对抗 95% 浩瀚吞噬环境呈现宇宙级戏剧性",
        "one_liner": "以 5% 渺小个体对抗 95% 浩瀚吞噬环境，或以前景庞然大物衬托远景微小猎物制造绝对支配",
        "intents": ["在单张画框内构建 1:20 甚至 1:50 的悬殊尺度对比展现个体的极端脆弱与被吞噬感", "以前景大特写局部（巨兽下颌、战靴）压迫远景渺小角色展现绝对支配权 (Dominance)", "在宏大庞大异星建筑身旁布置人体参考尺度标尺锚定受众空间宏伟感知"],
        "keywords": ["尺度对比", "Scale Contrast", "环境吞噬", "Dominance", "脆弱感", "Vulnerability", "威严压迫", "宏大叙事"],
        "also_read": ["three-layer-spatial-depth", "lens-perspective-wide-vs-telephoto"],
        "desc": "利用主体与环境或对手之间的极端悬殊比例差异制造压倒性心理支配力与史诗感的构图法则。不适用于等比例标准零件测绘。",
        "tags": ["composition", "scale", "contrast", "dominance", "environment"],
        "loc": "Chapter 4 'Composing the Shot & Geometry', pp. 78–105"
    },
    {
        "slug": "lens-perspective-wide-vs-telephoto",
        "title": "广角透视冲击 vs 长焦空间压缩窒息感",
        "importance": "high",
        "importance_rationale": "操纵三维空间与时间的透视魔法，广角拉伸 Z 轴强化冲击速度，长焦前后压缩贴合制造窒息绝望",
        "one_liner": "广角拉伸纵深距离强化冲撞爆发与孤立疏离，长焦压缩空间让追击者紧贴猎物制造窒息绝望",
        "intents": ["选用广角镜头 (14mm-24mm) 夸张近大远小对比，使武器肢体冲向前景产生破屏爆发力", "选用长焦镜头 (85mm-150mm) 压缩前后景物物理距离 (Spatial Compression) 制造无路可逃压迫", "依据追逐、对决与心理独白等不同戏剧需求匹配最精准的光学透视焦距心理学"],
        "keywords": ["镜头焦距", "Focal Length", "广角镜头", "Wide Angle", "长焦镜头", "Telephoto", "空间压缩", "Compression", "透视冲击"],
        "also_read": ["three-layer-spatial-depth", "scale-contrast-dominance"],
        "desc": "运用广角拉伸冲击与长焦压缩空间景深操纵心理距离与动作张力的虚拟摄影机透视工程。不适用于正交平行投影制图。",
        "tags": ["cinematography", "lenses", "perspective", "wide-angle", "telephoto"],
        "loc": "Chapter 5 'Perspective, Lenses & Depth', pp. 52–75"
    },
    {
        "slug": "negative-space-graphic-economy",
        "title": "留白力量、纯粹极简与负空间引力场",
        "importance": "high",
        "importance_rationale": "掌握减法的勇气，70%-80% 连贯负空间释放深沉心理引力，剔除视觉噪音赋予叙事纯粹重力",
        "one_liner": "以大面积空旷留白释放深沉心理引力，无情剔除视觉杂质，赋予叙事纯粹而锋利的情感重力",
        "intents": ["执行 40% 构图减法清理，无情剔除对剧情冲突无贡献的繁复背景杂线与装饰排线", "布局占据画面 70% 以上的大面积纯黑或纯白负空间海洋 (Negative Space)", "将孤立角色逼至画框极限边缘角落，利用负空间的巨大引力场制造绝境压迫与呼吸感"],
        "keywords": ["负空间", "Negative Space", "留白力量", "极简明晰", "Graphic Economy", "空间引力", "减法艺术", "呼吸感"],
        "also_read": ["black-white-value-distribution", "aspect-ratio-framing-psychology"],
        "desc": "以大面积连贯负空间与极度节制线条构建心理引力场与纯粹戏剧重量的极简构图工程。不适用于巴洛克式密集繁复雕花装饰。",
        "tags": ["composition", "negative-space", "simplicity", "minimalism", "graphic-design"],
        "loc": "Chapter 4 'Composing the Shot & Geometry', pp. 78–105"
    },
    {
        "slug": "storyboard-cadence-editorial-flow",
        "title": "故事板节拍编排、景别交替与动作分镜流水线",
        "importance": "critical",
        "importance_rationale": "分镜头动作连环动态交响诗，建立、中景推进与特写爆破景别阶梯交替，波浪式戏剧节奏编排",
        "one_liner": "全景建立、中景推进与特写爆破的戏剧节拍交替，编排具有电影呼吸感的动作故事板流水线",
        "intents": ["将剧本文字拆解为设定、推进、转折、爆发与余震等标准故事板节拍 (Beats)", "编排大远景 -> 中景 -> 大特写的波浪式景别交替阶梯，杜绝同一景别连续重复", "在动作爆发顶点执行切分 (Cutting on Action)，标注运镜指示与对白音效工业规范"],
        "keywords": ["故事板节拍", "Storyboard Cadence", "景别层级", "Shot Scale", "动作分镜", "Action Flow", "运镜指示", "电影呼吸"],
        "also_read": ["visual-continuity-eye-trace", "horizon-line-psychology"],
        "desc": "涵盖景别阶梯交替、剧本动作切分与影视运镜规范的故事板工业级分镜编排规程。不适用于静态单格概念插画。",
        "tags": ["storyboard", "cadence", "shot-hierarchy", "action-flow", "editorial"],
        "loc": "Chapter 6 'Continuity, Flow & Editorial Cadence', pp. 106–125"
    }
]

destinations_map = {}
capabilities = []

for c in caps_data:
    cid = f"cap.framed-ink.{c['slug']}"
    destinations_map[cid] = {
        "target_pack_slug": "framed-ink",
        "target_skill_slug": "framed-ink",
        "action": "create"
    }
    
    capabilities.append({
        "capability_id": cid,
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
    "bundle_id": "bundle.framed-ink",
    "book": {
        "title": "分镜构图圣经：墨水构图 (Framed Ink: Drawing and Composition for Visual Storytellers)",
        "source_pack": "books/framed-ink",
        "edition": "1st Edition",
        "authors": ["Marcos Mateu-Mestre"],
        "year": 2010,
    },
    "entry": {
        "name": "framed-ink",
        "description": "好莱坞概念设计、影视分镜 (Storyboard) 与视觉叙事 (Visual Storytelling) 殿堂级工程手册。涵盖极低仰视威权与极高俯视脆弱审视之视平线心理学 (Horizon Line & Eye Level)、60-30-10 黑白两极纯明度分布与逆光纯黑剪影 (Value Structure & Silhouettes)、对角斜线撕裂平衡与尖锐三角形侵略力场 (Diagonals & Geometric Tension)、环境透视与阴影边界 0.1 秒视线牵引铁轨 (Eye Leading Lines & Focal Paths)、前景深暗框架遮挡中景叙事远景大气透视之三层空间纵深 (3-Layer Spatial Depth)、4:3 幽闭压迫与 2.39:1 宽银幕宏大对峙画幅心理学 (Aspect Ratios & Framing)、画格切换受众瞳孔落点平滑滑动与 180° 轴线守恒 (Visual Continuity & Eye-Trace)、单一主光源切割几何光斑与顶光审判/底光诡谲之明暗对照法 (Chiaroscuro & Mood)、5% 渺小个体对抗 95% 浩瀚环境吞噬之尺度悬殊对比 (Scale Contrast & Dominance)、广角拉伸纵深爆发与长焦空间压缩窒息感 (Lens Perspective: Wide vs. Telephoto)、70% 连贯负空间深沉引力场与 40% 构图减法清理 (Negative Space & Graphic Economy)、全景建立中景推进特写爆破之故事板动作分镜节拍流水线 (Storyboard Cadence & Editorial Flow) 电影级构图规范。",
        "core_principles": [
            "构图的首要职责是支配情绪：画框不仅是物理边界，更是心理压迫的容器。视平线的高度直接裁定角色的戏剧权力地位（低视平线仰角神圣威权，高视平线俯角脆弱受审）。",
            "黑白明度结构是一切好构图的底座：剥离色彩后画面必须依靠 60% 主导调、30% 结构调与 10% 焦点爆破点严密立足，逆光纯黑剪影是 0.1 秒故事传达的第一利刃。",
            "对角线与三角形是动能的几何化身：水平线代表死寂与安宁，倾斜对角线破坏重力平衡注入下坠做功速度，尖锐锐角三角形如同箭头直刺戏剧靶心。",
            "环境中的每一根线条都是视觉铁轨：利用阴影边缘、地表反光与角色目光构建闭环导流轨道，将观者瞳孔在 0.1 秒内精准牵引至核心叙事焦点，消灭死胡同杂线。",
            "三维纵深必须被物理刺穿：前景纯黑框架提供偷窥代入感，中景展开核心搏杀，远景通过大气透视阶梯式衰减对比度推开无垠空间。",
            "故事板的核心生命力在于视线轨迹守恒（Eye-Trace Continuity）：画格 A 结束时的视觉聚焦点必须与画格 B 切入的第一冲击点物理坐标重合或同向滑动，严禁越过 180° 轴线跳轴。",
            "掌握减法的勇气：负空间不是虚无空白，而是充满情感重力的心理海洋。用 40% 减法剔除一切无关杂乱细节，让大面积留白与极端尺度对比释放出史诗级的戏剧震撼。"
        ],
        "out_of_scope": [
            "纯医学内窥镜显微组织病理学影像记录",
            "工业机械数控刀具走刀路径 CAM 编程切削",
            "静态纯商业无故事性条形码与标签排版设计"
        ],
        "stop_conditions": [
            "用户仅咨询机械数控刀路或商业标签排版，不涉及影视分镜、构图设计、镜头心理学与视觉叙事时判停",
            "已输出明确的视平线心理参数、黑白明度分布方案、视线引导轨道、三层纵深架构、镜头焦距选择或故事板节拍编排时判停"
        ]
    },
    "router_entry": {
        "name": "framed-ink",
        "description": "马科斯·马特乌-梅斯特墨水构图视觉叙事与故事板工程手册。提供视平线高度与镜头心理学、60-30-10黑白明度与剪影、对角线与三角形几何张力、环境线条引导与视线铁轨、前景中景远景三层纵深、银幕画幅宽高比心理压迫、分镜头连续视线轨迹守恒、明暗对照法戏剧布光、环境尺度悬殊对比、广角长焦透视心理学、负空间留白力场与故事板动作分镜流水线工程支持。"
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

out_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\framed-ink\.cangjie\capabilities\verified.yaml")
out_path.write_text(yaml.safe_dump(bundle, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
print(f"Written verified.yaml successfully: {out_path}")

dest_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\framed-ink\.cangjie\capabilities\destinations.json")
dest_path.write_text(json.dumps({
    "bundle_id": bundle["bundle_id"],
    "destinations": destinations_map
}, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated destinations.json successfully: {dest_path}")
