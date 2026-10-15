import json
from pathlib import Path

eval_suite = {
    "suite_id": "eval.illusion-of-life.v1",
    "pack_slug": "illusion-of-life",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": [
        {
            "case_id": "case-squash-and-stretch-01",
            "prompt": "在经典角色动画中，如何应用迪士尼十二黄金法则第一条“挤压与拉伸”（Squash & Stretch）？如何严格保持角色的三维常数体积守恒（Constant Volume），避免拉伸时充气膨胀？",
            "should_trigger": True,
            "expected_capability": "squash-and-stretch"
        },
        {
            "case_id": "case-anticipation-physics-01",
            "prompt": "角色在爆发猛烈动作前，为什么必须向反方向做动作预备（Anticipation）？在生物力学上拮抗肌是如何被拉伸蓄力的？如何通过 3:1 的速度反差引导受众视网膜注意力？",
            "should_trigger": True,
            "expected_capability": "anticipation-physics"
        },
        {
            "case_id": "case-staging-clarity-01",
            "prompt": "迪士尼动画大师是如何进行舞台调度（Staging）的？什么是纯黑剪影测试（Silhouette Test）？如何通过 3/4 视角旋转、释放几何负空间窗口并消除共线切线（Tangents）？",
            "should_trigger": True,
            "expected_capability": "staging-clarity"
        },
        {
            "case_id": "case-straight-ahead-pose-to-pose-01",
            "prompt": "连续画法（Straight Ahead）的自发动能灵感与姿态对应法（Pose to Pose）的结构控制在工业管线中是如何融合的？在何种段落使用 Pose to Pose，何种段落使用 Straight Ahead？",
            "should_trigger": True,
            "expected_capability": "straight-ahead-pose-to-pose"
        },
        {
            "case_id": "case-follow-through-overlapping-01",
            "prompt": "如何杜绝角色肢体同帧起止的木偶病？主动力源（骨盆/脊椎）先行时，被动附属物（长发、长耳、尾巴、衣服）的滞后拖尾（Drag）与刹车超量正弦衰减跟随（Follow Through）该如何编排？",
            "should_trigger": True,
            "expected_capability": "follow-through-overlapping"
        },
        {
            "case_id": "case-slow-in-slow-out-01",
            "prompt": "牛顿力学加减速在动画慢入慢出（Slow In & Slow Out）中是如何体现的？为什么极值姿态附近必须密集排布画稿，而在中间位移要快速撕裂？如何避免均等中割？",
            "should_trigger": True,
            "expected_capability": "slow-in-slow-out"
        },
        {
            "case_id": "case-arcs-of-motion-01",
            "prompt": "为什么生物骨骼关节运动必然遵循圆滑弧线（Arcs of Motion）？直线中割会导致四肢怎样萎缩和穿模？如何利用运动轨迹（Motion Trail）追踪弧线并保持骨架物理长度守恒？",
            "should_trigger": True,
            "expected_capability": "arcs-of-motion"
        },
        {
            "case_id": "case-secondary-action-01",
            "prompt": "次级动作（Secondary Action）与被动跟随动作（Follow Through）的本质区别是什么？次级动作如何作为角色心理潜台词的情绪放大器，同时严格服从主动作节奏不抢戏？",
            "should_trigger": True,
            "expected_capability": "secondary-action"
        },
        {
            "case_id": "case-timing-weight-acting-01",
            "prompt": "为什么说“画稿的帧数决定了角色的灵魂”？如何通过时间掌握（Timing）赋予二维线条数吨的真实物理重量感？在刺激与动作之间如何编排 3-6 帧心理思维停顿（Thinking Beat）？",
            "should_trigger": True,
            "expected_capability": "timing-weight-acting"
        },
        {
            "case_id": "case-exaggeration-essence-01",
            "prompt": "什么是迪士尼大师口中的“戏剧夸张是对本质真理的放大（Magnifying the Essence）”？如何将角色性格与冲突推向 150%-200% 的超真实，同时避免无动机的恶俗怪诞畸变？",
            "should_trigger": True,
            "expected_capability": "exaggeration-essence"
        },
        {
            "case_id": "case-solid-drawing-volume-01",
            "prompt": "纯熟绘图能力（Solid Drawing）如何赋予角色三维空间立体深度与体积？如何运用三大几何体块、环绕包裹截面线（Cross-Contour）与 T 形空间穿插彻底消除扁平纸片人？",
            "should_trigger": True,
            "expected_capability": "solid-drawing-volume"
        },
        {
            "case_id": "case-appeal-character-soul-01",
            "prompt": "为什么说“至高吸引力（Appeal）是一切动画设计的皇冠”？如何运用大中小（Large-Medium-Small）黄金比例、婴儿图式脆弱感与反派的宏伟几何纯度雕刻角色的终极魅力？",
            "should_trigger": True,
            "expected_capability": "appeal-character-soul"
        },
        {
            "case_id": "case-distractor-hydraulic-press-01",
            "prompt": "计算 500 吨四柱双动液压机的液压油泵排量、工作油缸活塞密封圈摩擦阻力与工作台有限元强度刚度分布。",
            "should_trigger": False,
            "expected_capability": None
        },
        {
            "case_id": "case-distractor-barcode-ean13-01",
            "prompt": "根据国家标准 GB 12904 生成 EAN-13 商品条形码前缀码与奇偶校验符，计算条空反射率与印刷对比度差值。",
            "should_trigger": False,
            "expected_capability": None
        },
        {
            "case_id": "case-distractor-forensic-toxicology-01",
            "prompt": "法医学毒物化学分析中，采用气相色谱-质谱联用仪（GC-MS）检测血液样品中有机磷农药残留的标准质控流程是什么？",
            "should_trigger": False,
            "expected_capability": None
        }
    ]
}

eval_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\illusion-of-life\.cangjie\evals")
eval_dir.mkdir(parents=True, exist_ok=True)
suite_file = eval_dir / "eval-suite.json"
suite_file.write_text(json.dumps(eval_suite, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Created Illusion of Life eval suite at: {suite_file}")
