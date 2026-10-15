import pypdf
from pathlib import Path

books_dir = Path(r"E:\知识库\百度网盘下载\动画专业力荐书单\书")
for pdf in books_dir.glob("*.pdf"):
    try:
        r = pypdf.PdfReader(str(pdf))
        chars = 0
        readable_sample = ""
        for i in range(min(15, len(r.pages))):
            t = r.pages[i].extract_text() or ""
            chars += len(t.strip())
            if len(t.strip()) > 50 and not readable_sample:
                # 检查是否为有效汉字或英文
                sample = t.strip()[:100].replace("\n", " ")
                readable_sample = sample
        print(f"[{pdf.name}] Pages: {len(r.pages)} | Chars: {chars} | Sample: {repr(readable_sample[:60])}")
    except Exception as e:
        print(f"[{pdf.name}] Error: {e}")
