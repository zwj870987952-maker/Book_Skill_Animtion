import fitz
import sys

pdf_path = r"E:\知识库\百度网盘下载\散本教程\Animators Survival Kit.pdf"
doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

sample_text_len = 0
for i in range(min(15, len(doc))):
    text = doc[i].get_text()
    sample_text_len += len(text)
    if len(text.strip()) > 0:
        print(f"Page {i}: {len(text)} chars | Sample: {text[:100].strip()!r}")

print(f"Total sample text length for first 15 pages: {sample_text_len}")
