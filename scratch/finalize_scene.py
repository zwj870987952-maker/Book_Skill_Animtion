# -*- coding: utf-8 -*-
import maya.cmds as cmds

for p in cmds.getPanel(type="modelPanel"):
    cmds.modelEditor(p, edit=True, nurbsCurves=True, polymeshes=True, displayAppearance="smoothShaded")

cmds.currentTime(1)
cmds.playbackOptions(min=1, max=24, playbackSpeed=1.0, loop="continuous")
print("Maya viewport and playback ready for user interaction.")
