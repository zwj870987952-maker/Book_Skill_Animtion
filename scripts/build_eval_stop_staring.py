import json
from pathlib import Path

eval_suite = {
    "suite_id": "eval.stop-staring.v1",
    "pack_slug": "stop-staring",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": [
        {
            "case_id": "case-viseme-ortho-01",
            "prompt": "在 Maya 中做角色口型绑定，为什么不能直接给 26 个英文字母各雕刻一个混合形？如何用开合 (Open/Closed) 与宽窄 (Wide/Narrow) 建立二维正交解耦系统？",
            "should_trigger": True,
            "expected_capability": "viseme-ortho-matrix"
        },
        {
            "case_id": "case-lip-sync-pipeline-01",
            "prompt": "角色说对白时嘴型看起来总是慢半拍，怎么用四步口型流水线排查？辅音闭唇提前 2-4 帧的视错觉超前量法则该如何实施？",
            "should_trigger": True,
            "expected_capability": "lip-sync-pipeline"
        },
        {
            "case_id": "case-facial-edge-flow-01",
            "prompt": "角色面部拓扑布线规范是什么？口轮匝肌同心环要留几层？为什么五星极点绝对不能放在唇红线或鼻唇沟折痕上？",
            "should_trigger": True,
            "expected_capability": "facial-edge-flow-topology"
        },
        {
            "case_id": "case-additive-blendshape-01",
            "prompt": "如何用加算目标体（Additive Blendshapes）解决微笑与张嘴同时激活时的嘴角撕裂？ss2_blend_taper 余弦空间平滑衰减的公式是什么？",
            "should_trigger": True,
            "expected_capability": "additive-blendshape-math"
        },
        {
            "case_id": "case-mouth-teeth-tongue-01",
            "prompt": "角色口腔内部结构如何绑定？抛物线牙弓与下巴骨骼铰链怎样对齐？发 L 和 TH 音时的舌尖三段变形怎么做？",
            "should_trigger": True,
            "expected_capability": "mouth-cavity-teeth-tongue"
        },
        {
            "case_id": "case-brow-emotion-01",
            "prompt": "如何将眉毛运动解耦为内眉、外眉与眉心挤压（Brow Squeeze）三轴？表达悲伤和怀疑时内外眉如何配合？",
            "should_trigger": True,
            "expected_capability": "brow-emotion-mechanics"
        },
        {
            "case_id": "case-eyelid-tension-01",
            "prompt": "怎么调出真实的真笑眼神（Duchenne Smile）？上眼睑主导警觉与下眼睑主导心理紧张（Squint）的解耦法则是什么？",
            "should_trigger": True,
            "expected_capability": "eyelid-expression-tension"
        },
        {
            "case_id": "case-eye-saccades-01",
            "prompt": "角色向下看时露出死鱼眼眼白怎么解决？眼球 Aim 旋转时上眼睑跟随（Lid Follow）系数怎么定？眼球在不同目标间转移为什么必须 1 帧扫视跳跃？",
            "should_trigger": True,
            "expected_capability": "eye-rig-lid-follow-saccades"
        },
        {
            "case_id": "case-zipper-lips-01",
            "prompt": "角色微张嘴说话时嘴角边缘太生硬像纸片，如何用距离测量节点构建拉链嘴唇（Zipper Lips）渐进剥离粘连效果？",
            "should_trigger": True,
            "expected_capability": "zipper-lips-sticky-rig"
        },
        {
            "case_id": "case-negative-rigging-car-01",
            "prompt": "在 Unreal Engine 中配置四轮越野车的双叉臂独立悬挂物理资产与阿克曼转向几何差速计算",
            "should_trigger": False,
            "negative_reason": "超出角色面部建模与表情绑定范围，属于机械载具物理动力学"
        },
        {
            "case_id": "case-negative-database-sql-01",
            "prompt": "分析一条 MySQL 联表慢查询的 EXPLAIN 执行计划，优化复合索引消除 Using filesort 瓶颈",
            "should_trigger": False,
            "negative_reason": "超出角色动画与数字资产范围，属于后端数据库性能调优"
        }
    ],
    "output_cases": [
        {
            "case_id": "out-lip-sync-timing-01",
            "prompt": "为台词单词'FANTASTIC'（/fænˈtæstɪk/）在 24fps 下设计一套分层口型时序方案，明确关键辅音接触与超前量",
            "assertions": [
                "明确指出发音首辅音 /f/ 采用唇齿视素 (FV)，且闭合接触必须提前 2-4 帧完成",
                "明确指出后续重音元音 /æ/ 对应 Wide+Open 状态，下巴下沉且嘴角向外拉开",
                "明确指出发 /s/ 和 /t/ 时上下牙列贴近咬合，舌尖抵住上牙龈 (Tongue_Up)",
                "明确指出开合主干、宽窄过渡与次级下巴惯性滞后 1 帧的分层逻辑"
            ]
        },
        {
            "case_id": "out-additive-taper-01",
            "prompt": "详细推导 Jason Osipa 的无冲突加算目标体余弦空间衰减算法（ss2_blend_taper），说明如何保证左右分离后在中线满足无缝守恒",
            "assertions": [
                "给出余弦平滑衰减权重函数公式 W_left(x) = 0.5 * [1.0 + sin(pi * x / (2T))]",
                "证明在全空间严格满足 W_left(x) + W_right(x) ≡ 1.0 互补守恒律",
                "说明加算差分矢量 ΔV = V_target - V_base 的线性叠加原理",
                "明确指出避免了传统全脸网格覆盖导致的顶点超调撕裂"
            ]
        }
    ]
}

out_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\stop-staring\evals")
out_dir.mkdir(parents=True, exist_ok=True)
suite_file = out_dir / "eval-suite.json"
suite_file.write_text(json.dumps(eval_suite, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Written eval suite: {suite_file}")
