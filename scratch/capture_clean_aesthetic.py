# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

# 获取当前模型面板
panel = cmds.getPanel(withFocus=True)
if not panel or "modelPanel" not in panel:
    for p in cmds.getPanel(type="modelPanel"):
        panel = p
        break

if panel:
    # 隐藏曲线、骨骼、定位器，只显示多边形网格
    cmds.modelEditor(panel, edit=True, nurbsCurves=False, joints=False, locators=False, ikHandles=False, deformers=False, wireframeOnShaded=False, displayAppearance="smoothShaded")

# 聚焦整个人物网格
meshes = cmds.ls(type="mesh")
transforms = list(set(cmds.listRelatives(meshes, parent=True) or []))
cmds.select(transforms)
cmds.viewFit("persp")
cmds.select(clear=True)

# 适度拉开一点透视
cmds.dolly("persp", relative=True, distance=-150)
cmds.track("persp", up=20)

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\aesthetic_clean"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

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
    out_file = os.path.join(out_dir, f"clean_{f:02d}_{name}.jpg")
    cmds.playblast(frame=[f], format="image", compression="jpg", completeFilename=out_file, showOrnaments=False, viewer=False, widthHeight=[960, 540], percent=100, forceOverwrite=True)

print("Captured clean aesthetic previews without rig clutter.")
