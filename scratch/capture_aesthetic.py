# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\aesthetic"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# 1. Persp 3/4 视角
cmds.lookThru("persp")
for f in [1, 4, 7, 10, 13, 19]:
    cmds.currentTime(f)
    out_file = os.path.join(out_dir, f"persp_{f:02d}.jpg")
    cmds.playblast(frame=[f], format="image", compression="jpg", completeFilename=out_file, showOrnaments=False, viewer=False, widthHeight=[960, 540], percent=100, forceOverwrite=True)

# 2. Side 视角
cmds.lookThru("side")
cmds.viewFit("side", all=True)
for f in [1, 7, 13]:
    cmds.currentTime(f)
    out_file = os.path.join(out_dir, f"side_{f:02d}.jpg")
    cmds.playblast(frame=[f], format="image", compression="jpg", completeFilename=out_file, showOrnaments=False, viewer=False, widthHeight=[960, 540], percent=100, forceOverwrite=True)

cmds.lookThru("persp")
print("Captured aesthetic previews.")
