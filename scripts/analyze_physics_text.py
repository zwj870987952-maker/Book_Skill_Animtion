import re

with open(r"c:\Users\zwj87\Documents\Book_Skill\books\physics-for-animators\source_text\physics_for_animators_text.txt", encoding="utf-8") as f:
    text = f.read()

# Let's find Section headings and Chapter headings
sections = re.findall(r"(SECTION\s+[123]\s*\n[^\n]+)", text)
print("Sections found:", sections)

chapters = re.findall(r"(\n\s*(?:CHAPTER\s+\d+|\d+)\s+[A-Z][A-Za-z\s]{3,40}\s*\n)", text)
print(f"Chapters found: {len(chapters)}")
for c in chapters[:15]:
    print(" - ", c.strip())
