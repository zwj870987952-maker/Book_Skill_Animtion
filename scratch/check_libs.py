import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
try:
    import pypdf
    print("pypdf available")
except ImportError:
    try:
        import PyPDF2 as pypdf
        print("PyPDF2 available")
    except ImportError:
        print("No pypdf")

# Also check olefile or similar for ppt text extraction
try:
    import olefile
    print("olefile available")
except ImportError:
    print("No olefile")
