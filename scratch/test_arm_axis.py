# -*- coding: utf-8 -*-
import maya.cmds as cmds

def test_arm_axis():
    orig_pos = cmds.xform("FKWrist_L", q=True, ws=True, t=True)
    
    for axis, val in [("rotateX", 30), ("rotateY", 30), ("rotateZ", 30)]:
        cmds.setAttr(f"FKShoulder_L.{axis}", val)
        new_pos = cmds.xform("FKWrist_L", q=True, ws=True, t=True)
        cmds.setAttr(f"FKShoulder_L.{axis}", 0)
        
        delta = [round(new_pos[i] - orig_pos[i], 2) for i in range(3)]
        print(f"FKShoulder_L.{axis}=30 -> Wrist Delta [dX, dY, dZ]: {delta}")

    # 同样测试 FKElbow_L 弯曲轴
    orig_wrist = cmds.xform("FKWrist_L", q=True, ws=True, t=True)
    for axis, val in [("rotateX", 30), ("rotateY", 30), ("rotateZ", 30)]:
        cmds.setAttr(f"FKElbow_L.{axis}", val)
        new_pos = cmds.xform("FKWrist_L", q=True, ws=True, t=True)
        cmds.setAttr(f"FKElbow_L.{axis}", 0)
        delta = [round(new_pos[i] - orig_wrist[i], 2) for i in range(3)]
        print(f"FKElbow_L.{axis}=30 -> Wrist Delta [dX, dY, dZ]: {delta}")

    # 测试 IKLeg_L.roll
    cmds.setAttr("IKLeg_L.roll", 30)
    toe_pos = cmds.xform("IKToes_L", q=True, ws=True, t=True)
    ankle_pos = cmds.xform("Ankle_L", q=True, ws=True, t=True)
    cmds.setAttr("IKLeg_L.roll", 0)
    print("roll=30 -> Ankle Y:", round(ankle_pos[1], 2), "Toes Y:", round(toe_pos[1], 2))

test_arm_axis()
