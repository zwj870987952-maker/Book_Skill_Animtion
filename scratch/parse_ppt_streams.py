import os
import sys
import struct

sys.stdout.reconfigure(encoding='utf-8')

# PPT Binary File Format Text Atom Record Types
# 0x0FA0: TextBytesAtom (1 byte per char)
# 0x0FA8: TextCharsAtom (2 bytes per char, utf-16le)
# 0x0F9F: CString (utf-16le)

def parse_ppt_atoms(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()

    texts = []
    i = 0
    n = len(data)
    while i <= n - 8:
        # read record header: ver_inst (2 bytes), rec_type (2 bytes), rec_len (4 bytes)
        ver_inst, rec_type, rec_len = struct.unpack('<HHI', data[i:i+8])
        if rec_len > 0 and i + 8 + rec_len <= n:
            rec_data = data[i+8:i+8+rec_len]
            if rec_type == 0x0FA8: # TextCharsAtom
                try:
                    s = rec_data.decode('utf-16le', errors='ignore').strip()
                    if len(s) > 1:
                        texts.append(s)
                except:
                    pass
            elif rec_type == 0x0FA0: # TextBytesAtom
                try:
                    # In Chinese PPTs, TextBytesAtom can be GBK
                    s = rec_data.decode('gbk', errors='ignore').strip()
                    if len(s) > 1:
                        texts.append(s)
                except:
                    pass
            elif rec_type == 0x0F9F: # CString
                try:
                    s = rec_data.decode('utf-16le', errors='ignore').strip()
                    if len(s) > 1:
                        texts.append(s)
                except:
                    pass
            # Move to next record or advance 2 bytes if scanning
            # Since atoms can be nested in containers, we advance by 1 or check valid types
        i += 1
    return texts

ppt_dir = r"E:\知识库\百度网盘下载\运动规律PPT版"
for f in os.listdir(ppt_dir):
    if f.endswith('.ppt'):
        path = os.path.join(ppt_dir, f)
        res = parse_ppt_atoms(path)
        # Deduplicate sequential identical strings
        dedup = []
        for t in res:
            t_clean = " ".join(t.split())
            if len(t_clean) >= 2 and (not dedup or dedup[-1] != t_clean):
                dedup.append(t_clean)
        print(f"=== {f}: Found {len(dedup)} text atoms ===")
        # Print first 10
        for sample in dedup[:12]:
            print("  -", sample[:90])
