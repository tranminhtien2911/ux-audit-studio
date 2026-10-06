"""
Public Web Tunnel Runner for UX Audit Studio using Cloudflare Tunnel.
Launches Streamlit and provides a public HTTPS URL accessible from anywhere.
"""

import os
import sys
import time
import subprocess
import re
from pathlib import Path

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
STUDIO_DIR = Path(__file__).resolve().parent
CLOUDFLARED_BIN = STUDIO_DIR / "cloudflared.exe"
STREAMLIT_BIN = ROOT_DIR / ".venv" / "Scripts" / "streamlit.exe"

if not STREAMLIT_BIN.exists():
    STREAMLIT_BIN = Path(sys.executable).parent / "streamlit.exe"


def main():
    print("=" * 65)
    print("UX AUDIT STUDIO - KHOI TAO DUONG DAN PUBLIC WEB (HTTPS)")
    print("=" * 65)

    # 1. Start Streamlit
    print("[1/2] Dang khoi dong Streamlit backend...")
    st_cmd = [
        str(STREAMLIT_BIN),
        "run",
        str(STUDIO_DIR / "app.py"),
        "--server.port", "8501",
        "--server.headless", "true",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false",
    ]

    st_log_file = open(STUDIO_DIR / "streamlit.log", "w", encoding="utf-8")
    st_process = subprocess.Popen(
        st_cmd,
        stdout=st_log_file,
        stderr=subprocess.STDOUT,
        cwd=str(ROOT_DIR),
    )

    time.sleep(3)

    # 2. Start Cloudflared Tunnel
    print("[2/2] Dang tao duong ham bao mat Cloudflare Tunnel...")
    cf_cmd = [
        str(CLOUDFLARED_BIN),
        "tunnel",
        "--url", "http://localhost:8501",
        "--no-autoupdate",
    ]

    cf_process = subprocess.Popen(
        cf_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )

    public_url = None
    url_regex = re.compile(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com")

    # Read output until URL is found
    start_time = time.time()
    while time.time() - start_time < 30:
        line = cf_process.stdout.readline()
        if not line:
            time.sleep(0.1)
            continue
        match = url_regex.search(line)
        if match:
            public_url = match.group(0)
            break

    if public_url:
        print("\n" + "=" * 65)
        print("DA MO PUBLIC WEB THANH CONG!")
        print(f"DUONG DAN TRUY CAP (HTTPS):")
        print(f"👉 {public_url}")
        print("=" * 65 + "\n")
        print("Ban co the gui link nay cho bat ky ai, mo tren dien thoai hoac may tinh khac.")
        print("Nhan Ctrl + C de dung chia se public.")

        # Save to file
        (STUDIO_DIR / "public_url.txt").write_text(public_url, encoding="utf-8")

        try:
            cf_process.wait()
        except KeyboardInterrupt:
            print("\nDang dung tien trinh...")
        finally:
            cf_process.terminate()
            st_process.terminate()
    else:
        print("Khong the lay duong dan public tu Cloudflare Tunnel.")
        cf_process.terminate()
        st_process.terminate()


if __name__ == "__main__":
    main()
