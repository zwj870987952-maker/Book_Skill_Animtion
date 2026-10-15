# -*- coding: utf-8 -*-
"""
=============================================================================
Aesthetic High-Fashion Feminine Walk Cycle (高审美女性/T台步态)
Key artistic drivers:
- Catwalk Crossover Stride (一字线猫步，双脚内收至中线)
- Sensual Hip Pop & Figure-8 Sway (骨盆大范围摇曳、顶胯拔高与侧倾)
- S-Curve Spine & Arch (挺胸提臀、腰部自然生理凹陷)
- Elegant Hand Pose & Organic Fingers (纤细手型，指节阶梯式微屈)
- Soft Fluid Arm Pendulum (告别机械大甩，贴体柔和钟摆与甩鞭延迟)
- High-Heel Biomechanics (高跟鞋脚背绷直与鞋跟受力)
=============================================================================
"""
import maya.cmds as cmds

def set_k(node, attr, f, val, in_t="spline", out_t="spline"):
    cmds.setKeyframe(node, attribute=attr, time=f, value=val, inTangentType=in_t, outTangentType=out_t)

def apply_aesthetic_walk():
    cmds.undoInfo(openChunk=True)
    try:
        print(">>> Applying Aesthetic Feminine Walk Cycle...")
        
        # 1. 时间轴设置
        cmds.playbackOptions(min=1, max=24, animationStartTime=1, animationEndTime=24)
        cmds.currentTime(1)
        
        # 2. 清理全部旧帧
        all_controls = [
            "RootX_M", "IKLeg_L", "IKLeg_R", "PoleLeg_L", "PoleLeg_R",
            "FKSpine1_M", "FKSpine2_M", "FKChest_M", "FKNeck_M", "FKHead_M",
            "FKScapula_L", "FKScapula_R",
            "FKShoulder_L", "FKElbow_L", "FKWrist_L",
            "FKShoulder_R", "FKElbow_R", "FKWrist_R"
        ]
        # 添加手指控制器
        for side in ["L", "R"]:
            for finger in ["Index", "Middle", "Ring", "Pinky", "Thumb"]:
                for idx in [1, 2, 3]:
                    all_controls.append(f"FK{finger}Finger{idx}_{side}")
                    
        for ctrl in all_controls:
            if cmds.objExists(ctrl):
                cmds.cutKey(ctrl, clear=True)
                for tr in ["translate", "rotate"]:
                    for ax in ["X", "Y", "Z"]:
                        full = f"{ctrl}.{tr}{ax}"
                        if cmds.objExists(full) and cmds.getAttr(full, settable=True):
                            cmds.setAttr(full, 0.0)
                if cmds.attributeQuery("roll", node=ctrl, exists=True):
                    cmds.setAttr(f"{ctrl}.roll", 0.0)

        # =====================================================================
        # 3. 手型塑造：永久注入优雅女性纤细手型 (Relaxed Feminine Hand Pose)
        # =====================================================================
        # 手指弯曲参数 (基节, 中节, 末节)
        finger_curls = {
            "Index":  [-12.0, -16.0, -10.0],
            "Middle": [-18.0, -22.0, -14.0],
            "Ring":   [-24.0, -28.0, -18.0],
            "Pinky":  [-28.0, -32.0, -20.0]
        }
        for side in ["L", "R"]:
            for finger, curls in finger_curls.items():
                for i, c in enumerate(curls):
                    node = f"FK{finger}Finger{i+1}_{side}"
                    if cmds.objExists(node):
                        cmds.setAttr(f"{node}.rotateZ", c)
            # 大拇指自然内收贴掌
            th1 = f"FKThumbFinger1_{side}"
            th2 = f"FKThumbFinger2_{side}"
            th3 = f"FKThumbFinger3_{side}"
            if cmds.objExists(th1):
                cmds.setAttr(f"{th1}.rotate", 12.0, -8.0, -15.0)
            if cmds.objExists(th2):
                cmds.setAttr(f"{th2}.rotateZ", -12.0)
            if cmds.objExists(th3):
                cmds.setAttr(f"{th3}.rotateZ", -10.0)

        # =====================================================================
        # 4. 步态运动学参数 (Catwalk High-Heel Stride)
        # =====================================================================
        stride_z = 15.5       # 稍微适中、修长的步长 (跨步不过大，保持收敛)
        cross_x = 4.2         # 落地时向中线内收，形成一字线走秀感 (Catwalk crossover)
        pass_lift_y = 5.2     # 经过时脚抬起高度 (膝盖提纯)
        
        # =====================================================================
        # 5. 右脚 (IKLeg_R)
        # 落地内收 (translateX=4.2 往中线聚拢)；经过时膝盖内扣、脚腕绷直 (roll=-10)
        # =====================================================================
        r_foot_keys = [
            # Frame, ty, tz, tx, roll, ry, tan_z
            (1,   0.0,         stride_z,        cross_x, -12.0, -1.0, "linear"), # Heel strike
            (4,   0.0,         stride_z * 0.6,  cross_x,   0.0, -1.0, "linear"), # Down 全掌贴地承重
            (7,   0.0,         0.0,             cross_x,   0.0, -1.0, "linear"), # Passing 承重立足点
            (10,  0.0,        -stride_z * 0.6,  cross_x,  28.0, -1.0, "linear"), # Up 前掌蹬地抬跟
            (13,  0.0,        -stride_z,        cross_x,  36.0, -1.0, "spline"), # Toe-off 离地
            (16,  pass_lift_y * 0.6, -stride_z * 0.6, cross_x * 0.5, 10.0, -0.5, "spline"), # 悬空中段
            (19,  pass_lift_y,  0.0,            1.0,     -12.0,  0.5, "spline"), # Passing 经过顶点脚尖绷直
            (22,  pass_lift_y * 0.5,  stride_z * 0.6, cross_x * 0.8, -14.0, -0.5, "spline"), # 前探准备
            (25,  0.0,         stride_z,        cross_x, -12.0, -1.0, "linear"), # 闭合 F1
        ]
        for f, ty, tz, tx, roll, ry, t_type in r_foot_keys:
            set_k("IKLeg_R", "translateY", f, ty, "spline", "spline")
            set_k("IKLeg_R", "translateZ", f, tz, t_type, t_type)
            set_k("IKLeg_R", "translateX", f, tx, "spline", "spline")
            set_k("IKLeg_R", "roll", f, roll, "spline", "spline")
            set_k("IKLeg_R", "rotateY", f, ry, "spline", "spline")

        # =====================================================================
        # 6. 左脚 (IKLeg_L) - 相对右脚严格相位偏移 12 帧
        # =====================================================================
        l_foot_keys = [
            (1,   0.0,        -stride_z,       -cross_x,  36.0,  1.0, "spline"),
            (4,   pass_lift_y * 0.6, -stride_z * 0.6, -cross_x * 0.5, 10.0, 0.5, "spline"),
            (7,   pass_lift_y,  0.0,           -1.0,     -12.0, -0.5, "spline"),
            (10,  pass_lift_y * 0.5,  stride_z * 0.6, -cross_x * 0.8, -14.0, 0.5, "spline"),
            (13,  0.0,         stride_z,       -cross_x, -12.0,  1.0, "linear"),
            (16,  0.0,         stride_z * 0.6, -cross_x,   0.0,  1.0, "linear"),
            (19,  0.0,         0.0,            -cross_x,   0.0,  1.0, "linear"),
            (22,  0.0,        -stride_z * 0.6, -cross_x,  28.0,  1.0, "linear"),
            (25,  0.0,        -stride_z,       -cross_x,  36.0,  1.0, "spline"),
        ]
        for f, ty, tz, tx, roll, ry, t_type in l_foot_keys:
            set_k("IKLeg_L", "translateY", f, ty, "spline", "spline")
            set_k("IKLeg_L", "translateZ", f, tz, t_type, t_type)
            set_k("IKLeg_L", "translateX", f, tx, "spline", "spline")
            set_k("IKLeg_L", "roll", f, roll, "spline", "spline")
            set_k("IKLeg_L", "rotateY", f, ry, "spline", "spline")

        # =====================================================================
        # 7. 骨盆质心动力学：极致的女性 8 字顶胯摇曳 (Sensual Hip Sway)
        # tx: 右承重向右 -3.2，左承重向左 +3.2 (极大增强女性髋部摆动)
        # rz: 骨盆侧倾达 -6.2度 / +6.2度 (承重侧髋骨显著拔高！)
        # ry: 跨步水平回旋达 -6.5度 / +6.5度
        # rx: 保持骨盆微前倾 +1.5度，腰窝深陷
        # =====================================================================
        root_keys = [
            # Frame, ty, tx, tz, rx, ry, rz
            (1,  -1.0,  0.0,  0.0,   1.5, -6.5,  0.0),  # Contact 1
            (4,  -2.4, -2.4, -0.3,   2.5, -4.2, -4.2),  # Down 1 (吸震，开始向右顶胯)
            (7,  -0.2, -3.2,  0.0,   1.5,  0.0, -6.2),  # Passing 1 (右髋顶出极值、拔高极值！)
            (10,  1.5, -2.0,  0.4,   0.5,  4.2, -3.5),  # Up 1 (蹬地挺拔)
            (13, -1.0,  0.0,  0.0,   1.5,  6.5,  0.0),  # Contact 2
            (16, -2.4,  2.4, -0.3,   2.5,  4.2,  4.2),  # Down 2 (吸震，开始向左顶胯)
            (19, -0.2,  3.2,  0.0,   1.5,  0.0,  6.2),  # Passing 2 (左髋顶出极值、拔高极值！)
            (22,  1.5,  2.0,  0.4,   0.5, -4.2,  3.5),  # Up 2
            (25, -1.0,  0.0,  0.0,   1.5, -6.5,  0.0),  # 闭合
        ]
        for f, ty, tx, tz, rx, ry, rz in root_keys:
            set_k("RootX_M", "translateY", f, ty)
            set_k("RootX_M", "translateX", f, tx)
            set_k("RootX_M", "translateZ", f, tz)
            set_k("RootX_M", "rotateX", f, rx)
            set_k("RootX_M", "rotateY", f, ry)
            set_k("RootX_M", "rotateZ", f, rz)

        # =====================================================================
        # 8. 脊柱与胸腔 (FKSpine1, FKSpine2, FKChest)
        # S 形体态：挺胸 (rx 为负)、Contrapposto 强烈反向倾斜 (rz) 与反相扭转 (ry)
        # =====================================================================
        # 胸腔核心
        chest_keys = [
            # Frame, rx, ry, rz
            (1,  -4.5,  5.0,  0.0),   # 挺胸 -4.5，反相扭转 +5.0
            (4,  -5.5,  3.2,  2.8),
            (7,  -4.5,  0.0,  4.5),   # 骨盆右倾 -6.2 -> 胸廓反向左倾 +4.5！绝美 S 弯！
            (10, -3.5, -3.2,  2.2),
            (13, -4.5, -5.0,  0.0),
            (16, -5.5, -3.2, -2.8),
            (19, -4.5,  0.0, -4.5),   # 骨盆左倾 +6.2 -> 胸廓反向右倾 -4.5！
            (22, -3.5,  3.2, -2.2),
            (25, -4.5,  5.0,  0.0),
        ]
        for f, rx, ry, rz in chest_keys:
            set_k("FKChest_M", "rotateX", f, rx)
            set_k("FKChest_M", "rotateY", f, ry)
            set_k("FKChest_M", "rotateZ", f, rz)
            
            # 脊椎第一节与第二节平滑分配，塑造有机腰身
            if cmds.objExists("FKSpine1_M"):
                set_k("FKSpine1_M", "rotateX", f, 1.2)
                set_k("FKSpine1_M", "rotateY", f, ry * 0.35)
                set_k("FKSpine1_M", "rotateZ", f, rz * 0.35)
            if cmds.objExists("FKSpine2_M"):
                set_k("FKSpine2_M", "rotateX", f, -1.5)
                set_k("FKSpine2_M", "rotateY", f, ry * 0.65)
                set_k("FKSpine2_M", "rotateZ", f, rz * 0.65)

        # =====================================================================
        # 9. 锁骨 (FKScapula_L / FKScapula_R) 呼吸感
        # =====================================================================
        for f, ry in [(1, 2.5), (7, 0.0), (13, -2.5), (19, 0.0), (25, 2.5)]:
            if cmds.objExists("FKScapula_L"):
                set_k("FKScapula_L", "rotateY", f, ry)
                set_k("FKScapula_L", "rotateZ", f, 1.0 if ry > 0 else -1.0)
            if cmds.objExists("FKScapula_R"):
                set_k("FKScapula_R", "rotateY", f, -ry)
                set_k("FKScapula_R", "rotateZ", f, -1.0 if ry > 0 else 1.0)

        # =====================================================================
        # 10. 双臂柔美摆动与流体延迟 (Soft Feminine Arm Pendulum)
        # 告别民兵大甩步：前后摆幅缩减至优雅的 [-7°, +11°]
        # rotateY 恒定内收 35°（贴近身体）
        # rotateX 给予前倾 6°~8°（手臂微弯向前，手掌贴近大腿）
        # 手腕液体滞后 (wr_rz)，手肘微曲自然外弓 (elb_rz 16°~22°)
        # =====================================================================
        arm_l_keys = [
            # Frame, sh_rz, sh_rx, elb_rz, wr_rz
            (1,   11.0,  7.0,  20.0,  -5.0), # 前摆顶点，手腕风阻后折
            (4,    6.0,  8.0,  22.0,  -2.0),
            (7,   -2.0,  7.0,  18.0,   1.0), # 经过身体中线
            (10,  -6.0,  6.0,  15.0,   4.0),
            (13,  -8.0,  5.0,  14.0,   5.0), # 后摆顶点，手腕前折
            (16,  -4.0,  6.0,  16.0,   3.0),
            (19,   1.0,  7.0,  18.0,  -1.0),
            (22,   7.0,  8.0,  21.0,  -4.0),
            (25,  11.0,  7.0,  20.0,  -5.0),
        ]
        for f, sh_rz, sh_rx, elb_rz, wr_rz in arm_l_keys:
            set_k("FKShoulder_L", "rotateZ", f, sh_rz)
            set_k("FKShoulder_L", "rotateY", f, 35.0)
            set_k("FKShoulder_L", "rotateX", f, sh_rx)
            set_k("FKElbow_L", "rotateZ", f, elb_rz)
            set_k("FKWrist_L", "rotateZ", f, wr_rz)
            set_k("FKWrist_L", "rotateX", f, 5.0)

        arm_r_keys = [
            (1,   -8.0,  5.0,  14.0,   5.0),
            (4,   -4.0,  6.0,  16.0,   3.0),
            (7,    1.0,  7.0,  18.0,  -1.0),
            (10,   7.0,  8.0,  21.0,  -4.0),
            (13,  11.0,  7.0,  20.0,  -5.0),
            (16,   6.0,  8.0,  22.0,  -2.0),
            (19,  -2.0,  7.0,  18.0,   1.0),
            (22,  -6.0,  6.0,  15.0,   4.0),
            (25,  -8.0,  5.0,  14.0,   5.0),
        ]
        for f, sh_rz, sh_rx, elb_rz, wr_rz in arm_r_keys:
            set_k("FKShoulder_R", "rotateZ", f, sh_rz)
            set_k("FKShoulder_R", "rotateY", f, 35.0)
            set_k("FKShoulder_R", "rotateX", f, sh_rx)
            set_k("FKElbow_R", "rotateZ", f, elb_rz)
            set_k("FKWrist_R", "rotateZ", f, wr_rz)
            set_k("FKWrist_R", "rotateX", f, 5.0)

        # =====================================================================
        # 11. 头部与颈部 (FKHead_M, FKNeck_M) 高贵仪态
        # 自信昂首 (rx = -3.0)，侧倾微幅反向代偿保持视线平稳
        # =====================================================================
        head_keys = [
            (1,  -3.0,  0.0),
            (4,  -2.5, -1.2),
            (7,  -3.0, -1.8),
            (10, -3.5, -0.8),
            (13, -3.0,  0.0),
            (16, -2.5,  1.2),
            (19, -3.0,  1.8),
            (22, -3.5,  0.8),
            (25, -3.0,  0.0),
        ]
        for f, rx, rz in head_keys:
            set_k("FKHead_M", "rotateX", f, rx)
            set_k("FKHead_M", "rotateZ", f, rz)

        # =====================================================================
        # 12. 开启所有曲线的无限循环外推 (Infinity Cycle)
        # =====================================================================
        for ctrl in all_controls:
            if cmds.objExists(ctrl):
                cmds.setInfinity(ctrl, pri="cycle", poi="cycle")

        print(">>> SUCCESS: Aesthetic Feminine Walk Cycle applied perfectly!")
        
    except Exception as err:
        cmds.warning(f"Error applying aesthetic walk: {err}")
        raise
    finally:
        cmds.undoInfo(closeChunk=True)

if __name__ == "__main__":
    apply_aesthetic_walk()
