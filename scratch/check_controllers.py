# -*- coding: utf-8 -*-
import maya.cmds as cmds

def check_controllers_and_switches():
    print("=== IK FK BLEND ATTRIBUTES ===")
    for switch_node in ["FKIKLeg_L", "FKIKLeg_R", "FKIKArm_L", "FKIKArm_R", "FKIKSpine_M"]:
        if cmds.objExists(switch_node):
            blend_val = cmds.getAttr(f"{switch_node}.FKIKBlend")
            print(f"{switch_node}.FKIKBlend = {blend_val}")
            
    # 查找所有以 IK 开头或结尾的控制器
    curves = cmds.ls(type="nurbsCurve")
    ctrls = list(set([cmds.listRelatives(c, parent=True, fullPath=False)[0] for c in curves if cmds.listRelatives(c, parent=True)]))
    
    print("\n=== FOOT / LEG CONTROLLERS ===")
    for c in ctrls:
        if any(k in c.lower() for k in ["leg", "foot", "ankle", "toe", "heel"]):
            print("Leg/Foot:", c)
            
    print("\n=== ARM / HAND CONTROLLERS ===")
    for c in ctrls:
        if any(k in c.lower() for k in ["arm", "hand", "wrist", "elbow", "scapula", "shoulder"]):
            print("Arm/Hand:", c)
            
    print("\n=== ROOT / SPINE CONTROLLERS ===")
    for c in ctrls:
        if any(k in c.lower() for k in ["root", "spine", "chest", "hip", "pelvis"]):
            print("Root/Spine:", c)

check_controllers_and_switches()
