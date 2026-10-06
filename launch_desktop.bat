@echo off
title UX Audit Studio Desktop Application
cd /d "%~dp0\.."

echo [1/2] Dang khoi dong backend UX Audit Studio...
start /b "" ".venv\Scripts\streamlit.exe" run "ux_audit_studio\app.py" --server.headless true --server.port 8501

echo [2/2] Dang mo cua so ung dung Windows Desktop...
timeout /t 3 /nobreak >nul
start "" "msedge.exe" --app="http://localhost:8501" --window-size=1360,900
