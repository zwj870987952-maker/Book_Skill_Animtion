import os
import sys
import pypdf

sys.stdout.reconfigure(encoding='utf-8')

books = [
    r"E:\知识库\百度网盘下载\散本教程\图说动画规律-给角色赋予生命力(PDF格式).pdf",
    r"E:\知识库\百度网盘下载\散本教程\图说动画规律（日）尾泽直志.pdf",
    r"E:\知识库\百度网盘下载\散本教程\微妙网-[动画-角色的运动和动作].(美).克里斯.韦伯斯特.扫描版.pdf",
    r"E:\知识库\百度网盘下载\散本教程\psoe设计基础篇.pptx"
]

for b in books:
    if os.path.exists(b):
        try:
            if b.endswith('.pptx'):
                from pptx import Presentation
                prs = Presentation(b)
                texts = []
                for slide in prs.slides:
                    for shape in slide.shapes:
                        if shape.has_text_frame:
                            for paragraph in shape.text_frame.paragraphs:
                                texts.append(paragraph.text)
                print(f"{b}: PPTX slides={len(prs.slides)}, text_chars={sum(len(t) for t in texts)}")
                print("First 300 chars:", " ".join(texts)[:300])
            else:
                reader = pypdf.PdfReader(b)
                print(f"{b}: Pages={len(reader.pages)}")
                # check first 5 pages for text
                txt = ""
                for p in reader.pages[:10]:
                    t = p.extract_text() or ""
                    txt += t
                print(f"  Extracted text length from first 10 pages: {len(txt)}")
                if len(txt) > 50:
                    print(f"  Sample text: {txt[:200]}")
        except Exception as e:
            print(f"{b}: Error {e}")
    else:
        print(f"Not found: {b}")
