# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews"
cmds.lookThru("persp")
out_file = os.path.join(out_dir, "zero_pose.jpg")
cmds.playblast(
    frame=[1],
    format="image",
    compression="jpg",
    completeFilename=out_file,
    showOrnaments=False,
    viewer=False,
    widthHeight=[960, 540],
    percent=100,
    forceOverwrite=True
)
print("Saved zero_pose.jpg")
