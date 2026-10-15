import yaml
import os

capabilities_raw = [
    {
        "slug": "human-run-and-sprint-mechanics",
        "title": "人类奔跑与极速冲刺动力学（双足奔跑六相位与步长步频标尺）",
        "one_liner": "双足奔跑六相位动力学、消除双重支撑、前倾角与蹬地腾空力学控制。",
        "keywords": ["human-run", "sprint-mechanics", "gait-phase", "flight-phase", "push-off", "running-cycle"],
        "also_read": ["jump-leap-and-land-impact", "wave-and-whip-secondary-curves"],
        "requirements": [
            "奔跑动作循环必须彻底消除双重支撑，必须包含明确的单足支撑与双足腾空期",
            "支撑脚在接触地面至离地期间坐标必须绝对锁定，杜绝地面打滑溜冰",
            "全速冲刺躯干前倾角控制在 15°-25°，手臂异侧对角线大摆幅平衡力矩"
        ],
        "antirequirements": [
            "严禁脚底在地面接触期间发生空间坐标滑动（溜冰步态）",
            "严禁身体上下颠簸使用匀速对称正弦波无视重力加速度"
        ]
    },
    {
        "slug": "jump-leap-and-land-impact",
        "title": "跳跃蹬地腾空与着地冲击缓冲全周期（预备深蹲与抛物线挂壁）",
        "one_liner": "深蹲蓄力压缩、离地瞬间爆发加速度、抛物线极值点挂壁滞空与落地屈膝吸能。",
        "keywords": ["jump-mechanics", "standing-broad-jump", "apex-hang-time", "impact-squash", "landing-dissipation"],
        "also_read": ["human-run-and-sprint-mechanics", "wave-and-whip-secondary-curves"],
        "requirements": [
            "起跳深蹲蓄力行程与离地初速度严格匹配，离地 1-2 帧内速度暴增",
            "抛物线最高极值点必须调出 2-4 帧微弱位移的挂壁滞空感",
            "落地触地瞬间必须解耦至少 3 帧垂直下沉深蹲吸能缓冲"
        ],
        "antirequirements": [
            "严禁刚体笔直触地不深蹲缓冲（刚体塑料玩偶砸地反模式）",
            "严禁空中上升与下落呈匀速线性运动无重力加速度"
        ]
    },
    {
        "slug": "quadruped-locomotion-walk-trot-gallop",
        "title": "四足动物步态全谱系（慢步四拍三角、小跑对角二拍与大跑双悬空）",
        "one_liner": "四足慢步非对称四拍三角支撑、小跑对角对称二拍与大跑双悬空脊椎弹簧。",
        "keywords": ["quadruped-walk", "quadruped-trot", "rotary-gallop", "spinal-bowing", "gathered-suspension"],
        "also_read": ["avian-aerodynamics-flight-and-glide", "aquatic-fish-and-reptile-undulation"],
        "requirements": [
            "慢步必须遵循左后→左前→右后→右前四拍节律，任何时刻维持三角静态稳定",
            "大跑疾驰必须展现极度收拢拱背与极度舒展张开的两个完全腾空期",
            "四足动物肩胛骨承重着地时必须向上滑动位移，禁止刚性锁死"
        ],
        "antirequirements": [
            "严禁四足动物慢步做成同侧同手同脚顺拐步态",
            "严禁大跑时后腿不敢向前大跨步穿插造成步幅过窄"
        ]
    },
    {
        "slug": "avian-aerodynamics-flight-and-glide",
        "title": "飞禽气动力学与振翅滑翔（大鸟重力滑翔与三段式多关节波浪）",
        "one_liner": "大鸟重力滑翔与多关节波浪下拍做功、小鸟高频折叠扑翼与起落减速刹车。",
        "keywords": ["bird-flight", "avian-aerodynamics", "wing-wave", "downstroke-power", "recovery-upstroke"],
        "also_read": ["quadruped-locomotion-walk-trot-gallop", "aquatic-fish-and-reptile-undulation"],
        "requirements": [
            "下拍做功相翅膀完全平展倒U形密封推风，上提回位相三关节折叠顺流切开空气",
            "翅膀自肩关节向腕部和初级飞羽尖端必须展现 1-3 帧逐级波浪延迟",
            "起飞必须包含腿部深蹲蹬地弹射，降落必须展翅摊爪气动刹车"
        ],
        "antirequirements": [
            "严禁翅膀如刚性硬纸板做对称上下等速扇动",
            "严禁飞行时身体直线平移毫无垂直升降颠簸"
        ]
    },
    {
        "slug": "aquatic-fish-and-reptile-undulation",
        "title": "游鱼与两栖爬行正弦波推进（大鱼全身S波传导与小鱼突刺滑行）",
        "one_liner": "水生生物推进波自前向后传递、头部极小摆动锁定视野、尾部振幅渐增推进。",
        "keywords": ["fish-locomotion", "undulatory-propulsion", "sinusoidal-thrust", "burst-and-coast", "caudal-fin"],
        "also_read": ["avian-aerodynamics-flight-and-glide", "wave-and-whip-secondary-curves"],
        "requirements": [
            "正弦推力波必须从鳃部向后传递，波速必须大于鱼体前行速度",
            "小鱼游动必须呈现 2-4 帧爆发突刺加 8-16 帧惯性滑行的非线性节拍",
            "身体振幅从头部向尾鳍呈指数级放大，头部摆角严格受限"
        ],
        "antirequirements": [
            "严禁鱼身笔直僵硬仅尾巴如雨刷机械摆动",
            "严禁鱼体位移速度与尾鳍拍击做功相位完全脱节"
        ]
    },
    {
        "slug": "wave-and-whip-secondary-curves",
        "title": "曲线运动波浪与鞭形次级传导（根部驱动节节贯穿与甩鞭能量聚焦）",
        "one_liner": "柔软物体逐级延迟时间偏置、S形波浪流淌、甩鞭末端突破音速折返回抽。",
        "keywords": ["wave-motion", "whip-snap", "segmental-propagation", "overlapping-action", "follow-through"],
        "also_read": ["human-run-and-sprint-mechanics", "water-splash-droplet-and-ripples"],
        "requirements": [
            "骨骼链条相邻关节必须在时间轴上顺延 1-2 帧偏置，形成清晰S弯",
            "甩鞭尖端在质量递减下必须展现 1 帧极速 180° 折返与回震衰减",
            "从动形变必须严格由基座根部运动引发，禁止无源自发形变"
        ],
        "antirequirements": [
            "严禁所有关节在同一帧同步弯曲和回直（折叠尺反模式）",
            "严禁波动传导在中途突然无缘由阻尼截断"
        ]
    },
    {
        "slug": "water-splash-droplet-and-ripples",
        "title": "水特效动力学：水滴、皇冠水花与扩散涟漪（表面张力与中央射流）",
        "one_liner": "水滴下落表面张力球化、撞击皇冠薄壁水幕升起、中央水柱冲天与同心涟漪。",
        "keywords": ["crown-splash", "worthington-jet", "water-droplet", "surface-tension", "gravity-ripples"],
        "also_read": ["water-waves-surge-and-turbulent-foam", "wave-and-whip-secondary-curves"],
        "requirements": [
            "水花演化必须分层经历极薄射流环、锯齿皇冠、中央水柱喷射与二次滴落",
            "同心圆涟漪扩散时波长向外拉长，振幅按几何级数迅速衰减平复",
            "细小水珠在空中必须迅速因表面张力收缩为正球形"
        ],
        "antirequirements": [
            "严禁水花作为刚性模型做单一缩放（冰雕喷泉反模式）",
            "严禁涟漪波纹间距始终等宽无衰减向外线性推移"
        ]
    },
    {
        "slug": "water-waves-surge-and-turbulent-foam",
        "title": "水特效动力学：涌浪、破碎翻滚与紊流泡沫（近岸卷浪与泡沫时滞）",
        "one_liner": "近岸浅水波峰变陡前倾、卷浪中空圆筒（Barrel Roll）与白色网状泡沫消散时滞。",
        "keywords": ["ocean-waves", "barrel-roll", "wave-breaking", "turbulent-foam", "foam-latency"],
        "also_read": ["water-splash-droplet-and-ripples", "explosion-shockwave-and-debris-field"],
        "requirements": [
            "浅水波浪必须呈现浪尖前探、浪唇悬空抛射形成中空圆筒空腔",
            "碰撞瞬间必须在基底激发出扇形高压白色水汽爆炸",
            "破碎后纯白水沫转为网格状泡沫丝并在沙滩滞留 1-2 秒消散"
        ],
        "antirequirements": [
            "严禁海浪像推土机平板整体平移无内卷空腔",
            "严禁泡沫随底层水体瞬间回抽无消散时滞"
        ]
    },
    {
        "slug": "fire-combustion-tongues-and-eddies",
        "title": "火焰燃烧动力学：火苗、火舌撕裂与热涡流（浮力加速与独立火球）",
        "one_liner": "热浮力加速升腾、底部冷空气颈缩、交替剪切涡流与火舌撕裂脱离熄灭。",
        "requirements": [
            "火焰底部必须呈现冷空气吸入的颈缩收窄，中上部形成S弯升腾",
            "火舌拉伸变细后必须在 1 帧内发生颈缩断裂，脱离成独立火球上升熄灭",
            "内部反应核呈现纯白高温过曝，向外过渡为橙黄与暗红边缘"
        ],
        "antirequirements": [
            "严禁火苗做机械对称左右摆动且形态永不撕裂",
            "严禁火焰材质使用单一纯橙色无高温白光核心"
        ],
        "keywords": ["fire-combustion", "flame-tongues", "thermal-eddies", "buoyancy-flow", "fireball-detachment"],
        "also_read": ["smoke-exhaust-and-thermal-plumes", "lightning-arc-and-flash-burst"]
    },
    {
        "slug": "smoke-exhaust-and-thermal-plumes",
        "title": "烟雾与热羽流扩散动力学（轻烟层流转紊流与浓烟多级滚涌涡环）",
        "one_liner": "轻烟平滑丝带突变螺旋紊流、浓烟自向外滚涌甜甜圈涡环与蘑菇云顶帽翻卷。",
        "keywords": ["smoke-plumes", "vortex-rings", "mushroom-cloud", "cauliflower-smoke", "thermal-buoyancy"],
        "also_read": ["fire-combustion-tongues-and-eddies", "explosion-shockwave-and-debris-field"],
        "requirements": [
            "重型浓烟必须具备中心高速外围摩擦向外翻卷的滚涌涡环结构",
            "烟雾总体积随上升高度呈非线性几何膨胀，边缘逐渐镂空透明淡出",
            "蘑菇云演化必须经历柱状茎干高速上冲、顶帽水平展开下垂与高空漂移"
        ],
        "antirequirements": [
            "严禁烟团作为单一实体做等比气球缩放",
            "严禁浓烟呈现扁平灰色无球状明暗体积感"
        ]
    },
    {
        "slug": "lightning-arc-and-flash-burst",
        "title": "雷电电弧、分叉路径与高能爆闪（阶跃先导分叉与单帧全白主回击）",
        "one_liner": "阶跃先导锯齿向下探寻、触地瞬间引爆单帧全白主回击与通道电离残影渐隐。",
        "keywords": ["lightning-arc", "stepped-leader", "return-stroke", "flash-burst", "plasma-channel"],
        "also_read": ["explosion-shockwave-and-debris-field", "fire-combustion-tongues-and-eddies"],
        "requirements": [
            "必须展现数帧微弱锯齿先导下探与 1 帧核心主干极亮纯白过曝的强烈极差",
            "主回击击中瞬间全屏白闪，未触地分支瞬间熄灭，主干保留 2-3 帧蓝紫余辉",
            "雷电拐点必须具备尖锐生硬的折角，杜绝平滑圆弧"
        ],
        "antirequirements": [
            "严禁使用平滑贝塞尔曲线做圆润S形闪电",
            "严禁闪电缓慢渐入渐出失去瞬间阶跃爆发力"
        ]
    },
    {
        "slug": "explosion-shockwave-and-debris-field",
        "title": "爆炸能量释放、冲击波与碎片抛体场（超音速火球与碎片变初速抛体）",
        "one_liner": "爆心第一帧超音速体积暴增、半透明激波光环扫起尘土、刚性碎片射穿火球。",
        "keywords": ["explosion-dynamics", "shockwave-front", "fireball-expansion", "debris-field", "ballistic-particles"],
        "also_read": ["smoke-exhaust-and-thermal-plumes", "lightning-arc-and-flash-burst"],
        "requirements": [
            "爆炸第一帧火球体积必须暴增 70%，并推开半透明折射激波光环",
            "刚性碎片的初速度必须远超火球膨胀速度，第一帧射穿火球沿抛物线抛射",
            "重型碎片撞地激起二次飞溅，烟团在爆心上方滞后升腾聚集成蘑菇云"
        ],
        "antirequirements": [
            "严禁火球体积使用线性平滑过渡缺乏瞬间暴增爆发感",
            "严禁固体碎片与火球同速运动被困在烟雾中"
        ]
    }
]

capabilities = []
for c in capabilities_raw:
    slug = c["slug"]
    cap_entry = {
        "capability_id": f"cap.locomotion-and-fx-dynamics.{slug}",
        "revision": 1,
        "status": "active",
        "aliases": [],
        "supersedes": [],
        "merged_into": None,
        "split_into": [],
        "slug": slug,
        "title": c["title"],
        "importance": "high",
        "importance_rationale": "该能力是《动画运动规律与自然特效动力学全景工程手册》中核心的 high 级别工业标准与物理运动规范。",
        "one_liner": c["one_liner"],
        "intents": [
            f"如何实现{c['title']}",
            f"应用{c['title']}的动作规律与物理特效设计规范",
            f"排查{c['title']}相关的常见动画与动力学反模式"
        ],
        "keywords": c["keywords"],
        "also_read": c["also_read"],
        "card": f"cards/{slug}.md",
        "frontmatter": {
            "title": c["title"],
            "importance": "high",
            "one_liner": c["one_liner"],
            "requirements": c["requirements"],
            "antirequirements": c["antirequirements"]
        }
    }
    capabilities.append(cap_entry)

verified_data = {
    "schema_version": 1,
    "bundle_id": "bundle.locomotion-and-fx-dynamics",
    "book": {
        "title": "动画运动规律与自然特效动力学全景工程手册",
        "source_pack": "books/locomotion-and-fx-dynamics",
        "edition": "Masterclass Engineering Edition",
        "authors": [
            "全国高校动画教育编委会",
            "Naoshi Ozawa (尾泽直志)",
            "Chris Webster (克里斯·韦伯斯特)"
        ],
        "year": 2026
    },
    "entry": {
        "name": "locomotion-and-fx-dynamics",
        "description": "经典角色运动规律与自然物理特效动力学工业级工程手册。涵盖人类奔跑与极速冲刺六相位步态动力学（步长步频标尺、前倾倾角、蹬地与双重腾空、对角线手臂摆动补偿）、跳跃深蹲蓄力离地滞空与着地屈膝吸能解耦全周期、四足动物慢步四拍非对称交叉/快步对角二拍/疾驰大跑双悬空脊椎强力弹簧步态全谱系、飞禽多关节波浪气动做功与折叠滑翔、游鱼与两栖爬行正弦波推进振幅渐增律与突刺滑行节拍、曲线运动柔软链条节节贯穿与甩鞭效应动量聚焦折返回抽、水滴表面张力形变与皇冠水花/中央射流/同心圆涟漪、近岸浅水卷浪中空圆筒（Barrel Roll）与白色紊流网状泡沫消散时滞、火焰热浮力加速与火舌S弯撕裂脱离消散、轻烟层流转紊流与浓烟滚涌多级涡环/爆炸蘑菇云热羽流、雷电阶跃先导分叉与单帧全白主回击爆闪极差、超音速爆炸光爆激波面与固体碎片变初速抛体场全套工业规范。",
        "core_principles": [
            "双足奔跑零双重支撑律：奔跑必须彻底消除双重支撑，由单足支撑与双足腾空交替循环构成，全速冲刺腾空期占比达 50% 以上。",
            "跳跃牛顿冲量与滞空挂壁法则：起跳蓄力深蹲深度与离地初速度严格匹配，最高极值点保留 2-4 帧微弱位移挂壁感，着地必须解耦至少 3 帧垂直下沉缓冲。",
            "四足动物对角相位锁定律：四足慢步严格遵守左后→左前→右后→右前四拍三角支撑，大跑必须展现极度收拢拱背与极度舒展张开的双重悬空期。",
            "飞禽扑翼气动流体不对称律：做功下拍翅膀完全平展倒U形密封推风，减阻上提三关节折叠顺流切开空气，严禁硬纸板对称扇动。",
            "水生鱼类正弦横波渐增律：鱼体推进波自颈部向尾梢传递，头部微幅摆动锁定视野，尾鳍振幅非线性放大产生反向推力。",
            "软体曲线节节贯穿与逐级延迟律：次级柔韧链条相邻骨骼节点之间恒定顺延 1-2 帧时间偏置，甩鞭尖端在质量锐减下爆发突破音速折返回抽。",
            "流体皇冠水花与中央射流演化：水面撞击必须分层经历极薄射流环、锯齿皇冠水幕升起、中央水柱垂直冲天回落与外扩重力涟漪。",
            "海浪卷浪中空管道与泡沫消散时滞：浅水浪头前倾翻越形成中空圆筒（Barrel），破碎后纯白水沫转为网格状泡沫丝并在沙滩滞留消散。",
            "火焰热浮力加速与火舌撕裂模型：基底冷空气卷入形成进气颈缩，中上部在剪切涡流下形成S弯并发生火舌断裂，脱离成独立火球上升熄灭。",
            "浓烟滚涌自持多级涡环律：重型浓烟与爆炸羽流以中心高速外围卷吸形成自翻滚甜甜圈结构，体积随高度呈三次方非线性剧烈膨胀。",
            "雷电先导微弱与主回击极亮爆闪极差律：数帧锯齿树状微弱先导下探触地后，瞬间引爆 1 帧核心主干极亮纯白过曝，全屏白闪伴随蓝紫残影渐隐。",
            "爆炸超音速激波面与碎片初速度分层律：爆心第一帧爆发 70% 尺寸火球并推开半透明折射激波光环，刚性碎片以极高初速度射穿火球沿抛物线抛射。"
        ],
        "out_of_scope": [
            "剧本写作与故事结构创作（请参阅故事与编剧类相关手册）",
            "电影分镜头脚本与镜头语法设计（请参阅分镜与电影语言相关手册）",
            "三维解算软件具体渲染器着色器底层着色代码（如Arnold/V-Ray C++底层API）"
        ],
        "stop_conditions": [
            "已为角色动作或自然物理特效建立完整的帧时序标尺、受力形变分析与防穿帮排障方案",
            "已提供各阶段关键帧Pose、Graph Editor曲线切线控制与多层动力学拆解规范"
        ]
    },
    "router_entry": {
        "name": "locomotion-and-fx-dynamics",
        "description": "运动规律与自然特效动力学全景工程手册。提供人类奔跑冲刺、跳跃腾空缓冲、四足走跑疾驰、飞禽扑翼滑翔、游鱼正弦推进、曲线甩鞭波浪、水花皇冠中央水柱、海浪卷浪泡沫、火焰火舌撕裂、浓烟蘑菇云羽流、雷电先导回击爆闪、爆炸激波碎片抛体全流程工业指导。"
    },
    "promotion_budget": 8,
    "capabilities": capabilities
}

target_yaml = r"books\locomotion-and-fx-dynamics\.cangjie\capabilities\verified.yaml"
with open(target_yaml, 'w', encoding='utf-8') as f:
    yaml.dump(verified_data, f, allow_unicode=True, sort_keys=False)

print(f"Successfully generated fully compliant verified.yaml at {target_yaml} with {len(capabilities)} capabilities.")
