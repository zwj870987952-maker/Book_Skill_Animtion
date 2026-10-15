# Book_Skill_Animtion: 动画与影视视听 AI 技能体系库

<p align="center">
  <b>基于经典神作蒸馏的 22 部世界级动画、解剖、分镜与视听语言 AI Skills 知识库</b>
</p>

<p align="center">
  <a href="./README.zh-CN.md"><b>简体中文</b></a> ·
  <a href="./README.md"><b>English</b></a>
</p>

---

## 📖 项目简介

**Book_Skill_Animtion** 是专为动画师、概念设计师、三维角色艺术家、分镜师及影视导演打造的 **AI 角色与动画工程技能库**。

本项目通过仓颉知识蒸馏引擎（Cangjie Skill），将全球动画与影视视听领域的 **22 部经典权威原著与工业实践手册** 进行深度解构与工程化提炼，转化为符合 Agent 规范的高密度、可执行、可验证的 **AI Skills**。

每个 Skill 均包含高密度规范指南（`SKILL.md`）、深度工程参考卡片（`references/`）以及结构化评测体系。

---

## 🚀 跨电脑一键安装指南

在任何新电脑上，你可以通过以下极简步骤安装全部动画技能，以便在 **Google Antigravity**、**Claude Code**、**Cursor** 等 AI 工具中即刻使用：

### 1. 克隆本仓库

```bash
git clone https://github.com/zwj870987952-maker/Book_Skill_Animtion.git
cd Book_Skill_Animtion
```

### 2. 运行一键安装脚本

#### Windows 用户 (PowerShell / CMD)
```powershell
# 交互式向导（推荐：支持选择安装平台与路径）
python install.py

# 或自动安装到所有检测到的支持平台（Antigravity、Claude Code、Cursor）
python install.py --all

# 或使用 PowerShell 快捷脚本
.\install.ps1 -All
```

#### macOS / Linux 用户
```bash
# 自动安装到所有已检测到的 AI 平台
python3 install.py --all

# 或使用 shell 脚本
chmod +x install.sh
./install.sh --all
```

### 3. 高级安装选项

```bash
# 列出全部 22 个可用技能
python install.py --list

# 安装到自定义目录
python install.py --target "C:/Users/YourUsername/.gemini/antigravity/skills"

# 使用软链接模式（节省空间，本地修改立即同步生效）
python install.py --all --link

# 仅安装特定技能（例如人体解剖与面部对白）
python install.py --skills anatomy-for-sculptors stop-staring facial-expressions
```

---

## 📚 22 个核心动画/影视 Skills 全景速查表

| # | Skill 名称 (`slug`) | 经典原著 / 领域 | 核心工程能力与规范 |
|---|---|---|---|
| **一** | **角色造型与解剖力学** | | |
| 1 | [`anatomy-for-sculptors`](.agents/skills/anatomy-for-sculptors/SKILL.md) | 《雕塑家人体解剖学》<br>Uldis Zarins | 皮下骨性标志、体块粗模 (Block-out)、肩带复合体 C 形夹钳、对立平衡 (Contrapposto)、足弓力学 |
| 2 | [`facial-expressions`](.agents/skills/facial-expressions/SKILL.md) | 《面部表情圣经与 FACS》<br>Mark Simon / Paul Ekman | FACS 面部动作编码系统、颅骨锚定点、眼轮/口轮匝肌运动解耦、七大核心情绪全参数拓扑 |
| 3 | [`stop-staring`](.agents/skills/stop-staring/SKILL.md) | 《Stop Staring: 面部建模与绑定》<br>Jason Osipa | Osipa 视素双轴正交解耦（开合 vs 宽窄）、对白口型提前量、差分加算目标体、眼睑跟随与眨眼动力学 |
| 4 | [`force-life-drawing`](.agents/skills/force-life-drawing/SKILL.md) | 《FORCE: 动态人体速写》<br>Michael Mattesi | 方向力与施加力物理学、过山车滑雪跳台力流、直线对抗曲线、纯黑剪影测试、衣褶七大经典力学 |
| 5 | [`force-character-design`](.agents/skills/force-character-design/SKILL.md) | 《FORCE: 角色设计与概念造型》<br>Michael Mattesi | 主观戏剧夸张、45° 强角施加力、空间包围盒系统、形状包围盒与三分法则不对称黄金分割 |
| 6 | [`force-animal-drawing`](.agents/skills/force-animal-drawing/SKILL.md) | 《FORCE: 动物动态速写》<br>Michael Mattesi | 蹠行/趾行/蹄行三大运动类群力学、人兽同源关节映射（肘后腕前、膝前踝后）、脊椎弹性动力学 |
| 7 | [`hayama-character-design`](.agents/skills/hayama-character-design/SKILL.md) | 《羽山淳一角色设计与作画实战》<br>羽山淳一 | 单一动作主线 (Line of Action)、极端仰俯十字经纬透视、45° 硬派影线分面、作画监督级时间图表 |
| 8 | [`drawn-to-life`](.agents/skills/drawn-to-life/SKILL.md) | 《大师动态速写与生命律动》<br>Walt Stanchfield | 动词意图驱动、坚韧直线对抗饱满曲线、0.1 秒纯黑剪影、头胸盆三轴反向扭转对抗、线条经济学 |
| **二** | **动画运动规律与力学** | | |
| 9 | [`animators-survival-kit`](.agents/skills/animators-survival-kit/SKILL.md) | 《原画人机密 (ASK)》<br>Richard Williams | 时空双轴标尺 (Timing & Spacing)、原画轨目表、四大黄金行走姿态、步频标尺、涂抹帧与多重肢体 |
| 10 | [`illusion-of-life`](.agents/skills/illusion-of-life/SKILL.md) | 《生命的幻象: 迪士尼动画》<br>Frank Thomas & Ollie Johnston | 迪士尼十二黄金法则、体积守恒挤压拉伸、动作预备 (Anticipation)、正弦跟随重叠、慢入慢出缓冲 |
| 11 | [`cartoon-animation`](.agents/skills/cartoon-animation/SKILL.md) | 《经典卡通动画制作》<br>Preston Blair | 经典卡通头身比、潜行步/阔步/飞轮腿步态库、多级波浪运动、吃惊与双重吃惊反应、Dope Sheet 规范 |
| 12 | [`timing-for-animation`](.agents/skills/timing-for-animation/SKILL.md) | 《动画的时间掌握》<br>Harold Whitaker & John Halas | 逐帧时间掌握与帧数计算、慢入慢出缓动曲线、重力加速度奇数定律、对白口型提前量与防频闪 |
| 13 | [`physics-for-animators`](.agents/skills/physics-for-animators/SKILL.md) | 《动画物理学与动力学》<br>Michele Bousquet | 自由落体、抛体运动、重心支撑面、打击冲量动量碰撞、倒单摆行走、流体与爆炸火球动力学 |
| 14 | [`locomotion-and-fx-dynamics`](.agents/skills/locomotion-and-fx-dynamics/SKILL.md) | 《角色步态力学与自然特效动力学》<br>工业级动画工程经验 | 人类冲刺六相位、跳跃腾空全周期、四足慢步/快步/疾驰步态全谱系、水花/火焰热羽流/雷电特效动力学 |
| **三** | **影视分镜与视听语言** | | |
| 15 | [`framed-ink`](.agents/skills/framed-ink/SKILL.md) | 《Framed Ink: 视觉叙事与分镜》<br>Marcos Mateu-Mestre | 视平线心理学、60-30-10 明度分布与逆光剪影、视线牵引铁轨、三层空间纵深 (前景/中景/背景) |
| 16 | [`storyboard-art`](.agents/skills/storyboard-art/SKILL.md) | 《影视工业标准化分镜手册》<br>Angelo Libutti | 16:9 / 2.39:1 安全框、七级人体解剖非关节裁切标尺、摄影机双线空心箭头系统、动作动量隐形剪辑 |
| 17 | [`storyboarding-and-master-shots`](.agents/skills/storyboarding-and-master-shots/SKILL.md) | 《Master Shots: 影视镜头机位》<br>Christopher Kenworthy | 六级景别心理距离、180° 轴线守恒与五大合法越轴走廊、主镜头 (Master Shot) 三角剖分、OTS 过肩正反打 |
| 18 | [`grammar-of-film-language`](.agents/skills/grammar-of-film-language/SKILL.md) | 《镜头语法》<br>Daniel Arijon | 全球影视导演红宝书、动作轴线守恒、三角形机位系统、视线对撞几何学、长镜头场面调度 |
| 19 | [`comics-grammar-and-sequential-art`](.agents/skills/comics-grammar-and-sequential-art/SKILL.md) | 《漫画视听文法与图像叙事学》<br>Will Eisner / Scott McCloud | 格间时空跃迁 (Closure)、美漫工业分镜脚本、日漫视线流势 (Z/S 流线)、竖屏条漫节奏工程 |
| **四** | **工业管线与编剧策划** | | |
| 20 | [`digital-animation-pipeline-and-perspective`](.agents/skills/digital-animation-pipeline-and-perspective/SKILL.md) | 《数字动画工业管线与透视几何》<br>工业三维制作实践 | Maya 动画脚本开发、透视网格空间几何、三维制作全管线数据流转与协作规范 |
| 21 | [`story-and-screenplay-engineering`](.agents/skills/story-and-screenplay-engineering/SKILL.md) | 《好莱坞故事编剧与结构力学》<br>Robert McKee / Blake Snyder | 三幕式结构力学、节拍表 (Beat Sheet)、冲突递进与人物弧光、剧本医生外科手术诊断规范 |
| 22 | [`cangjie-skill`](.agents/skills/cangjie-skill/SKILL.md) | 《仓颉知识蒸馏引擎》<br>Framework Core | 将任意图书、长视频、播客、课程蒸馏为标准化、确定性 AI Skills 的全流程引擎 |

---

## 📁 目录结构

```text
Book_Skill_Animtion/
├── .agents/skills/              # 🎯 22 个核心 Skills 的标准存放目录 (各大 AI 平台即开即用)
│   ├── anatomy-for-sculptors/
│   ├── animators-survival-kit/
│   ├── facial-expressions/
│   ├── stop-staring/
│   ├── framed-ink/
│   ├── ... (共 22 个完整技能包)
├── books/                       # 📚 22 部经典书籍的结构化拆解与蒸馏产物
│   ├── anatomy-for-sculptors/   # (BOOK_OVERVIEW.md, DIGEST.md, evals, verified cards)
│   ├── animators-survival-kit/
│   └── ...
├── scripts/                     # ⚙️ 编译、提取、校验与蒸馏自动化工具链
├── install.py                   # 🚀 跨平台智能一键安装器 (Python 3)
├── install.ps1                  # 🪟 Windows PowerShell 一键安装快捷入口
├── install.sh                   # 🐧 macOS / Linux 一键安装快捷入口
├── GITHUB_REPO.md               # 仓库元数据
└── README.md                    # 英文文档与指引
```

---

## 💡 使用示例

安装到你的 AI 助手后，AI 即可在涉及动画、分镜、角色设计、表演或视听语言时自动或按提示调用相关技能：

### 示例 1：三维角色行走循环与时间掌握
> **User**: "我想在 Maya 中制作一个写实女性走路循环动画，请按照标准行走步态给出关键帧姿态参数、时间掌握与重心位移规则。"
>
> **AI (自动触发 `animators-survival-kit` + `timing-for-animation`)**:
> 将按接触帧 (Contact)、下沉缓冲 (Down)、越过中间 (Pass)、最高伸展 (Up) 四大黄金姿态，输出 24 帧标准步频标尺与骨盆三轴反向倾斜律动。

### 示例 2：面部绑定与对白口型
> **User**: "角色需要说一句台词：'What are you doing here?'，请给出面部 Blendshape 的权重分配与关键视素时序。"
>
> **AI (自动触发 `stop-staring` + `facial-expressions`)**:
> 运用 Osipa 双轴正交解耦法则（开合与宽窄），提供提前 2-4 帧发音开启口型，并结合眨眼节拍与视线扫视（Saccade）。

### 示例 3：好莱坞级电影分镜设计
> **User**: "两位剑客在狭窄雨巷中对决，请设计一组 5 个画格的分镜头脚本，要求极具紧张感与空间纵深。"
>
> **AI (自动触发 `framed-ink` + `grammar-of-film-language` + `storyboard-art`)**:
> 运用 180° 假想动作轴线守恒、60-30-10 逆光黑白剪影对比、对角线张力与前景暗部框架构图。

---

## 📄 开源许可证

本项目采用 [MIT License](LICENSE) 开源协议。
提炼的方法论与技能卡片旨在用于学术研究与辅助创作，所引用的经典专著知识产权归原作者所有。
