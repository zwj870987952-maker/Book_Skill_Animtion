# 能力卡: 眼球追踪眼睑跟随与扫视跳跃绑定 (Lid Follow & Saccades)

## Rationale (核心原理)
在生物力学中，眼球是一个嵌在眼眶脂肪与肌肉中的球体。当眼球向上看时，眼球凸起的角膜会自然推挤上眼睑并随提上睑肌协同上提；当眼球向下看时，上眼睑必然大幅顺势下垂盖住眼球。
如果绑定中没有“眼睑跟随（Lid Follow）”，当角色向下看时，上眼睑仍高高挂在上方，会露出大面积惨白的上方巩膜，瞬间沦为极其吓人的“机械死鱼眼”。
同时，人类眼球的转动绝对不是平滑线性的——人类通过**扫视（Saccadic Movements / Eye Darts）**在不同观察点之间以极高角速度（每秒数百度）在 1 帧内离散跳跃，然后在目标点保持定格。

## Instruction (跟随算法与扫视工程规范)

### 1. 眼睑跟随 (Lid Follow) 自动化联动算法
在绑定层建立眼球 Pitch 旋转（绕 $X$ 轴俯仰）到上下眼睑骨骼/混合形的数学传递关系：
设眼球向上看时旋转角 $\theta > 0$，向下看时 $\theta < 0$：
- **上眼睑跟随位移 (Upper Lid Follow)**:
  $$\Delta Y_{\text{upper}} = \begin{cases} k_{\text{up}} \cdot \theta, & \text{if } \theta > 0 \quad (k_{\text{up}} \approx 0.25 \sim 0.35) \\ k_{\text{down}} \cdot \theta, & \text{if } \theta < 0 \quad (k_{\text{down}} \approx 0.40 \sim 0.50) \end{cases}$$
  *向下看时的跟随系数必须大于向上看时的系数，确保下看时眼睑能够完全跟进覆盖角膜*；
- **下眼睑跟随位移 (Lower Lid Follow)**:
  $$\Delta Y_{\text{lower}} = \begin{cases} m_{\text{up}} \cdot \theta, & \text{if } \theta > 0 \quad (m_{\text{up}} \approx 0.10 \sim 0.15) \\ m_{\text{down}} \cdot \theta, & \text{if } \theta < 0 \quad (m_{\text{down}} \approx 0.20 \sim 0.25) \end{cases}$$

### 2. 扫视跳跃 (Eye Darts / Saccades) 动画制作规范
- **单帧瞬移原则**: 视线从目标物体 A 转移到目标物体 B 时，眼球旋转控制器的关键帧插值**必须在 1 帧（最多 2 帧）内直接跳跃到位**；
- **消除平滑缓动**: 严禁在两个注视点之间使用慢入慢出（Ease-in / Ease-out）曲线；
- **注视保持周期 (Fixation Hold)**: 每次跳跃到位后，眼球必须在当前方向绝对定格 **8 到 24 帧（约 1/3 秒至 1 秒）**，模拟视网膜黄斑中心凹成像聚焦过程；
- **微颤动微跳 (Micro-Darts)**: 在长段倾听或对白中，眼球可在相距 $1^\circ \sim 2^\circ$ 的微小范围内发生极轻微的副跳动，表现活生生的思维流。

## Actionable Example (Maya 节点网络与关键帧曲线排布)
```python
# Maya / PyMEL 表达式或节点网络连接伪代码
def setup_lid_follow(eye_joint, upper_lid_ctrl, lower_lid_ctrl):
    """
    通过 Clamp 与 MultiplyDivide 节点构建无缝的眼睑跟随网络
    """
    import maya.cmds as cmds
    
    # 建立驱动键或表达式
    expr_code = """
    float $pitch = {eye}.rotateX;
    if ($pitch > 0) {
        {upper}.translateY = $pitch * 0.035;
        {lower}.translateY = $pitch * 0.015;
    } else {
        {upper}.translateY = $pitch * 0.050;
        {lower}.translateY = $pitch * 0.025;
    }
    """.format(eye=eye_joint, upper=upper_lid_ctrl, lower=lower_lid_ctrl)
    
    cmds.expression(s=expr_code, name="expr_lid_follow")
```

## Constraints (约束与禁止)
- **严禁眼球平滑线性漂移**: 严禁在没有任何眼球微跳的情况下让眼球缓慢滑移超过 6 帧；
- **注视点分离约束**: 角色双眼的目标约束（Aim Target）必须统一绑定在一个主控制器（Eye_LookAt_Main）上，并在局部保留双侧微调自由度，避免双眼出现方向脱节；
- **极限视角防穿插**: 眼球转到极左或极右时，角膜凸起不可穿透眼角内眦泪阜（Caruncle）几何体。

## Verification (验收标准)
- **俯仰动态测试**: 旋转眼球使角色从看天花板平滑连续过渡至看地面，全程观察眼白露出比例，上眼皮全程保持自然贴合角膜边缘，无惊恐露白穿帮；
- **视线真实感盲测**: 角色在 5 秒长镜头中观察环境，眼球呈现清晰的“跳跃-定格-跳跃”节奏，完全摒除机器人偶式悬浮平移。
