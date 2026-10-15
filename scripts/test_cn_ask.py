import pypdf
from pathlib import Path

cn_pdf = Path(r"E:\知识库\百度网盘下载\动画专业力荐书单\2.动画师生存手册.pdf")
print("Reading Chinese PDF:", cn_pdf.name)
r = pypdf.PdfReader(str(cn_pdf))
print(f"Total pages: {len(r.pages)}")
non_empty = 0
total_chars = 0
for i in range(min(30, len(r.pages))):
    txt = r.pages[i].extract_text() or ""
    if len(txt.strip()) > 0:
        non_empty += 1
        total_chars += len(txt)
print(f"First 30 pages: non-empty pages = {non_empty}, total characters = {total_chars}")
