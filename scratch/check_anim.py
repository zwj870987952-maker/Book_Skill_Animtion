# -*- coding: utf-8 -*-
import maya.cmds as cmds

def check_existing_animation():
    ctrls = ["RootX_M", "IKLeg_L", "IKLeg_R", "FKShoulder_L", "FKShoulder_R", "FKChest_M"]
    has_anim = False
    for c in ctrls:
        keys = cmds.keyframe(c, q=True, keyframeCount=True) or 0
        if keys > 0:
            print(f"{c} has {keys} keys!")
            has_anim = True
    if not has_anim:
        print("No animation on core controls. Clean scene!")
        
check_existing_animation()
