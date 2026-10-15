import sys
import pypdf

sys.stdout.reconfigure(encoding="utf-8")

pdf_path = r"E:\知识库\百度网盘下载\散本教程\Physics for animators (Bousquet, Michele).pdf"
reader = pypdf.PdfReader(pdf_path)

toc_text = ""
for i in range(7, 14):
    toc_text += f"\n--- Page {i+1} ---\n" + (reader.pages[i].extract_text() or "")

print(toc_text[:4000])
