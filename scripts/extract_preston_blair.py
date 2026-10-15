import sys
from pathlib import Path
import pypdf

sys.stdout.reconfigure(encoding="utf-8")

pdf_path = Path(r"E:\知识库\百度网盘下载\散本教程\Cartoon Animation by Preston Blair.pdf")
out_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\cartoon-animation\source_text")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "cartoon_animation_text.txt"

print(f"Reading {pdf_path}...")
reader = pypdf.PdfReader(str(pdf_path))
total = len(reader.pages)
print(f"Total pages: {total}")

lines = []
for i, page in enumerate(reader.pages):
    txt = page.extract_text() or ""
    lines.append(f"=== PAGE {i+1} ===\n{txt.strip()}\n")

content = "\n".join(lines)
out_file.write_text(content, encoding="utf-8")
print(f"Done! Written {len(content)} characters to {out_file}")
