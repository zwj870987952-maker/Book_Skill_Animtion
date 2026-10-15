import os
import pypdf

books = [
    (r"E:\知识库\百度网盘下载\散本教程\面部表情艺用解剖中文版V1.2.pdf", "facial-expressions"),
    (r"E:\知识库\百度网盘下载\动画专业力荐书单\书\开拍之前：故事板的艺术（美）约翰·哈特.pdf", "storyboard-art"),
    (r"E:\知识库\百度网盘下载\散本教程\超人气动画角色设计攻略羽山淳一的现场绘画解说课_14376168.pdf", "hayama-character-design"),
]

for path, tag in books:
    print(f"=== {tag} ===")
    if not os.path.exists(path):
        print("Path does not exist:", path)
        continue
    try:
        reader = pypdf.PdfReader(path)
        print(f"Total pages: {len(reader.pages)}")
        outline = reader.outline
        print(f"Outline items: {len(outline) if outline else 0}")
        sample = ""
        for i in range(min(10, len(reader.pages))):
            t = reader.pages[i].extract_text() or ""
            if t.strip():
                sample += f"[P{i+1}] {t[:200]}...\n"
        print("Sample extracted text:")
        print(sample[:800])
    except Exception as e:
        print("Error reading PDF:", e)
