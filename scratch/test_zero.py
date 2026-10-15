# -*- coding: utf-8 -*-
import maya.cmds as cmds

for ctrl in ["RootX_M", "IKLeg_L", "IKLeg_R"]:
    cmds.cutKey(ctrl, clear=True)
    cmds.setAttr(f"{ctrl}.translate", 0, 0, 0)
    cmds.setAttr(f"{ctrl}.rotate", 0, 0, 0)

print("IKLeg_L ws:", cmds.xform("IKLeg_L", q=True, ws=True, t=True))
print("Ankle_L ws:", cmds.xform("Ankle_L", q=True, ws=True, t=True))
print("RootX_M ws:", cmds.xform("RootX_M", q=True, ws=True, t=True))
