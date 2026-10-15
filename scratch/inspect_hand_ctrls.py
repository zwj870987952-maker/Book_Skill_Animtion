# -*- coding: utf-8 -*-
import maya.cmds as cmds

for node in ["FKWrist_L", "FKWrist_R"]:
    if cmds.objExists(node):
        print(f"{node} attrs:", cmds.listAttr(node, keyable=True))

# 检查手指控制器名称
sample_fingers = [
    "FKIndexFinger1_L", "FKIndexFinger2_L", "FKIndexFinger3_L",
    "FKMiddleFinger1_L", "FKMiddleFinger2_L", "FKMiddleFinger3_L",
    "FKRingFinger1_L", "FKRingFinger2_L", "FKRingFinger3_L",
    "FKPinkyFinger1_L", "FKPinkyFinger2_L", "FKPinkyFinger3_L",
    "FKThumbFinger1_L", "FKThumbFinger2_L", "FKThumbFinger3_L"
]
existing = [f for f in sample_fingers if cmds.objExists(f)]
print("Existing sample fingers:", existing)
