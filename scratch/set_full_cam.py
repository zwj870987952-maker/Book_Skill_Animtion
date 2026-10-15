# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

cmds.lookThru("persp")
cmds.setAttr("persp.translateX", 220)
cmds.setAttr("persp.translateY", 140)
cmds.setAttr("persp.translateZ", 600)
cmds.setAttr("persp.rotateX", -6)
cmds.setAttr("persp.rotateY", 20)
cmds.setAttr("persp.rotateZ", 0)

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\aesthetic_clean"

for f, name in [(1, "contact_01"), (7, "passing_01"), (10, "up_01"), (19, "passing_02")]:
    cmds.currentTime(f)
    out_file = os.path.join(out_dir, f"full_pose_{f:02d}_{name}.jpg")
    cmds.playblast(frame=[f], format="image", compression="jpg", completeFilename=out_file, showOrnaments=False, viewer=False, widthHeight=[960, 540], percent=100, forceOverwrite=True)

print("Saved full_pose frames.")
