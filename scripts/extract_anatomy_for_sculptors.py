import pypdf
from pathlib import Path

pdf_path = Path(r"E:\知识库\百度网盘下载\散本教程\anatomy for sculptors.pdf")
out_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\anatomy-for-sculptors\source_text")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "anatomy_text.txt"

reader = pypdf.PdfReader(str(pdf_path))
num_pages = len(reader.pages)
print(f"Total pages: {num_pages}")

extracted_text = []
for idx, page in enumerate(reader.pages):
    txt = page.extract_text() or ""
    extracted_text.append(f"--- PAGE {idx+1} ---\n{txt}")

full_content = "\n".join(extracted_text)
out_file.write_text(full_content, encoding="utf-8")
print(f"Extracted {len(full_content)} characters to {out_file}")
