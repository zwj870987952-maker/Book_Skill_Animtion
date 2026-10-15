# -*- coding: utf-8 -*-
import maya.cmds as cmds

for node in ["FKShoulder_L", "FKElbow_L", "FKWrist_L"]:
    cmds.cutKey(node, clear=True)
    cmds.setAttr(f"{node}.rotate", 0, 0, 0)

print("FKShoulder_L ws:", cmds.xform("FKShoulder_L", q=True, ws=True, t=True))
