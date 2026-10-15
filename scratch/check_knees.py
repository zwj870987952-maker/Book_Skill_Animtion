# -*- coding: utf-8 -*-
import maya.cmds as cmds

def check_knees():
    for f in [1, 7, 13, 19]:
        cmds.currentTime(f)
        for side in ["L", "R"]:
            pv = f"PoleLeg_{side}"
            if cmds.objExists(pv):
                pos = cmds.xform(pv, query=True, translation=True, worldSpace=True)
                knee = f"Knee_{side}"
                knee_pos = cmds.xform(knee, query=True, translation=True, worldSpace=True) if cmds.objExists(knee) else None
                print(f"Frame {f} {side}: PV={pos}, Knee={knee_pos}")

check_knees()
