# -*- coding: utf-8 -*-
import subprocess
import json
import sys
import os

def call_maya_script(py_file_path):
    cmd = [
        "dcc-mcp-cli",
        "call",
        "maya.14542b6c.maya_scripting__execute_python",
        "--json",
        json.dumps({"file_path": py_file_path})
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("STDOUT:\n", res.stdout)
    if res.stderr:
        print("STDERR:\n", res.stderr)

if __name__ == "__main__":
    path = r"C:\Users\zwj87\Documents\Book_Skill\scratch\inspect_scene.py"
    if len(sys.argv) > 1:
        path = os.path.abspath(sys.argv[1])
    call_maya_script(path)
