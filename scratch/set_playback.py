# -*- coding: utf-8 -*-
import maya.cmds as cmds

# 设置实时 24fps 播放，循环播放
cmds.playbackOptions(playbackSpeed=1.0, loop="continuous", min=1, max=24)
cmds.currentTime(1)
print("Playback speed:", cmds.playbackOptions(q=True, playbackSpeed=True))
print("Loop mode:", cmds.playbackOptions(q=True, loop=True))
print("Current frame:", cmds.currentTime(q=True))
print("Min/Max:", cmds.playbackOptions(q=True, min=True), cmds.playbackOptions(q=True, max=True))
