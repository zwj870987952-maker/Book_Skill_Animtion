# -*- coding: utf-8 -*-
import maya.cmds as cmds

def inspect():
    scene_name = cmds.file(q=True, sn=True)
    print("=== SCENE INFO ===")
    print("Scene Name:", scene_name)
    
    start_frame = cmds.playbackOptions(q=True, min=True)
    end_frame = cmds.playbackOptions(q=True, max=True)
    current_time = cmds.currentTime(q=True)
    print(f"Time Range: {start_frame} - {end_frame}, Current Time: {current_time}")
    
    selected = cmds.ls(sl=True)
    print("Selected Nodes:", selected)
    
    references = cmds.file(q=True, r=True)
    print("References:", references)
    
    # 查找可能的控制器
    all_ctrls = cmds.ls("*ctrl*", "*CTRL*", "*Ctrl*", "*con*", "*CON*", "*Con*", type="transform")
    print(f"Total potential controller nodes found: {len(all_ctrls)}")
    if all_ctrls:
        print("Sample Controllers (first 30):", all_ctrls[:30])
    
    # 查找骨骼
    joints = cmds.ls(type="joint")
    print(f"Total joints found: {len(joints)}")
    if joints:
        print("Sample Joints (first 20):", joints[:20])
        
    # 查找主要顶级节点
    top_assemblies = cmds.ls(assemblies=True)
    print("Top Assemblies:", top_assemblies)

inspect()
