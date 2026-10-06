@echo off
title UX Audit Studio
cd /d "%~dp0\.."
echo Dang khoi dong UX Audit Studio tren trinh duyet...
".venv\Scripts\streamlit.exe" run "ux_audit_studio\app.py"
pause
