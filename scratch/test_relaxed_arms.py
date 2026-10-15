# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

# 将左右手臂稍向内收，使其贴近身体两侧，自然下垂
cmds.setAttr("FKShoulder_L.rotate", 0, 16, 0)
cmds.setAttr("FKShoulder_R.rotate", 0, 16, 0)
cmds.setAttr("FKElbow_L.rotate", 0, 0, 12)
cmds.setAttr("FKElbow_R.rotate", 0, 0, 12)

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews"
cmds.lookThru("persp")
out_file = os.path.join(out_dir, "arms_relaxed_pose.jpg")
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
print("Saved arms_relaxed_pose.jpg")
