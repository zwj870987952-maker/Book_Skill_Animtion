# -*- coding: utf-8 -*-
import maya.cmds as cmds

def test_right_and_feet():
    # 测试右臂
    orig_pos_r = cmds.xform("FKWrist_R", q=True, ws=True, t=True)
    for axis in ["rotateX", "rotateY", "rotateZ"]:
        cmds.setAttr(f"FKShoulder_R.{axis}", 30)
        new_pos = cmds.xform("FKWrist_R", q=True, ws=True, t=True)
        cmds.setAttr(f"FKShoulder_R.{axis}", 0)
        dZ = round(new_pos[2] - orig_pos_r[2], 2)
        print(f"FKShoulder_R.{axis}=30 -> Wrist dZ: {dZ}")
        
    # 测试脚部着地（Heel strike）
    # 当 IKLeg_L.roll = -20 时
    cmds.setAttr("IKLeg_L.roll", -20)
    toe_y_neg = cmds.xform("IKToes_L", q=True, ws=True, t=True)[1]
    cmds.setAttr("IKLeg_L.roll", 0)
    print("roll=-20 -> Toe Y:", round(toe_y_neg, 2))
    
    # 当 IKLeg_L.rotateX = -20 时
    cmds.setAttr("IKLeg_L.rotateX", -20)
    toe_y_rotx = cmds.xform("IKToes_L", q=True, ws=True, t=True)[1]
    cmds.setAttr("IKLeg_L.rotateX", 0)
    print("rotateX=-20 -> Toe Y:", round(toe_y_rotx, 2))

test_right_and_feet()
