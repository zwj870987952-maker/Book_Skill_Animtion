# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

def capture_preview():
    out_dir = r"C:\Users\zwj87\Documents\Book_Skill\scratch\previews"
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        
    # 设置透视相机视角适中
    cmds.lookThru("persp")
    # 也可以检查相机参数
    # 抓取第 1, 4, 7, 10, 13 帧截图
    captured_files = []
    for f in [1, 4, 7, 10, 13]:
        cmds.currentTime(f)
        out_file = os.path.join(out_dir, f"walk_frame_{f}.jpg")
        res = cmds.playblast(
            frame=[f],
            format="image",
            compression="jpg",
            completeFilename=out_file,
            showOrnaments=False,
            viewer=False,
            widthHeight=[960, 540],
            percent=100,
            forceOverwrite=True
        )
        captured_files.append(res)
    print("CAPTURED:", captured_files)

capture_preview()
