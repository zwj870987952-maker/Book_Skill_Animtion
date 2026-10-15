# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

cmds.lookThru("persp")
# 向后拉远镜头
cmds.dolly("persp", relative=True, distance=-400)
cmds.track("persp", down=20)

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\aesthetic_clean"

for f, name in [(1, "contact_01"), (7, "passing_01"), (10, "up_01"), (19, "passing_02")]:
    cmds.currentTime(f)
    out_file = os.path.join(out_dir, f"full_clean_{f:02d}_{name}.jpg")
    cmds.playblast(frame=[f], format="image", compression="jpg", completeFilename=out_file, showOrnaments=False, viewer=False, widthHeight=[960, 540], percent=100, forceOverwrite=True)

print("Captured full clean frames.")
