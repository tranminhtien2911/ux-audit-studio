@echo off
chcp 65001 >nul
title "Đẩy UX Audit Studio lên GitHub và Cloud 24/7"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0deploy_to_github.ps1"
pause
