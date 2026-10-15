# -*- coding: utf-8 -*-
import maya.cmds as cmds

def check_axes():
    # 查找 Toes 坐标
    for node in ["FKToes_L", "IKToes_L", "Ankle_L"]:
        if cmds.objExists(node):
            pos = cmds.xform(node, q=True, ws=True, t=True)
            print(f"{node} Pos:", pos)
            
    # 检查手臂向前摆动的旋转轴向
    # 测试在 FKShoulder_L 上绕 X, Y, Z 分别旋转 30 度时手腕的世界 Z 坐标怎么变
    orig_wrist_z = cmds.xform("FKWrist_L", q=True, ws=True, t=True)[2]
    print("Original Wrist Z:", orig_wrist_z)
    
    # 检查根骨骼的局部坐标轴朝向
    print("RootX_M Rotate Axis:", cmds.getAttr("RootX_M.rotateAxis")[0])

check_axes()
