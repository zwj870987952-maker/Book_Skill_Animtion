import os
import sys

base = r'E:\知识库\百度网盘下载'
out_lines = []
for root, dirs, files in os.walk(base):
    for f in sorted(files):
        full = os.path.join(root, f)
        rel = os.path.relpath(full, base)
        size_mb = os.path.getsize(full) / (1024 * 1024)
        out_lines.append(f"{size_mb:6.1f} MB | {rel}")

with open("scratch/clean_inventory.txt", "w", encoding="utf-8") as fp:
    fp.write("\n".join(out_lines))
print(f"Total files: {len(out_lines)}")
