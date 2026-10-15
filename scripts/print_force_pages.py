from pathlib import Path
import re

content = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-life-drawing\source_text\force_text.txt").read_text(encoding="utf-8")

pages = re.findall(r"--- \[PAGE (\d+)/\d+\] ---\s*(.*?)(?=--- \[PAGE|\Z)", content, re.DOTALL)
for p_num, p_txt in pages[4:14]:
    print(f"=== PAGE {p_num} ===")
    lines = [line.strip() for line in p_txt.splitlines() if line.strip()]
    print("\n".join(lines[:20]))
    print()
