# -*- coding: utf-8 -*-
import maya.cmds as cmds

def verify():
    res = {}
    res["playback_min"] = cmds.playbackOptions(q=True, min=True)
    res["playback_max"] = cmds.playbackOptions(q=True, max=True)
    
    controllers = [
        "IKLeg_R", "IKLeg_L", "RootX_M", "FKChest_M", "FKShoulder_L", "FKShoulder_R"
    ]
    key_counts = {}
    for c in controllers:
        key_counts[c] = cmds.keyframe(c, query=True, keyframeCount=True)
    res["key_counts"] = key_counts
    
    # Check values at Frame 1, 4, 7, 10, 13
    frames_check = {}
    for f in [1, 4, 7, 10, 13, 16, 19, 22, 25]:
        cmds.currentTime(f)
        frames_check[f] = {
            "RootX_M_ty": round(cmds.getAttr("RootX_M.translateY"), 3),
            "RootX_M_tx": round(cmds.getAttr("RootX_M.translateX"), 3),
            "IKLeg_R_tz": round(cmds.getAttr("IKLeg_R.translateZ"), 3),
            "IKLeg_R_roll": round(cmds.getAttr("IKLeg_R.roll"), 3),
            "IKLeg_L_tz": round(cmds.getAttr("IKLeg_L.translateZ"), 3),
            "IKLeg_L_roll": round(cmds.getAttr("IKLeg_L.roll"), 3),
            "FKShoulder_L_rz": round(cmds.getAttr("FKShoulder_L.rotateZ"), 3),
            "FKShoulder_R_rz": round(cmds.getAttr("FKShoulder_R.rotateZ"), 3),
        }
    res["frames"] = frames_check
    
    print("VERIFICATION_RESULT:")
    import json
    print(json.dumps(res, indent=2))

verify()
