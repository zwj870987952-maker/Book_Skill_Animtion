import os

base = r"E:\知识库\百度网盘下载"
print(f"Scanning: {base}")
total_files = 0
for root, dirs, files in os.walk(base):
    for f in files:
        full = os.path.join(root, f)
        rel = os.path.relpath(full, base)
        total_files += 1
        print(f"[{total_files}] {rel}")

print(f"Total files in knowledge base: {total_files}")
