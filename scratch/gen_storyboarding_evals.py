import json
import os

eval_set = {
    "suite_id": "suite.storyboarding-and-master-shots",
    "book_id": "storyboarding-and-master-shots",
    "trigger_cases": [
        {
            "case_id": "eval-01",
            "query": "如何在分镜头中规划从极远景（ELS）到大特写（ECU）的六级景别梯次推进？肖像特写为什么推荐用85mm镜头？",
            "expected_capability": "cap.storyboarding-and-master-shots.shot-sizes-and-camera-optics",
            "type": "positive"
        },
        {
            "case_id": "eval-02",
            "query": "广角镜头拍摄人物贴面特写时产生的严重桶形畸变在视听心理学中会传达什么感受？该如何避免？",
            "expected_capability": "cap.storyboarding-and-master-shots.shot-sizes-and-camera-optics",
            "type": "positive"
        },
        {
            "case_id": "eval-03",
            "query": "双人对话中如何划定180度假想动作轴线？如果导演确实需要换到轴线对侧，有哪些合法的过轴走廊？",
            "expected_capability": "cap.storyboarding-and-master-shots.axis-of-action-and-180-rule",
            "type": "positive"
        },
        {
            "case_id": "eval-04",
            "query": "分镜剪辑中出现恶性跳轴导致两人视线都看向屏幕右侧，观众会产生什么错觉？如何修正？",
            "expected_capability": "cap.storyboarding-and-master-shots.axis-of-action-and-180-rule",
            "type": "positive"
        },
        {
            "case_id": "eval-05",
            "query": "摄影机推镜头（Dolly In）与变焦放大（Zoom In）在光学透视和心理聚焦上有何本质区别？",
            "expected_capability": "cap.storyboarding-and-master-shots.camera-movement-and-dynamic-tracking",
            "type": "positive"
        },
        {
            "case_id": "eval-06",
            "query": "横移跟拍镜头（Tracking Shot）中如何利用前景、中景与背景的三层速度差制造强烈的视差运动？",
            "expected_capability": "cap.storyboarding-and-master-shots.camera-movement-and-dynamic-tracking",
            "type": "positive"
        },
        {
            "case_id": "eval-07",
            "query": "好莱坞经典场面覆盖（Coverage）如何通过主镜头（Master）、双人中景与过肩对构成安全剪辑网？",
            "expected_capability": "cap.storyboarding-and-master-shots.master-shot-staging-and-coverage",
            "type": "positive"
        },
        {
            "case_id": "eval-08",
            "query": "室内戏如何通过三维走位阻塞（Blocking）打破两人并排坐沙发的扁平舞台剧感？",
            "expected_capability": "cap.storyboarding-and-master-shots.master-shot-staging-and-coverage",
            "type": "positive"
        },
        {
            "case_id": "eval-09",
            "query": "对话正反打中外侧过肩镜头（OTS）与内侧纯净单人特写（Clean Single）传达的心理亲密感有何不同？",
            "expected_capability": "cap.storyboarding-and-master-shots.dialogue-shot-reverse-shot-mechanics",
            "type": "positive"
        },
        {
            "case_id": "eval-10",
            "query": "为什么角色的面部前方必须保留2/3的朝向留白（Looking Room）？视线高度高低差如何匹配？",
            "expected_capability": "cap.storyboarding-and-master-shots.dialogue-shot-reverse-shot-mechanics",
            "type": "positive"
        },
        {
            "case_id": "eval-11",
            "query": "动作追逐戏中如何维持逃逸者与追击者的屏幕动势矢量一致性？正面拦截该如何切镜？",
            "expected_capability": "cap.storyboarding-and-master-shots.dynamic-action-and-fight-choreography",
            "type": "positive"
        },
        {
            "case_id": "eval-12",
            "query": "分镜中格斗出拳命中的瞬间冲击卡点（Impact Framing）与受力击飞在时序上如何安排？",
            "expected_capability": "cap.storyboarding-and-master-shots.dynamic-action-and-fight-choreography",
            "type": "positive"
        },
        {
            "case_id": "eval-13",
            "query": "为什么动作剪接（Cut on Action）必须在动作进行到30%-50%中段切镜？如何掩盖剪辑点？",
            "expected_capability": "cap.storyboarding-and-master-shots.continuity-editing-and-cutting-on-action",
            "type": "positive"
        },
        {
            "case_id": "eval-14",
            "query": "连续拍摄同一主体时30度法则和景别跃迁阈值是什么？J-Cut与L-Cut声音桥梁如何消除生硬感？",
            "expected_capability": "cap.storyboarding-and-master-shots.continuity-editing-and-cutting-on-action",
            "type": "positive"
        },
        {
            "case_id": "eval-15",
            "query": "电影分镜如何通过Z轴深度走位（Z-Axis Blocking）与多重画框（Frame within Frame）制造三维空间纵深？",
            "expected_capability": "cap.storyboarding-and-master-shots.visual-depth-and-blocking-composition",
            "type": "positive"
        },
        {
            "case_id": "eval-16",
            "query": "暗前景、亮中景、暗背景的三明治明暗构图在分镜视觉层级中起什么作用？",
            "expected_capability": "cap.storyboarding-and-master-shots.visual-depth-and-blocking-composition",
            "type": "positive"
        },
        {
            "case_id": "eval-17",
            "query": "平行蒙太奇与交叉剪辑（Cross-cutting）在制造悬念时如何建立统一的倒计时锚点？",
            "expected_capability": "cap.storyboarding-and-master-shots.montage-and-temporal-spatial-transitions",
            "type": "positive"
        },
        {
            "case_id": "eval-18",
            "query": "什么是图形匹配剪辑（Graphic Match Cut）？请举例说明其在时空跳跃中的转场隐喻。",
            "expected_capability": "cap.storyboarding-and-master-shots.montage-and-temporal-spatial-transitions",
            "type": "positive"
        },
        {
            "case_id": "eval-19",
            "query": "希区柯克关于桌底炸弹的悬念理论如何阐明信息认知不对称在视听语法中的核心价值？",
            "expected_capability": "cap.storyboarding-and-master-shots.suspense-and-reveal-camera-grammar",
            "type": "positive"
        },
        {
            "case_id": "eval-20",
            "query": "主观POV视点镜头如何通过关注镜头、视点镜头与反应镜头的三步法闭环建立代入感？",
            "expected_capability": "cap.storyboarding-and-master-shots.suspense-and-reveal-camera-grammar",
            "type": "positive"
        },
        {
            "case_id": "eval-21",
            "query": "动画动态故事板预演（Animatic）中如何测算画幅停留时间？对白提前量Pre-lap在时间轴上如何对齐？",
            "expected_capability": "cap.storyboarding-and-master-shots.animatic-timing-and-audio-sync",
            "type": "positive"
        },
        {
            "case_id": "eval-22",
            "query": "低成本电影如何通过单一机位复合长镜头（Single-take Hybrid）靠演员走位无缝覆盖全景到特写？",
            "expected_capability": "cap.storyboarding-and-master-shots.low-budget-master-shots-cinematic-tricks",
            "type": "positive"
        },
        {
            "case_id": "eval-23",
            "query": "在Maya中解算深水海浪FLIP粒子网格时流体黏度参数与阻尼场该如何设置？",
            "expected_capability": None,
            "type": "negative"
        },
        {
            "case_id": "eval-24",
            "query": "编剧在创作故事梗概时如何设计主角的救猫咪（Save the Cat）道德抉择？",
            "expected_capability": None,
            "type": "negative"
        }
    ]
}

target_eval = r"books\storyboarding-and-master-shots\.cangjie\evals\eval_set.json"
with open(target_eval, 'w', encoding='utf-8') as f:
    json.dump(eval_set, f, ensure_ascii=False, indent=2)

print(f"Generated eval_set.json at {target_eval} with {len(eval_set['trigger_cases'])} cases.")
