# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.physics.odd-rule-acceleration | 奇数定律加速标尺 | critical | 计算物体恒力起步加速的逐帧位置；排布起跑加速关键帧间距；消除加速运动机械匀速滑冰感 | 奇数定律、The Odd Rule、恒力加速、Uniform Acceleration、二次抛物线、间距标尺 | capabilities/odd-rule-acceleration.md |
| cap.physics.gravity-projectile-timing | 自由落体与抛体运动解耦 | critical | 计算自由下落时间与总帧数；排布投掷物体的抛物线轨迹；排查下落像带降落伞漂浮失重的物理错误 | 自由落体、Fourth Down at Half Time、四分之一半时定理、抛体运动、重力加速度、正交解耦 | capabilities/gravity-projectile-timing.md |
| cap.physics.center-of-gravity-balance | 重心稳定与支撑面倾覆判定 | high | 设计角色单脚站立或极限平衡姿态；判定推搡或失衡跌倒的倾覆临界点；调校弯腰举重物时的身体重心代偿 | 质心、Center of Gravity、重力垂线、Line of Gravity、支撑底面、Base of Support、倾覆力矩 | capabilities/center-of-gravity-balance.md |
| cap.physics.friction-drag-resistance | 摩擦阻尼与风阻终端速度 | medium | 计算物体在不同材质地面的滑行刹车帧数与距离；设定长距离高空跳伞的最高终端速度上限；制作冰面与粗糙地面滑行动画差异 | 动摩擦、静摩擦、Friction、刹车减速、空气阻力、终端速度、Terminal Velocity | capabilities/friction-drag-resistance.md |
| cap.physics.torque-lever-joints | 关节生物杠杆与转动惯量调速 | high | 调校空中后空翻或自转的团身加速与展开减速；分析四肢关节挥舞发力的速度杠杆机械效益；消除空中翻滚匀速烤肉串失真 | 转矩、Torque、生物杠杆、Levers、转动惯量、Rotational Inertia、角动量守恒 | capabilities/torque-lever-joints.md |
| cap.physics.action-reaction-impact | 打击冲量与后坐受力时序 | critical | 制作格斗击中下巴的受击后仰与打击定格时序；调校枪械射击与重拳挥出时的身体后坐力传导；消除打斗中像打在棉花上的软弱无力感 | 牛顿第三定律、作用力反作用力、冲量动量定理、Impulse、打击感、后坐力、Recoil、Hit-stop | capabilities/action-reaction-impact.md |
| cap.physics.character-jump-mechanics | 角色跳跃全周期动力学 | critical | 计算角色跳跃起跳推地、滞空与落地深蹲的精确帧数；制作平台跳跃游戏角色的跳跃力学前摇与后摇；消除起跳像被钢丝吊起、落地像木桩插地的虚假感 | 跳跃动力学、Push Time、推地时间、Hang Time、滞空时间、Stop Time、缓冲时间、深蹲缓冲 | capabilities/character-jump-mechanics.md |
| cap.physics.character-walk-energy | 行走倒单摆能量转换与肩髋扭转 | high | 调校写实行走重心垂直起伏与前进速度曲线；设置行进中肩部与骨盆的反向三轴旋转互锁；消除角色行走像圆规机械平移木偶的缺陷 | 倒单摆模型、Inverted Pendulum、行走动力学、肩髋扭转、Counter-rotation、动能势能转换 | capabilities/character-walk-energy.md |
| cap.physics.drag-follow-through-physics | 次级运动长度单摆与表面积风阻 | high | 根据物理长度计算长发与短发马尾辫的摆动周期与延迟帧数；制作披风、旗帜在不同风速与面积下的次级波动；排查次级动画千篇一律统一偏移导致的机械失真 | 次级运动、Drag、Follow-through、单摆周期公式、表面积风阻、发丝摆动、布料波动 | capabilities/drag-follow-through-physics.md |
| cap.physics.liquid-fluid-dynamics | 液体黏度倾倒与浅水碎浪动力学 | medium | 制作倒水、倒牛奶与倒蜂蜜的不同流态与线圈堆叠；设计海滩冲浪大浪在近岸变陡并卷管翻倒碎裂的动态；排查液体倒出像果冻胶水或海浪碎浪形态失真 | 流体动力学、黏度、Viscosity、表面张力、线圈堆叠、Coiling、浅水碎浪、Plunging breaker | capabilities/liquid-fluid-dynamics.md |
| cap.physics.fire-explosion-fracture | 爆炸热浮力涡流与脆性碎裂扩散 | medium | 制作大爆炸火球上升与外翻闭合环形涡流蘑菇云；设计玻璃受冲击破碎或地面受重锤砸裂的裂纹拓扑走向；消除爆炸沦为简单贴图缩放与碎裂杂乱无章的缺陷 | 大爆炸、热浮力、蘑菇云、Vortex Torus、冲击波、脆性碎裂、辐射裂纹、同心环裂纹 | capabilities/fire-explosion-fracture.md |
| cap.physics.light-shadow-optics | 光线平方反比衰减与几何半影光学 | medium | 设置 3D 场景灯光物理 Quadratic 平方反比衰减参数；调校人物投影脚底硬接触阴影向头部虚影的渐变过渡；排查室内打光缺乏空间深度或阴影边缘失真的光学缺陷 | 平方反比定律、Inverse Square Law、本影、Umbra、半影、Penumbra、接触阴影、软阴影 | capabilities/light-shadow-optics.md |
