# -*- coding: utf-8 -*-
import maya.cmds as cmds

def inspect_details():
    # 帧率
    fps = cmds.currentUnit(q=True, time=True)
    print("Time Unit (FPS):", fps)
    
    # 左右脚 IK 属性与坐标
    for foot in ["IKLeg_L", "IKLeg_R"]:
        pos = cmds.xform(foot, q=True, ws=True, t=True)
        rot = cmds.xform(foot, q=True, ws=True, ro=True)
        user_attrs = cmds.listAttr(foot, userDefined=True, keyable=True) or []
        print(f"{foot} WS Pos: {pos}, WS Rot: {rot}")
        print(f"{foot} Keyable User Attrs: {user_attrs}")
        
    # 骨盆与脊柱
    for node in ["RootX_M", "HipSwinger_M", "FKChest_M", "FKHead_M"]:
        pos = cmds.xform(node, q=True, ws=True, t=True)
        rot = cmds.xform(node, q=True, ws=True, ro=True)
        print(f"{node} WS Pos: {pos}, WS Rot: {rot}")
        
    # 手臂
    for node in ["FKShoulder_L", "FKElbow_L", "FKWrist_L"]:
        rot = cmds.getAttr(f"{node}.rotate")[0]
        print(f"{node} Local Rot: {rot}")

inspect_details()
