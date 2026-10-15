# -*- coding: utf-8 -*-
import maya.cmds as cmds

def check_local_rot():
    nodes = ["RootX_M", "FKChest_M", "FKSpine1_M", "FKNeck_M", "FKHead_M", "FKScapula_L", "FKScapula_R", "HipSwinger_M"]
    for n in nodes:
        if cmds.objExists(n):
            rot = cmds.getAttr(f"{n}.rotate")[0]
            print(f"{n} Local Rotate: {rot}")

check_local_rot()
