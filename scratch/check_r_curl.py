# -*- coding: utf-8 -*-
import maya.cmds as cmds

# 测量指尖到手腕距离
wrist_pos = cmds.xform("FKWrist_R", q=True, ws=True, t=True)

# 0度
cmds.setAttr("FKMiddleFinger1_R.rotateZ", 0)
cmds.setAttr("FKMiddleFinger2_R.rotateZ", 0)
d0 = cmds.xform("MiddleFinger3_R", q=True, ws=True, t=True)
dist0 = sum((d0[i]-wrist_pos[i])**2 for i in range(3))**0.5

# -30度
cmds.setAttr("FKMiddleFinger1_R.rotateZ", -30)
cmds.setAttr("FKMiddleFinger2_R.rotateZ", -30)
d_neg = cmds.xform("MiddleFinger3_R", q=True, ws=True, t=True)
dist_neg = sum((d_neg[i]-wrist_pos[i])**2 for i in range(3))**0.5

# +30度
cmds.setAttr("FKMiddleFinger1_R.rotateZ", 30)
cmds.setAttr("FKMiddleFinger2_R.rotateZ", 30)
d_pos = cmds.xform("MiddleFinger3_R", q=True, ws=True, t=True)
dist_pos = sum((d_pos[i]-wrist_pos[i])**2 for i in range(3))**0.5

cmds.setAttr("FKMiddleFinger1_R.rotateZ", 0)
cmds.setAttr("FKMiddleFinger2_R.rotateZ", 0)

print(f"Distances to wrist: 0 deg = {dist0:.2f}, -30 deg = {dist_neg:.2f}, +30 deg = {dist_pos:.2f}")
if dist_neg < dist0:
    print("Negative Z curls finger on Right Hand!")
elif dist_pos < dist0:
    print("Positive Z curls finger on Right Hand!")
