# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

# 把 side 相机拉远看全景
cmds.lookThru("side")
cmds.setAttr("side.translateX", 400)
cmds.setAttr("side.translateY", 120)
cmds.setAttr("side.translateZ", 0)

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\aesthetic_clean"
for f, name in [(1, "contact_01"), (7, "passing_01")]:
    cmds.currentTime(f)
    out_file = os.path.join(out_dir, f"side_full_{f:02d}_{name}.jpg")
    cmds.playblast(frame=[f], format="image", compression="jpg", completeFilename=out_file, showOrnaments=False, viewer=False, widthHeight=[960, 540], percent=100, forceOverwrite=True)

# 切回透视
cmds.lookThru("persp")
print("Saved full side frames.")
