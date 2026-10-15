import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

ppt_dir = r"E:\知识库\百度网盘下载\运动规律PPT版"

def extract_strings_from_ppt(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # PPT OLE files store text in UTF-16LE or ASCII/GBK
    # Let's extract UTF-16LE text strings
    pattern_utf16 = re.compile(b'(?:[\x20-\x7e\x00-\xff]\x00){4,}')
    # Let's search for runs of utf-16le characters
    found = []
    # Simple regex for utf-16-le sequences:
    # Match 4 or more UTF-16LE characters that are either ASCII or CJK
    # CJK in utf-16le is generally 0x4e00 to 0x9fa5 -> low byte, high byte (0x4e..0x9f)
    # We can scan through chunks
    i = 0
    n = len(data)
    curr = bytearray()
    text_blocks = []
    while i < n - 1:
        b0 = data[i]
        b1 = data[i+1]
        # Check if valid ascii or common chinese character in utf-16le
        # ASCII: b0 in 0x20..0x7e and b1 == 0x00, or \r, \n, \t
        # CJK: b1 in 0x4e..0x9f
        is_ascii = (0x20 <= b0 <= 0x7e or b0 in (10, 13, 9)) and b1 == 0
        is_cjk = (0x4e <= b1 <= 0x9f)
        if is_ascii or is_cjk:
            curr.append(b0)
            curr.append(b1)
            i += 2
        else:
            if len(curr) >= 8: # at least 4 characters
                try:
                    s = curr.decode('utf-16le')
                    s_clean = s.strip()
                    if len(s_clean) >= 2 and any('\u4e00' <= c <= '\u9fff' for c in s_clean):
                        text_blocks.append(s_clean)
                except:
                    pass
            curr.clear()
            i += 1
    return text_blocks

for f in os.listdir(ppt_dir):
    if f.endswith('.ppt'):
        path = os.path.join(ppt_dir, f)
        blocks = extract_strings_from_ppt(path)
        print(f"=== {f} (Found {len(blocks)} Chinese text blocks) ===")
        # print first 5 unique blocks
        seen = set()
        count = 0
        for b in blocks:
            if b not in seen and len(b) > 3:
                seen.add(b)
                print("  *", b[:80])
                count += 1
                if count >= 6:
                    break
