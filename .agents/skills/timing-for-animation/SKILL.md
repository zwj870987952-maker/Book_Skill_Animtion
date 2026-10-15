---
name: timing-for-animation
description: |
  动画时间掌握、帧数计算、节奏调校与运动规律工程手册。涵盖时空双轴标尺、慢入慢出缓动、动作预感、多级关节延迟、重量感自由落体、人类双足行走奔跑、四足动物步态、对白口型提前量、摄影机平移防频闪与高速动作跳帧排障。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.timing-for-animation
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# 动画的时间掌握 — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 剧本文学剧作构思与台词写作
- 角色概念设定与二维上色美术绘制细节
- 3D 角色材质贴图渲染器 Shader 编写

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 动画的重力与力量不是画出来的，而是由帧数（Timing）与空间位移间距（Spacing）共同决定的。
2. 任何动作必须满足视知觉闭环：反向预备蓄力（Anticipation）➔ 极速爆发 ➔ 惯性过冲 ➔ 充分停顿（Hold 8-16帧）。
3. 多级关节必须呈鞭梢状错落延迟到达，严禁所有肢体在同一帧同步停滞。
4. 人类视觉感知慢于听觉约40毫秒，对白口型与动作重音必须比音频发声点提前1-2帧对齐。
5. 极速位移严禁画平庸中间画，必须使用 Smear 变形张或速度线桥接以消除视网膜频闪跳帧。

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 计算动作总帧数与画稿张数；决定采用单格还是双格拍摄；消除动作机械匀速感 | references/capabilities/timing-spacing-core.md | references/capabilities/slow-in-slow-out.md、references/capabilities/weight-force-calculator.md、references/capabilities/camera-motion-timing.md |
| 调节动作的起动加速与刹车减速；排布中间画的间距标尺；调节曲线编辑器贝塞尔切线权重 | references/capabilities/slow-in-slow-out.md | references/capabilities/timing-spacing-core.md、references/capabilities/anticipation-execution.md、references/capabilities/weight-force-calculator.md |
| 设计挥拳、跳跃、冲刺前的蓄力动作；解决动作太快观众视网膜漏看的问题；建立打击感与动作力量 | references/capabilities/anticipation-execution.md | references/capabilities/slow-in-slow-out.md、references/capabilities/hold-and-reaction.md、references/capabilities/fast-action-troubleshooting.md |
| 制作头发、披风、尾巴等柔性次级运动；打破全身关节在同一帧同步停滞的僵硬感；调节手臂挥舞与鞭梢运动 | references/capabilities/follow-through-overlapping.md | references/capabilities/timing-spacing-core.md、references/capabilities/inanimate-physics.md、references/capabilities/walk-run-cycles.md |
| 计算不同重量物体的自由下落与弹跳帧数；制作跳跃落地与重物砸地碰撞；消除物体落地像气球的漂浮失重感 | references/capabilities/weight-force-calculator.md | references/capabilities/timing-spacing-core.md、references/capabilities/slow-in-slow-out.md、references/capabilities/inanimate-physics.md |
| 制作人类无缝行走与跑步循环动画；消除脚底打滑（Foot sliding）；根据角色情绪定制不同步频 | references/capabilities/walk-run-cycles.md | references/capabilities/follow-through-overlapping.md、references/capabilities/quadruped-locomotion.md、references/capabilities/camera-motion-timing.md |
| 制作狗、猫、马等四足动物行走与奔跑；纠正四足动物顺拐与左右对称开合错误；设计四足生物飞奔（Gallop）的脊椎波动 | references/capabilities/quadruped-locomotion.md | references/capabilities/walk-run-cycles.md、references/capabilities/follow-through-overlapping.md |
| 制作受惊、挨打、滑稽 Double-take 反应；解决动画节奏匆忙慌乱、包袱抖不响的问题；设定表情定格与停顿时间 | references/capabilities/hold-and-reaction.md | references/capabilities/anticipation-execution.md、references/capabilities/fast-action-troubleshooting.md |
| 根据对白录音波形制作口型动画；解决口型总是慢半拍对不上声音的问题；排布角色讲话时的头部与手势重音动作 | references/capabilities/dialogue-lip-sync.md | references/capabilities/timing-spacing-core.md、references/capabilities/hold-and-reaction.md |
| 计算摄影机平移摇镜头（Pan）安全速度；消除背景横移时的剧烈频闪（Strobing）与眩晕；锁定角色在平移背景上的奔跑相对位移 | references/capabilities/camera-motion-timing.md | references/capabilities/timing-spacing-core.md、references/capabilities/walk-run-cycles.md、references/capabilities/fast-action-troubleshooting.md |
| 制作极速挥刀、出拳、瞬移闪避动作；消除动作太快产生的脱节跳帧与鬼影闪烁；绘制风格化残影变形张（Smear frame） | references/capabilities/fast-action-troubleshooting.md | references/capabilities/anticipation-execution.md、references/capabilities/camera-motion-timing.md、references/capabilities/hold-and-reaction.md |
| 制作钟摆、吊灯、树枝弹回、天线晃动动画；解决物体振动在快停下时越摆越快的物理故障；计算阻尼衰减各轮极值振幅 | references/capabilities/inanimate-physics.md | references/capabilities/follow-through-overlapping.md、references/capabilities/weight-force-calculator.md、references/capabilities/slow-in-slow-out.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 用户仅需纯文本剧本创作，不涉及动画逐格动作设计时判停
- 已完成帧数计算、间距标尺与关键姿态律表输出时判停
