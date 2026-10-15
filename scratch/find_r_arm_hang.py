# -*- coding: utf-8 -*-
import maya.cmds as cmds

for ax in ['X', 'Y', 'Z']:
    for val in [-30, 30]:
        cmds.setAttr("FKShoulder_R.rotate", 0, 0, 0)
        cmds.setAttr(f"FKShoulder_R.rotate{ax}", val)
        pos = cmds.xform("FKWrist_R", q=True, ws=True, t=True)
        print(f"Right Rotate {ax}={val:3d} -> Wrist X={pos[0]:6.2f}, Y={pos[1]:6.2f}, Z={pos[2]:6.2f}")

cmds.setAttr("FKShoulder_R.rotate", 0, 0, 0)
