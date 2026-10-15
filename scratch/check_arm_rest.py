# -*- coding: utf-8 -*-
import maya.cmds as cmds

for side in ["L", "R"]:
    for part in ["Shoulder", "Elbow", "Wrist"]:
        node = f"FK{part}_{side}"
        if cmds.objExists(node):
            print(f"{node}: r={cmds.getAttr(node+'.rotate')}")
