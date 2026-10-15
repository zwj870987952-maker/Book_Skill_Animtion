# 候选框架池 (Candidate Frameworks)

> 提取器: `framework-extractor`
> 来源书籍: 《动画的时间掌握》（Timing for Animation）- 哈罗德·威特克 & 约翰·哈拉斯
> 说明: 包含思维模型、决策框架、动作机制流程与排障路径。

```yaml
- id: f01
  title: 动画时空双轴决策模型 (Timing vs Spacing)
  type: framework
  source_chapter: 第 4–5 页、第 36–39 页
  source_quote: |
    "时间掌握不仅关系到如何确定动画的间距、张数和画稿在银幕上持续多久才能获得最佳效果，而且关系到影片情节展开的节奏、速度和情调。"
  summary: |
    动作的质感由时间轴（Timing：两张原画之间的曝光帧数）与空间轴（Spacing：中间画在几何路径上的位移分布）共同决定。
    相同的时间长度（如12帧），若中间画均匀分布，表现为机械匀速运动；若中间画靠近一端密集，表现为剧烈加速或减速。
    设计动作时，必须先定关键姿态时间跨度，再定空间轨道的密度标尺（Spacing Chart）。
  inputs:
    - 起止关键姿态（Key A, Key B）
    - 预期总帧数（如 12 帧）
    - 动作的情绪与物理性质（轻快/沉重/受阻）
  steps:
    - 1. 确定两端关键原画的屏幕停留点与空间位置
    - 2. 在时间轴律表（Dope sheet）上分配总曝光格数
    - 3. 绘制中间画标尺（Timing chart），选择 1/2 对分、慢入或慢出
    - 4. 检查是否有物理加速度突变或视觉断层
  outputs:
    - 带有间距刻度的动画标尺与律表分帧编号
  tags: [timing, spacing, core-model, dope-sheet]

- id: f02
  title: 慢进慢出非线性缓动机制 (Slow-in & Slow-out)
  type: framework
  source_chapter: 第 40–45 页
  source_quote: |
    "自然界中几乎没有物体会瞬间达到最大速度，也没有物体会无缓冲地瞬间停止。起动与停顿必须有过渡间距。"
  summary: |
    任何有质量的物体在克服静摩擦力起动、或在制动力作用下停下时，速度均呈 S 型曲线变化。
    起动时原画附近中间画极度密集（Slow-out），中间阶段位移跨度最大（加速通过），接近目标原画时中间画再次密集（Slow-in）。
    在现代数字动画中，对应曲线编辑器（Graph Editor）贝塞尔手柄的平滑加权切线。
  inputs:
    - 初始速度（通常为 0）
    - 目标位置与期望制动时间
  steps:
    - 1. 设定起始原画与结束原画
    - 2. 插入正中间过渡张（Breakdown），打破机械对称，使之偏向某一侧
    - 3. 按照 1/2、1/4 的对半逼近法则在两端极值附近密排中间帧
    - 4. 验证加速度曲线，确保极值处无生硬跳跃
  outputs:
    - 渐变加速度的中间画排布序列
  tags: [ease-in-out, slow-in, slow-out, acceleration]

- id: f03
  title: 视知觉与动作闭环机制 (Anticipation-Action-Reaction Loop)
  type: framework
  source_chapter: 第 6 页、第 50–51 页、第 68–69 页
  source_quote: |
    "好的时间掌握，要有足够的时间先使观众预感到将有什么事情发生，然后用于表现动作本身，最后用来表达对动作的反应。"
  summary: |
    人类视觉无法倒带回看，单一孤立的主动作容易被观众忽略或显得苍白。
    完整的戏剧性动作必须闭环为四阶段：
    1. 预备蓄力（Anticipation）：反方向运动（如出拳前拉后肘），吸引观众视线并积累势能；
    2. 主动作（Action）：极短帧数内完成爆发位移（1–4 帧）；
    3. 追随交搭（Follow-through/Overlapping）：末端惯性冲过终点（Overshoot）；
    4. 停顿反应（Hold/Reaction）：静止停留 6–18 帧，给观众消化情绪与认知。
  inputs:
    - 叙事核心事件（如击打、受惊、跳跃、冲刺）
  steps:
    - 1. 设计反向预备姿态，分配 4–8 帧慢入蓄力
    - 2. 执行核心位移，压缩在 2–4 帧极速释放
    - 3. 实施过冲姿态（Overshoot），并在 3–5 帧内阻尼反弹回稳
    - 4. 设定角色或受体停顿定格（Hold），维持至少 8–16 帧
  outputs:
    - 具备完整戏剧张力与生理说服力的动作分段律表
  tags: [anticipation, action, reaction, perception, timing-loop]

- id: f04
  title: 多级关节鞭梢时序延迟机制 (Hierarchical Joint Transmission)
  type: framework
  source_chapter: 第 32–35 页、第 52–55 页
  source_quote: |
    "力通过有关节的肢体传送时，并不是所有部分同时运动。靠近躯干的关节先动，末梢关节滞后并呈鞭梢状展开。"
  summary: |
    人与动物肢体（如手臂挥舞、腿部踢击）以及软体结构（尾巴、丝带）的动力学本质是多级关节链的力传导。
    根部（Root/Shoulder）先行启动并首先制动；次级关节（Elbow/Knee）延迟 1–2 帧响应；末梢关节（Wrist/Ankle/Hand）延迟 2–4 帧到达极值。
    当根部反向折返时，末梢仍因惯性保持前向运动，形成经典的“S”形或破浪形交搭曲线。
  inputs:
    - 关节骨骼链条结构（主级 ➔ 次级 ➔ 末梢）
    - 动力驱动方向与初速度
  steps:
    - 1. 驱动根部关节运动并确立主动弧线
    - 2. 将次级骨骼的关键帧整体向后偏移 1–2 帧（Frame Offset）
    - 3. 将末端骨骼的关键帧向后偏移 2–4 帧，并加大拖拽角度（Drag）
    - 4. 在根部制动点，让末梢产生向前过冲，随后呈简谐振动收敛
  outputs:
    - 错落有致、无木偶僵硬感的流畅次级运动时序
  tags: [joint-hierarchy, overlapping, follow-through, drag, wave-motion]

- id: f05
  title: 质量与重量感判定换算框架 (Weight & Force Heuristics)
  type: framework
  source_chapter: 第 18–19 页、第 58–65 页
  source_quote: |
    "重量不是靠画稿的外形轮廓表现出来的，而是靠物体起动、停顿、下落及触地变形所消耗的时间决定的。"
  summary: |
    物体的重量感由三项时空指标唯一定义：
    1. 惯性时间：质量越大，克服静止或停止运动所需的时间帧数越长（轻物体起步 1–2 帧，巨型重物起步需 12–24 帧）；
    2. 下落加速度与弹跳周期：下落遵循重力加速度（开始慢、落地极快），轻气球匀速漂浮，保龄球急坠且触地无弹跳反弹；
    3. 挤压变形比（Squash & Stretch）：软物/轻物剧烈变形并多次反弹，重物落地直接将地面砸凹或自身微扁后长停（Heavy Hold）。
  inputs:
    - 物体材质（刚体/弹性体/软泥/重金属）
    - 物体预设重量与体积
  steps:
    - 1. 依据下落高度套用二次方间隔（下落位移按 1:4:9:16 增长）
    - 2. 计算着地接触帧（Impact frame）与挤压张变形量
    - 3. 根据弹性系数分配反弹帧数（保龄球 0 反弹，网球反弹 4–6 次且高度半减）
    - 4. 赋予接地停留（Hold on ground）：越重停留越长
  outputs:
    - 具备明确吨位与质感说服力的下落与碰撞曲线
  tags: [weight, gravity, impact, squash-stretch, physics]

- id: f06
  title: 人类步态循环工程框架 (Human Locomotion Cycles)
  type: framework
  source_chapter: 第 88–91 页、第 108–109 页
  source_quote: |
    "正常人的行走每秒两步（每步12格，共24格为一个完整左右脚循环）。快走每步8-9格，慢步拖行每步16-18格。"
  summary: |
    人类步态循环分为四大关键姿态与骨盆起伏曲线：
    1. 接触姿态（Contact）：双脚同时触地，跨度最大，重心居中；
    2. 下压缓冲（Down）：前脚全掌着地，膝盖弯曲，骨盆降到最低点（吸收重力冲击）；
    3. 通过姿态（Passing）：后脚离地向前摆动，支撑腿伸直，骨盆回升并侧倾；
    4. 蹬地腾空/上升（Up）：支撑腿脚后跟抬起，身体升至最高点，准备进入下一侧 Contact。
    奔跑循环与行走的根本区别在于存在“全腾空悬空相（Air time/No feet on ground）”，且身体前倾角度更大。
  inputs:
    - 行走类型（正常漫步/警惕潜行/欢快蹦跳/负重拖步/急促快跑）
    - 角色体型与性格
  steps:
    - 1. 选定步频节拍模数（12 格/步为基准；8 格为快跑；16 格为沉重缓行）
    - 2. 绘制第 1 帧与第 13 帧的两脚相反接触姿态（Contact）
    - 3. 在中间插入第 4 帧 Down（最低）与第 10 帧 Up（最高）建立重心波浪弧线
    - 4. 反向对称处理后半个循环（第 13–24 帧）
    - 5. 叠加手臂反向摆动（右脚向前则左手向前）与脊椎扭转
  outputs:
    - 无滑步（Foot sliding）、重心扎实的无缝无极循环律表
  tags: [walk-cycle, run-cycle, locomotion, contact-pose, passing-pose]

- id: f07
  title: 四足动物步态时序模型 (Quadruped Locomotion Engine)
  type: framework
  source_chapter: 第 94–99 页
  source_quote: |
    "四足动物行走时四只脚绝不一起移动。行走的标准步序是：左后脚、左前脚、右后脚、右前脚，呈现稳定的三角支撑交替。"
  summary: |
    四足动物因速度提升，其步态时序结构发生本质质变：
    1. 漫步（Walk）：前后斜向对角三角支撑交替，任何瞬间至少有 2–3 只脚着地，脊椎波动平缓；
    2. 小跑/慢跑（Trot）：对角线成对两只脚同时着地（左前+右后，右前+左后），存在微小悬空相；
    3. 飞奔（Gallop）：脊椎剧烈折叠与伸展（弹簧式驱动），后脚推蹬腾空 ➔ 前脚着地支撑 ➔ 悬空收腹抱团，具有大腾空时段。
  inputs:
    - 动物类别（猫科柔韧脊椎 / 犬科刚劲四肢 / 马科蹄类重型躯体）
    - 运动速度等级（Walk, Trot, Canter, Fast Gallop）
  steps:
    - 1. 确定步态类型与步周期帧数（慢走 24–32 帧循环，飞奔 12–16 帧循环）
    - 2. 排布四蹄落地点时序矩阵（后脚驱动先行）
    - 3. 绘制脊椎拱起（Flex）与拉直（Extend）的极限原画
    - 4. 纠正顺拐错误，确保重心在支撑三角形质心投影内
  outputs:
    - 真实符合生物解剖学力学的四足动物循环律表
  tags: [quadruped, animal-locomotion, trot, gallop, spine-wave]

- id: f08
  title: 戏剧停顿与受惊受击反应模型 (Hold & Take Mechanics)
  type: framework
  source_chapter: 第 48–49 页、第 68–69 页
  source_quote: |
    "反应动作（Take）越快越好，但停顿（Hold）必须足够长。如果反应慢了失去喜剧感，如果停顿短了观众根本看不懂发生了什么。"
  summary: |
    角色在受到突发外界刺激（如炸弹爆炸、猛烈挨打、发现惊天秘密）时的标准表演时序：
    1. 预知蓄力（Anticipation 2–3 帧）：微微后退缩起；
    2. 极端爆发（Hit/Flash 1–2 帧）：眼球弹出、下巴掉地或身体极端拉长变形；
    3. 震颤恢复（Vibration 3–4 帧）：身体在目标姿态前后小幅度高速振动；
    4. 呆滞定格（Hold 8–18 帧）：表情完全静止，眼神木讷，留出笑点或惊恐的观众反应窗口。
  inputs:
    - 刺激事件类型与冲击强度
    - 角色滑稽/严肃性格定位
  steps:
    - 1. 设计原画 A（常态）与原画 B（极端受惊变形张）
    - 2. 插入仅 1 帧反向预备，随后跳跃至原画 B（无中间画或仅 1 张速度线）
    - 3. 在原画 B 后紧跟 2–3 张微小摆动的减幅振颤张
    - 4. 锁定在原画 C（呆滞停顿）维持 12 帧以上不动
  outputs:
    - 极具喜剧张力与视听冲击的反应节拍动画
  tags: [take, hold, comedy-timing, shock-reaction, acting]

- id: f09
  title: 声画对齐与视听生理时钟同步框架 (Audio-Visual Lip Sync)
  type: framework
  source_chapter: 第 114–121 页
  source_quote: |
    "人的视觉反应时间比听觉略慢。因此口型在设计表上必须比声音波形发声点提前 1 到 2 格画出，在银幕上看起来才真正同步。"
  summary: |
    人类感官对声光的处理速度不同。如果动画师将嘴唇最大开合帧与音轨重音点精确对齐在同一帧，观众看片时会产生“口型慢半拍”的脱节感。
    必须采用“视觉提前量原则（Visual Lead Principle）”：
    - 闭唇音（B, P, M）：必须在听到声音前 2 帧紧紧闭合，发音瞬时爆破张开；
    - 宽元音（AH, OH）：张口最大幅度需比音频波形峰值提前 1–2 帧到达；
    - 对白重音动作（如重重挥手强调词句）：动作的冲击触点必须在重音词首发音前 2–4 帧到达。
  inputs:
    - 语音对白录音音轨与音频分析表（Phonetic breakdown）
    - 句子逻辑重音标记
  steps:
    - 1. 在摄制表声轨列逐帧标出发音元音（A, E, I, O, U, Consonants）
    - 2. 将每个发音词的核心口型姿态在时间轴上向左提前 1–2 格
    - 3. 忽略极短的无意义滑音，仅抓取核心元音与闭唇辅音（避免嘴部无意义狂抽）
    - 4. 配合眉毛、头部点头重音动作，重音动作比声音提前 2–3 帧触底
  outputs:
    - 自然咬合、生动可信的口型与表情表演设计表
  tags: [lip-sync, audio-sync, dialogue, phonetics, visual-lead]

- id: f10
  title: 摄影机摇移与背景平移防频闪决策框架 (Camera Motion & Pan Control)
  type: framework
  source_chapter: 第 124–127 页
  source_quote: |
    "如果背景平移速度不当，每格位移过大，银幕上就会产生令人难受的频闪（Strobing）或重影现象。"
  summary: |
    在 24fps 放映条件下，摄影机摇镜头（Pan）或角色奔跑时背景反向平移必须满足安全物理位移阈值：
    - 慢速移动：允许双格（On 2s）平移，画面平稳；
    - 中速移动：必须强制单格（On 1s）拍摄，消除断层；
    - 临界危险速度：每格位移若恰好等于垂直线条或物体间距的一半，人眼视觉暂留会产生剧烈频闪倒退错觉；
    - 超高速移动：必须引入背景运动模糊（Motion blur）或横向速度线，不能使用清晰单张平移。
  inputs:
    - 摄影机平移距离与期望完成秒数
    - 画面中垂直物体的密度（如电线杆、栅栏、树林）
  steps:
    - 1. 计算每格位移增量（增量 = 总位移 / 帧数）
    - 2. 检查增量是否落入“频闪危险区”（与背景周期纹理共振区）
    - 3. 若处于危险区，调整镜头秒数，或者采用双层视差平移（Parallax panning）
    - 4. 若角色在平移背景上奔跑，角色脚部后蹬位移必须与背景位移数值绝对恒等（相对位移为零），彻底消除滑步
  outputs:
    - 画面清晰无眩晕、背景与角色脚步严丝合缝的平移摄制指令
  tags: [camera-pan, strobing, parallax, motion-blur, cinematography]

- id: f11
  title: 极速运动跳帧排障机制 (Fast Action Discontinuity Troubleshooting)
  type: framework
  source_chapter: 第 42–43 页、第 102–107 页
  source_quote: |
    "当动作在 2-4 格内跨越大半个银幕时，人眼无法连贯成动作，而是看到两个跳跃的残影。此时必须使用特殊技法建立视觉连续性。"
  summary: |
    故障现象：角色击打或高速穿过银幕时，出现明显的抽搐、跳帧感，观众看不清动作轨迹。
    排障与修复机制决策树：
    1. 判断动作帧数：若位移消耗 1–3 帧，绝不可画写实中间画；
    2. 解决手段 A — 速度线（Speed lines）：在起始与终点之间绘制沿运动弧线的半透明条纹，引导视线贯通；
    3. 解决手段 B — 极端拉长变形（Elongated Inbetween / Smear frame）：将中间 1 帧画成连接起点和终点的面条状残影；
    4. 解决手段 C — 频闪多重影（Multiple images）：在单张画稿中画出同一肢体的 3 个渐变重影；
    5. 强化终点：终点姿态必须 Hold 至少 3–5 帧，让眼睛重新捕捉目标。
  inputs:
    - 高速位移的起止位置与跨度
    - 当前出现的跳帧或视觉断裂症状
  steps:
    - 1. 测量位移跨度是否超过视网膜暂留桥接阈值
    - 2. 移除平庸的中间画，用 Smear 变形张或速度线替换
    - 3. 在动作发生前确保有 3–6 帧充分的反向 Anticipation
    - 4. 在动作终止后添加 6–8 帧的 Overshoot 和 Hold
  outputs:
    - 视觉连贯凌厉、打击感强烈的极速动作序列
  tags: [fast-action, speed-lines, smear-frame, troubleshooting, strobing]

- id: f12
  title: 无生命物体受力与阻尼振荡模型 (Inanimate Physics & Oscillation)
  type: framework
  source_chapter: 第 24–31 页、第 56–57 页
  source_quote: |
    "钟摆或振动的弹簧遵循严格的力学衰减规律：周期恒定，但摆动幅度逐级递减，直至静止。"
  summary: |
    无生命物体（钟摆、下垂绳索、车线天线、弹性跳板）在受力后的运动是标准的简谐衰减振动：
    - 极值点速度为 0（中间画密集 Slow-out / Slow-in）；
    - 平衡位置速度最大（中间画间距最大）；
    - 每一轮往返振荡的振幅呈等比衰减（如 100% ➔ 50% ➔ 25% ➔ 10% ➔ 0）；
    - 振动周期帧数保持恒定（等时性），不可随振幅变小而缩短周期帧数。
  inputs:
    - 物体刚度与阻尼系数
    - 初始外力冲击幅度
  steps:
    - 1. 确定摆动单向半周期帧数（如 8 帧）
    - 2. 绘制各次反向摆动的极限角度（按照衰减比例逐次递减）
    - 3. 在每个半周期内部应用正弦/余弦间距（两端极慢、中间飞快）
    - 4. 衰减至极限残余振幅时，直接转入静止张（Hold）
  outputs:
    - 符合经典弹性力学规律的摆动与恢复律表
  tags: [pendulum, oscillation, damping, inanimate-physics, harmonic-motion]
```
