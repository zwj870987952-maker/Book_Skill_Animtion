import os
import pypdf
from rapidocr_onnxruntime import RapidOCR
import time

ocr = RapidOCR()
pdf_path = r"E:\知识库\百度网盘下载\动画专业力荐书单\8.动画的时间掌握.pdf"
out_dir = r"c:\Users\zwj87\Documents\Book_Skill\books\timing-for-animation\source_text"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "timing_for_animation_ocr.txt")

reader = pypdf.PdfReader(pdf_path)
total_pages = len(reader.pages)
print(f"Starting OCR on {total_pages} pages...")

start_time = time.time()
extracted_pages = []

with open(out_file, "w", encoding="utf-8") as f_out:
    for pno in range(total_pages):
        page = reader.pages[pno]
        page_lines = []
        
        # Check text layer first
        t = page.extract_text()
        if t and len(t.strip()) > 50:
            page_lines.append(t.strip())
        else:
            # Check images
            for img_obj in page.images:
                try:
                    img_bytes = img_obj.data
                    result, _ = ocr(img_bytes)
                    if result:
                        for item in result:
                            page_lines.append(item[1])
                except Exception as e:
                    page_lines.append(f"[OCR Error on page {pno+1}: {e}]")
                    
        page_text = "\n".join(page_lines)
        f_out.write(f"\n\n=== 第 {pno+1} 页 ===\n\n" + page_text)
        f_out.flush()
        
        if (pno + 1) % 10 == 0 or (pno + 1) == total_pages:
            elapsed = time.time() - start_time
            print(f"Progress: {pno+1}/{total_pages} pages processed ({elapsed:.1f}s)")

print(f"OCR finished completely! Saved to {out_file}")
