import pypdf

reader = pypdf.PdfReader(r"E:\知识库\百度网盘下载\散本教程\超人气动画角色设计攻略羽山淳一的现场绘画解说课_14376168.pdf")
print("Total pages:", len(reader.pages))

def print_outline(outline, depth=0):
    for item in outline:
        if isinstance(item, list):
            print_outline(item, depth + 1)
        elif hasattr(item, 'title'):
            print("  " * depth + f"- {item.title}")

if reader.outline:
    print_outline(reader.outline)
