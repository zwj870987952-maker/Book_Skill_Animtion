## R — 原文 (Reading)

> “In animating dialogue, do not try to animate every single letter of every word. Speech is a flow of sound. You must break dialogue down into phonetic sounds, or visemes: closed mouth for M, B, P; teeth touching lower lip for F and V; wide open for AH; oval for OH; and narrow stretched for EE. Most importantly, animate the mouth one or two frames ahead of the sound to match human perception.”
> 
> —— Preston Blair, *Cartoon Animation*, Chapter 4, pp. 182–188

## I — 方法论骨架 (Interpretation)

对白口型动画（Dialogue Lip-Sync）不仅是绘制嘴唇开合，更是一门将声学音素转化为视觉造型的工程系统：
1. **视素离散分类体系 (The Classic Viseme Chart)**:
   - **闭唇音 (M, B, P)**: 双唇紧贴并向内抿紧蓄压，直到发音爆破瞬间双唇破开；
   - **咬唇音 (F, V)**: 上门牙轻咬下嘴唇内侧红唇，下唇微凹；
   - **舌齿音 (L, TH, T, D, N)**: 嘴唇微张，舌尖向上顶在上前牙牙龈处清晰可见；
   - **宽元音 (A, AH, I)**: 下颌大幅向下垂直开合，形成宽阔竖向开口，舌头平放；
   - **窄元音 (E, EE)**: 嘴角水平向两侧拉宽收紧，露出整齐牙齿；
   - **圆孔元音 (O, OO, W, U)**: 双唇向前撅起突出成小正圆形，下巴微收；
2. **拒绝机械逐字母拼读 (Phonetics over Spelling)**:
   - 动画师绝不能为英文单词的每个字母画一张嘴（例如说“BREAD”只需抓 B 闭嘴、EH 宽嘴、D 齿舌 3 个主导视素，而不是画出 B-R-E-A-D 五张嘴）；
3. **视觉超前生理感知 (1–2 Frames Anticipation)**:
   - 人眼视知觉处理速度比听觉慢约 40ms，嘴唇必须在录音音频波形达到峰值前 1–2 帧提前到达目标口型极值。

## A1 — 案例 (Application Example)

### 书中例题: “WHAT DID YOU SAY?” 对白口型视素分解与重音排布 (worked_example)
- **任务**: 制作角色大声质问“What did you say?”（录音长 24 帧，重音在 WHAT 和 SAY）。
- **执行过程**:
  1. 抓取核心音素串：OO(What) ➔ AH ➔ T ➔ D(did) ➔ IH ➔ D ➔ Y(you) ➔ OO ➔ S(say) ➔ EH ➔ EE；
  2. 简化为 6 大主视素：
     - 帧 1–3: “WH-” ➔ 嘴唇撅起小圆孔（提前音频 1 帧）；
     - 帧 4–7: “-AT” ➔ 宽元音下颌猛烈张大（重音爆发！头部猛力向前下砸）；
     - 帧 8–11: “DID” ➔ 上下牙齿咬合闭口微张（轻声掠过）；
     - 帧 12–15: “YOU” ➔ 嘴唇再次撅起圆唇 OO；
     - 帧 16–20: “SAY” ➔ 牙齿闭合 S 迅速弹开至大开阔元音 EH（第二重音爆发！双眼圆睁，右手指伸出）；
     - 帧 21–24: 窄元音 EE 嘴角拉宽平复。
- **结果**: 口型锐利清晰、声画严丝合缝，身体肢体动作与台词重音浑然一体。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 二维手绘/三维动画角色对白表演与口型关键帧排布；
2. 游戏引擎（Unreal / Unity）面部捕捉与对白自动口型算法（Viseme Blendshapes）校准；
3. 排查角色讲话看起来“像嘴巴抽搐的木偶”或“口型总是慢半拍对不上声音”。

### 语言信号 (Triggers)
- "对白口型 lip sync 怎么对关键帧 / 音素视素映射"
- "Viseme mouth shapes for animation"
- "角色讲话怎么配动作重音 body accents"
- "口型提前 1-2 帧提前量设置"

### 与相邻能力的区分
- 与 `facial-expressions-squash-stretch` 的区别: 本能力处理对白语言发音过程中的嘴唇视素连续形变；`facial-expressions` 处理整体大喜大悲的情绪面部极值。
- 与 `dialogue-lip-sync` (Timing 领域) 的区别: 本能力融汇了布莱尔经典的 6 大手绘音素口型标准图表与肢体身体重音（Body Accents）演出结合法；`dialogue-lip-sync` 侧重时序毫秒物理对准。

## E — 可执行步骤 (Execution)

1. **听音扒波形 (Track Reading)**:
   - 在律表上标出对白音频波形峰值帧，识别重读单词（Accents）与弱读连接词。
2. **提取主导视素 (Viseme Reduction)**:
   - 过滤掉微小过渡字母，合并为核心视素序列（M/B/P, F/V, L/TH, A, E, O）。
3. **设置 1–2 帧提前量 (Lead the Audio)**:
   - 将主导元音和闭唇音的极限姿态帧，向前平移 1–2 帧（即发声在帧 10，嘴型极值定在帧 8–9）。
4. **绑定身体重音 (Body Accents)**:
   - 在核心重读音节帧，头部必须伴随点头或侧偏，主要手势必须在此帧到达挥动的击打极值。
5. **输出标准交付契约**:
   - 输出逐帧对白音标对照表、对应 Viseme 编号及肢体重音同步时间点。

## B — 边界与反模式 (Boundary)

### 失效边界
- 极快语速（如每秒超过 6 个音节的 Rap 饶舌或极速拍卖叫价），人类面部肌肉根本来不及逐个开合，必须每 3–4 帧只保留下颌大开合与整体震颤，忽略细微辅音。

### 常见反模式
- **字母拼读抽搐**: 严格为每一个英文字母画嘴，导致嘴唇在 24fps 下像缝纫机疯狂乱闪；
- **声画同帧或滞后**: 严格按照波峰画最大张嘴，观众在观影时会感觉口型永远慢半拍。
