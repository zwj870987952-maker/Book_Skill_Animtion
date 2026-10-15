import sys
import pypdf

# reconfigure stdout to utf-8
sys.stdout.reconfigure(encoding="utf-8")

books = {
    "preston_blair": r"E:\知识库\百度网盘下载\散本教程\Cartoon Animation by Preston Blair.pdf",
    "master_shots": r"E:\知识库\百度网盘下载\散本教程\微妙网-《大师镜头——低成本拍大片的100个高级技巧》.pdf",
    "survival_kit_cn": r"E:\知识库\百度网盘下载\动画专业力荐书单\2.原动画基础教程.pdf",
}

for name, path in books.items():
    print(f"=== {name} ===")
    try:
        reader = pypdf.PdfReader(path)
        print(f"Pages: {len(reader.pages)}")
        for i in range(min(5, len(reader.pages))):
            t = (reader.pages[i].extract_text() or "").strip()
            if t:
                print(f"Page {i+1}: {t[:250]}...\n")
    except Exception as e:
        print("Error:", e)
