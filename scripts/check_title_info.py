import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

with open(r"c:\Users\zwj87\Documents\Book_Skill\books\physics-for-animators\source_text\physics_for_animators_text.txt", encoding="utf-8") as f:
    text = f.read()

m = re.search(r"=== PAGE 1 ===(.*?)=== PAGE 5 ===", text, re.DOTALL)
if m:
    print(m.group(1)[:1000])
