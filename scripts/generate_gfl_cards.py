from pathlib import Path

cards_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\grammar-of-film-language\.cangjie\capabilities\cards")
cards_dir.mkdir(parents=True, exist_ok=True)

# 1. axis-of-action-180-rule.md
c1 = """# 能力卡: 180° 动作轴线守恒与合法越轴规程 (The 180° Action Axis & Crossing the Line)

## Rationale (核心原理)
在影视视听语言与分镜头设计中，**180° 动作轴线法则（The 180-Degree Line Rule）**是绝对不可撼动的“空间宪法”。
Daniel Arijon 在《电影语言的语法》中开篇确立第一几何公理：
> **“Draw an invisible line connecting the two interacting actors — this is the Line of Action. ALL camera placements MUST remain on ONE SIDE of this line! The moment you cross the line without preparation, you flip the screen direction, destroy spatial orientation, and cause the audience’s brain to crash!”（在两个互动的演员之间画一条无形的直线——这就是动作轴线。所有摄影机机位必须严格保持在这条轴线的同一侧！一旦你无准备地越轴，你就会颠倒屏幕方向，摧毁空间定位，并导致观众的大脑神经崩溃！）**

若机位越过轴线：
- 原本在画框左侧看向右方的角色 A，会突然变成在画框右侧看向左方；
- 两个正在激烈对话的角色看起来在望向同一个方向，受众内部建立的三维地理模型瞬间崩塌。

## Instruction (轴线守恒与合法越轴四步规程)

### 1. 180° 半圆轴线空间心智模型
```
                           [ 角色 A ] (面朝右看)
                              |
                     ==== [ 180° 动作轴线 Line of Action ] ====
                              |
                           [ 角色 B ] (面朝左看)

  ----------------------- [ 轴线法定边界 180° ] -----------------------
  [ 合法工作区 (同侧半圆) ]    (机位 1: Master)      (机位 2: A 反打)      (机位 3: B 反打)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  [ 严禁越轴禁区 (对侧) ]    (X 越轴机位 4: 产生致命左右颠倒空间崩溃！)
```

### 2. 合法越轴（Crossing the Line）四大工程手法
1. **手法 1: 连续移动镜头滑过轴线（Camera Movement on Shot）**:
   - 摄影机在单一不间断的长镜头中，缓缓从轴线右侧摇移或推轨横移滑到轴线左侧，观众亲眼见证了视角的转换，空间完全自洽；
2. **手法 2: 演员走位自主打破旧轴线（Actor Blocking Shift）**:
   - 角色 A 从座位站起走动，穿过两人的连线走到角色 B 身后；二人的相对空间位置改变，轴线自然重置；
3. **手法 3: 插入中性正视镜头过渡（Insert a Neutral Shot）**:
   - 镜头正正地对准角色正面（正视 0°，既不朝左也不朝右，或行车正中向前的视点）；切完中性镜头后，下一镜可合法落在轴线对侧；
4. **手法 4: 插入主观视点 POV（Insert a Subjective POV）**:
   - 插入角色 A 环顾四周的主观视点，借由第一人称视角抹平第三人称轴线。

## Actionable Example (调校两个谈判专家在走廊对峙的合法越轴)
1. **Shot 1 (合法区双人中景)**: 警探 A 在左侧，嫌疑人 B 在右侧，摄影机置于东侧走廊墙面；
2. **需要将机位转移到西侧墙面拍摄新线索**:
   - 严禁直接硬切到西侧墙面机位（越轴跳切！）；
3. **执行合法越轴方案**:
   - 警探 A 突然向前迈步逼近，从嫌疑人 B 的左侧擦肩而过，走到其身后掏出手铐；
   - 摄影机顺应 A 的走位跟摇，两人的视线轴线从“南北向”顺畅旋转为“东西向”；
   - 此时在西侧墙面切入反打特写，不仅完全符合 180° 规则，更增强了逮捕的气势。

## Constraints (约束与禁止)
- **严禁无动机粗暴越轴**: 严禁在连续剪辑中不经任何过渡镜头直接越过 180° 轴线；
- **严禁视线方向自相矛盾**: 确保对话双方在反打镜头中始终保持“一左一右”对撞，严禁两人视线同向朝右或同向朝左。

## Verification (验收标准)
- **平面顶视图校验**: 在场景平面图（Bird's-Eye View）上画出所有机位，所有镜头顶点是否严格落在轴线同侧半圆内；
- **银幕方向一致性**: 角色对话时，视线是否在屏幕水平方向上形成稳定的视觉对撞（Convergence）。
"""
(cards_dir / "axis-of-action-180-rule.md").write_text(c1, encoding="utf-8")

# 2. triangle-principle-setups.md
c2 = """# 能力卡: 三角形机位系统与双人对话布局 (The Triangle Principle for Two Actors)

## Rationale (核心原理)
无论一部好莱坞大片包含多少复杂的特效与宏大场面，其戏剧核心往往依然是“两个人在房间里对话与交锋”。
Daniel Arijon 在全书中将**三角形机位系统（The Triangle Principle）**誉为影视镜头语法的“几何母体”：
> **“The Triangle Principle is the most comprehensive, economical, and foolproof camera layout ever devised. Three camera setups located on one side of the action line give you complete cinematic coverage of any two-character scene!”（三角形原理是人类发明过的最全面、最经济、最严密可靠的机位布局。位于动作轴线同一侧的三个机位，就能为任何双人场景提供完美的电影级机位覆盖！）**

三角形的三个顶点：
1. **顶点 1（Base / Master Shot）**: 全景或双人中景，确立两人的相对空间、肢体语言与环境地理；
2. **顶点 2（Reverse Shot A）**: 专注拍摄角色 A 的单人近景或特写；
3. **顶点 3（Reverse Shot B）**: 专注拍摄角色 B 的单人近景或特写。

## Instruction (三角形机位布局四步规程)

### 1. 三角形机位系统几何顶视图心智模型
```
                         [ 角色 A ] <--- 动作轴线 ---> [ 角色 B ]
                              \                           /
                               \                         /
                                \                       /
            [ 机位 2: 拍 A ]       \                     /       [ 机位 3: 拍 B ]
            (面向 A 脸部)           \                   /        (面向 B 脸部)
                                     \                 /
                                      \               /
                                       v             v
                                     [ 机位 1: Master ]
                                     (双人建立全景)
```

### 2. 三角形系统实战四步流
1. **确立底边主镜头（Position the Base Master - Cam 1）**:
   - 放置在两个角色连线的正前方中央，通常使用 35mm-50mm 镜头，同时收纳两人的全身或腰上中景，交代距离感；
2. **确立对称反打内角（Establish Symmetric Reverse Angles - Cam 2 & Cam 3）**:
   - 机位 2 和机位 3 与轴线的夹角必须保持高度对称（如均为 30° 夹角）；
   - 两个反打镜头的焦距必须严格匹配（如均为 85mm），机位到角色的距离必须均等，确保两人在画面中的头部比例（Head Size）完全一致；
3. **机位高度锁定在眼平高（Lock Eye-Level Height）**:
   - 两个反打机位的高度必须与各自拍摄角色的眼睛高度平齐；
4. **剪辑节奏装配（Editing Assembly）**:
   - 用 Cam 1 建立场景 -> 双方平静交谈切入 Cam 2 / Cam 3 过肩中景 -> 情绪冲突爆发切入 Cam 2 / Cam 3 极近特写 -> 冲突平息切回 Cam 1 重置。

## Actionable Example (调校咖啡厅隔桌谈判的双人对话场景)
1. **Cam 1 (主镜头 Master)**:
   - 侧面双人中景：律师在画面左侧坐着，客户在画面右侧坐着，中间是放着合同与咖啡杯的桌子；
2. **Cam 2 (拍律师反打)**:
   - 位于客户右肩后方，拍摄律师的过肩中近景（OTS），律师面朝右侧讲话；
3. **Cam 3 (拍客户反打)**:
   - 位于律师左肩后方，拍摄客户的过肩中近景（OTS），客户面朝左侧聆听；
4. **结果**: 三个机位完美覆盖整场 3 分钟的谈判戏，空间关系清晰无误，剪辑节奏随情绪自然递进。

## Constraints (约束与禁止)
- **严禁反打机位角度悬殊不对称**: 严禁拍摄 A 用 15° 正面特写，而拍摄 B 用 85° 侧脸特写，否则会严重破坏对话双方的对等心理关系；
- **严禁头部尺寸比例失衡**: 双方地位对等时，反打镜头的景别大小必须严格一致，严禁一方是胸上近景而另一方是下巴大特写。

## Verification (验收标准)
- **剪辑对撞平滑度**: 在 Cam 2 和 Cam 3 之间快速反打切换，两人的视线是否形成稳固的向心汇聚，头部比例是否完全对称平衡；
- **空间地理完整度**: 观众是否能从 Master 镜头中清晰获知两人与桌椅环境的精确物理距离。
"""
(cards_dir / "triangle-principle-setups.md").write_text(c2, encoding="utf-8")

# 3. ots-vs-clean-single.md
c3 = """# 能力卡: 过肩外反打 vs 纯净内反打景别心理学 (External OTS vs. Internal Clean Singles)

## Rationale (核心原理)
在双人对话场景的反打镜头中，导演面临着一个至关重要的心理学决策：
在反打画面边缘，**是否保留对方角色的肩膀与后脑勺？**
Daniel Arijon 将反打镜头严格划分为两大阵营：
1. **过肩外反打（Over-The-Shoulder / External Reverse Shot）**:
   机位位于前景角色身后，将对方的肩膀、后脑或衣领剪影作为前景框架（占画幅 10%-15%）；
   - *心理学功能*: 强调**两人之间的连结、物理距离、交涉与心理博弈**。观众始终感知到对话者的在场与压迫，空间感极其确凿；
2. **纯净内反打（Clean Single / Internal Reverse Shot）**:
   机位移至两人空间内部，画框内只有目标角色一人，完全排除对方身体的任何碎片；
   - *心理学功能*: 强调**角色的绝对孤独、内心独白、道德撕裂或情感总爆发**。割裂了与对方的物理连结，让观众直接与角色的灵魂对话。

## Instruction (外反打 vs 内反打选用四步规程)

### 1. 外反打 (OTS) vs. 内反打 (Clean Single) 空间心智模型
```
  [ 过肩外反打 OTS (关系与空间连结) ]            [ 纯净内反打 Clean Single (孤立与情绪爆发) ]
  +---------------------------------+           +---------------------------------+
  |      \                          |           |                                 |
  |  (B的前景黑肩)    (A的面部表情)   |           |          (A的面部表情)          |
  |      /                          |           |       (四周完全虚化/无阻碍)      |
  +---------------------------------+           +---------------------------------+
  观众感受: A 正在对 B 说话，空间真实完整。      观众感受: A 处于极度内省孤立，情绪直击灵魂！
```

### 2. 反打景别阶梯实战四步流
1. **戏剧交涉阶段选用过肩外反打（Use OTS for Negotiation）**:
   - 在交谈的前半段、信息互换、博弈与常规对峙时，一律采用 OTS 镜头锚定空间关系；
2. **前景肩膀比例控制（Shoulder Ratio Rule）**:
   - 前景肩膀与后脑勺必须适度虚焦，占据画面边缘 10%-15% 的面积；严禁肩膀过大挡住被摄主体的嘴唇或眼神；
3. **情绪高潮切换为纯净内反打（Switch to Clean Singles for Climax）**:
   - 当角色道出核心秘密、拔枪威胁、崩溃痛哭或做出关键抉择时，瞬间推近切入纯净内反打（Clean Single）；
4. **双向对称切换原则（Mirror the Shift）**:
   - 若 A 切入了 Clean Single，当 B 做出同等强度的情绪回应时，B 也必须切换至 Clean Single，保持视听层级对等。

## Actionable Example (调校恋人分手戏的反打层级递进)
1. **阶段 1 (冷战交涉 - OTS 过肩)**:
   - 两人坐在长椅上。
   - 镜头 A: 越过男主肩膀拍摄女主面无表情的 OTS，空间距离疏离但依然同框；
   - 镜头 B: 越过女主肩膀拍摄男主焦急辩解的 OTS；
2. **阶段 2 (痛下决心 - 切入 Clean Single)**:
   - 女主下定决心，转过头直视男主说：“我们结束了。”
   - 镜头瞬间切入女主的**纯净内反打大特写（Clean Single）**，男主的肩膀被彻底剔除出画！
3. **结果**: 男主被彻底剥离出女主的视觉世界，象征着关系的绝对终结与不可挽回，给观众带来极大的心理震颤。

## Constraints (约束与禁止)
- **严禁前景肩膀穿模穿脸**: 前景角色的头部绝对不能遮挡被摄主体的眼睛或嘴唇，必须在两者之间留出通畅的视线通道；
- **严禁无动机的混合乱切**: 严禁一秒前是 OTS，下一句平庸台词无故变成 Clean Single，又毫无动机切回 OTS。

## Verification (验收标准)
- **心理张力阶梯度**: 从 OTS 切入 Clean Single 的瞬间，受众是否能明显感受到戏剧张力与亲密感的剧烈收紧；
- **空间连结感**: 在 OTS 镜头中，受众是否能确切感知两人之间的物理距离。
"""
(cards_dir / "ots-vs-clean-single.md").write_text(c3, encoding="utf-8")

# 4. parallel-screen-dialogue.md
c4 = """# 能力卡: 并排平行站位与车内吧台镜头调度 (Parallel Dialogue & Lateral Setups)

## Rationale (核心原理)
在很多经典影视情境中，角色并不是面对面站立，而是**并排坐着或并肩站立**（如在汽车前排驾驶座与副驾、酒吧吧台并排饮酒、公园长椅上并肩长谈）。
这种并排平行站位（Parallel Setups）给镜头调度带来了特殊的几何挑战：
两人的视线轴线不是相互对指，而是平行指向前方，且二人距离极近。
Daniel Arijon 在全书中解构了三种经典工程解决方案：
1. **侧面双人横向全景（Lateral Master）**: 拍摄两人的侧脸侧影，确立并排空间；
2. **外侧内向交叉反打（Cross-Shooting from Outside）**: 摄像机从左侧车门外拍摄副驾，从右侧车门外拍摄司机，形成交叉对撞；
3. **潜望后视镜与中性前反打（Frontal Mirrors & Neutral Dashboard）**: 利用车内后视镜反射或挡风玻璃正前方向后拍摄。

## Instruction (并排平行对话调度四步规程)

### 1. 汽车并排对话交叉机位心智模型
```
                     [ 挡风玻璃 Front Windshield ]
                                  |
              [ 司机 Driver A ] ------ [ 副驾 Passenger B ]
              (面朝前方/右侧)          (面朝前方/左侧)
                                  |
            [ 机位 2: 拍 B 反打 ]       [ 机位 3: 拍 A 反打 ]
            (穿过 A 的身体拍 B)          (穿过 B 的身体拍 A)
                                  |
                     [ 机位 1: 后座双人 Master ]
```

### 2. 并排平行调度实战四步流
1. **建立后座双人主镜头（Rear-Seat Master - Cam 1）**:
   - 机位架设在汽车后排正中央，拍摄两人后脑勺、后视镜及前方道路，交代驾驶环境与车速；
2. **架设车门外侧交叉反打（Lateral Cross-Angles - Cam 2 & Cam 3）**:
   - Cam 2 架设在司机左侧车窗外，对角线越过司机前胸拍摄副驾 B 的正面侧脸；
   - Cam 3 架设在副驾右侧车窗外，对角线拍摄司机 A 的正面侧脸；
3. **视线与转头时机捕捉（Turning of the Head）**:
   - 当副驾转头看向司机时，其视线从平视前方转为向左侧看，视线对撞瞬间形成强烈的面对面张力；
4. **挡风玻璃正向双人特写（Hood Mount Rig）**:
   - 在引擎盖上架设机位，透过挡风玻璃正向拍摄两人的半身特写，捕获两人双眼同时平视前方的微表情。

## Actionable Example (调校警匪片中两个警探在车内埋伏监视)
1. **Cam 1 (后排 Master)**:
   - 两个警探身穿风衣并排坐在车内，窗外阴雨绵绵，雨刮器规律摆动；
2. **Cam 2 (拍主驾老警探)**:
   - 镜头从副驾侧车窗斜拍老警探握着方向盘的坚毅侧脸，老警探紧盯前方大楼；
3. **Cam 3 (拍副驾年轻警探)**:
   - 镜头从主驾侧车窗斜拍年轻警探，年轻警探正紧张地擦拭配枪；
4. **视线交汇高潮**:
   - 年轻警探转头看向老警探：“要是他没来怎么办？”
   - 此时在 Cam 2 中，老警探微微转头回看，两人的目光在狭窄的车厢内形成极度紧张的对撞。

## Constraints (约束与禁止)
- **严禁车内轴线跳轴**: 一旦确立后排或前排单一视点，反打机位严禁突然跳至后备箱反向拍摄导致左右位置对调；
- **严禁无视后视镜反射穿模**: 使用前挡风玻璃机位时，检查后视镜中的反光，防止摄制组与器材穿模。

## Verification (验收标准)
- **并排空间自洽性**: 观众是否能清晰感知两人并肩同坐的物理相对位置；
- **转头视线对撞**: 当角色转头看向身侧同伴时，反打镜头的视线角度是否精准重合。
"""
(cards_dir / "parallel-screen-dialogue.md").write_text(c4, encoding="utf-8")

# 5. three-character-triangles.md
c5 = """# 能力卡: 三人及多角色对话多边形机位重组 (Three-Character Setups & Axis Reorientation)

## Rationale (核心原理)
当场景从两个人增加到三个人（A, B, C）甚至更多人时，几何复杂度呈指数级剧增。
如果导演不懂轴线重组，镜头切上几次，观众就会完全搞不清谁在对谁说话、谁站在谁的旁边。
Daniel Arijon 在全书中解构了三人对话的核心定理：
> **“At any given split-second of drama, a three-person scene is NEVER a three-person scene — it is a sequence of TWO-PERSON DIALOGUES with an outside observer! The Line of Action constantly shifts between A-B, B-C, and A-C as the dominant speaker changes!”（在任何戏剧瞬间，三人戏绝不是真正的三人戏——它是一连串附带一个外部观察者的双人对话！随着主导发言者的转换，动作轴线在 A-B、B-C 与 A-C 之间不断动态转移！）**

掌握三角形站位（The Triangle Formations）、外围观察者镜头（The Observer Shot）与主轴线转移规则，是驾驭复杂多角色群戏的最高分水岭。

## Instruction (三人对话多边形机位调度四步规程)

### 1. 三人几何站位与主轴线动态转移心智模型
```
                                  [ 角色 A (发言者) ]
                                    /           \\
                  [ 轴线 A-B ]     /             \\     [ 轴线 A-C ]
                                  /               \\
                       [ 角色 B ] --------------- [ 角色 C ]
                                    [ 轴线 B-C ]

  当 A 对 B 说话时: 激活 A-B 轴线，C 沦为被动观察者 (Observer)；机位锁定在 A-B 轴线同侧；
  当 A 转向对 C 说话时: 主轴线平滑旋转为 A-C 轴线！机位自然过渡至 A-C 轴线系统。
```

### 2. 三人对话调度实战四步流
1. **三人全景大 Master 确立几何站位（Three-Shot Master）**:
   - 交代 A、B、C 形成的正三角形或 L 形站位空间；
2. **分组归类为“二对一”（Two-against-One Grouping）**:
   - 将站在相近位置的两个人（如 B 和 C）拍在一个双人镜头中，与孤立的 A 单人镜头形成反打；
3. **主轴线转移的枢纽镜头（The Pivot / Transition Shot）**:
   - 当 A 讲完话转向 C 发言时，使用 A 的单人镜头作为枢纽：A 在画面内将头从左侧缓缓转向右侧，目光重新聚焦在 C 身上，自然完成轴线重置；
4. **观察者反应镜头插叙（The Reaction of the Third Party）**:
   - 在 A 和 B 激烈争吵时，切入沉默不语的 C 的单人特写，捕捉其微表情变化，维系三人共在感。

## Actionable Example (调校黑帮教父、卧底警探与暴躁手下的三人密室谈判)
1. **几何站位**:
   - 教父 A 坐在桌子尽头中央；卧底 B 坐在左侧；手下 C 站在右侧；
2. **阶段 1 (教父审问卧底)**:
   - 激活 A-B 轴线：机位 1 拍摄教父 A 的正面单人，机位 2 拍摄卧底 B 的紧张流汗单人；
   - 手下 C 仅在全景或作为背景模糊轮廓出现；
3. **阶段 2 (手下拔枪插话，轴线突变)**:
   - 手下 C 暴怒拔枪指向 B：“让我杀了他！”
   - 枢纽镜头：教父 A 缓缓转头看向 C，下巴微扬：“收起你的枪。”——轴线瞬间转移为 A-C 轴线！
4. **阶段 3 (教父压制手下)**:
   - 激活 A-C 轴线反打：切入手下 C 的惊恐收枪特写，以及教父冰冷威严的凝视。

## Constraints (约束与禁止)
- **严禁无视发言目标乱切单人反打**: 角色正在对左侧的人说话，切出的单人反打严禁面向右侧；
- **严禁遗忘第三人存在（Forgotten Actor Bug）**: 严禁连续 10 个镜头完全不给第三个角色任何反应镜头或背景同框，导致受众产生第三人已凭空离场的错觉。

## Verification (验收标准)
- **空间三角模型清晰度**: 观众在任何一个画格切换中，能否毫不费力地指出当前发言者在对谁说话、另外两个人在何处；
- **轴线转移平滑度**: 轴线在三人之间的动态切换是否通过角色转头或全景交代平稳过渡，无跳轴眩晕。
"""
(cards_dir / "three-character-triangles.md").write_text(c5, encoding="utf-8")

# 6. eyeline-match-convergence.md
c6 = """# 能力卡: 视线角度对撞匹配与空间汇聚几何学 (Eyeline Matching & Convergence Geometry)

## Rationale (核心原理)
为什么两个分别在不同时间、甚至不同绿幕影棚拍摄的单人特写镜头，剪辑在一起时，观众会坚信不疑他们正在**含情脉脉或怒目圆睁地看着彼此**？
秘密就在于极其严谨的**视线匹配（Eyeline Match）几何学**！
Daniel Arijon 指出：
> **“The human brain has an astonishing sensitivity to gaze direction. If character A looks 15 degrees off-camera to the right, character B MUST look 15 degrees off-camera to the left! If their vertical angles don’t complement each other, their eyes miss in space, and the emotional connection is dead!”（人类大脑对目光方向有着惊人的敏感度。如果角色 A 朝镜头右侧偏离 15° 注视，角色 B 必须朝镜头左侧偏离 15° 注视！如果他们的垂直仰俯夹角不能互补，他们的目光就会在虚空中错开，情感连接瞬间死亡！）**

视线匹配的三大几何要素：
1. **水平对称偏角（Horizontal Angle Symmetry）**: 离镜头轴线的偏角必须均等；
2. **垂直仰俯互补（Vertical Complementarity）**: 仰视角度 $\theta$ 必须等于反打镜头的俯视角度 $-\theta$；
3. **留白对称性（Nose Room / Looking Room Symmetry）**: 角色面朝的方向必须留出充足且对等的视觉呼吸空间。

## Instruction (视线匹配与空间汇聚几何四步规程)

### 1. 视线空间精准交汇心智模型
```
  [ 角色 A 特写 (画框左侧偏置) ]                     [ 角色 B 特写 (画框右侧偏置) ]
  +-------------------------------+                 +-------------------------------+
  |  (A的脸)  --> 视线向右留白 15° |                 | 视线向左留白 15° <-- (B的脸)   |
  |           -->                 |                 |                  <--          |
  +-------------------------------+                 +-------------------------------+
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  [ 受众大脑神经合成感知: 两个角色的目光在空间中间精准对撞相交！无缝建立戏剧强力场！]
```

### 2. 视线匹配实战四步流
1. **测量两人的物理垂直落差（Measure Physical Height Delta）**:
   - 巨人站立（高 2.1 米），矮人坐着（高 1.0 米），垂直落差 1.1 米；
2. **计算俯仰互补角（Calculate Complementary Tilt）**:
   - 拍摄巨人看矮人：镜头仰角架设，但机位**向下俯倾 25°**（俯视拍摄）；
   - 拍摄矮人看巨人：机位紧贴地面，**向上仰倾 25°**（仰视拍摄）；
3. **锁定水平偏离角与视线留白（Match Looking Room）**:
   - 角色 A 安置在画幅左三分线上，面向画面右侧留出 2/3 的视线空间（Looking Room）；
   - 角色 B 安置在画幅右三分线上，面向画面左侧留出 2/3 的视线空间；
4. **视线焦距深度匹配（Focal Distance Match）**:
   - 两人相距 1 米时，双眼必须呈现微微内聚（Convergence）；相距 50 米时，双眼必须呈现平行远眺。

## Actionable Example (调校悬崖营救场景的生死凝视)
1. **角色 A (悬崖顶端救援者)**:
   - 角色 A 趴在悬崖边缘，右臂向下伸出；
   - 镜头放置在崖边，俯视 45° 拍摄 A 的面部大特写，A 的双眼死死盯向画面右下方；
2. **角色 B (悬空抓绳者)**:
   - 镜头放置在崖壁下方，仰视 45° 拍摄 B 满是鲜血的面部特写，B 的双眼死死盯向画面左上方；
3. **结果**: 尽管两名演员可能在不同时间拍摄，但剪辑在一起时，45° 完美的仰俯对撞与对称视线，让观众感到两人的目光如钢缆般在生死边缘死死相扣。

## Constraints (约束与禁止)
- **严禁视线平行同向对打**: 严禁 A 向右看，反打镜头中 B 也向右看（导致两人看起来在看同一个画外物体）；
- **严禁视线穿顶或穿底**: 仰俯视夹角严禁过度悬殊，严禁一人仰角 60° 而另一人仅俯视 10° 导致视线擦肩而过。

## Verification (验收标准)
- **目光交汇直觉测试**: 快速来回切换反打镜头，观者是否能毫不怀疑地感到两人在正视对方的双眼；
- **视线留白对称度**: 两人面部前方的 Looking Room 像素比例是否保持严格对称平衡。
"""
(cards_dir / "eyeline-match-convergence.md").write_text(c6, encoding="utf-8")

# 7. screen-direction-continuity.md
c7 = """# 能力卡: 屏幕运动方向守恒与出入画对齐 (Screen Direction: Clean Exit & Clean Entrance)

## Rationale (核心原理)
在电影中，空间地理不是真实存在的，它只存在于**观众通过连续运动方向在大脑中拼贴出的认知地图中**。
如果一个逃亡者在第一个镜头中向屏幕右方狂奔，而在下一个镜头中突然从右方跑向左方，观众的第一生理直觉是：“他为什么掉头往回跑了？他遇到了埋伏吗？”
Daniel Arijon 指出：
> **“Screen direction is sacred! Left-to-right motion must remain left-to-right across every cut, until you legitimately change it. When an actor exits screen right, he MUST enter screen left in the next shot!”（屏幕运动方向是神圣的！从左到右的运动必须跨越每一次剪辑保持从左到右，直到你合法改变它。当演员从屏幕右侧出画时，下一个镜头他必须从屏幕左侧入画！）**

屏幕方向守恒（Screen Direction Continuity）是维护动作追逐、长途跋涉与史诗战役空间逻辑的绝对基石。

## Instruction (屏幕方向守恒与出入画对齐四步规程)

### 1. 屏幕运动矢量与出入画对齐心智模型
```
  [ Shot 1: 角色向右狂奔并出画 ] ------------------> 顺畅剪切! ------> [ Shot 2: 角色从左侧入画继续向右狂奔 ]
  +-------------------------------+                                 +-------------------------------+
  |   (奔跑) ===> ===>  [出画 ->] |                                 | [-> 入画]  ===> ===>  (奔跑)  |
  |                               |                                 |                               |
  +-------------------------------+                                 +-------------------------------+
  受众大脑空间合成: 角色正在向同一个地理目的地持续快速推进！逻辑丝滑无比！
```

### 2. 屏幕方向连续性实战四步流
1. **锁定地理全局矢量（Lock the Global Geographic Vector）**:
   - 规定逃亡方向为“从左向右（西向东）”，追击者方向同样必须为“从左向右”；
2. **干净出画与干净入画（Clean Exit & Clean Entrance）**:
   - Shot A 结束前，必须让角色完全离开画框（Clean Exit），画框留空 3-6 帧；
   - Shot B 开始时，画框先留空 3-6 帧，随后角色完整从对侧入画（Clean Entrance）；
3. **追逐场景的速度与落差控制（Pursuit Staging）**:
   - 逃亡者先从左向右跑过画框；几秒后切入同一机位，追击者从左向右冲入画框，明确传达两者在同一空间轨迹上追击；
4. **合法改变运动方向的三种手法（Changing Screen Direction）**:
   - *手法 1*: 让角色在同一镜头内当众拐弯变向；
   - *手法 2*: 插入正对镜头的迎面奔跑或背对镜头的远去奔跑（中性轴向 Neutral Shot）；
   - *手法 3*: 镜头跟随角色转弯进行大角度摇移（Pan）。

## Actionable Example (调校战马传令兵跨越三个不同地形的急行军分镜)
1. **Shot 1 (森林公路)**:
   - 战马从画面左侧冲入，沿林间小道向画面右下方飞奔，穿出画框右侧（干净出画）；
2. **Shot 2 (荒凉峡谷)**:
   - 峡谷全景，画面先空旷 4 帧；
   - 战马从画面左侧狂飙入画（干净入画），向画面右侧疾驰穿过峡谷，再次从右侧出画；
3. **Shot 3 (城堡吊桥冲刺)**:
   - 城堡大门前，战马继续从画面左侧轰鸣入画，冲向右侧的吊桥守卫停下；
4. **结果**: 三个跨越数公里的不同地理空间，仅凭严格的从左到右屏幕矢量，在观众心中合成了一段目标明确、动能不竭的伟大急行军。

## Constraints (约束与禁止)
- **严禁右出画右入画（Exit Right, Enter Right）**: 角色从右侧离开，下一镜头又从右侧冲入，会导致严重的折返冲突；
- **严禁对决双方同向奔跑**: 两军交锋冲撞时，一方必须从左向右冲，另一方必须从右向左冲，绝不能两方朝同一个方向跑。

## Verification (验收标准)
- **矢量一致性自检**: 逐格核对剪辑序列，角色的速度水平矢量符号（$+X$ 或 $-X$）是否保持完全一致；
- **出入画呼吸感**: 出画与入画之间是否有足够的空镜留白帧，确保节奏不仓促穿帮。
"""
(cards_dir / "screen-direction-continuity.md").write_text(c7, encoding="utf-8")

# 8. cutting-on-action-momentum.md
c8 = """# 能力卡: 动作剪辑点与动量惯性掩盖法则 (Cutting on Action & Momentum Match)

## Rationale (核心原理)
很多剪辑师和分镜师感到困惑：为什么有些镜头切换看起来生硬无比、像打了一个激灵；而有些镜头的景别切换却丝滑如水，观众甚至根本没有意识到镜头的转换？
好莱坞最伟大的剪辑魔法就在于**动量动作剪辑法则（Cutting on Action / Match Cut on Momentum）**！
Daniel Arijon 揭示了人类大脑神经的视觉盲区：
> **“When the human brain is tracking a fast, powerful, and decisive motion, its visual processing is entirely consumed by the MOMENTUM! If you cut from Shot A to Shot B during the apex of this action, the momentum effortlessly bridges the cut, rendering the physical splice completely invisible!”（当人类大脑正在追踪一个快速、强大且决定性的动作时，其视觉处理中枢完全被动量所占据！如果你在这个动作的最高潮瞬间从镜头 A 切到镜头 B，动量就会轻松跨越剪辑点，让物理切口变得完全隐形！）**

如果在静止或动作停顿瞬间切镜头，观众的大脑就会清晰看到切口的跳跃；在做功运动的中途切镜头，动量则化作无形的隐形衣。

## Instruction (动量动作剪辑四步规程)

### 1. 静止切硬跳 vs. 动量动作剪辑隐形心智模型
```
  [ 错误: 静止状态切镜头 (观众大脑感知到硬切跳跃) ]
  Shot A: 角色静止站立 ------------------> 明显硬切! -------> Shot B: 角色静止近景特写

  [ 大师级工程: 动量动作剪辑 Cutting on Action (绝对丝滑隐形) ]
  Shot A: [ 角色猛烈起立到一半，躯干快速上升速度最大处 Frame 15 ]
                        |  (动量无缝跨越剪切点！)
                        v
  Shot B: [ 镜头直接在 Frame 16 接上角色继续上升并完全站直定格！]
  观众感知: 大脑完全被起立的动量吸引，视神经自动将两个镜头合成为一个不可分割的连续生命动作！
```

### 2. 动量动作剪辑实战四步流
1. **寻找黄金动作切分点（Identify the Motion Apex）**:
   - 永远不要在动作发起前或动作结束后切！寻找速度最快、位移最大的瞬间（如开门瞬间把手下压至 45° 处、挥拳手臂划过半圆处、拔剑出鞘一半处）；
2. **两端动作重叠重合（Overlap the Action in Shooting）**:
   - 在实拍或 3D 动画中，镜头 A 和镜头 B 必须将该动作完整演完，保留至少 1 秒的动作重叠区（Overlap）；
3. **帧级对齐与动能衔接（Match Frame-Accurate Position）**:
   - 提取 Shot A 切出帧的角色四肢姿态坐标；Shot B 的切入第一帧必须紧密承接下一微小位移，严禁产生重复或漏帧；
4. **景别与角度跳跃配合（Combine with Angle Shift）**:
   - 动作剪辑必须伴随景别（全景切特写）或机位角度（改变 45° 以上）的变化，严禁在同一景别微弱角度下动量剪切。

## Actionable Example (调校特工从二楼破窗跳下一楼的动作分镜)
1. **Shot 1 (室内全景)**:
   - 特工助跑，飞身撞向玻璃窗；玻璃在第 12 帧碎裂成无数碎片，特工身体前半段冲出窗外；
2. **黄金切分点（Frame 13）**:
   - 在特工身体悬空于窗框一半、动量最大的瞬间果断切出！
3. **Shot 2 (室外仰视近景)**:
   - 镜头放置在室外地面仰视窗口；
   - 第 14 帧直接切入：特工带着漫天飞溅的玻璃碎片继续破窗冲出，在空中翻滚直坠地面；
4. **结果**: 碎裂的玻璃碎片与特工前冲的巨大动量完美掩盖了镜头切换，受众感到整个人如同一枚炮弹般被连贯射出。

## Constraints (约束与禁止)
- **严禁重复动作（No Double Bounce）**: 切镜头后严禁让角色重新再做一遍刚才已经做完的动作（如 Shot A 门已开了一半，Shot B 门又从紧闭状态重新开启）；
- **严禁动量丢失（No Loss of Velocity）**: Shot A 是极速挥拳，Shot B 切入时严禁突然变成慢动作挥拳，速度必须严格守恒。

## Verification (验收标准)
- **瞬态隐形测试**: 以正常播放速度观看剪辑点，观者是否感知不到物理画格的切换；
- **动能守恒自检**: 动作在跨越剪切点的前后 2 帧，位移速度矢量是否平滑连续，无突兀刹车或瞬移。
"""
(cards_dir / "cutting-on-action-momentum.md").write_text(c8, encoding="utf-8")

# 9. pov-three-step-architecture.md
c9 = """# 能力卡: 主观视点镜头三步法与视听投射 (The 3-Step POV System: Look, Object, React)

## Rationale (核心原理)
电影最强大的魔力之一，是能够强行将观众塞进角色的躯壳之中，让观众“透过角色的眼睛看世界”。
这就是**主观视点镜头（Point-of-View / POV）**。
然而，很多初学者误以为只要随便放一个手持摇晃的镜头就是 POV，结果导致观众茫然失措、无法代入。
Daniel Arijon 在全书中解构了经典好莱坞与希区柯克（Alfred Hitchcock）确立的黄金法则——**经典三步 POV 系统（The 3-Step POV Architecture）**：
> **“A subjective point-of-view is NOT a single shot; it is a THREE-SHOT PSYCHOLOGICAL CHAIN: 1. The Character Looks; 2. The POV Target; 3. The Character Reacts! Without the third shot (the reaction), the emotional loop is incomplete!”（主观视点绝非单个孤立镜头；它是一个三镜头心理闭环：1. 角色注视；2. 视点目标；3. 角色心理反应！没有第三个镜头（反应特写），情感闭环就彻底残缺不全！）**

## Instruction (主观视点三步法编排规程)

### 1. 经典三步 POV 心理闭环心智模型
```
  [ 第 1 步: 注视镜头 The Look ] --------> 中景/特写: 角色转头、目光锁定某一画外点 (建立欲望与好奇)
                 |
                 v
  [ 第 2 步: 目标镜头 The POV ] ---------> 主观机位: 模拟角色双眼高度与视角，展现其所见之物 (提供客观事实)
                 |
                 v
  [ 第 3 步: 反应镜头 The Reaction ] ----> 极致特写: 镜头切回角色面部，捕捉其震惊、恐惧或狂喜微表情 (完成情感升华)
```

### 2. 三步 POV 实战四步流
1. **第 1 步（The Looking Shot）**:
   - 拍摄角色的头部近景或特写；角色正在做某事，突然停下动作，双眼被画外某处强烈吸引，目光锁定；
2. **第 2 步（The POV / Object Shot）**:
   - 摄影机高度必须**严格等于角色的物理眼睛高度**；
   - 视角必须带上角色的主观生理属性（如角色微醺则画面边缘微糊晃动，角色在暗处偷窥则带门缝或望远镜圆环遮罩）；
3. **第 3 步（The Reaction Shot）**:
   - 镜头瞬间切回角色的面部大特写！必须精准捕捉在看到第 2 步内容后的瞬间心理震颤（瞳孔收缩、倒吸凉气、嘴角冷笑）；
4. **时间节奏比例控制（Cadence Ratio）**:
   - Look (2秒) -> POV (3秒) -> Reaction (2秒)；根据惊悚或温情基调微调停顿。

## Actionable Example (调校小女孩在床底发现怪物的经典惊悚段落)
1. **Shot 1 (The Look)**:
   - 小女孩趴在木地板上，把头慢慢贴近垂落的床单；她的眼睛睁得大大的，小心翼翼掀起床单边缘，目光探向漆黑的床底；
2. **Shot 2 (The POV)**:
   - 镜头贴地机位，穿过掀起的床单流苏；
   - 漆黑深处，两只散发着幽绿色冷光的怪兽眼珠在黑暗中缓缓睁开，伴随着粗重的呼吸声；
3. **Shot 3 (The Reaction)**:
   - 镜头闪电般切回小女孩惨白的脸孔大特写！
   - 瞳孔猛烈放大，右手死死捂住嘴巴防止尖叫出声，一滴冷汗顺着额头滑落；
4. **结果**: 三步心理闭环让观众与小女孩的神经中枢完全绑定，恐怖感呈几何级数引爆。

## Constraints (约束与禁止)
- **严禁斩断第三步反应镜头**: 严禁只展示角色看、展示了所见之物后就直接切到下一个无关场景，缺少角色反应的 POV 是没有灵魂的死镜头；
- **严禁 POV 机位高度错位**: 大人看地面的 POV 机位严禁卡在 1.8 米平视，必须以大人的俯视角度向下拍摄。

## Verification (验收标准)
- **代入感闭环测试**: 受众在看到 Shot 3 时，是否产生强烈的同理心与情感共鸣；
- **机位主观性验证**: Shot 2 的视野、高度与晃动感是否完全符合 Shot 1 角色的生理与空间状态。
"""
(cards_dir / "pov-three-step-architecture.md").write_text(c9, encoding="utf-8")

# 10. master-shot-coverage-system.md
c10 = """# 能力卡: 主镜头空间建立与分切覆盖装配工程 (Master Shot Technique & Coverage)

## Rationale (核心原理)
在影视工业化生产中，导演和分镜师最常犯的错误之一是“只见树木，不见森林”——一上来就沉迷于局部的近景与特写对切，结果剪辑出来后，整场戏的空间七零八落，观众完全不知道角色身在何处。
Daniel Arijon 在全书中系统化传授好莱坞百年不衰的工业支柱——**主镜头覆盖体系（The Master Shot Coverage System）**：
> **“The Master Shot is the anchor of reality! It establishes the geography, records the entire continuous action of the scene from start to finish, and serves as the safety net and emotional reset button for the entire sequence!”（主镜头是现实的绝对锚点！它确立了场景地理，从头到尾完整记录整场戏的连续动作，并充当整段镜头的安全网与情绪重置按钮！）**

一个标准的工业场景覆盖（Coverage）包含：
1. **主镜头（Master Shot）**: 全景不间断贯穿始终；
2. **中景双人镜头（Two-Shots）**: 承载中段关系推进；
3. **特写反打镜头（Close-Up Reverses）**: 捕捉情绪高潮；
4. **插入镜头（Inserts / Cutaways）**: 关键道具与细节特写。

## Instruction (主镜头覆盖装配四步规程)

### 1. 经典主镜头覆盖金字塔心智模型
```
  [ 顶层: 主镜头 Master Shot (空间地理绝对锚点) ] 全景连续完整贯穿全场戏
                       |
       +---------------+---------------+
       |                               |
       v                               v
  [ 中层: 过肩中景 OTS Two-Shots ]      [ 局部插入 Inserts / Cutaways ]
  (推进核心动作交涉与走位)              (钟表/信件/武器特写安全网)
       |                               |
       +---------------+---------------+
                       |
                       v
  [ 底层: 极限特写 Extreme Close-Ups ] (情绪爆发致命点)
```

### 2. 主镜头覆盖装配实战四步流
1. **拍摄/绘制完整主镜头（The Unbroken Master）**:
   - 从角色走入房间、坐下交谈、争吵、直到最后一人摔门而去，用全景机位从头到尾完整跑一遍，确立无可辩驳的时空基底；
2. **切入关键特写覆盖（Shoot the Coverage）**:
   - 将主镜头中最重要的戏剧高潮部分（如争吵、告白、拔枪），用三角形反打机位提取特写覆盖；
3. **剪辑节奏装配（Assemble the Scene）**:
   - *开篇*: 用 Master Shot 确立空间关系（3-5秒）；
   - *展开*: 顺畅切入 OTS 中景推进台词；
   - *高潮*: 切入特写 Clean Single 强化戏剧冲撞；
   - *重置*: 冲突告一段落时，果断切回 Master Shot 重新锚定空间，平复节奏；
4. **利用插入镜头消除断裂（Use Inserts as Cutaways）**:
   - 当两段反打特写由于表演节奏不一致无法顺畅硬切时，插入一张桌上时钟或茶杯的特写（Cutaway），完美衔接时间裂缝。

## Actionable Example (调校董事会罢免 CEO 的 3 分钟室内群戏)
1. **Master Shot (建立全景)**:
   - 会议室长桌全景，10 名董事围坐，窗外是摩天大楼天际线；
2. **装配流线**:
   - 前 20 秒在 Master 镜头中展开：董事长宣布议题，CEO 翻阅文件；
   - 第 21 秒切入 CEO 的中景反打与董事长的过肩中景（OTS）；
   - 第 60 秒举手表决：董事长率先举手，镜头切入 3 个董事的快速中景反应；
   - 第 90 秒情绪顶峰：CEO 猛烈拍桌站起怒斥，镜头切入 CEO 愤怒的双眼大特写；
   - 第 110 秒戏剧平复：CEO 抓起公文包大步离开，镜头顺畅切回 Master Shot，全景目送 CEO 摔门而出，会议室留下一片死寂。

## Constraints (约束与禁止)
- **严禁全场戏只用特写（Talking Heads Syndrome）**: 严禁整场戏只有两颗大头在不停说话，毫无主镜头空间呼吸与环境交代；
- **严禁主镜头缺乏完整连续性**: 在实拍与动画预演中，主镜头必须完整演完动作，严禁碎片化录制导致后期剪辑无全景可用。

## Verification (验收标准)
- **地理逻辑自检**: 观看剪辑成片，受众是否对会议室或房间内每个人的空间朝向与物理位置了如指掌；
- **剪辑呼吸弹性**: 在情绪爆发前后，是否有主镜头作为节奏的张弛缓冲区。
"""
(cards_dir / "master-shot-coverage-system.md").write_text(c10, encoding="utf-8")

# 11. actor-blocking-camera-reposition.md
c11 = """# 能力卡: 角色走位引导轴线转移与机位重置 (Actor Blocking & Natural Axis Shift)

## Rationale (核心原理)
在很多平庸的影视作品中，演员像钉在地面上的木桩一样一动不动地站着说话，全靠剪辑师在几个机位之间机械切换；而在真正大师级的电影调度中，**演员的走位（Actor Blocking）是重塑空间几何、重置动作轴线并引导摄影机机位重组的最高引擎**！
Daniel Arijon 指出：
> **“A dynamic scene is driven by actor blocking! When an actor moves, he doesn't just change his physical position — HE REDEFINES THE ENTIRE GEOMETRY OF THE SCENE! A master director uses the actor’s movement to rotate the axis, open new camera angles, and eliminate awkward cuts!”（一个充满活力的场景是由演员走位驱动的！当演员移动时，他不仅改变了自己的物理位置——他重新定义了整个场景的几何结构！大师级导演利用演员的移动来旋转轴线、开拓全新机位角度，并消灭生硬的剪辑！）**

通过角色的自然走位（站起、踱步、倒水、倚靠窗台）：
- 轴线自然完成空间旋转，合法进入此前被禁止的拍摄死角；
- 场景在不经历任何暴力越轴跳切的情况下，完成了镜头视听语言的全面升华。

## Instruction (角色走位引导轴线重置四步规程)

### 1. 角色走位重置空间轴线心智模型
```
  [ 初始状态: 轴线 1 (水平走向) ]
  角色 A (坐着) ---------------- 动作轴线 1 ---------------- 角色 B (站立)
        |
        v  (角色 A 站起，沿着曲线走向后方吧台倒酒)
  [ 走位中途: 摄影机摇镜头跟随 A 移动 (Camera Pans with A) ]
        |
        v  (A 到达吧台站定，转过身面对 B)
  [ 终态重置: 轴线 2 (垂直走向) ]
  角色 B (原处) <=============== 动作轴线 2 ===============> 角色 A (吧台)
  摄影机合法进入全新的 180° 工作半圆，彻底开拓全新空间景别！
```

### 2. 走位轴线重组实战四步流
1. **设计富有戏剧动机的走位（Motivated Movement）**:
   - 严禁为了走位而走位！移动必须有心理动机：愤怒而起立踱步、心虚而避开目光走向窗台、试图掌控全局而在房间内来回巡视；
2. **摄影机运动绑定引导（Bind Camera to Actor）**:
   - 当角色启动位移瞬间，摄影机立即摇镜头（Pan）或推轨跟拍（Track），将受众注意力完全锁定在角色的运动身上；
3. **定位全新轴线落点（Anchor the New Axis）**:
   - 当角色到达新位置停下转头时，连接其与对方的新连线确立为“轴线 2”；
4. **合法重组三角形机位（Re-deploy the Triangle）**:
   - 在新轴线的法定 180° 半圆内，重新架设全景、反打与特写机位，空间关系焕然一新。

## Actionable Example (调校将军审问逃兵的军帐走位调度)
1. **阶段 1 (初始对峙)**:
   - 将军背手站在帐篷中央，逃兵跪在地上，机位在右侧半圆拍摄过肩对话；
2. **阶段 2 (走位打破僵局)**:
   - 将军冷笑一声，大步走向逃兵身后悬挂的巨幅战役地图；
   - 摄影机推轨横移跟随将军走向地图；
3. **阶段 3 (轴线自然旋转 90°)**:
   - 将军在地图前停下，拿起匕首钉在地图上，转过身俯视逃兵：“你原本应该守住这个隘口。”
   - 逃兵转头仰望将军；
   - 两人之间的轴线自然从纵向旋转为斜向，摄影机合法移入原本属于禁区的左侧空间；
4. **结果**: 场面调度充满电影级流动感与不可阻挡的威严压迫。

## Constraints (约束与禁止)
- **严禁无动机的漂移徘徊**: 角色走位必须具备明确的起点、路径与落点，严禁像无头苍蝇一样在场景中无意义打转；
- **严禁走位中途摄影机跟丢主体**: 摄影机必须精准捕捉起步、行进与停顿全过程，确保受众大脑能够完整跟随轴线的连续位移。

## Verification (验收标准)
- **空间平滑度测试**: 轴线旋转前后，观众是否感到一切顺理成章、毫无方向颠倒与违和感；
- **戏剧动机合理性**: 角色的每一次迈步与停顿是否深刻符合其当下的心理欲望与权力博弈。
"""
(cards_dir / "actor-blocking-camera-reposition.md").write_text(c11, encoding="utf-8")

# 12. sequence-shot-choreography.md
c12 = """# 能力卡: 一镜到底场面调度与无剪辑景别转换 (Sequence Shot & Mise-en-Scène Choreography)

## Rationale (核心原理)
在影视艺术的皇冠之巅，存在一种不需要任何剪辑硬切、却能完美呈现完整戏剧段落的最高技艺——**一镜到底长镜头场面调度（The Sequence Shot / Plan-Séquence）**。
从奥逊·威尔斯（Orson Welles）的《历劫佳人》到当代大师阿方索·卡隆（Alfonso Cuarón）的《人类之子》，长镜头场面调度是检验导演视听统御力的终极试金石。
Daniel Arijon 在全书中深刻阐明长镜头的核心工业机理：
> **“A sequence shot is NOT a lazy, static wide angle! It is dynamic montage ACCOMPLISHED INSIDE THE CAMERA FRAME! Through fluid camera choreography and precise actor blocking, you transition from an establishing long shot, into a two-shot, and down to an intimate close-up — ALL WITHOUT A SINGLE EDIT!”（长镜头绝非偷懒静止的大全景！它是在画框内部完成的动态蒙太奇！通过流畅的摄影机运镜与精密的演员走位，你在同一个不间断镜头内，完成从宏观全景、到双人中景、再到亲密特写的景别转换——全过程无需一次剪辑！）**

## Instruction (一镜到底场面调度编排四步规程)

### 1. 镜头内蒙太奇 (Montage within the Shot) 连续流态心智模型
```
  [ 00:00 - 00:15 大远景 ELS ] ------> 摄影机高悬俯视: 宏大城市街道，主角车辆驶入并停靠
                 |
                 v  (摄影机顺畅推下并前推 Tracking In)
  [ 00:15 - 00:30 双人中景 MS ] -------> 主角推门下车，与路边线人接头交谈 (自然的双人构图)
                 |
                 v  (线人悄然递出信封，摄影机紧贴推入 Close-Up)
  [ 00:30 - 00:45 极近特写 ECU ] -------> 纯净特写锁定主角拆开信封时惊恐收缩的瞳孔！
  全过程零剪辑硬切，时空连续性如行云流水，身临其境感与沉浸感拉满！
```

### 2. 长镜头场面调度实战四步流
1. **多重节拍路径编排（Multi-Beat Choreography Path）**:
   - 将整场戏划分为 3-4 个关键戏剧节拍，为每个节拍分配物理场景中的停靠站（Station A, B, C）；
2. **利用前景走位变换景别（Change Scale via Distance）**:
   - 不需要变焦镜头！当角色走向摄影机时，景别自然从中景推向特写；当角色转身走远时，景别自然展开为全景；
3. **摄影机三轴立体运动（3D Camera Trajectory）**:
   - 结合推拉（Dolly）、升降（Crane/Jib）与横摇（Pan/Tilt），摄影机穿梭于家具与门框之间，形成天然画中画遮挡与空间揭示；
4. **隐藏切口设计（Whip Pan & Object Wipes for Safety）**:
   - 在复杂长镜头中，巧妙设计角色后背完全挡住镜头（Body Wipe）或极速甩镜头（Whip Pan）的瞬间，预留工业级的无缝接缝安全网。

## Actionable Example (调校一段侦探步入凶案现场的 60 秒长镜头调度)
1. **第 0-15 秒（全景建立）**:
   - 摄影机从凶宅二楼窗外缓缓穿窗而入（全景 ELS），展现凌乱昏暗的客厅与地面勾画的白色人体轮廓；
2. **第 16-30 秒（中景跟随）**:
   - 侦探推门走入，摄影机摇移跟随侦探步伐（推轨中景 MS），侦探走过翻倒的沙发，蹲在白色人体轮廓旁；
3. **第 31-45 秒（特写聚焦）**:
   - 侦探伸出戴手套的手捡起地毯上一枚闪烁微光的黄金纽扣，摄影机借由侦探蹲下的动作顺畅俯冲下推，画面自然收紧为纽扣与侦探指尖的极限大特写（ECU）；
4. **第 46-60 秒（戏剧重置全景）**:
   - 门外突然传来急促的刹车声与警笛声，侦探猛烈抬头，摄影机伴随侦探站立迅速后撤升起，再次拉开为全景俯视侦探与门口冲入的支援警力。

## Constraints (约束与禁止)
- **严禁无意义的眩晕跟拍**: 摄影机移动必须严格服务于叙事信息的揭示与人物情绪的推进，严禁为了炫技而无节制乱晃；
- **严禁焦点虚焦穿帮**: 在长镜头中多景别转换时，跟焦员（Focus Puller）必须严格锁定焦点深度，严禁关键面部长期处于脱焦状态。

## Verification (验收标准)
- **时空沉浸真实感**: 整个镜头是否具备一气呵成的真实沉浸感与不可中断的戏剧张力；
- **景别转换自然度**: 镜头内部从全景到特写的过渡是否宛如呼吸般自然，无机械卡顿与镜头找寻感。
"""
(cards_dir / "sequence-shot-choreography.md").write_text(c12, encoding="utf-8")

print(f"Authored all 12 RIA++ capability cards in {cards_dir} for Grammar of Film Language successfully!")
