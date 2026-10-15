# 《漫画视听文法与图像叙事工程手册》（comics-grammar-and-sequential-art）项目概述

## 一、文献源与大师谱系
本技能包系统性萃取并熔铸了世界漫画理论、图像叙事学与美日商业漫画工业管线的四大核心经典：
1. **斯科特·麦克劳德（Scott McCloud）** ——《理解漫画：无形之艺》（*Understanding Comics: The Invisible Art*）
   - 漫画定义：连续并置的图像叙事（Sequential Art）；
   - 图标金字塔（The Big Triangle）：现实写实 vs 抽象偶像化（Cartoon Icon） vs 纯粹意义语言；
   - 面具效应（The Masking Effect）：写实背景 + 极简卡通角色，诱发读者无意识的自我投射与深度代入；
   - 格隙（The Gutter）与闭合（Closure）：读者大脑在两格之间的无意识脑补与时空跳跃力学；
   - 六大格跃迁（Panel-to-Panel Transitions）：时刻到时刻、动作到动作、主体到主体、场景到场景、角度到角度、非推论跃迁。
2. **斯科特·麦克劳德（Scott McCloud）** ——《制造漫画：漫画、图像小说叙事秘籍》（*Making Comics*）
   - 漫画家五大关键抉择（Five Choices）：选择时刻（Moment）、选择画框（Frame）、选择图像（Image）、选择文字（Word）、选择流动（Flow）；
   - 角色面部表情演算法：初学者通道与混合情绪表达谱；
   - 视觉清晰度（Clarity）优先法则。
3. **夏目房之介（Natsume Fusanosuke）** ——《日本漫画为什么有趣：表现和“文法”》（*マンガはなぜ面白いのか その表現と文法*）
   - 日漫分格（コマ割り / Koma-wari）的视线诱导流势；
   - 日漫独创的“漫符”（Manpu）记号体系（青筋、汗滴、眩晕圈、惊愕线）；
   - 形与线的身体性（肉体感与运动感线条）；
   - 拟声词（オノマトペ / Onomatopoeia）与画面的物理融合。
4. **美国 DC/漫威工业脚本导师群** ——《1519美国漫画脚本写作教程》（*Comic Book Scriptwriting*）
   - 全脚本（Full Script）工业排版规范：页码标尺（Page 1）、格数限制（Panel 1-5）、镜头描述与对白气泡（Dialogue & SFX）；
   - 漫威法（Marvel Style）协作机制：编剧梗概 $\rightarrow$ 画师绘制 $\rightarrow$ 编剧填词；
   - 翻页悬念（The Page-Turn Reveal）力学法则。

---

## 二、架构决策：Single 模式与 12 大能力卡

本技能包采用统一的 `single` 架构，包含 12 项高内聚能力卡：
1. `visual-iconography-and-abstraction-pyramid` (图像符号学与具象-抽象三角金字塔)
2. `gutter-closure-and-six-panel-transitions` (格隙闭合心理学与六大分格跃迁)
3. `time-space-mapping-and-panel-duration` (空间画框时间映射与感知时长)
4. `manga-visual-grammar-and-koma-flow` (日漫视听文法与分格流势)
5. `line-dynamics-synaesthesia-and-emotive-marks` (线条动力学通感与情绪记号)
6. `sound-effects-and-lettering-typography` (拟音词拟态词音画字型排印)
7. `word-and-picture-seven-combinations` (文图关系七大交锋组合)
8. `page-layout-and-dramatic-page-turn` (整页网格构架与翻页绝壁悬念)
9. `character-design-expressiveness-and-facial-acting` (漫画角色可塑性与表情演员力学)
10. `american-comic-scriptwriting-format` (美漫工业脚本格式规范)
11. `webtoon-vertical-scroll-grammar` (竖屏条漫无限下滚视听文法)
12. `comics-troubleshooting-and-flow-auditing` (漫画分格排障与眼球轨迹流势审计)
