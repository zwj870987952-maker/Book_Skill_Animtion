from pathlib import Path

txt_path = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\master-shots\source_text\master_shots_text.txt")
text = txt_path.read_text(encoding="utf-8")

pages = text.split("--- PAGE ")
for p in pages[1:10]:
    p_num = p.split(" ---")[0]
    p_content = p.split(" ---", 1)[1].strip()
    safe_lines = [l.strip() for l in p_content.splitlines() if l.strip()][:5]
    print(f"=== Page {p_num} ===")
    for l in safe_lines:
        print("  ", l.encode('ascii', errors='backslashreplace').decode('ascii'))
