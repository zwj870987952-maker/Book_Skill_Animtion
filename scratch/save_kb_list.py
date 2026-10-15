# -*- coding: utf-8 -*-
import os

path = r"E:\知识库\百度网盘下载"
all_files = []
for root, dirs, files in os.walk(path):
    for f in files:
        all_files.append(os.path.join(root, f))

with open("scratch/kb_files_utf8.txt", "w", encoding="utf-8") as out:
    for i, f in enumerate(sorted(all_files), 1):
        rel = os.path.relpath(f, path)
        out.write(f"{i:02d}: {rel}\n")

print("Saved to scratch/kb_files_utf8.txt")
