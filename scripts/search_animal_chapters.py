from pathlib import Path
import re

content = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\force-animal-drawing\source_text\force_animal_text.txt").read_text(encoding="utf-8")

# Let's search for "Chapter" across the entire text
matches = re.findall(r"(Chapter\s+\d+[:\s\-\–—][^\n]+)", content, re.IGNORECASE)
print("Unique Chapter matches:", len(matches))
found = []
for m in matches:
    clean = m.strip()
    if clean not in found:
        found.append(clean)
for f in found:
    print("-", f)

# Also check for Part or major headings
print("\nMajor Headings:")
headings = re.findall(r"\n\n([A-Z][A-Z\s,]{4,40})\n\n", content)
for h in set(headings[:30]):
    if any(w in h for w in ["PLANTIGRADE", "DIGITIGRADE", "UNGULIGRADE", "ANIMAL", "LOCOMOTION", "FORCE"]):
        print("-", h.strip())
