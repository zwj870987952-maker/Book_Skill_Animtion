import pypdf
from pathlib import Path

pdf_path = Path(r"E:\知识库\百度网盘下载\散本教程\微妙网-《大师镜头——低成本拍大片的100个高级技巧》.pdf")
out_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\master-shots\source_text")
out_dir.mkdir(parents=True, exist_ok=True)

reader = pypdf.PdfReader(str(pdf_path))
print(f"Total pages: {len(reader.pages)}")

extracted = []
total_chars = 0
for idx, page in enumerate(reader.pages):
    txt = page.extract_text() or ""
    total_chars += len(txt)
    extracted.append(f"--- PAGE {idx+1} ---\n{txt}")

out_file = out_dir / "master_shots_text.txt"
content = "\n".join(extracted)
out_file.write_text(content, encoding="utf-8")
print(f"Extracted {len(content)} chars across {len(reader.pages)} pages to {out_file}")
print(f"Total text characters: {total_chars}")
