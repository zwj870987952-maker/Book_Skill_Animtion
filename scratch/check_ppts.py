import os
import sys

ppt_dir = r"E:\知识库\百度网盘下载\运动规律PPT版"
for f in os.listdir(ppt_dir):
    full = os.path.join(ppt_dir, f)
    print(f, os.path.getsize(full))
