import sys
from pathlib import Path
import pypdf

root = Path(r"E:\知识库\百度网盘下载")
target = None
for pdf in root.rglob("*.pdf"):
    if "Force_ Dynamic Life Drawing" in pdf.name or "Dynamic Life Drawing for Animators" in pdf.name:
        target = pdf
        break

if not target:
    print("Error: Target Force pdf not found.")
    sys.exit(1)

print("Found target:", str(target))
reader = pypdf.PdfReader(str(target))
print("Total pages:", len(reader.pages))

# Sample first 15 pages for TOC
for i in range(min(15, len(reader.pages))):
    txt = reader.pages[i].extract_text() or ""
    if "Contents" in txt or "Table of Contents" in txt or "Force" in txt:
        print(f"=== PAGE {i+1} ===")
        print(txt.strip()[:600])
        print()
