import pypdf
import sys

pdf_path = r"E:\知识库\百度网盘下载\散本教程\Animators Survival Kit.pdf"
reader = pypdf.PdfReader(pdf_path)
print(f"Total pages: {len(reader.pages)}")

extracted = []
for i in range(min(15, len(reader.pages))):
    txt = reader.pages[i].extract_text() or ""
    if txt.strip():
        extracted.append(f"--- Page {i+1} ---\n{txt[:200]}")

print(f"Pages with text extracted (in first 15): {len(extracted)}")
if extracted:
    print("Sample extracted text:")
    for sample in extracted[:3]:
        print(sample)
