from pathlib import Path
import re

content = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-life-drawing\source_text\force_text.txt").read_text(encoding="utf-8")

matches = re.findall(r"(Chapter \d+[:\s\-\–—][^\n]+)", content, re.IGNORECASE)
found = []
for m in matches:
    clean = m.strip()
    if clean not in found:
        found.append(clean)

for f in found:
    print("-", f)

# Also check for main headings in first 30 pages
pages = re.findall(r"--- \[PAGE (\d+)/\d+\] ---\s*(.*?)(?=--- \[PAGE|\Z)", content, re.DOTALL)
for p_num, p_txt in pages[14:26]:
    for line in p_txt.splitlines()[:5]:
        if any(w in line for w in ["Chapter", "CHAPTER", "Force", "Space", "Shape", "Form"]):
            print(f"P.{p_num}: {line.strip()}")
