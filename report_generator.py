"""
Report generator for UX Audit Studio.
Generates printable Executive HTML/PDF reports and Jira/Linear CSV task exports.
"""

import html
import json
import csv
import io
from datetime import datetime
from typing import Dict, Any, List


def generate_executive_html_report(
    result: Dict[str, Any],
    project_name: str = "Dự án Chưa đặt tên",
    persona: str = "Người dùng phổ thông",
    platform: str = "Đa nền tảng (Web/Mobile)",
    audit_mode: str = "Toàn diện (Norman + Krug + Nielsen + WCAG)",
) -> str:
    """
    Generate a standalone, beautifully styled, printable Executive UX Audit Report.
    Includes print CSS so users can directly press Ctrl+P to save as PDF.
    """
    data = result.get("structured_data", {})
    overall_score = data.get("ux_health_score", 0)
    verdict = data.get("verdict", "Chưa xác định")
    scores = data.get("scores", {})
    issues = data.get("issues", [])
    strengths = data.get("strengths", [])
    engine = result.get("engine", "UX Audit Engine")
    sources = result.get("knowledge_sources", [])
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Score color
    if overall_score >= 80:
        score_badge = "#10b981"
        score_bg = "#ecfdf5"
    elif overall_score >= 60:
        score_badge = "#f59e0b"
        score_bg = "#fffbeb"
    else:
        score_badge = "#ef4444"
        score_bg = "#fef2f2"

    # Count issues
    crit_count = sum(1 for i in issues if i.get("severity") == "Critical")
    maj_count = sum(1 for i in issues if i.get("severity") == "Major")
    min_count = sum(1 for i in issues if i.get("severity") == "Minor")

    # Build Issues HTML
    issues_html = ""
    for idx, issue in enumerate(issues, 1):
        sev = issue.get("severity", "Major")
        if sev == "Critical":
            border_c = "#ef4444"
            bg_c = "#fef2f2"
            badge_c = "#991b1b"
            badge_bg = "#fee2e2"
            icon = "🚨"
        elif sev == "Major":
            border_c = "#f97316"
            bg_c = "#fff7ed"
            badge_c = "#9a3412"
            badge_bg = "#ffedd5"
            icon = "⚠️"
        else:
            border_c = "#eab308"
            bg_c = "#fefce8"
            badge_c = "#854d0e"
            badge_bg = "#fef9c3"
            icon = "💡"

        issues_html += f"""
        <div class="issue-card" style="border-left: 5px solid {border_c}; background: {bg_c}; margin-bottom: 16px; padding: 16px 20px; border-radius: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div>
                    <span style="background: {badge_bg}; color: {badge_c}; font-weight: 700; font-size: 11px; padding: 3px 10px; border-radius: 12px; text-transform: uppercase;">
                        {icon} {sev}
                    </span>
                    <strong style="font-size: 15px; margin-left: 10px; color: #1e293b;">{html.escape(issue.get('element', 'Phần tử'))}</strong>
                    <span style="color: #64748b; font-size: 13px;"> ({html.escape(issue.get('screen', 'Màn hình'))})</span>
                </div>
            </div>
            <p style="margin: 6px 0; color: #334155; font-size: 14px;"><strong>Vấn đề:</strong> {html.escape(issue.get('issue', ''))}</p>
            <p style="margin: 6px 0; color: #475569; font-size: 13px;"><strong>Nguyên lý vi phạm:</strong> <em>{html.escape(issue.get('principle', ''))}</em></p>
            <div style="margin-top: 10px; padding: 10px 14px; background: rgba(255,255,255,0.7); border-radius: 6px; border: 1px dashed {border_c};">
                <strong style="color: #0f172a; font-size: 13px;">💡 Đề xuất giải pháp (Actionable Redesign):</strong>
                <p style="margin: 4px 0 0 0; color: #047857; font-size: 13.5px; font-weight: 500;">{html.escape(issue.get('recommendation', ''))}</p>
            </div>
        </div>
        """

    # Build Strengths HTML
    strengths_html = ""
    for s in strengths:
        strengths_html += f"<li style='margin-bottom: 6px; color: #065f46;'>✓ {html.escape(s)}</li>"

    # Build Sources List
    sources_text = ", ".join(sources) if sources else "Don Norman & Steve Krug Principles, Jakob Nielsen 10 Heuristics, W3C WCAG 2.2"

    html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Báo Cáo Kiểm Toán UX - {html.escape(project_name)}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #1e293b;
            background: #f8fafc;
            padding: 40px 20px;
            line-height: 1.6;
        }}
        .report-container {{
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
            padding: 48px;
            border: 1px solid #e2e8f0;
        }}
        .header {{
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 24px;
            margin-bottom: 32px;
        }}
        .header h1 {{
            font-size: 28px;
            font-weight: 800;
            color: #0f172a;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .meta-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-top: 16px;
            background: #f1f5f9;
            padding: 16px;
            border-radius: 10px;
            font-size: 13.5px;
        }}
        .meta-item strong {{
            color: #475569;
        }}
        .score-hero {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: {score_bg};
            border: 2px solid {score_badge};
            padding: 24px 32px;
            border-radius: 12px;
            margin-bottom: 32px;
        }}
        .score-val {{
            font-size: 54px;
            font-weight: 800;
            color: {score_badge};
            line-height: 1;
        }}
        .score-title {{
            font-size: 14px;
            text-transform: uppercase;
            font-weight: 700;
            color: #64748b;
            letter-spacing: 0.5px;
        }}
        .score-verdict {{
            font-size: 20px;
            font-weight: 700;
            color: #0f172a;
            margin-top: 4px;
        }}
        .pillars-grid {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 12px;
            margin-bottom: 32px;
        }}
        .pillar-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            padding: 14px 10px;
            border-radius: 10px;
            text-align: center;
        }}
        .pillar-score {{
            font-size: 22px;
            font-weight: 700;
            color: #4f46e5;
        }}
        .pillar-label {{
            font-size: 11px;
            color: #64748b;
            font-weight: 600;
            text-transform: uppercase;
            margin-top: 2px;
        }}
        .severity-bar {{
            display: flex;
            gap: 16px;
            margin-bottom: 24px;
            padding: 12px 18px;
            background: #f8fafc;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }}
        .section-title {{
            font-size: 20px;
            font-weight: 700;
            color: #0f172a;
            margin: 28px 0 16px 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .btn-print {{
            display: inline-block;
            background: #4f46e5;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            border: none;
            margin-bottom: 24px;
        }}
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            .report-container {{
                box-shadow: none;
                border: none;
                padding: 0;
                max-width: 100%;
            }}
            .btn-print {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="report-container">
        <button class="btn-print" onclick="window.print()">🖨️ In Báo Cáo / Lưu PDF (Ctrl + P)</button>
        
        <div class="header">
            <h1>🎨 BÁO CÁO KIỂM TOÁN TRẢI NGHIỆM NGƯỜI DÙNG (UX AUDIT)</h1>
            <p style="color: #64748b; margin-top: 4px;">Được thực hiện bởi UX Audit Studio • Chuẩn mực Quốc tế Don Norman, Steve Krug, NN/g & W3C WCAG</p>
            
            <div class="meta-grid">
                <div class="meta-item"><strong>Dự án:</strong> {html.escape(project_name)}</div>
                <div class="meta-item"><strong>Ngày đánh giá:</strong> {timestamp}</div>
                <div class="meta-item"><strong>Đối tượng người dùng:</strong> {html.escape(persona)}</div>
                <div class="meta-item"><strong>Nền tảng mục tiêu:</strong> {html.escape(platform)}</div>
                <div class="meta-item"><strong>Chế độ kiểm toán:</strong> {html.escape(audit_mode)}</div>
                <div class="meta-item"><strong>Động cơ phân tích:</strong> {html.escape(engine)}</div>
            </div>
        </div>

        <div class="score-hero">
            <div>
                <div class="score-title">Chỉ Số Sức Khỏe UX Tổng Thể (UX Health Score)</div>
                <div class="score-verdict">{html.escape(verdict)}</div>
                <div style="font-size: 13px; color: #475569; margin-top: 6px;">
                    Benchmark khuyến nghị: <strong>85 / 100 điểm</strong> cho ứng dụng chuyên nghiệp.
                </div>
            </div>
            <div class="score-val">{overall_score}<span style="font-size: 24px;">/100</span></div>
        </div>

        <h3 class="section-title">📊 1. Điểm Số Theo 5 Chiều Kích Khả Dụng</h3>
        <div class="pillars-grid">
            <div class="pillar-card">
                <div class="pillar-score">{scores.get('visibility', 0)}</div>
                <div class="pillar-label">Tính Trực Quan (Visibility)</div>
            </div>
            <div class="pillar-card">
                <div class="pillar-score">{scores.get('feedback', 0)}</div>
                <div class="pillar-label">Phản Hồi (Feedback)</div>
            </div>
            <div class="pillar-card">
                <div class="pillar-score">{scores.get('affordance', 0)}</div>
                <div class="pillar-label">Định Hướng (Affordance)</div>
            </div>
            <div class="pillar-card">
                <div class="pillar-score">{scores.get('navigation', 0)}</div>
                <div class="pillar-label">Điều Hướng (Navigation)</div>
            </div>
            <div class="pillar-card">
                <div class="pillar-score">{scores.get('cognitive_load', 0)}</div>
                <div class="pillar-label">Tinh Gọn Nhận Thức</div>
            </div>
        </div>

        <h3 class="section-title">🚨 2. Danh Sách Lỗi & Đề Xuất Cải Tiến Kỹ Thuật ({len(issues)} vấn đề)</h3>
        <div class="severity-bar">
            <div>🔴 <strong>Critical:</strong> {crit_count}</div>
            <div>🟠 <strong>Major:</strong> {maj_count}</div>
            <div>🟡 <strong>Minor:</strong> {min_count}</div>
        </div>

        {issues_html if issues_html else "<p style='color: #64748b;'>Không phát hiện vấn đề nghiêm trọng nào.</p>"}

        <h3 class="section-title">✨ 3. Điểm Sáng Đã Làm Tốt (Usability Strengths)</h3>
        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 18px 24px; border-radius: 10px;">
            <ul style="list-style-type: none; padding-left: 0;">
                {strengths_html if strengths_html else "<li>Giao diện sạch sẽ, phân cấp rõ ràng.</li>"}
            </ul>
        </div>

        <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #e2e8f0; font-size: 12px; color: #94a3b8; display: flex; justify-content: space-between;">
            <div>Hệ tri thức áp dụng: {html.escape(sources_text)}</div>
            <div>UX Audit Studio PRO</div>
        </div>
    </div>
</body>
</html>
    """
    return html_template


def generate_jira_csv(issues: List[Dict[str, Any]], project_key: str = "UX") -> str:
    """
    Generate CSV file format ready to import directly into Jira, GitHub Issues, Linear, or Trello.
    """
    output = io.StringIO()
    writer = csv.writer(output)

    # Jira standard import headers
    headers = [
        "Issue Type",
        "Summary",
        "Description",
        "Priority",
        "Component",
        "Environment",
        "Acceptance Criteria",
    ]
    writer.writerow(headers)

    for idx, item in enumerate(issues, 1):
        sev = item.get("severity", "Major")
        if sev == "Critical":
            priority = "Highest"
        elif sev == "Major":
            priority = "High"
        else:
            priority = "Medium"

        summary = f"[{item.get('screen', 'UI')}] {item.get('element', 'Element')}: {item.get('issue', '')[:80]}"
        desc = (
            f"Màn hình: {item.get('screen')}\n"
            f"Thành phần: {item.get('element')}\n"
            f"Vấn đề phát hiện: {item.get('issue')}\n"
            f"Nguyên lý vi phạm: {item.get('principle')}\n"
            f"Đề xuất chỉnh sửa: {item.get('recommendation')}"
        )
        acceptance = f"Khắc phục theo đề xuất: {item.get('recommendation')}"

        writer.writerow([
            "Bug",
            summary,
            desc,
            priority,
            "UI/UX Usability",
            item.get("screen", "Web/Mobile"),
            acceptance,
        ])

    return output.getvalue()
