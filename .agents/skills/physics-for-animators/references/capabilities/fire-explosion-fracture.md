## R — 原文 (Reading)

> “An explosion is a rapid expansion of gas, driving shockwaves faster than the speed of sound. In large explosions, thermal buoyancy forces hot gases upward into a rising fireball, while cold surrounding air is drawn in, forming the characteristic vortex torus of a mushroom cloud. When brittle objects fracture from an impact, cracks initiate in two phases: straight radial cracks spreading outward, followed by concentric circular ring cracks connecting them.”
> 
> —— Michele Bousquet & Alejandro Garcia, *Physics for Animators*, Chapter 8, pp. 249–265

## I — 方法论骨架 (Interpretation)

大爆炸、火球对流与固体碎裂具有高度特异性的流体热力学与断裂力学拓扑：
1. **爆炸三阶段与蘑菇云环形涡流 (Mushroom Cloud Torus)**:
   - **阶段一：化学闪爆 (Flash, 1–2 帧)**: 极高温极高压气体在核心点瞬时膨胀，产生超音速空气冲击波（Air shockwave）；
   - **阶段二：热浮力上升与环形涡旋 (Buoyancy & Torus, 4–12 帧)**: 极热气体密度远低于冷空气，以极高垂直速度向上喷射；由于内部低压，周围冷空气从外围向中心卷吸，火球顶部向外下翻卷，形成标志性的甜甜圈状自旋转**涡旋环 (Vortex torus)**；
   - **阶段三：地面吸附烟柱 (Stem, 12–30 帧)**: 底部强烈气流卷起地面尘土泥沙形成细长直立烟柱；火球随热量散失由亮橙黄变为红褐，最后冷凝成深灰黑浓烟；
2. **刚体脆性碎裂的两相裂纹拓扑 (Fracture Crack Patterns)**:
   - 受到强冲击（如子弹穿透玻璃、重锤砸裂地面）时，材料应力破坏严格分两步：
     1. **辐射裂纹 (Radial Cracks)**: 从受撞击中心点向外辐射状极速穿刺展开的直线型放射裂纹；
     2. **同心环裂纹 (Concentric Cracks)**: 随后由弯曲拉伸应力在辐射裂纹之间横向贯通的同心圆环形裂纹，将材料最终解构为扇形小碎片。

## A1 — 案例 (Application Example)

### 书中例题: 地面大爆炸热对流火球与碎石断裂排布 (worked_example)
- **任务**: 制作一枚重型炸弹在坚硬地面引爆的完整视觉特效。
- **执行过程**:
  1. 第 1 帧：中心纯白过曝强闪光，高压半球形空气冲击波在地面展开白色扭曲环；
  2. 第 2–3 帧：地面受击中心产生数十条直线辐射裂纹（Radial cracks），碎块沿切线垂直向上被炸飞；
  3. 第 4–8 帧：紧接着同心圆裂纹横向咬合，地表彻底崩解；中心炽热火球高速垂直升起；
  4. 第 9–16 帧：火球到达一定高度，顶部向外翻卷形成环形涡流蘑菇头（Torus），底部垂直烟柱形成；火球由鲜黄色演变为翻滚红橙色浓烟；
  5. 第 17–36 帧：蘑菇头缓慢膨胀并与上升烟柱融合，转为深灰黑烟向空中弥散消退。
- **结果**: 层次井然有序，完全脱离了“火球放大多边形变黑”的劣质游戏动效质感。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 制作手雷、火炮、炸药大爆炸、核爆或陨石撞击场景；
2. 制作玻璃击碎、墙壁重拳砸裂、冰面受压裂开的断裂纹理与碎片散落；
3. 排查爆炸看起来像静态贴图缩放、或者碎裂裂纹杂乱无章违背物理规则。

### 语言信号 (Triggers)
- "大爆炸蘑菇云形态怎么做 / vortex torus 涡旋"
- "爆炸冲击波与三阶段时序排布"
- "玻璃碎裂 / 地面砸裂裂纹走向怎么画"
- "Radial cracks and concentric ring cracks pattern"

### 与相邻能力的区分
- 与 `liquid-fluid-dynamics` 的区别: 本能力用于高温气体热对流膨胀与脆性固体断裂力学；`liquid-fluid` 用于常温液体黏度与水面破浪。
- 与 `action-reaction-impact` 的区别: 本能力用于宏观环境能量释放与破坏碎裂纹理；`action-reaction` 聚焦角色单体受击反冲。

## E — 可执行步骤 (Execution)

1. **分段排布爆炸核心时间轴**:
   - 帧 1: 闪光（Flash，白色单帧过曝）；
   - 帧 2–4: 冲击波半球扫过，中心火球急速膨胀；
   - 帧 5–12: 垂直热浮力上升，顶部形成外翻环形涡旋（蘑菇头）；
   - 帧 13–24: 底部烟柱连接地面，外层卷吸冷空气冷却为深色滚滚浓烟。
2. **绘制脆性碎裂几何拓扑**:
   - 步骤 1：以撞击中心为原点，向外绘制多条直线射线（辐射裂纹 Radial cracks）；
   - 步骤 2：在辐射线之间以中心为圆心画出多层同心圆弧（同心圆裂纹 Concentric cracks）；
   - 步骤 3：靠近撞击点碎片密而小，远离撞击点碎片大而稀疏。
3. **输出碎片抛射初速度**:
   - 碎片沿放射裂纹正交方向向外呈抛物线飞溅，水平速度匀速，垂直速度受重力下落。
4. **输出标准交付契约**:
   - 输出爆炸形态演化律表与断裂网格裂纹生成参数。

## B — 边界与反模式 (Boundary)

### 失效边界
- 太空真空环境中的爆炸（如无重力、无空气介质的飞船自爆），不存在空气阻力，也不存在热浮力对流，绝对不会产生蘑菇云或烟柱，而是呈完全对称的球形光球与高速碎片向四面八方等速散开。

### 常见反模式
- **太空蘑菇云**: 在外太空无重力真空中画出直立上升的蘑菇云；
- **裂纹杂乱无章**: 碎裂地面没有放射线与同心圆结构，胡乱画成蜘蛛网或均匀瓷砖碎块。
