# -*- coding: utf-8 -*-
import maya.cmds as cmds

tip_0 = cmds.xform("MiddleFinger3_L", q=True, ws=True, t=True)

for ax in ['X', 'Y', 'Z']:
    for f in ["FKMiddleFinger1_L", "FKMiddleFinger2_L", "FKMiddleFinger3_L"]:
        cmds.setAttr(f"{f}.rotate", 0, 0, 0)
        cmds.setAttr(f"{f}.rotate{ax}", 30)
    tip = cmds.xform("MiddleFinger3_L", q=True, ws=True, t=True)
    diff = [round(tip[i] - tip_0[i], 2) for i in range(3)]
    print(f"+30 on {ax}: diff={diff}")
    
for f in ["FKMiddleFinger1_L", "FKMiddleFinger2_L", "FKMiddleFinger3_L"]:
    cmds.setAttr(f"{f}.rotate", 0, 0, 0)
