from pathlib import Path

text_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\anatomy-for-sculptors\source_text\anatomy_text.txt")
content = text_path.read_text(encoding="utf-8")

pages = content.split("--- PAGE ")
out_file = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\anatomy-for-sculptors\toc_dump.txt")

lines = []
for idx in range(1, min(20, len(pages))):
    p = pages[idx]
    if any(k in p.upper() for k in ["CONTENTS", "CHAPTER", "HEAD", "TORSO", "ARM", "LEG"]):
        lines.append(f"=== PAGE CANDIDATE {idx} ===\n{p}\n\n")

out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Dumped TOC candidates to {out_file}")
