import os

base = r"E:\知识库\百度网盘下载"
out_lines = []

for root, dirs, files in os.walk(base):
    for f in sorted(files):
        full = os.path.join(root, f)
        rel = os.path.relpath(full, base)
        size_mb = os.path.getsize(full) / (1024 * 1024)
        out_lines.append(f"{size_mb:6.1f} MB | {rel}")

with open(r"c:\Users\zwj87\Documents\Book_Skill\scratch\all_files_inventory.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print(f"Inventory saved. Total files: {len(out_lines)}")
for line in out_lines:
    print(line)
