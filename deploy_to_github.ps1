# Automated GitHub Deployment Script for UX Audit Studio
$ErrorActionPreference = "Stop"

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   🚀 DỰNG & ĐẨY LÊN GITHUB ĐỂ CHẠY CLOUD 24/7 VĨNH VIỄN   " -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Cyan

Set-Location $PSScriptRoot

# Kiểm tra trạng thái Git
git status

# Kiểm tra xem đã kết nối với GitHub chưa
$remotes = git remote
if (-not ($remotes -contains "origin")) {
    Write-Host ""
    Write-Host "Chưa có liên kết với GitHub repository!" -ForegroundColor Yellow
    Write-Host "1. Vào https://github.com/new và tạo repo mới (đặt tên: ux-audit-studio, Public, KHÔNG cần tích README)" -ForegroundColor White
    Write-Host "2. Copy link HTTPS của repo (ví dụ: https://github.com/tmtien2911/ux-audit-studio.git)" -ForegroundColor White
    $repoUrl = Read-Host "Nhập đường dẫn GitHub Repository URL của bạn"
    if ($repoUrl) {
        git remote add origin $repoUrl.Trim()
        Write-Host "Đã liên kết với: $repoUrl" -ForegroundColor Green
    } else {
        Write-Host "Chưa nhập URL, hủy bỏ." -ForegroundColor Red
        exit 1
    }
}

# Thêm và commit thay đổi
git add .
$commitMsg = Read-Host "Nhập thông điệp cập nhật (Enter để lấy mặc định: Update UX Audit Studio)"
if (-not $commitMsg) {
    $commitMsg = "Update UX Audit Studio"
}
try {
    git commit -m "$commitMsg"
} catch {
    Write-Host "Không có thay đổi mới cần commit." -ForegroundColor Gray
}

# Đẩy code lên nhánh main
Write-Host ""
Write-Host "Đang đẩy code lên GitHub..." -ForegroundColor Cyan
git branch -M main
git push -u origin main

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "✅ ĐÃ ĐẨY CODE LÊN GITHUB THÀNH CÔNG!" -ForegroundColor Green
Write-Host "👉 Bây giờ hãy mở https://share.streamlit.io để kích hoạt Cloud 24/7:" -ForegroundColor Yellow
Write-Host "   1. Đăng nhập bằng GitHub" -ForegroundColor White
Write-Host "   2. Chọn repo: ux-audit-studio -> Main file path: app.py" -ForegroundColor White
Write-Host "   3. Thêm Secrets (GEMINI_API_KEY) trong Advanced Settings" -ForegroundColor White
Write-Host "   4. Bấm Deploy! Web sẽ chạy vĩnh viễn 24/7!" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan
