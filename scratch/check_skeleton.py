# -*- coding: utf-8 -*-
import maya.cmds as cmds

def check_skeleton():
    # 查找主骨骼 Hip 或 Root
    joints = ["Root_M", "Hip_M", "Spine1_M", "Chest_M", "Head_M", "Ankle_L", "Ankle_R"]
    for j in joints:
        if cmds.objExists(j):
            print(f"{j} ws pos: {cmds.xform(j, q=True, ws=True, t=True)}")
            
    # 查找所有以 Main 或 Master 开头的控制器
    main_ctrls = cmds.ls("*Main*", "*Master*", "*Global*", type="transform")
    print(f"Main controllers: {main_ctrls}")
    for mc in main_ctrls:
        print(f"  {mc}: ws={cmds.xform(mc, q=True, ws=True, t=True)}, scale={cmds.getAttr(mc + '.scale')}")

check_skeleton()
