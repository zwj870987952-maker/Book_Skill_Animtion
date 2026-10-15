from pathlib import Path
import re

text_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\stop-staring\source_text\stop_staring_text.txt")
content = text_path.read_text(encoding="utf-8")

print(f"Total length: {len(content)}")

# Look for table of contents
toc_match = re.search(r"Contents\s*\n(.*?)(?=Introduction|Chapter 1)", content, re.DOTALL | re.IGNORECASE)
if toc_match:
    print("--- TOC FOUND ---")
    print(toc_match.group(0)[:2000])
else:
    # Look for chapter headers
    print("--- CHAPTER SEARCH ---")
    chapters = re.findall(r"(Chapter \d+\s*[–—\-]?\s*[^\n]+)", content, re.IGNORECASE)
    for c in set(chapters[:30]):
        print("-", c)
