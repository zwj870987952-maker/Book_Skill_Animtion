# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\master"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# 适度调整透视相机以看清全身
cmds.lookThru("persp")
# 捕获 4 大黄金姿态
frames = [
    (1, "contact_01"),
    (4, "down_01"),
    (7, "passing_01"),
    (10, "up_01"),
    (13, "contact_02")
]

for f, name in frames:
    cmds.currentTime(f)
    out_file = os.path.join(out_dir, f"{f:02d}_{name}.jpg")
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
