---
name: physics-for-animators
description: |
  动画与数字资产物理动力学、牛顿力学计算、经典物理仿真与运动规律工程手册。涵盖奇数定律加速度标尺、重力自由落体与抛体运动、重心支撑面稳定平衡、摩擦风阻终端速度、关节生物杠杆与转动惯量、打击冲量动量碰撞、角色跳跃蹬地滞空缓冲全周期、倒单摆行走能量转换、柔性次级运动表面积阻力、液体黏度与浅水碎浪、爆炸火球热涡流与刚体脆性碎裂、物理光照平方反比与阴影半影光学。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.physics-for-animators
  cangjie.capability-count: 12
  cangjie.entrypoint-count: 1
---
# 动画师物理学 — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 纯手绘二维美术角色原画人体线条上色风格设定
- 非物理超现实抽象概念实验动画无重力意识流剪辑
- 动画电影长篇编剧故事大纲与文学剧作台词撰写

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 动画中物体的加速度与间距严格遵循经典力学；恒力加速位移遵循奇数定律 1:3:5:7:9 增量比。
2. 自由下落遵循四分之一半时定理：总时间过半时垂直位移仅完成总高度的 25%，严禁时间过半高度过半的漂浮失真。
3. 角色静力学平衡由重力垂线是否落入触地支撑底面多边形决定；迈步是主动制造失衡再重建平衡的闭环。
4. 打击的破坏力与击退质感不仅取决于碰撞动量，更取决于接触挤压受力时间 delta t（硬撞1帧，软撞6帧）。
5. 跳跃必须由推地蓄力（Push）、空中抛物线滞空（Air）与着地深屈缓冲（Stop）三段动力学闭环组成。
6. 次级悬挂物摆动固有频率由长度平方根主导，严禁不同长度的头发、尾巴和披风在时间轴上一刀切设置相同延迟。

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 计算物体恒力起步加速的逐帧位置；排布起跑加速关键帧间距；消除加速运动机械匀速滑冰感 | references/capabilities/odd-rule-acceleration.md | references/capabilities/gravity-projectile-timing.md、references/capabilities/friction-drag-resistance.md |
| 计算自由下落时间与总帧数；排布投掷物体的抛物线轨迹；排查下落像带降落伞漂浮失重的物理错误 | references/capabilities/gravity-projectile-timing.md | references/capabilities/odd-rule-acceleration.md、references/capabilities/character-jump-mechanics.md、references/capabilities/friction-drag-resistance.md |
| 设计角色单脚站立或极限平衡姿态；判定推搡或失衡跌倒的倾覆临界点；调校弯腰举重物时的身体重心代偿 | references/capabilities/center-of-gravity-balance.md | references/capabilities/character-walk-energy.md、references/capabilities/torque-lever-joints.md |
| 计算物体在不同材质地面的滑行刹车帧数与距离；设定长距离高空跳伞的最高终端速度上限；制作冰面与粗糙地面滑行动画差异 | references/capabilities/friction-drag-resistance.md | references/capabilities/odd-rule-acceleration.md、references/capabilities/gravity-projectile-timing.md |
| 调校空中后空翻或自转的团身加速与展开减速；分析四肢关节挥舞发力的速度杠杆机械效益；消除空中翻滚匀速烤肉串失真 | references/capabilities/torque-lever-joints.md | references/capabilities/center-of-gravity-balance.md、references/capabilities/character-jump-mechanics.md |
| 制作格斗击中下巴的受击后仰与打击定格时序；调校枪械射击与重拳挥出时的身体后坐力传导；消除打斗中像打在棉花上的软弱无力感 | references/capabilities/action-reaction-impact.md | references/capabilities/character-jump-mechanics.md、references/capabilities/torque-lever-joints.md |
| 计算角色跳跃起跳推地、滞空与落地深蹲的精确帧数；制作平台跳跃游戏角色的跳跃力学前摇与后摇；消除起跳像被钢丝吊起、落地像木桩插地的虚假感 | references/capabilities/character-jump-mechanics.md | references/capabilities/gravity-projectile-timing.md、references/capabilities/odd-rule-acceleration.md |
| 调校写实行走重心垂直起伏与前进速度曲线；设置行进中肩部与骨盆的反向三轴旋转互锁；消除角色行走像圆规机械平移木偶的缺陷 | references/capabilities/character-walk-energy.md | references/capabilities/center-of-gravity-balance.md、references/capabilities/torque-lever-joints.md |
| 根据物理长度计算长发与短发马尾辫的摆动周期与延迟帧数；制作披风、旗帜在不同风速与面积下的次级波动；排查次级动画千篇一律统一偏移导致的机械失真 | references/capabilities/drag-follow-through-physics.md | references/capabilities/torque-lever-joints.md、references/capabilities/character-walk-energy.md |
| 制作倒水、倒牛奶与倒蜂蜜的不同流态与线圈堆叠；设计海滩冲浪大浪在近岸变陡并卷管翻倒碎裂的动态；排查液体倒出像果冻胶水或海浪碎浪形态失真 | references/capabilities/liquid-fluid-dynamics.md | references/capabilities/fire-explosion-fracture.md |
| 制作大爆炸火球上升与外翻闭合环形涡流蘑菇云；设计玻璃受冲击破碎或地面受重锤砸裂的裂纹拓扑走向；消除爆炸沦为简单贴图缩放与碎裂杂乱无章的缺陷 | references/capabilities/fire-explosion-fracture.md | references/capabilities/liquid-fluid-dynamics.md、references/capabilities/action-reaction-impact.md |
| 设置 3D 场景灯光物理 Quadratic 平方反比衰减参数；调校人物投影脚底硬接触阴影向头部虚影的渐变过渡；排查室内打光缺乏空间深度或阴影边缘失真的光学缺陷 | references/capabilities/light-shadow-optics.md | references/capabilities/odd-rule-acceleration.md |

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

- 用户仅咨询纯文本剧本创作或美术设定线稿，不涉及物理动力学与动画关键帧时判停
- 已输出明确的物理参数计算、逐帧时间-间距律表与关键姿态力学分析时判停
