import pypdf

pdf_path = r"E:\知识库\百度网盘下载\动画专业力荐书单\书\开拍之前：故事板的艺术（美）约翰·哈特.pdf"
reader = pypdf.PdfReader(pdf_path)
print("Total pages:", len(reader.pages))

# Inspect outline
if reader.outline:
    print("Outline count:", len(reader.outline))
    for item in reader.outline[:25]:
        if hasattr(item, 'title'):
            print(" -", item.title)
        elif isinstance(item, list) and len(item) > 0 and hasattr(item[0], 'title'):
            print("   *", item[0].title)

# Sample some early pages
for i in range(5, 18):
    t = reader.pages[i].extract_text()
    if t and len(t.strip()) > 50:
        print(f"=== Page {i+1} ===")
        print(t[:500])
