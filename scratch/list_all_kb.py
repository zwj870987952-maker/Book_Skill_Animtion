# -*- coding: utf-8 -*-
import os

path = r"E:\知识库\百度网盘下载"
if os.path.exists(path):
    files = sorted(os.listdir(path))
    print(f"Total files: {len(files)}")
    for i, f in enumerate(files, 1):
        print(f"{i:02d}: {f}")
else:
    print("Path does not exist!")
