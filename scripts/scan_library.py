import os
from pathlib import Path
import pypdf

root = Path(r"E:\知识库\百度网盘下载")
results = []

for pdf in root.rglob("*.pdf"):
    rel = pdf.relative_to(root)
    try:
        reader = pypdf.PdfReader(str(pdf))
        num_pages = len(reader.pages)
        # check first 5 pages for text
        text_len = 0
        for p in reader.pages[:min(5, num_pages)]:
            text_len += len((p.extract_text() or "").strip())
        results.append((rel, num_pages, text_len > 100, pdf.stat().st_size))
    except Exception as e:
        results.append((rel, -1, False, pdf.stat().st_size))

print(f"{'Relative Path':<50} | {'Pages':<6} | {'TextLayer':<9} | {'Size(MB)':<8}")
print("-" * 80)
for rel, pages, has_text, size in sorted(results, key=lambda x: str(x[0])):
    size_mb = f"{size / (1024*1024):.1f}"
    print(f"{str(rel)[:50]:<50} | {pages:<6} | {str(has_text):<9} | {size_mb:<8}")
