# -*- coding: utf-8 -*-
import maya.cmds as cmds

def inspect_ik_chain():
    for s in ["L", "R"]:
        ik_ctrl = f"IKLeg_{s}"
        ws = cmds.xform(ik_ctrl, q=True, ws=True, t=True)
        parents = cmds.listRelatives(ik_ctrl, parent=True)
        print(f"{ik_ctrl}: ws={ws}, parent={parents}")
        
        # 查找 IK handle
        handles = cmds.ls(f"*{s}*", type="ikHandle")
        print(f"  ikHandles: {handles}")
        for h in handles:
            print(f"    {h} driven by: {cmds.listConnections(h, d=False, s=True)}")
            print(f"    {h} ws pos: {cmds.xform(h, q=True, ws=True, t=True)}")

inspect_ik_chain()
