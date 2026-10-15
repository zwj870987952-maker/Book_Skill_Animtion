import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

ppt_dir = r"E:\知识库\百度网盘下载\运动规律PPT版"

def extract_gbk(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # In GBK, Chinese characters are two bytes: 0x81-0xFE, 0x40-0xFE (excluding 0x7F)
    # ASCII text is 0x20-0x7e
    gbk_pattern = re.compile(b'(?:[\x81-\xfe][\x40-\xfe]|[\x20-\x7e\r\n\t]){4,}')
    matches = gbk_pattern.findall(data)
    results = []
    for m in matches:
        try:
            s = m.decode('gbk').strip()
            # Must have at least some Chinese characters and meaningful length
            if len(s) > 3 and any('\u4e00' <= c <= '\u9fff' for c in s):
                results.append(s)
        except:
            pass
    return results

for f in os.listdir(ppt_dir):
    if f.endswith('.ppt'):
        path = os.path.join(ppt_dir, f)
        res = extract_gbk(path)
        print(f"=== {f} (Found {len(res)} GBK strings) ===")
        # show top 8 distinct strings
        seen = set()
        count = 0
        for s in res:
            if s not in seen and len(s) > 6:
                seen.add(s)
                print("  *", s[:100])
                count += 1
                if count >= 8:
                    break
