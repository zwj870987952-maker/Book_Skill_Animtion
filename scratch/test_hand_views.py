# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

# 聚焦左手
cmds.viewFit("persp", "FKWrist_L")
out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\hands"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# 试验不同的手指姿态
# 1. 默认
cmds.playblast(frame=[1], format="image", compression="jpg", completeFilename=os.path.join(out_dir, "hand_default.jpg"), showOrnaments=False, viewer=False, widthHeight=[640, 640], percent=100, forceOverwrite=True)

# 2. 绕 Z 轴弯曲
for f in ["Index", "Middle", "Ring", "Pinky"]:
    for i in [1, 2, 3]:
        ctrl = f"FK{f}Finger{i}_L"
        if cmds.objExists(ctrl):
            cmds.setAttr(f"{ctrl}.rotateZ", 20)
cmds.playblast(frame=[1], format="image", compression="jpg", completeFilename=os.path.join(out_dir, "hand_z_pos20.jpg"), showOrnaments=False, viewer=False, widthHeight=[640, 640], percent=100, forceOverwrite=True)

# 3. 绕 Z 轴负向弯曲
for f in ["Index", "Middle", "Ring", "Pinky"]:
    for i in [1, 2, 3]:
        ctrl = f"FK{f}Finger{i}_L"
        if cmds.objExists(ctrl):
            cmds.setAttr(f"{ctrl}.rotateZ", -20)
cmds.playblast(frame=[1], format="image", compression="jpg", completeFilename=os.path.join(out_dir, "hand_z_neg20.jpg"), showOrnaments=False, viewer=False, widthHeight=[640, 640], percent=100, forceOverwrite=True)

# 复原
for f in ["Index", "Middle", "Ring", "Pinky"]:
    for i in [1, 2, 3]:
        ctrl = f"FK{f}Finger{i}_L"
        if cmds.objExists(ctrl):
            cmds.setAttr(f"{ctrl}.rotateZ", 0)

print("Captured hand variations.")
