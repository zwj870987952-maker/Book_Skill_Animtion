import pypdf

pdf_path = r"E:\知识库\百度网盘下载\散本教程\超人气动画角色设计攻略羽山淳一的现场绘画解说课_14376168.pdf"
reader = pypdf.PdfReader(pdf_path)
print("Total pages:", len(reader.pages))

if reader.outline:
    print("Outline count:", len(reader.outline))
    for item in reader.outline[:30]:
        if hasattr(item, 'title'):
            print(" -", item.title)
        elif isinstance(item, list) and len(item) > 0 and hasattr(item[0], 'title'):
            print("   *", item[0].title)

# Sample pages
for i in [3, 4, 5, 6, 7, 8, 9, 10]:
    t = reader.pages[i].extract_text()
    if t and len(t.strip()) > 20:
        print(f"=== Page {i+1} ===")
        print(t[:400])
