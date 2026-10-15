from pathlib import Path
import re

content = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-animal-drawing\source_text\force_animal_text.txt").read_text(encoding="utf-8")

pages = re.findall(r"--- \[PAGE (\d+)/\d+\] ---\s*(.*?)(?=--- \[PAGE|\Z)", content, re.DOTALL)
out_lines = []
for p_num, p_txt in pages[14:26]:
    out_lines.append(f"=== PAGE {p_num} ===")
    lines = [line.strip() for line in p_txt.splitlines() if line.strip()]
    out_lines.extend(lines[:25])
    out_lines.append("")

Path("books/force-animal-drawing/toc_dump2.txt").write_text("\n".join(out_lines), encoding="utf-8")
print("Dumped pages 15-26")
