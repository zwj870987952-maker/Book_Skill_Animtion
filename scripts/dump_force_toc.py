from pathlib import Path
import re

content = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-life-drawing\source_text\force_text.txt").read_text(encoding="utf-8")

pages = re.findall(r"--- \[PAGE (\d+)/\d+\] ---\s*(.*?)(?=--- \[PAGE|\Z)", content, re.DOTALL)
out_lines = []
for p_num, p_txt in pages[4:14]:
    out_lines.append(f"=== PAGE {p_num} ===")
    lines = [line.strip() for line in p_txt.splitlines() if line.strip()]
    out_lines.extend(lines)
    out_lines.append("")

Path("books/force-life-drawing/toc_dump.txt").write_text("\n".join(out_lines), encoding="utf-8")
print("Dumped TOC to books/force-life-drawing/toc_dump.txt")
