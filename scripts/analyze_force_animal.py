from pathlib import Path
import re

content = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-animal-drawing\source_text\force_animal_text.txt").read_text(encoding="utf-8")

print(f"Total length: {len(content)}")

# Look for table of contents
toc_match = re.search(r"(Table of Contents|Contents)\s*\n(.*?)(?=Introduction|Chapter 1)", content, re.DOTALL | re.IGNORECASE)
if toc_match:
    print("--- TOC FOUND ---")
    print(toc_match.group(0)[:2500])
else:
    # search pages 4 to 15
    pages = re.findall(r"--- \[PAGE (\d+)/\d+\] ---\s*(.*?)(?=--- \[PAGE|\Z)", content, re.DOTALL)
    for p_num, p_txt in pages[3:14]:
        for line in p_txt.splitlines()[:10]:
            if any(k in line.lower() for k in ["chapter", "contents", "section", "part"]):
                print(f"P.{p_num}: {line.strip()}")
