# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

cmds.lookThru("persp")
cmds.setAttr("persp.translateX", 160)
cmds.setAttr("persp.translateY", 130)
cmds.setAttr("persp.translateZ", 480)
cmds.setAttr("persp.rotateX", -6)
cmds.setAttr("persp.rotateY", 20)
cmds.setAttr("persp.rotateZ", 0)

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\aesthetic"
frames = [
    (1, "contact_01"),
    (4, "down_01"),
    (7, "passing_01"),
    (10, "up_01"),
    (13, "contact_02"),
    (19, "passing_02")
]

for f, name in frames:
    cmds.currentTime(f)
    out_file = os.path.join(out_dir, f"full_{f:02d}_{name}.jpg")
    cmds.playblast(frame=[f], format="image", compression="jpg", completeFilename=out_file, showOrnaments=False, viewer=False, widthHeight=[960, 540], percent=100, forceOverwrite=True)

print("Captured full body frames.")
