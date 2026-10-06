param (
    [int]$Port = 8501
)

$RootDir = Split-Path -Parent $PSScriptRoot
Set-Location $RootDir

$StreamlitExe = Join-Path $RootDir ".venv\Scripts\streamlit.exe"

if (-not (Test-Path $StreamlitExe)) {
    Write-Host "Không tìm thấy môi trường ảo .venv. Đang chạy qua python -m streamlit..." -ForegroundColor Yellow
    python -m streamlit run (Join-Path $PSScriptRoot "app.py") --server.port $Port
} else {
    Write-Host "Đang khởi chạy UX Audit Studio trên cổng $Port..." -ForegroundColor Green
    & $StreamlitExe run (Join-Path $PSScriptRoot "app.py") --server.port $Port
}
