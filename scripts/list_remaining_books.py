from pathlib import Path
import pypdf

root = Path(r"E:\知识库\百度网盘下载")
already_done = [
    "timing-for-animation",
    "physics-for-animators",
    "cartoon-animation",
    "stop-staring",
    "force-life-drawing"
]

results = []
for pdf in root.rglob("*.pdf"):
    try:
        reader = pypdf.PdfReader(str(pdf))
        num_pages = len(reader.pages)
        has_text = False
        text_len = 0
        for p in reader.pages[:min(5, num_pages)]:
            text_len += len((p.extract_text() or "").strip())
        has_text = text_len > 100
        results.append((pdf, num_pages, has_text, pdf.stat().st_size))
    except Exception as e:
        results.append((pdf, -1, False, pdf.stat().st_size))

print(f"Total PDFs found: {len(results)}\n")
print(f"{'Index':<5} | {'Pages':<6} | {'Text':<5} | {'Size(MB)':<8} | {'Filename'}")
print("-" * 90)

for idx, (pdf, pages, has_text, size) in enumerate(sorted(results, key=lambda x: (not x[2], -x[1])), 1):
    size_mb = f"{size / 1024 / 1024:.1f}"
    print(f"{idx:<5} | {pages:<6} | {str(has_text):<5} | {size_mb:<8} | {pdf.name}")
