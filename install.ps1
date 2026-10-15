# Book_Skill_Animtion 快速安装脚本 (PowerShell)
param(
    [switch]$All,
    [string]$Target,
    [switch]$Link,
    [switch]$List
)

$PythonCmd = if (Get-Command python -ErrorAction SilentlyContinue) { "python" } elseif (Get-Command py -ErrorAction SilentlyContinue) { "py" } else { $null }

if (-not $PythonCmd) {
    Write-Host "[!] 未检测到 Python，请先安装 Python 3.8+ 后再运行本安装器。" -ForegroundColor Red
    exit 1
}

$ArgsList = @()
if ($List) { $ArgsList += "--list" }
if ($All) { $ArgsList += "--all" }
if ($Link) { $ArgsList += "--link" }
if ($Target) { $ArgsList += "--target"; $ArgsList += $Target }

& $PythonCmd "$PSScriptRoot\install.py" @ArgsList
