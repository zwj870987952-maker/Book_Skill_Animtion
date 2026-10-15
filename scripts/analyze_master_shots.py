from pathlib import Path
import re

txt_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\master-shots\source_text\master_shots_text.txt")
text = txt_path.read_text(encoding="utf-8")

# 寻找各章标题
chapters = re.findall(r"(?:第[一二三四五六七八九十\d]+章|Chapter\s*\d+)[^\n]*", text, re.IGNORECASE)
print(f"Found {len(chapters)} chapter headings:")
for c in set(chapters):
    print(" -", c)

# 寻找各小节/技巧
techniques = [line.strip() for line in text.splitlines() if re.match(r"^\d+\.\d+", line.strip())]
print(f"\nFound {len(techniques)} technique numbered items, sample:")
for t in techniques[:20]:
    print(" -", t)
