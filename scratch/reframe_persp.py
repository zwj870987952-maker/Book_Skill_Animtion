# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

# 将 persp 相机调到经典的 3/4 全身构图
cmds.lookThru("persp")
cmds.viewFit("persp", all=True)
# 稍微拉开一点距离，调至 3/4 俯平视视角
cmds.setAttr("persp.translateX", 140)
cmds.setAttr("persp.translateY", 150)
cmds.setAttr("persp.translateZ", 260)
cmds.setAttr("persp.rotateX", -12)
cmds.setAttr("persp.rotateY", 28)
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
    out_file = os.path.join(out_dir, f"persp_{f:02d}_{name}.jpg")
    cmds.playblast(frame=[f], format="image", compression="jpg", completeFilename=out_file, showOrnaments=False, viewer=False, widthHeight=[960, 540], percent=100, forceOverwrite=True)

print("Captured proper persp frames.")
