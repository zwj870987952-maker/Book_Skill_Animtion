# -*- coding: utf-8 -*-
import os

path = r"E:\知识库\百度网盘下载"
if os.path.exists(path):
    files = sorted(os.listdir(path))
    for f in files:
        if any(k in f for k in ["漫画", "脚本"]):
            print(f)
else:
    print("Path does not exist!")
