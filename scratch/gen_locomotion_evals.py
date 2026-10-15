import json
import os

eval_set = {
    "suite_id": "suite.locomotion-and-fx-dynamics",
    "book_id": "locomotion-and-fx-dynamics",
    "trigger_cases": [
        {
            "case_id": "eval-01",
            "query": "如何在动画中制作角色全速冲刺（Sprint）的8帧循环？需要哪些相位Pose和前倾角度？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.human-run-and-sprint-mechanics",
            "type": "positive"
        },
        {
            "case_id": "eval-02",
            "query": "角色跑步时脚底在地面滑动打滑，像在溜冰一样，该如何排查和修正地面接触？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.human-run-and-sprint-mechanics",
            "type": "positive"
        },
        {
            "case_id": "eval-03",
            "query": "立定跳远起跳前需要下蹲蓄力几帧？空中最高点如何调出牛顿抛物线挂壁感？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.jump-leap-and-land-impact",
            "type": "positive"
        },
        {
            "case_id": "eval-04",
            "query": "角色从高处跳下落地时感觉像刚体塑料玩偶直接砸在地上，怎么做深蹲吸能缓冲和解耦？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.jump-leap-and-land-impact",
            "type": "positive"
        },
        {
            "case_id": "eval-05",
            "query": "四足猎豹全速疾驰大跑（Gallop）时，收拢腾空与舒展腾空的脊椎形变规律是什么？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.quadruped-locomotion-walk-trot-gallop",
            "type": "positive"
        },
        {
            "case_id": "eval-06",
            "query": "怎么做狗的慢步（Walk）四拍节拍？如何避免前后腿顺拐？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.quadruped-locomotion-walk-trot-gallop",
            "type": "positive"
        },
        {
            "case_id": "eval-07",
            "query": "鹰等大型猛禽在滑翔和向下扑翼时，翅膀多关节与初级飞羽的波浪传导时序是怎样的？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.avian-aerodynamics-flight-and-glide",
            "type": "positive"
        },
        {
            "case_id": "eval-08",
            "query": "为什么鸟类翅膀扇动看起来像两块硬纸板？上提和下拍的流体力学几何差异在哪里？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.avian-aerodynamics-flight-and-glide",
            "type": "positive"
        },
        {
            "case_id": "eval-09",
            "query": "制作大鱼游动时，身体正弦横波推进的振幅随身长递增公式是什么？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.aquatic-fish-and-reptile-undulation",
            "type": "positive"
        },
        {
            "case_id": "eval-10",
            "query": "小鱼游动时的突刺-滑行（Burst-and-Coast）非线性节奏在 24fps 下如何分层 K 帧？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.aquatic-fish-and-reptile-undulation",
            "type": "positive"
        },
        {
            "case_id": "eval-11",
            "query": "制作鞭子甩动（Whip Snap）时，为什么末端线速度会突破音速？关键折返帧怎么定？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.wave-and-whip-secondary-curves",
            "type": "positive"
        },
        {
            "case_id": "eval-12",
            "query": "狐狸尾巴或飘带在运动时，如何通过逐级延迟时间偏置（Offset）做出自然的S形波浪？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.wave-and-whip-secondary-curves",
            "type": "positive"
        },
        {
            "case_id": "eval-13",
            "query": "石头砸入水面形成的皇冠水花（Crown Splash）和中间冲起的中央水柱（Worthington Jet）演化时序是怎样的？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.water-splash-droplet-and-ripples",
            "type": "positive"
        },
        {
            "case_id": "eval-14",
            "query": "水面重力涟漪扩散时，为什么同心圆波长向外拉长而振幅按几何级数衰减？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.water-splash-droplet-and-ripples",
            "type": "positive"
        },
        {
            "case_id": "eval-15",
            "query": "海浪在浅水区变陡并形成中空圆筒卷浪（Barrel Roll）向下跌落的流体动力学过程是怎样的？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.water-waves-surge-and-turbulent-foam",
            "type": "positive"
        },
        {
            "case_id": "eval-16",
            "query": "巨浪拍在礁石上破碎后，白色网状泡沫丝（Foam Texture）在沙滩上的消散时滞如何处理？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.water-waves-surge-and-turbulent-foam",
            "type": "positive"
        },
        {
            "case_id": "eval-17",
            "query": "火焰为什么在上升过程中会发生火舌撕裂（Pinching & Detachment）并脱离成独立游离火球？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.fire-combustion-tongues-and-eddies",
            "type": "positive"
        },
        {
            "case_id": "eval-18",
            "query": "营火或火把的内焰与外焰温度分层及颜色渐变如何设计才能避免纯橙色的扁平感？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.fire-combustion-tongues-and-eddies",
            "type": "positive"
        },
        {
            "case_id": "eval-19",
            "query": "烟雾从轻烟的平滑层流转为紊流螺旋的物理临界点在哪里？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.smoke-exhaust-and-thermal-plumes",
            "type": "positive"
        },
        {
            "case_id": "eval-20",
            "query": "爆炸升腾蘑菇云的垂直气柱喷射与顶帽翻卷展开在 24fps 下的帧数标尺如何划分？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.smoke-exhaust-and-thermal-plumes",
            "type": "positive"
        },
        {
            "case_id": "eval-21",
            "query": "雷电动画中微弱阶跃先导与单帧全白主回击爆闪的强烈反差时序该如何编排？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.lightning-arc-and-flash-burst",
            "type": "positive"
        },
        {
            "case_id": "eval-22",
            "query": "制作大爆炸特效时，为什么第一帧必须爆发超音速激波光环，碎片的初速度如何分层？",
            "expected_capability": "cap.locomotion-and-fx-dynamics.explosion-shockwave-and-debris-field",
            "type": "positive"
        },
        {
            "case_id": "eval-23",
            "query": "如何构思一部动画长片的三幕式剧本高潮与角色性格弧光？",
            "expected_capability": None,
            "type": "negative"
        },
        {
            "case_id": "eval-24",
            "query": "分镜故事板中如何规划双人正反打镜头的 180 度轴线规则？",
            "expected_capability": None,
            "type": "negative"
        }
    ]
}

target_eval = r"books\locomotion-and-fx-dynamics\.cangjie\evals\eval_set.json"
with open(target_eval, 'w', encoding='utf-8') as f:
    json.dump(eval_set, f, ensure_ascii=False, indent=2)

print(f"Clean written eval_set.json at {target_eval} with {len(eval_set['trigger_cases'])} cases.")
