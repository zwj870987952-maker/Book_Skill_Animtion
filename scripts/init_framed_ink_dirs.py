from pathlib import Path

base = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\framed-ink")
dirs = [
    base / "source_text",
    base / "candidates",
    base / ".cangjie" / "capabilities" / "cards",
    base / ".cangjie" / "capabilities" / "book",
    base / ".cangjie" / "evals"
]

for d in dirs:
    d.mkdir(parents=True, exist_ok=True)
    print(f"Created directory: {d}")
