import pypdf
from pathlib import Path

pdf1_path = Path(r"E:\知识库\百度网盘下载\散本教程\Drawn to Life 20 Golden Years of Disney Master Classes Volume 1 The Walt Stanchfield Lectures by Walt Stanchfield, Don Hahn.pdf")
pdf2_path = Path(r"E:\知识库\百度网盘下载\散本教程\Drawn to life 2 20 golden years of Disney master classes volume 2 the Walt Stanchfield lectures by Hahn, DonStanchfield, Walt.pdf")

out_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\drawn-to-life\source_text")
out_dir.mkdir(parents=True, exist_ok=True)

# Volume 1
reader1 = pypdf.PdfReader(str(pdf1_path))
print(f"Vol 1 pages: {len(reader1.pages)}")
extracted1 = []
for idx, page in enumerate(reader1.pages):
    txt = page.extract_text() or ""
    extracted1.append(f"--- VOL1 PAGE {idx+1} ---\n{txt}")

vol1_file = out_dir / "vol1_text.txt"
vol1_content = "\n".join(extracted1)
vol1_file.write_text(vol1_content, encoding="utf-8")
print(f"Extracted {len(vol1_content)} chars from Vol 1 to {vol1_file}")

# Volume 2
reader2 = pypdf.PdfReader(str(pdf2_path))
print(f"Vol 2 pages: {len(reader2.pages)}")
extracted2 = []
for idx, page in enumerate(reader2.pages):
    txt = page.extract_text() or ""
    extracted2.append(f"--- VOL2 PAGE {idx+1} ---\n{txt}")

vol2_file = out_dir / "vol2_text.txt"
vol2_content = "\n".join(extracted2)
vol2_file.write_text(vol2_content, encoding="utf-8")
print(f"Extracted {len(vol2_content)} chars from Vol 2 to {vol2_file}")
