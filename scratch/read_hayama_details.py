import pypdf

reader = pypdf.PdfReader(r"E:\知识库\百度网盘下载\散本教程\超人气动画角色设计攻略羽山淳一的现场绘画解说课_14376168.pdf")
# Read TOC pages around 4-10
for p in range(3, 12):
    t = reader.pages[p].extract_text()
    if t:
        print(f"=== Page {p+1} ===")
        print(t)
