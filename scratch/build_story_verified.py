import yaml
import os

capabilities_raw = [
    {
        "slug": "story-structure-and-three-act-architecture",
        "title": "经典故事结构与三幕式建筑力学（三幕八序列时序标尺与中点危机）",
        "one_liner": "悉德·菲尔德范式、经典三幕八序列时序标尺、情节点与中点危机攻守反转。",
        "keywords": ["story-structure", "three-act-paradigm", "plot-points", "midpoint-crisis", "eight-sequences", "inciting-incident"],
        "also_read": ["pacing-crisis-climax-and-resolution", "scene-design-and-conflict-beats"],
        "requirements": [
            "全片严格确立激励事件（第10-12页）、情节点I（第25-30页）、中点危机（第55-60页）与情节点II（第85-90页）标准时序标尺",
            "中点必须发生决定性攻守逆转（假胜利或假失败）并启动不可逆的倒计时时钟（Ticking Clock）",
            "八序列结构必须各自具备独立次级戏剧悬念与序列高潮，形成波浪递进阶梯"
        ],
        "antirequirements": [
            "严禁第1幕拖沓至30页以上才发生激励事件导致故事慢启动死机",
            "严禁第二幕中段缺乏中点翻转导致剧情泥潭塌陷、行动原地打转"
        ]
    },
    {
        "slug": "controlling-idea-and-thematic-truth",
        "title": "主导论题与哲学核心确立（价值冲突极性对抗与反论辩证矩阵）",
        "one_liner": "罗伯特·麦基主导论题、价值对抗极性、正论反论合论辩证矩阵与高潮验证。",
        "keywords": ["controlling-idea", "thematic-truth", "core-value", "counter-idea", "dialectic-matrix", "moral-premise"],
        "also_read": ["character-arc-and-inner-flaw", "antagonist-and-forces-of-antagonism"],
        "requirements": [
            "主导论题必须由单一核心价值（Cause）与最终胜出的核心结果（Effect）构成严密因果命题",
            "全剧必须构建正论（Idea）与反论（Counter-Idea）势均力敌的辩证交锋矩阵",
            "终极高潮必须以主角在生死抉择中的物理行动直接验证哲学真理，而非口号宣讲"
        ],
        "antirequirements": [
            "严禁编剧把故事变成直白廉价的说教布道与单一正义口号灌输",
            "严禁正义方全知全能无缺陷、反派降智沦为脸谱化恶棍导致辩证交锋失衡"
        ]
    },
    {
        "slug": "character-arc-and-inner-flaw",
        "title": "人物弧光与致命内在缺陷（非典型主角欲望三角与蜕变顿悟）",
        "one_liner": "外在目标Want与内在需求Need撕裂、致命缺陷、幽灵创伤与高潮顿悟涅槃。",
        "keywords": ["character-arc", "inner-flaw", "want-vs-need", "ghost-wound", "epiphany", "character-dimension"],
        "also_read": ["controlling-idea-and-thematic-truth", "antagonist-and-forces-of-antagonism"],
        "requirements": [
            "主角必须存在显性欲望（Want）与深层内在精神需求（Need）的根本性撕裂与错位",
            "致命缺陷必须由过去的童年/历史心理创伤（The Ghost / Wound）驱动，具有自我保护与自毁双重性",
            "灵魂暗夜（All Hope Is Lost）必须促成核心顿悟（Epiphany），舍弃虚妄Want拥抱Need完成蜕变"
        ],
        "antirequirements": [
            "严禁塑造毫无内在缺陷、道德完美无瑕、开局即巅峰的玛丽苏/扁平纸片人",
            "严禁主角人物弧光缺乏外部重大代价与痛苦牺牲直接无痛顿悟"
        ]
    },
    {
        "slug": "scene-design-and-conflict-beats",
        "title": "场景设计与戏剧冲突节拍（场景价值极性翻转与三层对抗断层）",
        "one_liner": "场景微观力学、开场至结尾价值正负极翻转、内心/个人/环境三层对抗断层。",
        "keywords": ["scene-design", "conflict-beats", "polarity-turn", "gap-in-reality", "text-and-subtext", "beat-progression"],
        "also_read": ["dialogue-subtext-and-exposition-delivery", "pacing-crisis-climax-and-resolution"],
        "requirements": [
            "每个场景必须以特定价值状态入场，并经历突发鸿沟（Gap）以完全相反或剧变的极性出场（+/- 翻转）",
            "场景冲突必须交织内心（Inner）、人际（Personal）与外部环境（Extra-personal）三层对抗网络",
            "严格遵循晚进早出（Late In, Early Out）法则，坚决切除无实质冲突的寒暄废戏"
        ],
        "antirequirements": [
            "严禁出现场景结尾价值状态与开头毫无变化、纯粹为了交代信息的零价值垃圾场景",
            "严禁角色行动总是完全符合预期，缺乏现实残酷反弹产生的戏剧断层"
        ]
    },
    {
        "slug": "dialogue-subtext-and-exposition-delivery",
        "title": "对白潜台词与背景信息解耦（冰山理论言外之意与信息炸药法则）",
        "one_liner": "海明威冰山理论、台词与行动解耦、潜台词言外之意与背景信息戏剧化投放。",
        "keywords": ["dialogue-subtext", "iceberg-theory", "exposition-delivery", "unfilmables", "talking-heads", "dramatic-ammo"],
        "also_read": ["scene-design-and-conflict-beats", "screenplay-formatting-and-action-lines"],
        "requirements": [
            "台词必须呈现表面文本（Text）与深层欲望/谎言/潜台词（Subtext）的二元错位",
            "背景信息（Exposition）只能转化为冲突中的弹药，在角色的极端生死交锋中被逼说出",
            "严格执行遮名测试，确保每个角色拥有独特的语言词汇库、语速节奏与思维方式"
        ],
        "antirequirements": [
            "严禁“正如你所知（As you know, Bob）”式直白向观众交代世界观背景的解释性对白",
            "严禁所有角色台词千人一面、口吻与编剧自身完全一致（Talking Heads）"
        ]
    },
    {
        "slug": "antagonist-and-forces-of-antagonism",
        "title": "反派力量与对抗阻力矩阵（自洽正义反派与四级矛盾升级网络）",
        "one_liner": "自洽正义反派、罗伯特·麦基四级对抗方阵（矛盾-对立-否定之否定）、智商在线。",
        "keywords": ["antagonist", "forces-of-antagonism", "antagonism-square", "credible-threat", "villain-motivation", "dialectic-opposition"],
        "also_read": ["character-arc-and-inner-flaw", "controlling-idea-and-thematic-truth"],
        "requirements": [
            "反派在其自身世界观内必须是拯救者与正义主角，具备极高自洽逻辑与无可辩驳的情感支撑",
            "反派的智谋、力量与资源储备必须始终压制主角30%以上，逼迫主角调用全部潜能",
            "对抗力量必须沿“矛盾（Contradictory）→ 对立（Contrary）→ 否定之否定（Negation of Negation）”四级方阵递进升级"
        ],
        "antirequirements": [
            "严禁塑造毫无动机单纯为了邪恶而邪恶的脸谱化降智反派",
            "严禁反派在绝境中突发愚蠢失误或心慈手软让主角不劳而获翻盘"
        ]
    },
    {
        "slug": "animation-screenplay-and-visual-gag",
        "title": "动画剧本特化语法与视觉笑料设计（物理喜剧Visual Gag与高密度动作）",
        "one_liner": "动画媒介语法特化、纯视觉优先Show Don't Tell、四步视觉笑料与动物拟人逻辑。",
        "keywords": ["animation-screenplay", "visual-gag", "slapstick-comedy", "anthropomorphism", "action-density", "cartoon-logic"],
        "also_read": ["animation-series-bible-and-pitching", "scene-design-and-conflict-beats"],
        "requirements": [
            "动画剧本台词必须极度精简，将叙事重心全力押注于肢体语言、微表情变形与物理奇观",
            "视觉笑料必须严格遵循“铺垫常识→期待加剧→荒诞现实反转→反应与复原”四步力学闭环",
            "拟人化动物或物体必须严格遵守其自然生物物理特性与人类心智的辩证结合"
        ],
        "antirequirements": [
            "严禁把动画剧本写成两个角色原地站立纯聊天的真人长镜头文戏",
            "严禁笑料缺乏逻辑前置铺垫与现实反转，沦为毫无由来的低级恶搞与胡闹"
        ]
    },
    {
        "slug": "pacing-crisis-climax-and-resolution",
        "title": "节奏张力危机高潮与结局闭环（两难道德危机绝境与终极不可逆高潮）",
        "one_liner": "最佳坏选择/不可兼得双难危机、终极高潮不可逆转性、叙事闭环与余波余韵。",
        "keywords": ["dramatic-pacing", "crisis-dilemma", "climax-execution", "irreversible-resolution", "two-irreconcilable-goods", "catharsis"],
        "also_read": ["story-structure-and-three-act-architecture", "controlling-idea-and-thematic-truth"],
        "requirements": [
            "危机（Crisis）必须设计为“不可兼得的两种善”或“两害相权取其轻”的极限两难道德抉择",
            "终极高潮必须以角色的物理核心抉择引爆，彻底摧毁旧世界并带来不可逆的生命重构",
            "结局（Resolution）必须干脆利落收束伏笔，展现新秩序稳定态并给予观众深刻情感宣泄（Catharsis）"
        ],
        "antirequirements": [
            "严禁设计主角既能拯救世界又能保全自身利益的零代价廉价大团圆",
            "严禁在高潮后拖沓冗长交代琐事，导致观众情感宣泄后注意力迅速流失"
        ]
    },
    {
        "slug": "sub-plot-and-character-ensemble",
        "title": "支线副线交织与群像角色网络（次要情节回响主旨与群像网状互动）",
        "one_liner": "A线主情节与B/C副线呼吸交织、副线对主旨的多角度辩证回响、群像功能矩阵。",
        "keywords": ["sub-plots", "character-ensemble", "b-story", "thematic-echo", "dramatic-contrast", "ensemble-dynamics"],
        "also_read": ["story-structure-and-three-act-architecture", "character-arc-and-inner-flaw"],
        "requirements": [
            "支线（B-Story / C-Story）必须紧扣核心主题，从不同极端切面为主导论题提供镜像反思或对照",
            "群像角色必须各自承担明确戏剧职能（导师、弄臣、怀疑者、镜子）且拥有互斥性格极端",
            "副线情节在高潮前必须与主线发生物理合流，成为推动主线危机突破的关键催化剂"
        ],
        "antirequirements": [
            "严禁插入与主线核心命题毫无关联、纯粹为了凑时长的碎片化琐碎支线",
            "严禁群像角色职能重叠、性格雷同导致读者对角色产生严重混淆"
        ]
    },
    {
        "slug": "screenplay-formatting-and-action-lines",
        "title": "剧本标准工业格式与动作行写作法则（好莱坞排版、留白艺术与运镜禁忌）",
        "one_liner": "Courier 12pt好莱坞工业施工图纸规范、动作行Whitespace留白艺术、强动词与消灭We See。",
        "keywords": ["screenplay-formatting", "action-lines", "whitespace-rule", "sluglines", "unfilmables", "camera-directions"],
        "also_read": ["dialogue-subtext-and-exposition-delivery", "screenplay-troubleshooting-and-rewrite-doctor"],
        "requirements": [
            "严格遵循好莱坞工业标准格式（场景标题Slugline全大写、页边距排版、1页对应1分钟）",
            "动作行遵循留白法则（Whitespace Rule），每段不超过3-4行，使用强动词现在进行时",
            "坚决杜绝“不可拍摄内容”（Unfilmables）与越俎代庖的运镜指令（Camera Directions/We See）"
        ],
        "antirequirements": [
            "严禁出现连续8-10行密不透风的大黑砖文字块（Wall of Text）阻塞阅读节奏",
            "严禁在动作行中长篇大论描写角色不可拍摄的内心独白、历史回忆与未表现心理"
        ]
    },
    {
        "slug": "animation-series-bible-and-pitching",
        "title": "动画剧集项目企划圣经制作与商业提案工程（Show Bible、Logline与商业提案）",
        "one_liner": "动画企划圣经七大工业模块、黄金Logline公式、剧集产生引擎与商业提案答辩策略。",
        "keywords": ["show-bible", "pitch-bible", "logline-formula", "episode-generator", "pitch-meeting", "animation-franchise"],
        "also_read": ["animation-screenplay-and-visual-gag", "screenplay-troubleshooting-and-rewrite-doctor"],
        "requirements": [
            "企划圣经必须完整覆盖高概念Logline、目标受众画像、世界观法则、角色群像档案与剧集产生引擎",
            "一句话故事梗概（Logline）必须严格包含缺陷主角、突发激励、外在目标、对立阻力与失败赌注五要素",
            "商业提案答辩必须在前90秒内完成高能抓人（Hook），并明确玩具衍生品与生产预算控制方案"
        ],
        "antirequirements": [
            "严禁前20页陷入庞杂的世界观历史年表（Lore Dump）而迟迟不展现核心角色与故事冲突",
            "严禁提出只能拍一集短片、缺乏稳定剧集产生机制（Episode Generator）的单薄概念"
        ]
    },
    {
        "slug": "screenplay-troubleshooting-and-rewrite-doctor",
        "title": "剧本医生系统诊断与重写重构外科手术（七大病灶排查与四轮重写流水线）",
        "one_liner": "好莱坞剧本医生诊断清单、被动主角/中段塌陷/机械降神切除、晚进早出与四轮重写流水线。",
        "keywords": ["script-doctor", "screenplay-rewrite", "passive-protagonist", "sagging-second-act", "deus-ex-machina", "four-pass-pipeline"],
        "also_read": ["story-structure-and-three-act-architecture", "scene-design-and-conflict-beats"],
        "requirements": [
            "对照七大病灶清单无情排查（慢启动、被动主角、第二幕塌陷、机械降神、同声千人一面、零价值场景）",
            "巧合事件只能用于将主角推入绝境，严禁使用任何机械降神与外界巧合解脱危机",
            "重写必须遵循“骨架重构→角色弧光→场景张力→台词抛光”四轮降维外科手术流水线"
        ],
        "antirequirements": [
            "严禁允许主角充当被动旁观者被环境推着走，情节推进必须源自主角主动作出的极限冒险选择",
            "严禁场景包含冗长无用的寒暄进门与客套出门，坚决晚进早出（Late in, early out）"
        ]
    }
]

capabilities = []
for cap in capabilities_raw:
    slug = cap["slug"]
    intents = [
        f"如何理解和应用{cap['title']}",
        f"在剧本创作中实施{slug}的最佳实践",
        f"排查与解决{slug}相关的编剧失误与剧情断裂"
    ]
    capabilities.append({
        "capability_id": f"cap.story-and-screenplay-engineering.{slug}",
        "slug": slug,
        "title": cap["title"],
        "importance": "high",
        "importance_rationale": f"《故事》《你的剧本逊毙了！》《电影剧本写作基础》《动画剧本创作与营销》等编剧圣经核心支柱：{cap['one_liner']}",
        "one_liner": cap["one_liner"],
        "intents": intents,
        "keywords": cap["keywords"],
        "also_read": cap["also_read"],
        "card": f"cards/{slug}.md",
        "frontmatter": {
            "title": cap["title"],
            "importance": "high",
            "one_liner": cap["one_liner"],
            "requirements": cap["requirements"],
            "antirequirements": cap["antirequirements"]
        }
    })

bundle_data = {
    "schema_version": 1,
    "bundle_id": "bundle.story-and-screenplay-engineering",
    "book": {
        "slug": "story-and-screenplay-engineering",
        "title": "电影故事编剧与动画剧本工程手册",
        "subtitle": "融合罗伯特·麦基《故事》、威廉·埃克斯《你的剧本逊毙了！》、悉德·菲尔德《电影剧本写作基础》、杰弗里·斯科特《动画剧本创作与营销》等世界级编剧巨著",
        "authors": [
            "Robert McKee (罗伯特·麦基)",
            "William M. Akers (威廉·M·埃克斯)",
            "Syd Field (悉德·菲尔德)",
            "Jeffrey Scott (杰弗里·斯科特)"
        ],
        "edition": "Industrial Screenplay & Story Engineering Edition",
        "summary": "涵盖好莱坞经典三幕八序列架构、主导论题哲学因果矩阵、人物内在缺陷弧光、场景正负极性翻转、台词潜台词冰山力学、自洽对抗力量方阵、动画剧本物理笑料特化、道德两难危机高潮、群像副线交织、工业格式动作行留白、动画企划圣经制作与剧本医生四轮外科手术重写流水线。"
    },
    "entry": {
        "name": "story-and-screenplay-engineering",
        "description": "电影故事编剧、动画剧本创作、好莱坞结构力学与剧本医生外科手术诊断系统工程指南。",
        "core_principles": [
            "经典三幕八序列结构基准：激励事件、第一情节点、中点危机攻守翻转与第二情节点时序守恒",
            "主导论题哲学因果矩阵：价值冲突极性对抗，终极高潮必须以角色的物理决绝行动验证真理",
            "外在欲望Want与内在需求Need撕裂：幽灵创伤孕育致命缺陷，绝境暗夜舍弃虚妄Want拥抱Need",
            "场景价值极性翻转（+/-）：突发现实断层（Gap），晚进早出（Late In, Early Out）切除废戏",
            "对白潜台词冰山理论：表面言不由衷，背景信息戏剧化投放为武器，坚决消灭千人一面",
            "自洽正义反派方阵：反派是其自身世界观的英雄，智商战力高出30%，四级对抗矛盾递进升级",
            "动画剧本纯视觉优先与物理笑料：Show Don't Tell推向极致，四步视觉笑料力学与动物拟人逻辑",
            "道德两难危机与不可逆高潮：两难不可兼得极限抉择，引爆旧世界完成不可逆生命重构",
            "好莱坞工业排版与留白艺术：Courier 12pt规范，动作行留白Whitespace法则，消灭We See与未拍心理",
            "动画企划圣经与剧集产生引擎：黄金Logline公式，受众画像，世界观法则与商业提案答辩",
            "剧本医生四轮重写流水线：巧合只推入绝境严禁解套，骨架重构、人物弧光、场景张力与台词抛光分层降维"
        ],
        "out_of_scope": [
            "三维动画骨骼绑定与权重蒙皮（参见 stop-staring / cartoon-animation）",
            "逐帧动画时间掌握与物理动力学（参见 timing-for-animation / physics-for-animators）",
            "动画分镜头台本摄影机光学焦距与180度轴线绘制（参见 storyboarding-and-master-shots）"
        ],
        "stop_conditions": [
            "剧本格式符合好莱坞工业标准，动作行具备高度视听感且消灭全部不可拍摄心理描写",
            "三幕节点与中点危机清晰明确，场景具备正负极性翻转与严密潜台词",
            "反派智力在线动机自洽，危机高潮完成道德两难抉择并达成哲学主导论题闭环"
        ]
    },
    "router_entry": {
        "name": "story-and-screenplay-engineering",
        "description": "提供电影故事结构规划、动画剧本创作、场景冲突节拍设计、台词潜台词剖析、反派塑造与剧本医生诊断重写支持。"
    },
    "promotion_budget": 8,
    "capabilities": capabilities
}

target_path = "books/story-and-screenplay-engineering/.cangjie/capabilities/verified.yaml"
with open(target_path, "w", encoding="utf-8") as f:
    yaml.dump(bundle_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

print(f"Successfully generated {target_path} with {len(capabilities)} capabilities!")
