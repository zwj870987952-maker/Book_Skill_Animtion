import pypdf
from pathlib import Path

books = [
    ("Illusion of Life", r"E:\知识库\百度网盘下载\散本教程\The illusion of life Disney animation by Frank Thomas, Ollie Johnston.pdf"),
    ("Framed Ink", r"E:\知识库\百度网盘下载\散本教程\《Framed ink》汉化众译版.pdf"),
    ("Master Shots", r"E:\知识库\百度网盘下载\散本教程\微妙网-《大师镜头——低成本拍大片的100个高级技巧》.pdf"),
    ("Grammar of Film Language", r"E:\知识库\百度网盘下载\散本教程\电影语言的语法  插图修订版.pdf"),
    ("Grammar of the Shot", r"E:\知识库\百度网盘下载\散本教程\镜头的语法插图修订第2版.pdf"),
    ("Storyboard Design Course", r"E:\知识库\百度网盘下载\动画专业力荐书单\书\分镜头脚本设计教程.pdf"),
    ("Before You Begin Storyboard", r"E:\知识库\百度网盘下载\动画专业力荐书单\书\开拍之前：故事板的艺术（美）约翰·哈特.pdf"),
    ("Action Analysis", r"E:\知识库\百度网盘下载\散本教程\微妙网-[动画-角色的运动和动作].(美).克里斯.韦伯斯特.扫描版.pdf"),
    ("Hayama Junichi", r"E:\知识库\百度网盘下载\散本教程\超人气动画角色设计攻略羽山淳一的现场绘画解说课_14376168.pdf"),
    ("Facial Anatomy", r"E:\知识库\百度网盘下载\散本教程\面部表情艺用解剖中文版V1.2.pdf"),
]

for name, p_str in books:
    p = Path(p_str)
    if not p.exists():
        print(f"[{name}] File not found: {p}")
        continue
    try:
        r = pypdf.PdfReader(str(p))
        total_p = len(r.pages)
        chars = 0
        for i in range(min(20, total_p)):
            t = r.pages[i].extract_text() or ""
            chars += len(t)
        print(f"[{name}] Pages: {total_p} | Chars in first 20 pages: {chars}")
    except Exception as e:
        print(f"[{name}] Error: {e}")
