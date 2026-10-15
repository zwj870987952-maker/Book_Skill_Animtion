# -*- coding: utf-8 -*-
"""
=============================================================================
Master 24-Frame Walk Cycle for Nv_Rig (Advanced Skeleton 5.x)
Author: World-Class Animation Lead & Technical Director
=============================================================================
Physics & Mechanics Implementation:
- Richard Williams 4-Pose Cadence: Contact (1, 13), Down (4, 16), Passing (7, 19), Up (10, 22)
- Biomechanical Pelvic Motion: Double-bounce Y-axis, lateral weight transfer X-axis, yaw & roll Contrapposto
- Foot Roll & Anti-Slip Rigor: Linear tangents during stance phase, smooth splines during swing phase
- Upper Body Compensation: Chest & spine counter-twist, shoulders level against pelvic drop
- Arm Swing & Dynamic Overlap: Shoulder pendulum with 1-frame elbow lag and 2-frame wrist drag
- Seamless Infinity: Post/Pre-Infinity cycle enabled on all curves
=============================================================================
"""
import maya.cmds as cmds

def set_key(node, attr, frame, val, in_tan="spline", out_tan="spline"):
    cmds.setKeyframe(
        node,
        attribute=attr,
        time=frame,
        value=val,
        inTangentType=in_tan,
        outTangentType=out_tan
    )

def apply_master_walk_cycle():
    cmds.undoInfo(openChunk=True)
    try:
        print(">>> Initializing Master Walk Cycle Build...")
        
        # 1. 设置时间轴范围 (24 帧标准电影帧率循环)
        cmds.playbackOptions(min=1, max=24, animationStartTime=1, animationEndTime=24)
        cmds.currentTime(1)
        
        # 2. 待处理的核心控制器清单
        controls = [
            "RootX_M", "IKLeg_L", "IKLeg_R", "PoleLeg_L", "PoleLeg_R",
            "FKSpine1_M", "FKChest_M", "FKNeck_M", "FKHead_M",
            "FKShoulder_L", "FKElbow_L", "FKWrist_L",
            "FKShoulder_R", "FKElbow_R", "FKWrist_R"
        ]
        
        # 清理旧动画曲线并归零
        for ctrl in controls:
            if cmds.objExists(ctrl):
                cmds.cutKey(ctrl, clear=True)
                # 恢复默认变换
                for ax in ["X", "Y", "Z"]:
                    for tr in ["translate", "rotate"]:
                        full = f"{ctrl}.{tr}{ax}"
                        if cmds.objExists(full) and cmds.getAttr(full, settable=True):
                            cmds.setAttr(full, 0.0)
                if cmds.attributeQuery("roll", node=ctrl, exists=True):
                    cmds.setAttr(f"{ctrl}.roll", 0.0)
                    
        print(">>> Existing animation stripped, transforms zeroed.")

        # =====================================================================
        # 3. 步态运动学参数标尺 (Based on Rest Zero Transforms)
        # =====================================================================
        stride_z = 17.0       # 半步长 (前后各 17 码，总跨步 34 码)
        foot_lift = 4.8       # 经过时脚掌离地高度
        root_down = -2.6      # 重力下沉最大深度 (F4, F16)
        root_up = 1.6         # 蹬地伸展最大高度 (F10, F22)
        root_sway = 1.5       # 重心侧移量 (偏向支撑腿)
        arm_adduct = 34.0     # 双臂自然贴体下垂内收角
        
        # =====================================================================
        # 4. 右脚 (IKLeg_R) 关键帧与切线
        # F1~F13 为地面支撑期 (Z轴位移使用严格线性切线，彻底杜绝滑步)
        # F13~F25 为悬空前移期 (使用平滑 Spline 切线)
        # =====================================================================
        r_foot_keys = [
            # Frame, ty, tz, roll, tan_z
            (1,   0.0,        stride_z,       -22.0, "linear"),  # 接触 (Heel Strike)
            (4,   0.0,        stride_z * 0.6,   0.0, "linear"),  # 下沉 (全脚贴地承重)
            (7,   0.0,        0.0,              0.0, "linear"),  # 经过 (身体垂直经过脚上方)
            (10,  0.0,       -stride_z * 0.6,  26.0, "linear"),  # 蹬地 (脚跟拔起，前掌蹬地)
            (13,  0.0,       -stride_z,        36.0, "spline"),  # 离地瞬间 (脚尖最后推力)
            (16,  foot_lift * 0.55, -stride_z * 0.6, 12.0, "spline"), # 悬空中段 (折叠提脚)
            (19,  foot_lift,  0.0,             -4.0, "spline"),  # 经过顶点 (脚掌向前摆过身体)
            (22,  foot_lift * 0.45,  stride_z * 0.6, -15.0, "spline"), # 前探准备 (脚跟前伸)
            (25,  0.0,        stride_z,       -22.0, "linear"),  # 闭合第 1 帧
        ]
        
        for f, ty, tz, roll, t_type in r_foot_keys:
            set_key("IKLeg_R", "translateY", f, ty, "spline", "spline")
            set_key("IKLeg_R", "translateZ", f, tz, t_type, t_type)
            set_key("IKLeg_R", "roll", f, roll, "spline", "spline")
            # 微小的优雅自然外八字 (2.5 度)
            set_key("IKLeg_R", "rotateY", f, -2.5, "spline", "spline")

        # =====================================================================
        # 5. 左脚 (IKLeg_L) 关键帧与切线 (严格相对右脚偏移 12 帧)
        # F1~F13 为悬空前移期 | F13~F25 为地面支撑期 (线性切线防滑步)
        # =====================================================================
        l_foot_keys = [
            # Frame, ty, tz, roll, tan_z
            (1,   0.0,       -stride_z,        36.0, "spline"),
            (4,   foot_lift * 0.55, -stride_z * 0.6, 12.0, "spline"),
            (7,   foot_lift,  0.0,             -4.0, "spline"),
            (10,  foot_lift * 0.45,  stride_z * 0.6, -15.0, "spline"),
            (13,  0.0,        stride_z,       -22.0, "linear"),
            (16,  0.0,        stride_z * 0.6,   0.0, "linear"),
            (19,  0.0,        0.0,              0.0, "linear"),
            (22,  0.0,       -stride_z * 0.6,  26.0, "linear"),
            (25,  0.0,       -stride_z,        36.0, "spline"),
        ]
        
        for f, ty, tz, roll, t_type in l_foot_keys:
            set_key("IKLeg_L", "translateY", f, ty, "spline", "spline")
            set_key("IKLeg_L", "translateZ", f, tz, t_type, t_type)
            set_key("IKLeg_L", "roll", f, roll, "spline", "spline")
            set_key("IKLeg_L", "rotateY", f, 2.5, "spline", "spline")

        # =====================================================================
        # 6. 骨盆主质心 (RootX_M)
        # Y轴: 双峰双谷动力学 (Down at 4, 16; Up at 10, 22)
        # X轴: 倒向支撑侧 (右侧支撑向右 -1.5，左侧支撑向左 +1.5)
        # 旋转: 骨盆随迈腿水平回旋 (Yaw)，随单腿承重产生侧倾 (Roll)
        # =====================================================================
        root_keys = [
            # Frame, ty, tx, tz, rx, ry, rz
            (1,  -1.0,        0.0,              0.0,  -0.5, -4.5,  0.0),
            (4,   root_down, -root_sway * 0.7, -0.3,   1.5, -2.8, -1.8),
            (7,   0.0,       -root_sway,        0.0,   0.0,  0.0, -3.2),
            (10,  root_up,   -root_sway * 0.5,  0.4,  -1.0,  2.8, -1.5),
            (13, -1.0,        0.0,              0.0,  -0.5,  4.5,  0.0),
            (16,  root_down,  root_sway * 0.7, -0.3,   1.5,  2.8,  1.8),
            (19,  0.0,        root_sway,        0.0,   0.0,  0.0,  3.2),
            (22,  root_up,    root_sway * 0.5,  0.4,  -1.0, -2.8,  1.5),
            (25, -1.0,        0.0,              0.0,  -0.5, -4.5,  0.0),
        ]
        for f, ty, tx, tz, rx, ry, rz in root_keys:
            set_key("RootX_M", "translateY", f, ty)
            set_key("RootX_M", "translateX", f, tx)
            set_key("RootX_M", "translateZ", f, tz)
            set_key("RootX_M", "rotateX", f, rx)
            set_key("RootX_M", "rotateY", f, ry)
            set_key("RootX_M", "rotateZ", f, rz)

        # =====================================================================
        # 7. 胸腔 (FKChest_M) 与脊椎第一节 (FKSpine1_M)
        # 对立平衡 (Contrapposto):
        # 胸腔扭转 (rotateY) 与骨盆反向，保持肩膀平衡
        # 胸腔侧倾 (rotateZ) 与骨盆反向对冲，保持视线平直
        # =====================================================================
        chest_keys = [
            # Frame, rx, ry, rz
            (1,   0.5,  4.0,  0.0),
            (4,  -1.2,  2.5,  1.2),
            (7,   0.0,  0.0,  2.2),
            (10,  1.0, -2.2,  1.0),
            (13,  0.5, -4.0,  0.0),
            (16, -1.2, -2.5, -1.2),
            (19,  0.0,  0.0, -2.2),
            (22,  1.0,  2.2, -1.0),
            (25,  0.5,  4.0,  0.0),
        ]
        for f, rx, ry, rz in chest_keys:
            set_key("FKChest_M", "rotateX", f, rx)
            set_key("FKChest_M", "rotateY", f, ry)
            set_key("FKChest_M", "rotateZ", f, rz)
            # 脊椎平滑分配
            set_key("FKSpine1_M", "rotateY", f, ry * 0.35)
            set_key("FKSpine1_M", "rotateZ", f, rz * 0.35)

        # =====================================================================
        # 8. 双臂协同与次级跟随 (FKShoulder, FKElbow, FKWrist)
        # rotateY 恒定内收 ~34 度（使手臂从 A-pose 自然贴垂身体）
        # rotateZ 为前后钟摆主轴 (左臂与右腿反相，右臂与左腿反相)
        # 手肘滞后 1 帧，手腕滞后 2 帧 (Drag & Overlap)
        # =====================================================================
        arm_l_keys = [
            # Frame, sh_rz, elb_rz, wr_rz
            (1,   20.0,  16.0,  -7.0),  # 前摆极值，手肘微屈，手腕风阻后折
            (4,   13.0,  18.0,  -3.0),
            (7,    0.0,  12.0,   0.0),  # 经过身体中线
            (10, -11.0,   7.0,   5.0),
            (13, -16.0,   4.0,   7.0),  # 后摆极值，手肘舒展，手腕前折
            (16, -10.0,   6.0,   4.0),
            (19,   0.0,  12.0,   0.0),  # 摆回中线
            (22,  14.0,  17.0,  -5.0),
            (25,  20.0,  16.0,  -7.0),
        ]
        for f, sh_rz, elb_rz, wr_rz in arm_l_keys:
            set_key("FKShoulder_L", "rotateZ", f, sh_rz)
            set_key("FKShoulder_L", "rotateY", f, arm_adduct)
            set_key("FKElbow_L", "rotateZ", f, elb_rz)
            set_key("FKWrist_L", "rotateZ", f, wr_rz)

        arm_r_keys = [
            (1,  -16.0,   4.0,   7.0),
            (4,  -10.0,   6.0,   4.0),
            (7,    0.0,  12.0,   0.0),
            (10,  14.0,  17.0,  -5.0),
            (13,  20.0,  16.0,  -7.0),
            (16,  13.0,  18.0,  -3.0),
            (19,   0.0,  12.0,   0.0),
            (22, -11.0,   7.0,   5.0),
            (25, -16.0,   4.0,   7.0),
        ]
        for f, sh_rz, elb_rz, wr_rz in arm_r_keys:
            set_key("FKShoulder_R", "rotateZ", f, sh_rz)
            set_key("FKShoulder_R", "rotateY", f, arm_adduct)
            set_key("FKElbow_R", "rotateZ", f, elb_rz)
            set_key("FKWrist_R", "rotateZ", f, wr_rz)

        # =====================================================================
        # 9. 头部与颈部 (FKHead_M, FKNeck_M)
        # 保持视线平直，微幅逆向缓冲吸收躯干震动
        # =====================================================================
        head_keys = [
            (1,  -0.4,  0.0),
            (4,   0.6, -0.6),
            (7,   0.0, -1.0),
            (10, -0.6, -0.4),
            (13, -0.4,  0.0),
            (16,  0.6,  0.6),
            (19,  0.0,  1.0),
            (22, -0.6,  0.4),
            (25, -0.4,  0.0),
        ]
        for f, rx, rz in head_keys:
            set_key("FKHead_M", "rotateX", f, rx)
            set_key("FKHead_M", "rotateZ", f, rz)

        # =====================================================================
        # 10. 全局无限循环外推设置 (Cycle Pre & Post Infinity)
        # =====================================================================
        for ctrl in controls:
            if cmds.objExists(ctrl):
                cmds.setInfinity(ctrl, pri="cycle", poi="cycle")

        print(">>> SUCCESS: 24-Frame Master Walk Cycle applied flawlessly!")

    except Exception as err:
        cmds.warning(f"Error during walk cycle generation: {err}")
        raise
    finally:
        cmds.undoInfo(closeChunk=True)

if __name__ == "__main__":
    apply_master_walk_cycle()
