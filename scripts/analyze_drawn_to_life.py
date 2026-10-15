from pathlib import Path

vol1_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\drawn-to-life\source_text\vol1_text.txt")
vol2_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\drawn-to-life\source_text\vol2_text.txt")

out_file = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\drawn-to-life\toc_dump.txt")

vol1_pages = vol1_path.read_text(encoding="utf-8").split("--- VOL1 PAGE ")
vol2_pages = vol2_path.read_text(encoding="utf-8").split("--- VOL2 PAGE ")

lines = ["=== VOLUME 1 CONTENTS CANDIDATES ==="]
for idx in range(1, min(25, len(vol1_pages))):
    p = vol1_pages[idx]
    if "CONTENTS" in p.upper() or "LECTURE" in p.upper() or "FOREWORD" in p.upper():
        lines.append(f"--- VOL 1 PAGE {idx} ---\n{p}\n")

lines.append("\n=== VOLUME 2 CONTENTS CANDIDATES ===")
for idx in range(1, min(25, len(vol2_pages))):
    p = vol2_pages[idx]
    if "CONTENTS" in p.upper() or "LECTURE" in p.upper() or "FOREWORD" in p.upper():
        lines.append(f"--- VOL 2 PAGE {idx} ---\n{p}\n")

out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Dumped Drawn to Life TOC candidates to {out_file}")
