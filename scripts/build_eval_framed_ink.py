import json
from pathlib import Path

eval_suite = {
    "suite_id": "eval.framed-ink.v1",
    "pack_slug": "framed-ink",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": [
        {
            "case_id": "case-horizon-line-psychology-01",
            "prompt": "在电影概念分镜中，视平线（Horizon Line）的高低如何支配受众的心理感受？极低视平线仰视机位与极高视平线俯视全景各自适合传达角色的何种权力地位与心理状态？",
            "should_trigger": True,
            "expected_capability": "horizon-line-psychology"
        },
        {
            "case_id": "case-black-white-value-distribution-01",
            "prompt": "如何避免分镜构图陷入灰蒙蒙的 50% 泥潭（Muddy Midtones）？60-30-10 黑白纯明度层级架构是怎样构建的？逆光纯黑剪影（Silhouette）在瞬间叙事中的作用是什么？",
            "should_trigger": True,
            "expected_capability": "black-white-value-distribution"
        },
        {
            "case_id": "case-dynamic-geometric-tension-01",
            "prompt": "如何打破呆板的横平竖直九十度网格？在构图中如何运用倾斜对角线（Diagonals）注入速度动能，以及如何利用锐角三角形力场强化画面的攻击性与危险悬念？",
            "should_trigger": True,
            "expected_capability": "dynamic-geometric-tension"
        },
        {
            "case_id": "case-eye-leading-focal-paths-01",
            "prompt": "什么是视觉叙事中的“无形铁轨”？如何利用环境透视线、阴影边缘与角色视线目光，将观众的注意力在 0.1 秒内精准导引至核心叙事靶点？如何避免死胡同废线？",
            "should_trigger": True,
            "expected_capability": "eye-leading-focal-paths"
        },
        {
            "case_id": "case-three-layer-spatial-depth-01",
            "prompt": "如何刺穿二维屏幕构建三维纵深感？前景纯黑剪影框架（Framing within a Frame）、中景戏剧舞台与远景大气透视（Atmospheric Perspective）三层空间是如何相互咬合的？",
            "should_trigger": True,
            "expected_capability": "three-layer-spatial-depth"
        },
        {
            "case_id": "case-aspect-ratio-framing-psychology-01",
            "prompt": "不同的银幕画幅宽高比（Aspect Ratio）具有怎样的心理学属性？1.33:1 封闭画框的垂直压迫与 2.39:1 Cinemascope 宽银幕的史诗对峙各适合什么题材？如何利用子画框？",
            "should_trigger": True,
            "expected_capability": "aspect-ratio-framing-psychology"
        },
        {
            "case_id": "case-visual-continuity-eye-trace-01",
            "prompt": "连续分镜头画格切换时，视线轨迹守恒（Eye-Trace Continuity）是如何避免观众眼球疲劳的？如何严格遵守 180° 轴线规则，并在动作爆发顶点执行连贯动作切分（Cutting on Action）？",
            "should_trigger": True,
            "expected_capability": "visual-continuity-eye-trace"
        },
        {
            "case_id": "case-chiaroscuro-lighting-mood-01",
            "prompt": "卡拉瓦乔与黑色电影中的明暗对照法（Chiaroscuro）是如何用光线雕刻阴影的？顶光审判感、底光诡谲怪诞与侧光道德撕裂在心理学上是如何映射的？",
            "should_trigger": True,
            "expected_capability": "chiaroscuro-lighting-mood"
        },
        {
            "case_id": "case-scale-contrast-dominance-01",
            "prompt": "如何用极端的尺度悬殊对比（Scale Contrast）制造心理震撼？当 5% 的微小个体对抗 95% 的浩瀚吞噬环境，或前景巨大怪兽特写压迫远景渺小逃亡者时，如何保留人类标尺？",
            "should_trigger": True,
            "expected_capability": "scale-contrast-dominance"
        },
        {
            "case_id": "case-lens-perspective-wide-telephoto-01",
            "prompt": "虚拟摄影机焦距透视对戏剧空间有什么操纵作用？广角镜头（18mm）拉伸 Z 轴爆发冲撞速度与长焦镜头（135mm）空间压缩（Spatial Compression）贴紧猎物各在何时使用？",
            "should_trigger": True,
            "expected_capability": "lens-perspective-wide-vs-telephoto"
        },
        {
            "case_id": "case-negative-space-graphic-economy-01",
            "prompt": "为什么说“负空间是一片承载情感重力的无形海洋”？如何运用 40% 构图减法剔除无关细节杂质？大面积纯黑或纯白留白是如何将孤立角色推向边缘产生绝境压迫的？",
            "should_trigger": True,
            "expected_capability": "negative-space-graphic-economy"
        },
        {
            "case_id": "case-storyboard-cadence-editorial-flow-01",
            "prompt": "如何将剧本文字拆解为具有电影呼吸感的故事板节拍（Storyboard Cadence）？大远景（ELS）、全景、中景到大特写（ECU）的景别阶梯交替与运镜指示规范是怎样的？",
            "should_trigger": True,
            "expected_capability": "storyboard-cadence-editorial-flow"
        },
        {
            "case_id": "case-distractor-cnc-toolpath-01",
            "prompt": "请编写四轴数控铣床加工球头铣刀曲面精加工的 G 代码，设定主轴进给率与刀尖圆弧半径补偿值。",
            "should_trigger": False,
            "expected_capability": None
        },
        {
            "case_id": "case-distractor-pathology-endoscope-01",
            "prompt": "在消化道电子胃镜检查中，胃溃疡边缘粘膜活检取材的操作流程与福尔马林病理送检固定液配比是什么？",
            "should_trigger": False,
            "expected_capability": None
        },
        {
            "case_id": "case-distractor-barcode-label-01",
            "prompt": "设计物流仓储 Code128 条形码标签印刷模版，计算校验位并在热敏打印机驱动中设置打印浓度和标签间距。",
            "should_trigger": False,
            "expected_capability": None
        }
    ]
}

eval_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\framed-ink\.cangjie\evals")
eval_dir.mkdir(parents=True, exist_ok=True)
suite_file = eval_dir / "eval-suite.json"
suite_file.write_text(json.dumps(eval_suite, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Created Framed Ink eval suite at: {suite_file}")
