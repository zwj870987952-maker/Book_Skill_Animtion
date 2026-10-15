from pathlib import Path

content = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\stop-staring\source_text\stop_staring_text.txt").read_text(encoding="utf-8")

# Let's inspect pages 9 to 15
import re
pages = re.findall(r"--- \[PAGE (\d+)/\d+\] ---\s*(.*?)(?=--- \[PAGE|\Z)", content, re.DOTALL)
for p_num, p_txt in pages[8:16]:
    print(f"=== PAGE {p_num} ===")
    print(p_txt.strip()[:1000])
    print()
