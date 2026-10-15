# -*- coding: utf-8 -*-
import maya.cmds as cmds

def inspect_rest_pose():
    # 检查 FKIKLeg 是否真的是 IK 模式
    for s in ["L", "R"]:
        blend_node = f"FKIKLeg_{s}"
        if cmds.objExists(blend_node):
            attrs = cmds.listAttr(blend_node, keyable=True) or []
            print(f"{blend_node} attrs: {attrs}")
            for a in ["FKIKBlend", "fkik"]:
                if cmds.attributeQuery(a, node=blend_node, exists=True):
                    print(f"  {blend_node}.{a} = {cmds.getAttr(blend_node + '.' + a)}")
        
        ik_ctrl = f"IKLeg_{s}"
        if cmds.objExists(ik_ctrl):
            print(f"{ik_ctrl}:")
            print("  tx:", cmds.getAttr(f"{ik_ctrl}.translateX"))
            print("  ty:", cmds.getAttr(f"{ik_ctrl}.translateY"))
            print("  tz:", cmds.getAttr(f"{ik_ctrl}.translateZ"))
            
        ankle_joint = f"Ankle_{s}"
        if cmds.objExists(ankle_joint):
            pos = cmds.xform(ankle_joint, q=True, ws=True, t=True)
            print(f"  {ankle_joint} ws pos: {pos}")
            
        leg_joint = f"Leg_{s}"
        if cmds.objExists(leg_joint):
            pos = cmds.xform(leg_joint, q=True, ws=True, t=True)
            print(f"  {leg_joint} ws pos: {pos}")

inspect_rest_pose()
