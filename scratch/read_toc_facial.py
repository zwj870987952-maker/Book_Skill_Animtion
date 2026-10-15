import pypdf

reader = pypdf.PdfReader(r"E:\知识库\百度网盘下载\散本教程\面部表情艺用解剖中文版V1.2.pdf")
print("Total pages:", len(reader.pages))

# Print pages 5 to 15 (table of contents and introduction)
for i in range(4, 15):
    t = reader.pages[i].extract_text()
    print(f"=== Page {i+1} ===")
    print(t)
