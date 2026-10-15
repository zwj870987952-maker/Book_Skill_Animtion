# -*- coding: utf-8 -*-
import maya.cmds as cmds

def scan_controllers():
    # 查找手指控制器
    fingers = cmds.ls("*Finger*", "*Thumb*", "*Index*", "*Middle*", "*Ring*", "*Pinky*", type="transform")
    print(f"Fingers found ({len(fingers)}): {fingers[:20]}")
    
    # 查找锁骨 / 肩胛骨
    clavicles = cmds.ls("*Clavicle*", "*Scapula*", "*Collar*", type="transform")
    print(f"Clavicles found: {clavicles}")
    
    # 查找脚部属性
    for foot in ["IKLeg_L", "IKLeg_R"]:
        if cmds.objExists(foot):
            attrs = cmds.listAttr(foot, keyable=True) or []
            print(f"{foot} keyable attrs: {attrs}")
            
    # 查找脊柱各节
    spines = cmds.ls("*Spine*", "*Chest*", type="transform")
    print(f"Spines/Chest found: {spines}")

scan_controllers()
