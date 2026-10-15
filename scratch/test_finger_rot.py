# -*- coding: utf-8 -*-
import maya.cmds as cmds

for ax in ['X', 'Y', 'Z']:
    cmds.setAttr("FKMiddleFinger1_L.rotate", 0, 0, 0)
    cmds.setAttr(f"FKMiddleFinger1_L.rotate{ax}", 30)
    print(f"Finger Middle 1 +30 on {ax}: OK")

cmds.setAttr("FKMiddleFinger1_L.rotate", 0, 0, 0)

# 检查手指关节的旋转限制或朝向
for f in ["FKIndexFinger1_L", "FKMiddleFinger1_L", "FKThumbFinger1_L"]:
    j = f.replace("FK", "")
    if cmds.objExists(j):
        print(f"Joint {j} orient:", cmds.getAttr(f"{j}.jointOrient"))
