@echo off
title UX Audit Studio - Public Web Tunnel
cd /d "%~dp0\.."
echo Dang khoi tao public web bang Cloudflare Tunnel...
".venv\Scripts\python.exe" "ux_audit_studio\share_tunnel.py"
pause
