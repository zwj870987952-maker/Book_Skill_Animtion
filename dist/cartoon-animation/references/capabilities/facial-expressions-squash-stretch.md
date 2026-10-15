## R — 原文 (Reading)

> “A cartoon head can be stretched or squashed to strengthen an expression. Notice that the oval containing the eyes does not change much, but the mouth area varies greatly. Small details react along with the larger form in which they are contained. The animator must be a master of portraying emotions. Studying your own grimaces in a mirror is an absolute must.”
> 
> —— Preston Blair, *Cartoon Animation*, Chapter 1, pp. 24–28

## I — 方法论骨架 (Interpretation)

面部表情是角色内心世界的直接投射，而卡通表情的极致感染力源于**符合容积守恒的挤压拉伸（Squash & Stretch）**：
1. **表情区域与刚体区划分**:
   - 脑颅区（眼眶上方至后脑勺）：属于坚固骨骼结构，形变极小，是锁定角色头颅体量不变的“锚点”；
   - 颌面与口吻区（眉毛以下至下巴）：属于高延展性柔性肌肉与下颌活动铰链，承担 $80\%$ 的形变张力；
2. **容积守恒物理原则**:
   - **拉伸 (Stretch)**: 极度吃惊、大声呐喊、狂喜时，下颌向下大幅拉长，垂直高度拉伸为 $1.5–2.0$ 倍；此时**两侧脸颊必须等比例向内收缩变窄**，严禁只拉长不收窄；
   - **挤压 (Squash)**: 咬牙切齿、诡异大笑、痛苦隐忍时，下巴向上挤压贴近鼻孔，垂直高度压缩至 $0.5–0.7$ 倍；此时**两侧脸颊和眼角必须向外横向膨胀凸出**；
3. **五官连锁反应 (Secondary Chain)**:
   - 眉毛、眼睑、眼珠、鼻翼与嘴角必须形成联动机制（如嘴巴拉伸张开时，眉毛必定高高扬起，眼珠随之放大拉长）。

## A1 — 案例 (Application Example)

### 书中例题: 卡通狂喜大笑的拉伸与挤压交替调校 (worked_example)
- **任务**: 制作角色从普通微笑过渡到放声狂喜大笑的表情爆发。
- **执行过程**:
  1. 初始姿态（普通笑）：嘴唇微弯，面部处于基准球形；
  2. 预备挤压（Squash 帧）：下巴向上抬起，眼睛眯起挤成一条细缝，脸颊向外横向鼓起成肉团（垂直压扁，横向扩张，容积守恒）；
  3. 爆发拉伸（Stretch 帧）：下巴猛烈向下拉至极限，嘴巴张开成垂直长椭圆，脸颊向内深深凹陷变窄，眼球高高冲出眉骨拉长；
  4. 恢复常态（Settle 帧）：嘴巴回弹至稳定的大笑开怀姿态，脸颊横向宽度恢复适中。
- **结果**: 表情爆发力极其充沛、生动传神，且角色头颅体量完全没有失真。

## A2 — 触发情境与语言信号 (Future Trigger)

### 适用场景
1. 设计角色狂喜、愤怒、惊恐、沮丧、困惑等极端表情原画；
2. 3D 面部绑定制作极端表情 Blendshapes / Shape Keys 目标体；
3. 排查角色面部表情在大幅变形时看起来像“气球充气变大”或“缩水消失”。

### 语言信号 (Triggers)
- "卡通面部表情怎么画更夸张生动"
- "表情挤压与拉伸 squash and stretch on face"
- "面部变形容积守恒 volume conservation"
- "下巴张开和脸颊联动的调节规则"

### 与相邻能力的区分
- 与 `dialogue-viseme-mouth-shapes` 的区别: 本能力用于整体情绪与夸张表情的戏剧性形变；`dialogue-viseme` 专用于对白发音时口型音素的精确几何形态。
- 与 `exaggerated-takes-reactions` 的区别: 本能力聚焦面部五官局部容积形变；`exaggerated-takes` 涵盖全身姿态暴退跳跃的完整时序。

## E — 可执行步骤 (Execution)

1. **确定表情主基调与形变倾向**:
   - 兴奋/恐惧/惊叫 ➔ **垂直拉伸倾向 (Vertical Stretch)**；
   - 愤怒/咬牙/假笑/沉思 ➔ **垂直压缩挤压倾向 (Vertical Squash)**。
2. **执行容积守恒形变公式换算**:
   - 若下颌下拉伸长至 $1.5$ 倍高度（$\Delta H = 1.5$）：
   - 两侧脸颊宽度必须缩窄至原宽度的 $\frac{1}{\sqrt{1.5}} \approx 0.81$ 倍（收缩约 $20\%$）；
   - 若面部挤压至 $0.6$ 倍高度（$\Delta H = 0.6$）：
   - 两侧脸颊宽度必须外扩至原宽度的 $\frac{1}{\sqrt{0.6}} \approx 1.29$ 倍（膨胀约 $30\%$）。
3. **联动五官连锁细节**:
   - 垂直拉伸：眉毛上挑、眼眶竖长、嘴唇上下分离开合；
   - 垂直挤压：眉心下沉挤出皱纹、眼眶横向压扁、嘴角向外裂开。
4. **输出标准交付契约**:
   - 输出表情基准极值图、形变缩放比例数据与容积校验结论。

## B — 边界与反模式 (Boundary)

### 失效边界
- 纯写实超逼真电影 VFX（如真人动作捕捉），面部皮肤与骨骼位移受严格肌肉肌腱解剖限制，不可使用卡通量级的 $50\%$ 超尺度挤压拉伸。

### 常见反模式
- **充气膨胀**: 嘴巴张大拉长，脸颊却维持原宽甚至变胖，导致头颅在银幕上瞬间充气放大一圈；
- **石膏脑门**: 颅骨完全僵硬，眉毛不与眼球联动，表情显得呆滞死板。
