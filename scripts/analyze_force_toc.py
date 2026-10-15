from pathlib import Path
import re

text_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-life-drawing\source_text\force_text.txt")
content = text_path.read_text(encoding="utf-8")

print(f"Total length: {len(content)}")

# Look for table of contents
toc_match = re.search(r"(Table of Contents|Contents)\s*\n(.*?)(?=Introduction|Chapter 1)", content, re.DOTALL | re.IGNORECASE)
if toc_match:
    print("--- TOC FOUND ---")
    print(toc_match.group(0)[:2500])
else:
    # Look for pages 5 to 12
    pages = re.findall(r"--- \[PAGE (\d+)/\d+\] ---\s*(.*?)(?=--- \[PAGE|\Z)", content, re.DOTALL)
    for p_num, p_txt in pages[4:12]:
        if "Chapter" in p_txt or "Contents" in p_txt:
            print(f"=== PAGE {p_num} ===")
            print(p_txt.strip()[:1000])
