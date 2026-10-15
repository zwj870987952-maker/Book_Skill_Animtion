# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

cmds.lookThru("side")
cmds.viewFit("side", all=True)

# 确保 side 面板也隐藏控制器曲线
panel = cmds.getPanel(withFocus=True)
if not panel or "modelPanel" not in panel:
    for p in cmds.getPanel(type="modelPanel"):
        panel = p
        break
if panel:
    cmds.modelEditor(panel, edit=True, nurbsCurves=False, joints=False, locators=False, ikHandles=False, deformers=False, wireframeOnShaded=False, displayAppearance="smoothShaded")

out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews\aesthetic_clean"
for f, name in [(1, "contact_01"), (7, "passing_01"), (10, "up_01")]:
    cmds.currentTime(f)
    out_file = os.path.join(out_dir, f"side_clean_{f:02d}_{name}.jpg")
    cmds.playblast(frame=[f], format="image", compression="jpg", completeFilename=out_file, showOrnaments=False, viewer=False, widthHeight=[960, 540], percent=100, forceOverwrite=True)

print("Saved clean side frames.")
