import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open(r"c:\Users\zwj87\Documents\Book_Skill\books\cartoon-animation\source_text\cartoon_animation_text.txt", encoding="utf-8") as f:
    text = f.read()

# Let's see pages 1 to 15
for p in range(1, 15):
    m = re.search(rf"=== PAGE {p} ===(.*?)=== PAGE {p+1} ===", text, re.DOTALL)
    if m:
        t = m.group(1).strip()
        if t:
            print(f"--- PAGE {p} ---")
            print(t[:300])
