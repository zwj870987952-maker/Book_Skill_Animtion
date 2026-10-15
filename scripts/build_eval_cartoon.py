import json
from pathlib import Path

eval_suite = {
    "suite_id": "eval.cartoon-animation.v1",
    "pack_slug": "cartoon-animation",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": [
        {
            "case_id": "case-construction-head-01",
            "prompt": "设计一个美式经典卡通狐狸角色的头部三维结构，如何使用基础球体、十字定位线和头身比规范透视旋转？",
            "should_trigger": True,
            "expected_capability": "character-construction-proportions"
        },
        {
            "case_id": "case-body-mass-01",
            "prompt": "卡通小熊在下蹲压扁时，如何保持实心肉块体积不变？怎样避免画成松垮的橡皮管？",
            "should_trigger": True,
            "expected_capability": "skeletal-posture-weight"
        },
        {
            "case_id": "case-line-of-action-01",
            "prompt": "角色挥棒击球的瞬间动态僵硬，如何使用动作线（Line of Action）理顺从后脚跟到棒尖的单一贯穿力道？",
            "should_trigger": True,
            "expected_capability": "line-of-action-dynamism"
        },
        {
            "case_id": "case-rhythm-curves-01",
            "prompt": "为什么角色轮廓两边都是对称圆弧看起来像气球？动画中的直线与曲线对立律（Straight vs Curved）怎么应用？",
            "should_trigger": True,
            "expected_capability": "rhythm-curved-movement"
        },
        {
            "case_id": "case-four-legged-walk-01",
            "prompt": "猎犬慢步走和急速奔跑的四足步态规律是什么？前后肢交错接触地面顺序与脊椎波浪怎么画？",
            "should_trigger": True,
            "expected_capability": "four-legged-locomotion"
        },
        {
            "case_id": "case-take-anticipation-01",
            "prompt": "设计一个被鬼吓到的夸张大反应动作（Double Take），起势、缩紧、反冲爆炸和震颤定格该怎么排？",
            "should_trigger": True,
            "expected_capability": "take-anticipation-recoil"
        },
        {
            "case_id": "case-dialogue-mouth-01",
            "prompt": "角色念单词'Explosion'和'Fantastic'时，口型张开与牙齿舌头怎么画？为什么不能按每个字母死板对口型？",
            "should_trigger": True,
            "expected_capability": "dialogue-mouth-anatomy"
        },
        {
            "case_id": "case-hands-gesture-01",
            "prompt": "经典卡通手为什么通常画四根手指？手掌掌骨扇形基底与指关节透视怎样画出生命感？",
            "should_trigger": True,
            "expected_capability": "cartoon-hands-gesture"
        },
        {
            "case_id": "case-negative-shader-01",
            "prompt": "在 Unity 中编写一个各向异性毛发 PBR Shader，使用 HLSL 实现双高光次表面散射计算",
            "should_trigger": False,
            "negative_reason": "超出卡通传统动画形体与运动规律范围，属于 3D 实时渲染技术"
        },
        {
            "case_id": "case-negative-web-frontend-01",
            "prompt": "使用 Vue3 Composition API 与 Pinia 状态库开发一个用户购物车结算与优惠券抵扣组件",
            "should_trigger": False,
            "negative_reason": "超出动画角色设计与运动规律范围，属于前端 Web 软件工程"
        }
    ],
    "output_cases": [
        {
            "case_id": "out-line-of-action-01",
            "prompt": "排查并修正一个奔跑急停推门动作。当前草图在躯干处出现生硬折角，请给出动作线修正方案与关键张绘制规范",
            "assertions": [
                "明确指出动作线（Line of Action）的单一贯穿主弧线原则（C 弧或反 C 弧）",
                "指出破坏动态张力的生硬折角排查与消除方法",
                "包含直线与曲线对立（Straight vs Curved）在张力侧与压缩侧的应用",
                "给出躯干、骨盆与四肢沿动作线顺势延伸的构图说明"
            ]
        },
        {
            "case_id": "out-four-legged-walk-01",
            "prompt": "规划一个中型犬 12 帧/步的经典四足慢步行走循坏（24fps 下每步半秒），详细列出前后肢落地点、脊椎起伏与足序",
            "assertions": [
                "明确指出四足行走标准足序：左后(LH) -> 左前(LF) -> 右后(RH) -> 右前(RF) 或对角支撑交替",
                "明确指出后脚先动并推挤躯干向前，前脚负责支撑刹车与引导演进",
                "包含肩胛骨与骨盆高低交替运动及头部/尾巴的滞后摆动",
                "给出 1-12 帧关键帧、过客帧与支撑帧的结构分布"
            ]
        }
    ]
}

out_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\cartoon-animation\evals")
out_dir.mkdir(parents=True, exist_ok=True)
suite_file = out_dir / "eval-suite.json"
suite_file.write_text(json.dumps(eval_suite, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Written eval suite: {suite_file}")
