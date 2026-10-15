# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.stop-staring.viseme-ortho-matrix | 口型正交解耦与视素矩阵 | critical | 设计无冲突的口型动画目标体系统；将语音音标转换为三维角色口型状态矢量；解决多音素连续发音时的嘴角穿插冲突 | 视素、Viseme、开合轴、Open-Closed、宽窄轴、Wide-Narrow、正交矩阵、Orthogonal | capabilities/viseme-ortho-matrix.md |
| cap.stop-staring.lip-sync-pipeline | 工业级对白口型动画流水线 | critical | 制作长段角色台词对白口型动画；排查口型滞后于声音的视听不同步缺陷；规范口型关键帧的分层打标流程 | 口型流水线、Lip Sync、超前量、Advance Rule、分层动画、接触辅音、MBP、FV | capabilities/lip-sync-pipeline.md |
| cap.stop-staring.facial-edge-flow-topology | 面部环形循环布线与形变拓扑 | critical | 构建支持高精度面部形变的三维头部拓扑；排查嘴角与眼周在拉伸时的光影撕裂缺陷；布置眼口鼻三大表情区域的同心环形布线 | 边流、Edge Flow、同心环、Loops、口轮匝肌、眼轮匝肌、鼻唇沟、极点隔离 | capabilities/facial-edge-flow-topology.md |
| cap.stop-staring.additive-blendshape-math | 无冲突加算目标体与权重渐变算法 | critical | 编写表情绑定目标体的差分权重计算脚本；将对称雕刻的完整表情拆分为独立的左右半脸目标体；消除微笑与张嘴同时激活时的顶点超调撕裂 | 加算目标体、Additive Blendshapes、差分矢量、Delta、余弦衰减、Taper、中线分离 | capabilities/additive-blendshape-math.md |
| cap.stop-staring.mouth-cavity-teeth-tongue | 口腔结构工程：牙弓与舌头多段变形 | high | 绑定三维角色牙齿与下巴旋转关节；制作舌头在发 L/TH/S 音时的卷曲变形；构建暗色防漏光的封闭口腔壁几何体 | 牙弓、Dental Arch、下颌铰链、Jaw Joint、舌头三段变形、Tongue Rig、口腔壁 | capabilities/mouth-cavity-teeth-tongue.md |
| cap.stop-staring.brow-emotion-mechanics | 眉毛三轴情绪解剖学与形态构建 | high | 设计表达悲伤、惊讶、狂怒或怀疑的眉毛形态；绑定单侧独立挑眉与眉心纵向皱纹挤压；解决双眉聚拢时的中线顶点相撞穿插 | 眉毛解耦、Inner Brow、Outer Brow、眉心挤压、Brow Squeeze、额头折痕、Wrinkle Maps | capabilities/brow-emotion-mechanics.md |
| cap.stop-staring.eyelid-expression-tension | 上下眼睑情绪张力与注视感知 | high | 制作真笑时的眼周微表情挤压 (Duchenne Smile)；调配狐疑、蔑视、惊恐等细微眼神状态；校准摄影机视角下的角膜高光与真实注视线偏差 | 上眼睑、Upper Lid、下眼睑、Lower Lid、真笑挤压、Squint、视线感知、Eyeline | capabilities/eyelid-expression-tension.md |
| cap.stop-staring.eye-rig-lid-follow-saccades | 眼球追踪眼睑跟随与扫视跳跃绑定 | critical | 构建眼球 Aim 约束与眼睑自动跟随联动网络；制作自然生动、拒绝平滑漂移的眼球注视动画；消除眼球向下看时露白严重的死鱼眼穿帮 | 眼球追踪、Eye Aim、眼睑跟随、Lid Follow、扫视、Saccades、视线微跳、Eye Darts | capabilities/eye-rig-lid-follow-saccades.md |
| cap.stop-staring.blink-dynamics-thought-break | 眨眼动力学与思维顿悟阻断机制 | high | 制作富有呼吸感与生命力的自然眨眼动画；在角色思考、下定决心或视线转移节点编排眨眼；排查机械对称节拍器眨眼的动画缺陷 | 眨眼动力学、Blink Timing、非对称曲线、思维句号、Mental Punctuation、视线同步 | capabilities/blink-dynamics-thought-break.md |
| cap.stop-staring.zipper-lips-sticky-rig | 拉链嘴唇渐进粘连绑定 | high | 绑定逼真的写实嘴角黏膜粘连效果；解决角色微张嘴说话时嘴角边缘呈现生硬折角的缺陷；构建单侧独立撇嘴粘连控制网络 | 拉链唇、Zipper Lips、嘴角粘连、Sticky Lips、距离衰减、Distance Remap | capabilities/zipper-lips-sticky-rig.md |
| cap.stop-staring.slider-interface-driver-rig | 二维滑块面部控制器界面与驱动键约束 | critical | 搭建直观高效的 Osipa 风格 2D 面部控制面板；使用 Set Driven Key (SDK) 连接控制器与底层目标体；限制控制器位移范围以避免非法目标体超调破面 | 二维滑块、2D Slider、控制面板、Interface、驱动键、Set Driven Key、边界限制 | capabilities/slider-interface-driver-rig.md |
| cap.stop-staring.squoosh-head-squash-stretch | 头部整体 Squoosh 挤压拉伸多层变形绑定 | high | 为角色头部添加夸张的卡通挤压拉伸变形器；保证头部剧烈形变时面部微表情与口型仍可正常播放；计算头颅挤压拉伸时的横向体积守恒补偿因子 | Squoosh、挤压拉伸、Squash and Stretch、分层变形、晶格绑定、Lattice、体积守恒 | capabilities/squoosh-head-squash-stretch.md |
