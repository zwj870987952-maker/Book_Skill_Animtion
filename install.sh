#!/usr/bin/env bash
# Book_Skill_Animtion 快速安装脚本 (macOS / Linux)

if command -v python3 &>/dev/null; then
    PYTHON_CMD=python3
elif command -v python &>/dev/null; then
    PYTHON_CMD=python
else
    echo "[!] 未检测到 Python，请先安装 Python 3.8+ 后再运行。"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"$PYTHON_CMD" "$SCRIPT_DIR/install.py" "$@"
