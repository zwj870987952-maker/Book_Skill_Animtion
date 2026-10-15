import json
from pathlib import Path

eval_suite = {
    "suite_id": "eval.drawn-to-life.v1",
    "pack_slug": "drawn-to-life",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": [
        {
            "case_id": "case-gesture-drawing-vital-force-01",
            "prompt": "在动画动态速写中，如何践行 Walt Stanchfield 的“不要画形体是什么，要画形体在做什么”？如何提炼第一笔贯穿全身的主导动力线（The Driving Line of Action）避免死尸速写？",
            "should_trigger": True,
            "expected_capability": "gesture-drawing-vital-force"
        },
        {
            "case_id": "case-squash-stretch-volume-01",
            "prompt": "角色在受重力压迫猛烈落地冲击或下蹲蓄力时，如何表现极致的挤压拉伸形变（Squash and Stretch），同时严格确保角色的三维体积与质量守恒？",
            "should_trigger": True,
            "expected_capability": "squash-stretch-volume-weight"
        },
        {
            "case_id": "case-straights-curves-design-01",
            "prompt": "迪士尼造型设计中如何运用“直线对抗曲线”（Straights Against Curves）原则？为什么不能画对称的香肠肢体？挺拔直线如何作为视觉加速跑道引导能量？",
            "should_trigger": True,
            "expected_capability": "straights-against-curves-design"
        },
        {
            "case_id": "case-silhouette-clarity-staging-01",
            "prompt": "如何用 0.1 秒纯黑剪影测试检验原画关键姿态的瞬间叙事可读性？如何排查共线与切线（Tangents），并利用几何负空间进行清晰的舞台视线引导？",
            "should_trigger": True,
            "expected_capability": "silhouette-clarity-staging"
        },
        {
            "case_id": "case-opposing-forces-contrapposto-01",
            "prompt": "角色在重力场中单脚承重站立或发力时，头、胸、盆三大刚性体块在空间中是如何反向倾斜（Counter-Tilt）与扭转代偿以维系动态平衡的？",
            "should_trigger": True,
            "expected_capability": "opposing-forces-contrapposto-twist"
        },
        {
            "case_id": "case-line-economy-calories-01",
            "prompt": "什么是绘画中的“卡路里法则”（Drawing Calories）与线条经济学？如何用大臂带动画笔消除犹豫细碎排线（Chicken Scratching），用极简果断长线承载大体块？",
            "should_trigger": True,
            "expected_capability": "line-economy-drawing-calories"
        },
        {
            "case_id": "case-overlap-follow-through-01",
            "prompt": "在动作重叠（Overlapping Action）与跟随惯性中，主动力源与末端柔性附着物（长发、披风、松弛肌肉）的多级参差延迟时序是怎样的？如何杜绝同帧起止？",
            "should_trigger": True,
            "expected_capability": "overlap-follow-through-drag"
        },
        {
            "case_id": "case-acting-story-pose-01",
            "prompt": "如何将戏剧心理与潜台词注入动画原画？在设计关键动作故事姿态（Story Pose）时，如何让单张画稿同时容纳角色的过去动机、当下挣扎与未来意图？",
            "should_trigger": True,
            "expected_capability": "acting-performance-story-pose"
        },
        {
            "case_id": "case-facial-acting-eye-direction-01",
            "prompt": "面部表演中“思维先于动作”是如何体现的？眼神视线提前 2-4 帧扫视先行（Saccade）与思维顿悟时的眨眼节拍该如何编排？五官如何保持呼吸张力？",
            "should_trigger": True,
            "expected_capability": "facial-acting-eye-expression"
        },
        {
            "case_id": "case-perspective-ground-plane-01",
            "prompt": "如何用环绕包裹截面线（Cross-Contour）赋予角色三维空间厚度与进深？角色双足与地平面及环境桌椅道具之间应如何产生坚实真实的重力反作用踩踏？",
            "should_trigger": True,
            "expected_capability": "perspective-spatial-depth-environment"
        },
        {
            "case_id": "case-rhythm-bodily-accents-01",
            "prompt": "动画节奏为什么不能像节拍器一样匀速机械？如何为动作编排像爵士交响乐一样的多声部律动、极慢蓄力与闪电爆发重音（Accents），并注入生命的呼吸停顿？",
            "should_trigger": True,
            "expected_capability": "rhythm-accents-animation-timing"
        },
        {
            "case_id": "case-simplicity-caricature-appeal-01",
            "prompt": "迪士尼至高吸引力（Appeal）的本质是什么？如何提炼角色的深层性格特质并进行 150%-200% 的戏剧夸张（Caricature），用极简几何大轮廓取代繁杂细节？",
            "should_trigger": True,
            "expected_capability": "simplicity-caricature-appeal"
        },
        {
            "case_id": "case-distractor-industrial-lathe-01",
            "prompt": "请帮我编写数控车床加工 G 代码，切削直径 40mm 的公制粗牙梯形螺纹导轨，计算主轴转速与刀具进给速度。",
            "should_trigger": False,
            "expected_capability": None
        },
        {
            "case_id": "case-distractor-forensic-tissue-01",
            "prompt": "法医学尸体防腐处理中，福尔马林灌注固定与组织切片苏木精-伊红（HE）染色的标准病理实验室操作规范是什么？",
            "should_trigger": False,
            "expected_capability": None
        },
        {
            "case_id": "case-distractor-pure-fractal-01",
            "prompt": "在复平面上用 Python 迭代生成 Mandelbrot 分形集合与 Julia 集合，不考虑任何质量、重力与物理力学模拟。",
            "should_trigger": False,
            "expected_capability": None
        }
    ]
}

eval_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\drawn-to-life\.cangjie\evals")
eval_dir.mkdir(parents=True, exist_ok=True)
suite_file = eval_dir / "eval-suite.json"
suite_file.write_text(json.dumps(eval_suite, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Created Drawn to Life eval suite at: {suite_file}")
