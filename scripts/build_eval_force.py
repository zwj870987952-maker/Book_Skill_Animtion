import json
from pathlib import Path

eval_suite = {
    "suite_id": "eval.force-life-drawing.v1",
    "pack_slug": "force-life-drawing",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": [
        {
            "case_id": "case-force-directional-applied-01",
            "prompt": "在画动态速写时，如何分析人体的受力矢量？顺流推进的方向力（Directional Force）与遭遇骨骼支点的施加力（Applied Force）是怎么相互转化的？",
            "should_trigger": True,
            "expected_capability": "directional-applied-force"
        },
        {
            "case_id": "case-force-rhythm-rollercoaster-01",
            "prompt": "为什么速写角色看起来肢体散架互不相干？如何用滑雪跳台比喻（Ski Slope Analogy）让能量从一侧凸面连续顺滑反弹至对侧凹面，构建过山车力量闭环？",
            "should_trigger": True,
            "expected_capability": "force-rhythm-rollercoaster"
        },
        {
            "case_id": "case-opposing-torso-01",
            "prompt": "人体躯干怎么画才充满动力学扭矩？胸腔和骨盆的反向倾斜（Counter-Tilt）与反向扭转该如何配合？怎样表现挤压侧（Squash）与拉伸侧（Stretch）的楔形对立？",
            "should_trigger": True,
            "expected_capability": "opposing-curves-torso"
        },
        {
            "case_id": "case-wrapping-cross-contour-01",
            "prompt": "不打复杂素描调子，如何用环绕包裹线（Wrapping Lines）交代手臂和大腿的三维空间进深？视平线高低是如何决定横截面圆弧的弯曲朝向的？",
            "should_trigger": True,
            "expected_capability": "wrapping-lines-cross-contour"
        },
        {
            "case_id": "case-straight-vs-curved-01",
            "prompt": "为什么给大腿和小腿两侧都画对称圆弧看起来像充气香肠？直线对抗曲线（Straight vs. Curved）的美学法则是什么？骨骼支撑侧和发力侧该怎么配对？",
            "should_trigger": True,
            "expected_capability": "straight-vs-curved-shapes"
        },
        {
            "case_id": "case-asymmetry-thirds-01",
            "prompt": "为什么弧顶在 50% 正中央的曲线没有推进方向感？三分法则（Law of Thirds）是如何通过将曲线顶点偏向 1/3 处来创造动态推力加速度的？",
            "should_trigger": True,
            "expected_capability": "asymmetry-law-of-thirds"
        },
        {
            "case_id": "case-silhouette-negative-01",
            "prompt": "如何用 0.1 秒纯黑剪影测试检验动作的瞬间可读性？肢体与躯干之间构成的张力锐角三角形负空间该如何设计？",
            "should_trigger": True,
            "expected_capability": "silhouette-negative-space"
        },
        {
            "case_id": "case-clothing-folds-01",
            "prompt": "衣服不是死皮，服装衣褶受骨骼支撑点和重力影响的规律是什么？管状褶、半圆褶、螺旋褶和之字褶分别是在什么力学条件下产生的？",
            "should_trigger": True,
            "expected_capability": "fabric-drape-folds-mechanics"
        },
        {
            "case_id": "case-quick-sketch-01",
            "prompt": "在地铁或街头画真实路人，人一直在动根本不给摆姿势，如何用 5 秒骨架抓捕法和 30 秒叙事速写流抓住人物的重心与生活人情味？",
            "should_trigger": True,
            "expected_capability": "quick-sketch-reportage"
        },
        {
            "case_id": "case-animal-homology-01",
            "prompt": "画狗、猫和奔马时总是把前后腿关节画折断，人类手臂与腿部和四足哺乳动物的前膝、后飞节在骨骼同源上是怎么对应的？四足脊椎波浪力量怎么传导？",
            "should_trigger": True,
            "expected_capability": "human-animal-comparative-force"
        },
        {
            "case_id": "case-negative-sql-query-01",
            "prompt": "在 PostgreSQL 中使用 EXPLAIN ANALYZE 排查一个带 JSONB 字段的 GIN 索引慢查询",
            "should_trigger": False,
            "negative_reason": "超出人体速写与角色动态设计范围，属于数据库技术"
        },
        {
            "case_id": "case-negative-cloud-docker-01",
            "prompt": "编写一个 Kubernetes StatefulSet 部署清单，挂载动态 PVC 存储卷并配置反亲和性拓扑分布",
            "should_trigger": False,
            "negative_reason": "超出美术造型与人体运动力学范围，属于云原生容器架构"
        }
    ],
    "output_cases": [
        {
            "case_id": "out-contrapposto-rhythm-01",
            "prompt": "为经典单脚承重站姿（Contrapposto）规划全套力量过山车流线，详细说明头部、胸腔、骨盆、承重腿与放松腿之间的对立力量流与直曲对抗",
            "assertions": [
                "明确指出承重侧骨盆高高顶起（Applied Force 碰撞点），胸腔向对侧反向倾斜（Counter-Tilt）形成楔形夹角",
                "明确指出承重腿侧由骨骼长直线主导（Straight for Support），非承重放松腿由肌肉 C 弧主导",
                "包含能量从头部经胸腔、反弹至骨盆大转子、再贯穿承重腿直插地面的无间断力量节奏（Force Rhythm）",
                "指出腹部受压侧（Squash）肉褶与对侧拉伸侧（Stretch）长平线的张力对立"
            ]
        },
        {
            "case_id": "out-clothing-folds-01",
            "prompt": "分析一个身披长风衣坐姿靠椅角色，从骨骼支撑点、重力下拉以及布料动力学角度，详细列举各部位产生的衣褶类型及力学成因",
            "assertions": [
                "明确指出双肩、手肘与膝盖作为关键骨骼支撑点（Points of Support）",
                "指出背部靠椅与臀部坐垫接触面产生的惰性折叠褶（Inert Folds）与重力挤压",
                "指出膝盖弯曲处产生的半锁褶（Half-Lock）以及下垂裤管在脚踝处形成的之字褶（Zigzag Folds）",
                "指出风衣下摆悬空悬挂产生的重力垂直管状褶（Pipe Folds）与两腿之间的落水半圆褶（Swag Folds）"
            ]
        }
    ]
}

out_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-life-drawing\evals")
out_dir.mkdir(parents=True, exist_ok=True)
suite_file = out_dir / "eval-suite.json"
suite_file.write_text(json.dumps(eval_suite, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Written eval suite: {suite_file}")
