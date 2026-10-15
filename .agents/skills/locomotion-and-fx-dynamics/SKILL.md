---
name: locomotion-and-fx-dynamics
description: |
  经典角色运动规律与自然物理特效动力学工业级工程手册。涵盖人类奔跑与极速冲刺六相位步态动力学（步长步频标尺、前倾倾角、蹬地与双重腾空、对角线手臂摆动补偿）、跳跃深蹲蓄力离地滞空与着地屈膝吸能解耦全周期、四足动物慢步四拍非对称交叉/快步对角二拍/疾驰大跑双悬空脊椎强力弹簧步态全谱系、飞禽多关节波浪气动做功与折叠滑翔、游鱼与两栖爬行正弦波推进振幅渐增律与突刺滑行节拍、曲线运动柔软链条节节贯穿与甩鞭效应动量聚焦折返回抽、水滴表面张力形变与皇冠水花/中央射流/同心圆涟漪、近岸浅水卷浪中空圆筒（Barrel Roll）与白色紊流网状泡沫消散时滞、火焰热浮力加速与火舌S弯撕裂脱离消散、轻烟层流转紊流与浓烟滚涌多级涡环/爆炸蘑菇云热羽流、雷电阶跃先导分叉与单帧全白主回击爆闪极差、超音速爆炸光爆激波面与固体碎片变初速抛体场全套工业规范。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.locomotion-and-fx-dynamics
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# 动画运动规律与自然特效动力学全景工程手册 — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 剧本写作与故事结构创作（请参阅故事与编剧类相关手册）
- 电影分镜头脚本与镜头语法设计（请参阅分镜与电影语言相关手册）
- 三维解算软件具体渲染器着色器底层着色代码（如Arnold/V-Ray C++底层API）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 双足奔跑零双重支撑律：奔跑必须彻底消除双重支撑，由单足支撑与双足腾空交替循环构成，全速冲刺腾空期占比达 50% 以上。
2. 跳跃牛顿冲量与滞空挂壁法则：起跳蓄力深蹲深度与离地初速度严格匹配，最高极值点保留 2-4 帧微弱位移挂壁感，着地必须解耦至少 3 帧垂直下沉缓冲。
3. 四足动物对角相位锁定律：四足慢步严格遵守左后→左前→右后→右前四拍三角支撑，大跑必须展现极度收拢拱背与极度舒展张开的双重悬空期。
4. 飞禽扑翼气动流体不对称律：做功下拍翅膀完全平展倒U形密封推风，减阻上提三关节折叠顺流切开空气，严禁硬纸板对称扇动。
5. 水生鱼类正弦横波渐增律：鱼体推进波自颈部向尾梢传递，头部微幅摆动锁定视野，尾鳍振幅非线性放大产生反向推力。
6. 软体曲线节节贯穿与逐级延迟律：次级柔韧链条相邻骨骼节点之间恒定顺延 1-2 帧时间偏置，甩鞭尖端在质量锐减下爆发突破音速折返回抽。
7. 流体皇冠水花与中央射流演化：水面撞击必须分层经历极薄射流环、锯齿皇冠水幕升起、中央水柱垂直冲天回落与外扩重力涟漪。
8. 海浪卷浪中空管道与泡沫消散时滞：浅水浪头前倾翻越形成中空圆筒（Barrel），破碎后纯白水沫转为网格状泡沫丝并在沙滩滞留消散。
9. 火焰热浮力加速与火舌撕裂模型：基底冷空气卷入形成进气颈缩，中上部在剪切涡流下形成S弯并发生火舌断裂，脱离成独立火球上升熄灭。
10. 浓烟滚涌自持多级涡环律：重型浓烟与爆炸羽流以中心高速外围卷吸形成自翻滚甜甜圈结构，体积随高度呈三次方非线性剧烈膨胀。
11. 雷电先导微弱与主回击极亮爆闪极差律：数帧锯齿树状微弱先导下探触地后，瞬间引爆 1 帧核心主干极亮纯白过曝，全屏白闪伴随蓝紫残影渐隐。
12. 爆炸超音速激波面与碎片初速度分层律：爆心第一帧爆发 70% 尺寸火球并推开半透明折射激波光环，刚性碎片以极高初速度射穿火球沿抛物线抛射。

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 如何实现人类奔跑与极速冲刺动力学（双足奔跑六相位与步长步频标尺）；应用人类奔跑与极速冲刺动力学（双足奔跑六相位与步长步频标尺）的动作规律与物理特效设计规范；排查人类奔跑与极速冲刺动力学（双足奔跑六相位与步长步频标尺）相关的常见动画与动力学反模式 | references/capabilities/human-run-and-sprint-mechanics.md | references/capabilities/jump-leap-and-land-impact.md、references/capabilities/wave-and-whip-secondary-curves.md |
| 如何实现跳跃蹬地腾空与着地冲击缓冲全周期（预备深蹲与抛物线挂壁）；应用跳跃蹬地腾空与着地冲击缓冲全周期（预备深蹲与抛物线挂壁）的动作规律与物理特效设计规范；排查跳跃蹬地腾空与着地冲击缓冲全周期（预备深蹲与抛物线挂壁）相关的常见动画与动力学反模式 | references/capabilities/jump-leap-and-land-impact.md | references/capabilities/human-run-and-sprint-mechanics.md、references/capabilities/wave-and-whip-secondary-curves.md |
| 如何实现四足动物步态全谱系（慢步四拍三角、小跑对角二拍与大跑双悬空）；应用四足动物步态全谱系（慢步四拍三角、小跑对角二拍与大跑双悬空）的动作规律与物理特效设计规范；排查四足动物步态全谱系（慢步四拍三角、小跑对角二拍与大跑双悬空）相关的常见动画与动力学反模式 | references/capabilities/quadruped-locomotion-walk-trot-gallop.md | references/capabilities/avian-aerodynamics-flight-and-glide.md、references/capabilities/aquatic-fish-and-reptile-undulation.md |
| 如何实现飞禽气动力学与振翅滑翔（大鸟重力滑翔与三段式多关节波浪）；应用飞禽气动力学与振翅滑翔（大鸟重力滑翔与三段式多关节波浪）的动作规律与物理特效设计规范；排查飞禽气动力学与振翅滑翔（大鸟重力滑翔与三段式多关节波浪）相关的常见动画与动力学反模式 | references/capabilities/avian-aerodynamics-flight-and-glide.md | references/capabilities/quadruped-locomotion-walk-trot-gallop.md、references/capabilities/aquatic-fish-and-reptile-undulation.md |
| 如何实现游鱼与两栖爬行正弦波推进（大鱼全身S波传导与小鱼突刺滑行）；应用游鱼与两栖爬行正弦波推进（大鱼全身S波传导与小鱼突刺滑行）的动作规律与物理特效设计规范；排查游鱼与两栖爬行正弦波推进（大鱼全身S波传导与小鱼突刺滑行）相关的常见动画与动力学反模式 | references/capabilities/aquatic-fish-and-reptile-undulation.md | references/capabilities/avian-aerodynamics-flight-and-glide.md、references/capabilities/wave-and-whip-secondary-curves.md |
| 如何实现曲线运动波浪与鞭形次级传导（根部驱动节节贯穿与甩鞭能量聚焦）；应用曲线运动波浪与鞭形次级传导（根部驱动节节贯穿与甩鞭能量聚焦）的动作规律与物理特效设计规范；排查曲线运动波浪与鞭形次级传导（根部驱动节节贯穿与甩鞭能量聚焦）相关的常见动画与动力学反模式 | references/capabilities/wave-and-whip-secondary-curves.md | references/capabilities/human-run-and-sprint-mechanics.md、references/capabilities/water-splash-droplet-and-ripples.md |
| 如何实现水特效动力学：水滴、皇冠水花与扩散涟漪（表面张力与中央射流）；应用水特效动力学：水滴、皇冠水花与扩散涟漪（表面张力与中央射流）的动作规律与物理特效设计规范；排查水特效动力学：水滴、皇冠水花与扩散涟漪（表面张力与中央射流）相关的常见动画与动力学反模式 | references/capabilities/water-splash-droplet-and-ripples.md | references/capabilities/water-waves-surge-and-turbulent-foam.md、references/capabilities/wave-and-whip-secondary-curves.md |
| 如何实现水特效动力学：涌浪、破碎翻滚与紊流泡沫（近岸卷浪与泡沫时滞）；应用水特效动力学：涌浪、破碎翻滚与紊流泡沫（近岸卷浪与泡沫时滞）的动作规律与物理特效设计规范；排查水特效动力学：涌浪、破碎翻滚与紊流泡沫（近岸卷浪与泡沫时滞）相关的常见动画与动力学反模式 | references/capabilities/water-waves-surge-and-turbulent-foam.md | references/capabilities/water-splash-droplet-and-ripples.md、references/capabilities/explosion-shockwave-and-debris-field.md |
| 如何实现火焰燃烧动力学：火苗、火舌撕裂与热涡流（浮力加速与独立火球）；应用火焰燃烧动力学：火苗、火舌撕裂与热涡流（浮力加速与独立火球）的动作规律与物理特效设计规范；排查火焰燃烧动力学：火苗、火舌撕裂与热涡流（浮力加速与独立火球）相关的常见动画与动力学反模式 | references/capabilities/fire-combustion-tongues-and-eddies.md | references/capabilities/smoke-exhaust-and-thermal-plumes.md、references/capabilities/lightning-arc-and-flash-burst.md |
| 如何实现烟雾与热羽流扩散动力学（轻烟层流转紊流与浓烟多级滚涌涡环）；应用烟雾与热羽流扩散动力学（轻烟层流转紊流与浓烟多级滚涌涡环）的动作规律与物理特效设计规范；排查烟雾与热羽流扩散动力学（轻烟层流转紊流与浓烟多级滚涌涡环）相关的常见动画与动力学反模式 | references/capabilities/smoke-exhaust-and-thermal-plumes.md | references/capabilities/fire-combustion-tongues-and-eddies.md、references/capabilities/explosion-shockwave-and-debris-field.md |
| 如何实现雷电电弧、分叉路径与高能爆闪（阶跃先导分叉与单帧全白主回击）；应用雷电电弧、分叉路径与高能爆闪（阶跃先导分叉与单帧全白主回击）的动作规律与物理特效设计规范；排查雷电电弧、分叉路径与高能爆闪（阶跃先导分叉与单帧全白主回击）相关的常见动画与动力学反模式 | references/capabilities/lightning-arc-and-flash-burst.md | references/capabilities/explosion-shockwave-and-debris-field.md、references/capabilities/fire-combustion-tongues-and-eddies.md |
| 如何实现爆炸能量释放、冲击波与碎片抛体场（超音速火球与碎片变初速抛体）；应用爆炸能量释放、冲击波与碎片抛体场（超音速火球与碎片变初速抛体）的动作规律与物理特效设计规范；排查爆炸能量释放、冲击波与碎片抛体场（超音速火球与碎片变初速抛体）相关的常见动画与动力学反模式 | references/capabilities/explosion-shockwave-and-debris-field.md | references/capabilities/smoke-exhaust-and-thermal-plumes.md、references/capabilities/lightning-arc-and-flash-burst.md |

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

- 已为角色动作或自然物理特效建立完整的帧时序标尺、受力形变分析与防穿帮排障方案
- 已提供各阶段关键帧Pose、Graph Editor曲线切线控制与多层动力学拆解规范
