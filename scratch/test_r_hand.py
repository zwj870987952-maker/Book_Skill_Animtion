# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\hands"
cmds.viewFit("persp", "FKWrist_R")

for f in ["Index", "Middle", "Ring", "Pinky"]:
    for i in [1, 2, 3]:
        ctrl = f"FK{f}Finger{i}_R"
        if cmds.objExists(ctrl):
            cmds.setAttr(f"{ctrl}.rotateZ", -20)
cmds.playblast(frame=[1], format="image", compression="jpg", completeFilename=os.path.join(out_dir, "hand_r_neg20.jpg"), showOrnaments=False, viewer=False, widthHeight=[640, 640], percent=100, forceOverwrite=True)

for f in ["Index", "Middle", "Ring", "Pinky"]:
    for i in [1, 2, 3]:
        ctrl = f"FK{f}Finger{i}_R"
        if cmds.objExists(ctrl):
            cmds.setAttr(f"{ctrl}.rotateZ", 20)
cmds.playblast(frame=[1], format="image", compression="jpg", completeFilename=os.path.join(out_dir, "hand_r_pos20.jpg"), showOrnaments=False, viewer=False, widthHeight=[640, 640], percent=100, forceOverwrite=True)

for f in ["Index", "Middle", "Ring", "Pinky"]:
    for i in [1, 2, 3]:
        ctrl = f"FK{f}Finger{i}_R"
        if cmds.objExists(ctrl):
            cmds.setAttr(f"{ctrl}.rotateZ", 0)
