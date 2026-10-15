import sys
from pathlib import Path
import pypdf

root = Path(r"E:\知识库\百度网盘下载")
target = None
for pdf in root.rglob("*.pdf"):
    if "Stop.Staring" in pdf.name or "Stop Staring" in pdf.name:
        target = pdf
        break

if not target:
    print("Not found")
    sys.exit(1)

print("Target path:", str(target))
reader = pypdf.PdfReader(str(target))
print("Total pages:", len(reader.pages))

# Print outlines / TOC if available
print("\n--- OUTLINES / TOC ---")
try:
    outline = reader.outline
    def print_outline(items, depth=0):
        for item in items:
            if isinstance(item, list):
                print_outline(item, depth+1)
            else:
                title = getattr(item, 'title', str(item))
                page = reader.get_destination_page_number(item) if hasattr(reader, 'get_destination_page_number') else '?'
                print("  " * depth + f"- {title} (p.{page})")
    print_outline(outline[:20])
except Exception as e:
    print("Could not get outline:", e)

# Sample text from first few pages
print("\n--- FIRST PAGES TEXT ---")
for i in range(min(15, len(reader.pages))):
    txt = reader.pages[i].extract_text() or ""
    if "Table of Contents" in txt or "Contents" in txt or "Jason Osipa" in txt:
        print(f"Page {i+1}:\n{txt[:400]}\n")
