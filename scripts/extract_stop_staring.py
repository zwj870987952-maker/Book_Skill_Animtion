import sys
from pathlib import Path
import pypdf

root = Path(r"E:\知识库\百度网盘下载")
target = None
for pdf in root.rglob("*.pdf"):
    if "Stop.Staring" in pdf.name or "Stop Staring" in pdf.name:
        target = pdf
        break

if not target:
    print("Error: Target Stop Staring pdf not found.")
    sys.exit(1)

out_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\stop-staring\source_text")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "stop_staring_text.txt"

print(f"Reading {target} ({target.stat().st_size / 1024 / 1024:.2f} MB)...")
reader = pypdf.PdfReader(str(target))
num_pages = len(reader.pages)
print(f"Total pages: {num_pages}")

extracted_text = []
for idx, page in enumerate(reader.pages):
    txt = page.extract_text() or ""
    header = f"\n\n--- [PAGE {idx+1}/{num_pages}] ---\n\n"
    extracted_text.append(header + txt)

full_content = "".join(extracted_text)
out_file.write_text(full_content, encoding="utf-8")
print(f"Successfully extracted {len(full_content)} characters across {num_pages} pages to {out_file}")
