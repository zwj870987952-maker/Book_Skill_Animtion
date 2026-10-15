import json
from pathlib import Path

eval_suite = {
    "suite_id": "eval.force-character-design.v1",
    "pack_slug": "force-character-design",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": [
        {
            "case_id": "case-opinion-hierarchy-01",
            "prompt": "在画角色概念设计时，为什么老是画得千人一面像塑料模特？如何克服恐惧并用主观观点（Opinion）与金字塔层级（Hierarchy）自顶向下主导设计？",
            "should_trigger": True,
            "expected_capability": "opinion-hierarchy-concept"
        },
        {
            "case_id": "case-pushing-poses-angles-01",
            "prompt": "如何把平淡写实的模特动态推向 150% 戏剧性极值？45° 神奇角度（Amazing Angles）施加力是如何激发高张力反弹曲线与极端挤压拉伸的？",
            "should_trigger": True,
            "expected_capability": "pushing-poses-amazing-angles"
        },
        {
            "case_id": "case-spatial-bounding-box-01",
            "prompt": "如何用六面空间包围盒（Spatial Bounding Box）在二维纸面上画出破屏而出的透视缩短？尺寸即深度与位置即深度两大定律是如何运作的？",
            "should_trigger": True,
            "expected_capability": "spatial-bounding-box-depth"
        },
        {
            "case_id": "case-forceful-triangle-01",
            "prompt": "为什么要在角色设计中抽象出动能三角形（Forceful Triangle）？三角形的锐角顶点是如何充当物理矢量箭头引导观众视线穿透空间的？",
            "should_trigger": True,
            "expected_capability": "forceful-shape-triangle"
        },
        {
            "case_id": "case-law-of-thirds-asymmetry-01",
            "prompt": "为什么力量曲线的最高顶点（Apex）绝不能落在 50% 几何中点？三分法则（Law of Thirds）是如何通过将顶点偏向 1/3 创造弹射加速度的？",
            "should_trigger": True,
            "expected_capability": "shape-bounding-box-asymmetry"
        },
        {
            "case_id": "case-facial-ratios-caricature-01",
            "prompt": "打破古典三庭五眼 1:1:1 均分比例，如何通过戏剧化拉伸或压缩下巴、额头与鼻梁比例，塑造出粗暴打手或阴险巫师的面部性格符号？",
            "should_trigger": True,
            "expected_capability": "facial-ratios-caricature"
        },
        {
            "case_id": "case-tone-value-staging-01",
            "prompt": "画面调子灰蒙蒙或碎成碎花布，如何用受控的 3-4 阶明度系统（Tone & Value）进行舞台调度？如何用最高黑白反差精准锚定叙事焦点？",
            "should_trigger": True,
            "expected_capability": "tone-value-visual-staging"
        },
        {
            "case_id": "case-color-costume-narrative-01",
            "prompt": "服装不仅是好看的贴皮，如何运用冷暖色温与色彩重音（Color Accent）？如何通过布料重力下垂、生活磨损与道具配重代偿诉说角色历史？",
            "should_trigger": True,
            "expected_capability": "color-theory-character-costume"
        },
        {
            "case_id": "case-life-reportage-character-01",
            "prompt": "在地铁或街头画真实路人纪实速写（Reportage），如何抓取最本真的自然生理重心与标志性小动作，并施加 150% 夸张蜕变为动画角色？",
            "should_trigger": True,
            "expected_capability": "life-reportage-to-character"
        },
        {
            "case_id": "case-character-layout-staging-01",
            "prompt": "多角色同框排版（Character Layout）时如何避免画面散乱与角色打架？如何利用主从层级、犬牙交错的高低重叠与动作视线闭环编排力场？",
            "should_trigger": True,
            "expected_capability": "character-layout-staging"
        },
        {
            "case_id": "case-architecture-character-01",
            "prompt": "为什么背后的建筑背景画得像冷冰冰的 CAD 工业图纸？如何赋予房屋屋脊、立柱与门窗以重力下沉与疲惫倾斜的角色生命律动？",
            "should_trigger": True,
            "expected_capability": "architecture-with-character"
        },
        {
            "case_id": "case-anthropomorphic-animal-01",
            "prompt": "设计拟人化动物角色（如疯狂动物城风格），如何保留物种核心骨性力学（如猫犬悬空飞节与吻部），同时同源嫁接人类双足站姿与社会心理？",
            "should_trigger": True,
            "expected_capability": "anthropomorphic-animal-design"
        },
        {
            "case_id": "case-negative-spring-boot-java-01",
            "prompt": "在 Spring Boot 3 中配置 Reactive Redis 连接池与分布式缓存熔断器",
            "should_trigger": False,
            "negative_reason": "超出动画角色设计与动态速写范畴，属于后端微服务技术"
        },
        {
            "case_id": "case-negative-machine-learning-loss-01",
            "prompt": "推导 Transformer 架构中交叉熵损失函数关于注意力权重矩阵的反向传播梯度公式",
            "should_trigger": False,
            "negative_reason": "超出角色造型与速写美学范畴，属于深度学习数学推导"
        }
    ],
    "output_cases": [
        {
            "case_id": "out-thug-character-workflow-01",
            "prompt": "从街头抓捕一名凶悍保镖为原型，详细规划从主观观点提炼、45° 姿态推挤、空间包围盒透视、大形状三分法则、下庭拉伸面部比例到 4 阶明度调度的完整角色设计案",
            "assertions": [
                "明确提出核心主观观点隐喻（如花岗岩石块/开路推土机）",
                "指出前倾与下压姿态推挤至 45° 强施加力角，扩大站立承重多边形",
                "运用空间包围盒建立近大远小的透视压迫感（近端拳头或肩膀放大）",
                "面部重构中指出下庭（下巴）拉长至 60% 以上，额头极度压缩至 15%",
                "运用 4 阶明度系统将最大反差精准投放在面部眼神与拳套武器边缘"
            ]
        },
        {
            "case_id": "out-multicharacter-staging-01",
            "prompt": "规划一个三名盗贼在阴暗酒馆密谋的同框排版（Layout Staging），详细说明角色间的主从层级、高低交错、空间遮挡以及视线闭环流动",
            "assertions": [
                "确立唯一主导主角（Primary Driver）与次级响应者（Subordinate Reactors）的层次分工",
                "运用位置即深度与尺寸即深度建立前景、中景与后景的空间重叠（Overlap）",
                "角色头部呈犬牙交错的高低对角线分布（Staggering），杜绝水平一条线",
                "构建动作手势与视线的闭环回流，确保视觉动能不从画框边缘泄露"
            ]
        }
    ]
}

eval_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-character-design\evals")
eval_dir.mkdir(parents=True, exist_ok=True)
out_file = eval_dir / "eval-suite.json"
out_file.write_text(json.dumps(eval_suite, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Written eval-suite.json successfully: {out_file}")
