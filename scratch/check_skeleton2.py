# -*- coding: utf-8 -*-
import maya.cmds as cmds

joints = ["Root_M", "Hip_M", "Spine1_M", "Chest_M", "Head_M", "Ankle_L", "Ankle_R"]
for j in joints:
    if cmds.objExists(j):
        print(f"{j} ws pos: {cmds.xform(j, q=True, ws=True, t=True)}")

for c in ["Main", "Root_M", "RootX_M", "Hip_M"]:
    if cmds.objExists(c):
        print(f"{c}: t={cmds.getAttr(c+'.translate')}, r={cmds.getAttr(c+'.rotate')}")
