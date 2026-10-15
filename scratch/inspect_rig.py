# -*- coding: utf-8 -*-
import maya.cmds as cmds
import json

def find_rig_details():
    results = {}
    
    # 查找所有以 Group 或 UnrealRoot 下的控制器曲线 (nurbsCurve)
    curves = cmds.ls(type="nurbsCurve")
    ctrl_transforms = list(set([cmds.listRelatives(c, parent=True, fullPath=False)[0] for c in curves if cmds.listRelatives(c, parent=True)]))
    
    results["total_nurbs_controllers"] = len(ctrl_transforms)
    
    # 关键字匹配
    categories = {
        "root_cog_pelvis": [],
        "feet_ik": [],
        "legs_fk": [],
        "knees_pv": [],
        "spine_chest": [],
        "neck_head": [],
        "arms_ik": [],
        "arms_fk": [],
        "elbows_pv": [],
        "shoulders_clavicle": [],
        "ik_fk_switches": []
    }
    
    keywords = {
        "root_cog_pelvis": ["root", "cog", "pelvis", "hip", "body", "center", "master"],
        "feet_ik": ["foot", "ankle", "leg_ik", "ik_leg", "heel", "toe"],
        "legs_fk": ["leg_fk", "fk_leg", "thigh_fk", "knee_fk"],
        "knees_pv": ["knee", "pv_leg", "leg_pv", "pole"],
        "spine_chest": ["spine", "chest", "torso", "waist", "mid"],
        "neck_head": ["neck", "head"],
        "arms_ik": ["arm_ik", "ik_arm", "hand_ik", "wrist_ik"],
        "arms_fk": ["arm_fk", "fk_arm", "shoulder_fk", "elbow_fk", "wrist_fk"],
        "elbows_pv": ["elbow", "pv_arm", "arm_pv"],
        "shoulders_clavicle": ["shoulder", "clavicle", "scapula"]
    }
    
    for ctrl in ctrl_transforms:
        ctrl_lower = ctrl.lower()
        for cat, kw_list in keywords.items():
            if any(k in ctrl_lower for k in kw_list):
                categories[cat].append(ctrl)
                
        # 查找有无特殊属性如 ik, fk, switch, mode
        user_attrs = cmds.listAttr(ctrl, userDefined=True) or []
        for attr in user_attrs:
            if any(k in attr.lower() for k in ["ik", "fk", "switch", "blend", "mode"]):
                categories["ik_fk_switches"].append(f"{ctrl}.{attr}")

    for k, v in categories.items():
        categories[k] = sorted(list(set(v)))

    print("=== RIG CATEGORIES ===")
    for k, v in categories.items():
        print(f"[{k}] ({len(v)}):", v[:15])

    # 打印一些重要控制器的层级和当前世界坐标
    sample_nodes = categories["root_cog_pelvis"] + categories["feet_ik"][:4] + categories["spine_chest"][:4]
    print("\n=== SAMPLE NODE POSITIONS & ROTATIONS ===")
    for node in sample_nodes[:10]:
        t = cmds.getAttr(f"{node}.translate")[0]
        r = cmds.getAttr(f"{node}.rotate")[0]
        print(f"{node} -> Trans: {t}, Rot: {r}")

find_rig_details()
