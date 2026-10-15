# -*- coding: utf-8 -*-
"""
Professional 24-Frame Walk Cycle for Nv_Rig (Advanced Skeleton)
Built by Animation Lead & TD
"""
import maya.cmds as cmds

def set_key(node, attr, frame, val, in_tangent="auto", out_tangent="auto"):
    cmds.setKeyframe(node, attribute=attr, time=frame, value=val, inTangentType=in_tangent, outTangentType=out_tangent)

def build_pro_walk_cycle():
    # 开启原子撤销块保护
    cmds.undoInfo(openChunk=True)
    try:
        # 设置时间轴为 24 帧标准回放范围
        cmds.playbackOptions(min=1, max=24, animationStartTime=1, animationEndTime=24)
        cmds.currentTime(1)
        
        # 核心基准参数
        base_foot_y = 14.212
        base_foot_z = -6.515
        stride_z = 17.5       # 半步长
        foot_lift_y = 6.2     # 经过时脚抬起高度
        
        base_root_y = 103.805
        base_root_z = -1.544
        root_drop = 2.6       # 下沉幅度
        root_lift = 1.4       # 蹬地推高幅度
        root_sway_x = 1.4     # 骨盆侧向横移
        
        # 清理旧帧
        anim_controls = [
            "RootX_M", "IKLeg_L", "IKLeg_R", "PoleLeg_L", "PoleLeg_R",
            "FKSpine1_M", "FKChest_M", "FKNeck_M", "FKHead_M",
            "FKShoulder_L", "FKElbow_L", "FKWrist_L",
            "FKShoulder_R", "FKElbow_R", "FKWrist_R"
        ]
        for ctrl in anim_controls:
            if cmds.objExists(ctrl):
                cmds.cutKey(ctrl, clear=True)
                
        print("Cleared animation curves on core controls.")

        # =========================================================
        # 1. 右脚 (IKLeg_R) 动画
        # F1: 接触 (前) | F4: 下沉贴地 | F7: 经过支撑 | F10: 蹬地抬跟 | F13: 后极值离地
        # F16: 离地前行 | F19: 悬空最高 | F22: 前探准备着地 | F25: 闭合
        # =========================================================
        r_foot_data = [
            # (Frame, ty, tz, roll, tan_z)
            (1,  base_foot_y, base_foot_z + stride_z, -22.0, "linear"),
            (4,  base_foot_y, base_foot_z + stride_z * 0.6, 0.0, "linear"),
            (7,  base_foot_y, base_foot_z, 0.0, "linear"),
            (10, base_foot_y, base_foot_z - stride_z * 0.6, 26.0, "linear"),
            (13, base_foot_y, base_foot_z - stride_z, 35.0, "spline"),
            (16, base_foot_y + 2.8, base_foot_z - stride_z * 0.6, 12.0, "spline"),
            (19, base_foot_y + foot_lift_y, base_foot_z, -4.0, "spline"),
            (22, base_foot_y + 2.5, base_foot_z + stride_z * 0.6, -14.0, "spline"),
            (25, base_foot_y, base_foot_z + stride_z, -22.0, "linear"),
        ]
        for f, ty, tz, roll, t_type in r_foot_data:
            set_key("IKLeg_R", "translateY", f, ty, t_type, t_type)
            set_key("IKLeg_R", "translateZ", f, tz, t_type, t_type)
            set_key("IKLeg_R", "roll", f, roll, "spline", "spline")
            # 微小的内收外八字保持自然
            set_key("IKLeg_R", "rotateY", f, -2.0, "spline", "spline")

        # =========================================================
        # 2. 左脚 (IKLeg_L) 动画 - 相对右脚严格相位偏移 12 帧
        # =========================================================
        l_foot_data = [
            (1,  base_foot_y, base_foot_z - stride_z, 35.0, "spline"),
            (4,  base_foot_y + 2.8, base_foot_z - stride_z * 0.6, 12.0, "spline"),
            (7,  base_foot_y + foot_lift_y, base_foot_z, -4.0, "spline"),
            (10, base_foot_y + 2.5, base_foot_z + stride_z * 0.6, -14.0, "spline"),
            (13, base_foot_y, base_foot_z + stride_z, -22.0, "linear"),
            (16, base_foot_y, base_foot_z + stride_z * 0.6, 0.0, "linear"),
            (19, base_foot_y, base_foot_z, 0.0, "linear"),
            (22, base_foot_y, base_foot_z - stride_z * 0.6, 26.0, "linear"),
            (25, base_foot_y, base_foot_z - stride_z, 35.0, "spline"),
        ]
        for f, ty, tz, roll, t_type in l_foot_data:
            set_key("IKLeg_L", "translateY", f, ty, t_type, t_type)
            set_key("IKLeg_L", "translateZ", f, tz, t_type, t_type)
            set_key("IKLeg_L", "roll", f, roll, "spline", "spline")
            set_key("IKLeg_L", "rotateY", f, 2.0, "spline", "spline")

        # =========================================================
        # 3. 骨盆总重心 (RootX_M)
        # Y轴: 双峰双谷 (Down at 4, 16; Up at 10, 22)
        # X轴: 倒向支撑脚 (右脚承重向右负值，左脚承重向左正值)
        # 旋转: 反向平衡
        # =========================================================
        root_data = [
            # Frame, ty, tx, tz, rx, ry, rz
            (1,  base_root_y - 1.2,  0.0,            base_root_z,        -0.5, -4.0,  0.0),
            (4,  base_root_y - root_drop, -root_sway_x*0.7, base_root_z - 0.4,  1.5, -2.5, -1.8),
            (7,  base_root_y,        -root_sway_x,      base_root_z,         0.0,  0.0, -3.2),
            (10, base_root_y + root_lift, -root_sway_x*0.5, base_root_z + 0.5, -1.2,  2.5, -1.5),
            (13, base_root_y - 1.2,  0.0,            base_root_z,        -0.5,  4.0,  0.0),
            (16, base_root_y - root_drop,  root_sway_x*0.7, base_root_z - 0.4,  1.5,  2.5,  1.8),
            (19, base_root_y,         root_sway_x,      base_root_z,         0.0,  0.0,  3.2),
            (22, base_root_y + root_lift,  root_sway_x*0.5, base_root_z + 0.5, -1.2, -2.5,  1.5),
            (25, base_root_y - 1.2,  0.0,            base_root_z,        -0.5, -4.0,  0.0),
        ]
        for f, ty, tx, tz, rx, ry, rz in root_data:
            set_key("RootX_M", "translateY", f, ty, "spline", "spline")
            set_key("RootX_M", "translateX", f, tx, "spline", "spline")
            set_key("RootX_M", "translateZ", f, tz, "spline", "spline")
            set_key("RootX_M", "rotateX", f, rx, "spline", "spline")
            set_key("RootX_M", "rotateY", f, ry, "spline", "spline")
            set_key("RootX_M", "rotateZ", f, rz, "spline", "spline")

        # =========================================================
        # 4. 胸腔 (FKChest_M) 与脊椎 (FKSpine1_M)
        # 对立抗衡 (Contrapposto): ry 与骨盆反向，rz 与骨盆反向对冲倾斜
        # =========================================================
        chest_data = [
            # Frame, rx, ry, rz
            (1,   0.5,  3.5,  0.0),
            (4,  -1.0,  2.0,  1.2),
            (7,   0.0,  0.0,  2.2),
            (10,  1.0, -2.0,  1.0),
            (13,  0.5, -3.5,  0.0),
            (16, -1.0, -2.0, -1.2),
            (19,  0.0,  0.0, -2.2),
            (22,  1.0,  2.0, -1.0),
            (25,  0.5,  3.5,  0.0),
        ]
        for f, rx, ry, rz in chest_data:
            set_key("FKChest_M", "rotateX", f, rx, "spline", "spline")
            set_key("FKChest_M", "rotateY", f, ry, "spline", "spline")
            set_key("FKChest_M", "rotateZ", f, rz, "spline", "spline")
            # 脊柱第一节微幅协同 (占 35% 权重)
            set_key("FKSpine1_M", "rotateY", f, ry * 0.35, "spline", "spline")
            set_key("FKSpine1_M", "rotateZ", f, rz * 0.35, "spline", "spline")

        # =========================================================
        # 5. 手臂摆动 (FKShoulder, FKElbow, FKWrist)
        # 右脚前迈(F1) -> 左手向前摆动(rotateZ > 0), 右手向后摆动(rotateZ < 0)
        # 手肘滞后 1 帧，手腕滞后 2 帧
        # =========================================================
        arm_l_data = [
            # Frame, sh_rz, sh_rx, elb_rz, wr_rz
            (1,   22.0,  -4.0,  15.0,  -8.0),   # 前摆极值，手肘微屈，手腕后折(Drag)
            (4,   14.0,  -2.0,  18.0,  -4.0),
            (7,    0.0,   0.0,  10.0,   0.0),   # 经过身体中线
            (10, -12.0,   2.0,   6.0,   6.0),
            (13, -18.0,   3.0,   4.0,   8.0),   # 后摆极值，手肘伸展，手腕前翻
            (16, -12.0,   2.0,   6.0,   4.0),
            (19,   0.0,   0.0,  12.0,   0.0),   # 经过中线向前
            (22,  15.0,  -3.0,  16.0,  -5.0),
            (25,  22.0,  -4.0,  15.0,  -8.0),
        ]
        for f, sh_rz, sh_rx, elb_rz, wr_rz in arm_l_data:
            set_key("FKShoulder_L", "rotateZ", f, sh_rz, "spline", "spline")
            set_key("FKShoulder_L", "rotateX", f, sh_rx, "spline", "spline")
            set_key("FKElbow_L", "rotateZ", f, elb_rz, "spline", "spline")
            set_key("FKWrist_L", "rotateZ", f, wr_rz, "spline", "spline")

        # 右臂镜像半周期 (偏移 12 帧)
        arm_r_data = [
            (1,  -18.0,   3.0,   4.0,   8.0),
            (4,  -12.0,   2.0,   6.0,   4.0),
            (7,    0.0,   0.0,  12.0,   0.0),
            (10,  15.0,  -3.0,  16.0,  -5.0),
            (13,  22.0,  -4.0,  15.0,  -8.0),
            (16,  14.0,  -2.0,  18.0,  -4.0),
            (19,   0.0,   0.0,  10.0,   0.0),
            (22, -12.0,   2.0,   6.0,   6.0),
            (25, -18.0,   3.0,   4.0,   8.0),
        ]
        for f, sh_rz, sh_rx, elb_rz, wr_rz in arm_r_data:
            set_key("FKShoulder_R", "rotateZ", f, sh_rz, "spline", "spline")
            set_key("FKShoulder_R", "rotateX", f, sh_rx, "spline", "spline")
            set_key("FKElbow_R", "rotateZ", f, elb_rz, "spline", "spline")
            set_key("FKWrist_R", "rotateZ", f, wr_rz, "spline", "spline")

        # =========================================================
        # 6. 头部与颈部 (FKHead_M, FKNeck_M)
        # 保持前向水平，微幅吸收反冲 (极佳的生动灵性)
        # =========================================================
        head_data = [
            (1,  -0.5,  0.0,  0.0),
            (4,   0.8,  0.0, -0.6),
            (7,   0.0,  0.0, -1.0),
            (10, -0.8,  0.0, -0.4),
            (13, -0.5,  0.0,  0.0),
            (16,  0.8,  0.0,  0.6),
            (19,  0.0,  0.0,  1.0),
            (22, -0.8,  0.0,  0.4),
            (25, -0.5,  0.0,  0.0),
        ]
        for f, rx, ry, rz in head_data:
            set_key("FKHead_M", "rotateX", f, rx, "spline", "spline")
            set_key("FKHead_M", "rotateZ", f, rz, "spline", "spline")

        # =========================================================
        # 7. 循环无限设置 (Post-Infinity / Pre-Infinity Cycle)
        # 使得动画能够从 1 帧播放到无限帧！
        # =========================================================
        for ctrl in anim_controls:
            if cmds.objExists(ctrl):
                cmds.setInfinity(ctrl, pri="cycle", poi="cycle")

        print("SUCCESS: 24-Frame Professional Walk Cycle created with perfect loops and infinity settings!")

    except Exception as e:
        cmds.warning(f"Error creating walk cycle: {e}")
        raise
    finally:
        cmds.undoInfo(closeChunk=True)

build_pro_walk_cycle()
