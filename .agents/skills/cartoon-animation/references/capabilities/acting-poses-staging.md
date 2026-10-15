## R — 原文 (Reading)

> “Staging is the presentation of an idea so that it is completely and unmistakably clear. An animated character is an actor on a stage. Every pose, gesture, and eye glance must direct the viewer’s attention to the story point. Avoid clutter; use strong silhouettes and clear paths of action. If the audience doesn't know where to look, the animation fails.”
> 
> —— Preston Blair, *Cartoon Animation*, Chapter 3, pp. 136–139; Chapter 5, pp. 204–212

## I — 方法论骨架 (Interpretation)

动画不仅是画出流畅的动作，更是一场严格受控的视听戏剧表演（Acting & Staging）：
1. **单一视觉焦点 (One Idea at a Time)**:
   - 在任何给定的关键帧内，画面中只能允许一个主导动作发生；如果主角在举枪射击，背景角色必须处于静止定格（Hold）或极其微弱的次级呼吸状态，严禁多个角色同时进行剧烈动作抢戏；
2. **视线引导链 (Eyeline Vector)**:
   - 角色的眼球朝向、手指指向以及动作线延伸方向，必须如聚光灯般精准引导观众视线穿过画面，投向下一个戏剧重点；
3. **动作弧线法则 (Arcs of Action)**:
   - 人体所有自然动作轨迹必须落在优美舒展的弧线（Arcs）上；中间过渡画（Breakdown）必须严格放置在弧线顶点，绝不可落在两点直线切线上；
4. **舞台剪影空间 (Negative Space)**:
   - 角色身体必须与环境产生清晰的负空间分界，避免肢体与背景高对比度杂物重叠混合。

## A1 — 案例 (Application Example)

### 书中例题: 角色发现藏宝箱的视线引导与舞台调度 (worked_example)
- **任务**: 表现角色推开暗门、第一眼发现发光藏宝箱并兴奋指向宝箱的表演过程。
- **执行过程**:
  1. 进场姿态 (Staging 1): 角色侧身推门，全身动作线向左倾斜，眼神紧紧锁定在右下角的宝箱；
  2. 视线传递 (Staging 2): 角色身体保持静止 4 帧，仅让眼球急速向右转动，强力吸引观众视线提前看向宝箱；
  3. 戏剧动作 (Staging 3): 角色双臂向上向右猛烈扬起，右手伸出食指笔直指向宝箱，全身反 C 形动作线与手臂完全形成一条直射宝箱的箭头向量；
  4. 剪影检验 (Staging 4): 纯黑剪影下，伸出的手臂与手指与暗门背景完全分离，处于纯净明亮的空气负空间中。
- **结果**: 戏剧意图清晰无误，叙事节奏流畅明快。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 动画分镜故事板（Storyboard）镜头构图与表演规划；
2. 3D 动画布局（Layout）与镜头摄影机视线调度；
3. 排查画面“看起来乱糟糟观众不知道该看哪”、“表演缺乏戏剧焦点”。

### 语言信号 (Triggers)
- "动画舞台调度 Staging 怎么做 / 戏剧表演姿态"
- "如何引导观众视线焦点 eyeline direction"
- "动作弧线 Arcs 怎么画 / 消除直线生硬动作"
- "双人对手戏动作主次节奏与防抢戏设计"

### 与相邻能力的区分
- 与 `line-of-action-rhythm` 的区别: 本能力用于角色与舞台空间、镜头焦点及叙事意图的宏观调度；`line-of-action` 聚焦单角色解剖骨架线条。
- 与 `exposure-sheet-field-charts` 的区别: 本能力是导演戏剧表演法；`exposure-sheet` 是底层技术规格框与摄影律表对位。

## E — 可执行步骤 (Execution)

1. **确立单一视觉焦点 (Primary Focal Point)**:
   - 明确当前 1–2 秒镜头内的唯一核心叙事信息（如“看到炸弹”或“拔出钥匙”）；
   - 压低画面其余次要元素的动态，除主角色外其余角色保持 Hold 或微弱呼吸。
2. **绘制动作弧线 (Path of Action Arcs)**:
   - 连接起始姿态 A 与终态 B，绘制两点之间的抛物线或椭圆弧；
   - 强制将中间画（Breakdown）放置在弧线波峰处。
3. **校准视线引导向量**:
   - 检查角色的眼球、鼻尖与主要手势，是否呈一条直线直指核心道具或对手角色。
4. **输出标准交付契约**:
   - 输出镜头调度透视图、动作弧线标尺与核心视线向量图。

## B — 边界与反模式 (Boundary)

### 失效边界
- 表现战争灾难、混乱集市或狂欢节等特意营造群魔乱舞、多焦点信息过载的宏观大全景镜头，可放宽单一焦点限制。

### 常见反模式
- **抢戏混乱 (Upstaging)**: 前景角色在讲严肃对白，背景角色在大幅度挠头跳舞，导致观众大脑认知割裂；
- **直线切片**: 转头动作直接沿直线平移过去，导致角色在中间帧产生诡异的面部坍塌感。
