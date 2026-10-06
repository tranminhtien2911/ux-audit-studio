$RootDir = Split-Path -Parent $PSScriptRoot
Set-Location $RootDir
$PythonExe = Join-Path $RootDir ".venv\Scripts\python.exe"

Write-Host "Dang khoi tao public web bang Cloudflare Tunnel..." -ForegroundColor Cyan
& $PythonExe (Join-Path $PSScriptRoot "share_tunnel.py")
