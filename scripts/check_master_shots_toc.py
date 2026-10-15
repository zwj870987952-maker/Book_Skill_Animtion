from pathlib import Path

txt_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\master-shots\source_text\master_shots_text.txt")
text = txt_path.read_text(encoding="utf-8")

lines = text.splitlines()
print(f"Total lines: {len(lines)}")
for i, line in enumerate(lines[:120]):
    if line.strip():
        print(f"L{i+1}: {line.strip()}")
