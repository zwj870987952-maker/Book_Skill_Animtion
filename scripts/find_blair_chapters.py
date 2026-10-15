import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open(r"c:\Users\zwj87\Documents\Book_Skill\books\cartoon-animation\source_text\cartoon_animation_text.txt", encoding="utf-8") as f:
    text = f.read()

chapters = set(re.findall(r"(Chapter\s+\d+[^\n]*)", text))
for c in sorted(chapters):
    print(c)
