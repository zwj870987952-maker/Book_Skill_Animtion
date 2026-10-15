import sys
import pypdf

sys.stdout.reconfigure(encoding="utf-8")

pdf_path = r"E:\知识库\百度网盘下载\散本教程\Physics for animators (Bousquet, Michele).pdf"
reader = pypdf.PdfReader(pdf_path)

print(f"Total pages: {len(reader.pages)}")
# TOC is around pages 5 to 14
toc_text = ""
for i in range(4, 14):
    toc_text += reader.pages[i].extract_text() or ""

print("TOC:\n", toc_text[:3500])
