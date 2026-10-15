# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\side"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# 切换到 side 摄影机并适度 frame
cmds.lookThru("side")
cmds.viewFit("side", all=True)

frames = [
    (1, "contact_01"),
    (4, "down_01"),
    (7, "passing_01"),
    (10, "up_01"),
    (13, "contact_02")
]

for f, name in frames:
    cmds.currentTime(f)
    out_file = os.path.join(out_dir, f"side_{f:02d}_{name}.jpg")
    cmds.playblast(
        frame=[f],
        format="image",
        compression="jpg",
        completeFilename=out_file,
        showOrnaments=False,
        viewer=False,
        widthHeight=[960, 540],
        percent=100,
        forceOverwrite=True
    )
    print(f"Captured {out_file}")

# 切回 persp
cmds.lookThru("persp")
