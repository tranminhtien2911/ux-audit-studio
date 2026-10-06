"""
UX Audit Studio - Ứng dụng kiểm toán giao diện người dùng dựa trên tri thức từ NotebookLM
(Don Norman: The Design of Everyday Things & Steve Krug: Don't Make Me Think)
Nâng cấp: Scorecard Đa chiều, Biểu đồ Radar Chart & Phân cấp Độ nghiêm trọng của Lỗi.
"""

import os
import sys
from pathlib import Path
from PIL import Image
import streamlit as st
import plotly.graph_objects as go

# Add workspace directory to path
current_dir = Path(__file__).resolve().parent
workspace_dir = current_dir.parent
if str(workspace_dir) not in sys.path:
    sys.path.insert(0, str(workspace_dir))
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

try:
    from ux_audit_studio.notebook_bridge import fetch_notebooks, DEFAULT_NOTEBOOK_ID
    from ux_audit_studio.audit_engine import run_ux_audit
except (ImportError, ValueError):
    from notebook_bridge import fetch_notebooks, DEFAULT_NOTEBOOK_ID
    from audit_engine import run_ux_audit

# Page configuration
st.set_page_config(
    page_title="UX Audit Studio Pro",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling (CSS)
st.markdown(
    """
    <style>
    .main-header {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        padding: 24px 32px;
        border-radius: 16px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 14px rgba(79, 70, 229, 0.25);
    }
    .main-header h1 {
        color: white !important;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .main-header p {
        color: #e0e7ff !important;
        font-size: 1.05rem;
        margin: 0;
    }
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        margin: 4px 0;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #64748b;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    .issue-card {
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 12px;
        border-left: 6px solid #94a3b8;
        background: #f8fafc;
    }
    .issue-critical {
        border-left-color: #ef4444 !important;
        background: #fef2f2 !important;
    }
    .issue-major {
        border-left-color: #f97316 !important;
        background: #fff7ed !important;
    }
    .issue-minor {
        border-left-color: #eab308 !important;
        background: #fefce8 !important;
    }
    .badge-pill {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        margin-right: 8px;
    }
    .badge-crit { background: #fee2e2; color: #991b1b; }
    .badge-maj { background: #ffedd5; color: #9a3412; }
    .badge-min { background: #fef9c3; color: #854d0e; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
    <div class="main-header">
        <h1>🎨 UX Audit Studio <span style="font-size: 1.1rem; background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px;">PRO EDITION</span></h1>
        <p>Kiểm toán trải nghiệm người dùng đa chiều dựa trên tri thức từ NotebookLM: 
        <strong>Don Norman</strong> (<em>The Design of Everyday Things</em>) & 
        <strong>Steve Krug</strong> (<em>Don't Make Me Think</em>)</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Cấu hình Hệ thống")

    # Check NotebookLM Connection Status
    try:
        from ux_audit_studio.notebook_bridge import get_nlm_client
    except (ImportError, ValueError):
        from notebook_bridge import get_nlm_client

    nlm_client = get_nlm_client()
    if nlm_client:
        st.markdown(
            """
            <div style="margin-bottom: 16px;">
                <span style="background: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0; padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 0.85rem;">
                🟢 Gemini NotebookLM: Đã kết nối Live
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div style="margin-bottom: 16px;">
                <span style="background: #eff6ff; color: #1e40af; border: 1px solid #bfdbfe; padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 0.85rem;">
                🔵 Chế độ Norman/Krug Heuristic Engine
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.subheader("📚 Nguồn Tri thức (Knowledge Base)")
    notebook_id = st.text_input(
        "Notebook UUID",
        value=DEFAULT_NOTEBOOK_ID,
        help="Mã định danh của Notebook 'The Design of Everyday Creative Things'",
    )
    st.caption("Đang liên kết: **The Design of Everyday Creative Things** (Don Norman & Steve Krug)")

    st.divider()

    st.subheader("🤖 Phân tích Thị giác (Vision AI)")
    default_api_key = os.environ.get("GEMINI_API_KEY", "")
    if not default_api_key:
        try:
            if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
                default_api_key = st.secrets["GEMINI_API_KEY"]
        except Exception:
            pass

    api_key_input = st.text_input(
        "Google Gemini API Key",
        value=default_api_key,
        type="password",
        help="Nhập Gemini API Key hoặc cấu hình trong Secrets để bật tính năng phân tích đa phương thức (Multimodal Vision) trực tiếp trên ảnh.",
    )


    model_choice = st.selectbox(
        "Mô hình Gemini Vision",
        options=["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"],
        index=0,
    )

    st.divider()

    with st.expander("📖 5 Trụ cột Tiêu chuẩn Quốc tế"):
        st.markdown(
            """
            1. **Tính trực quan (Visibility - Norman & NN/g):** Xóa bỏ khoảng cách Thực thi & Đánh giá; phản hồi trạng thái hệ thống.
            2. **Phản hồi hệ thống (Feedback - Norman & Krug):** Tức thì, rõ ràng; phòng ngừa lỗi; điều hướng "You Are Here".
            3. **Định hướng tương tác (Affordance & Signifiers):** Tín hiệu hành động hiển nhiên (Self-evident); nhận biết thay vì nhớ lại.
            4. **Tiêu chuẩn Tiếp cận (W3C WCAG 2.2):** Tương phản màu >= 4.5:1; vùng chạm >= 24-44px; không dùng màu làm tín hiệu duy nhất.
            5. **Tâm lý học UX (Laws of UX & Krug):** Định luật Jakob, Fitts, Hick, Miller; *Đừng bắt tôi suy nghĩ!*
            """
        )

    with st.expander("📂 Nguồn Tài liệu Chuẩn (Knowledge Base)"):
        st.markdown(
            """
            Đã tích hợp 5 bộ tài liệu chuẩn sẵn trong thư mục `ux_audit_studio/knowledge_base/`:
            - `01_nielsen_10_usability_heuristics.md` (NN/g)
            - `02_wcag_2_2_accessibility_standards.md` (W3C)
            - `03_laws_of_ux_psychology.md` (Laws of UX)
            - `04_form_and_data_table_ux.md` (Form & Data Tables)
            - `05_mobile_touch_and_navigation_hig.md` (Apple HIG)
            """
        )


# Main Area: Input Section
col_left, col_right = st.columns([1, 1], gap="medium")

uploaded_images = []
uploaded_names = []

with col_left:
    st.subheader("1. Tải lên Ảnh Giao diện (UI Flow)")

    use_sample = st.checkbox("Sử dụng ảnh mẫu giao diện (Demo Screen)", value=False)
    sample_path = current_dir / "sample_ui.png"

    uploaded_files = st.file_uploader(
        "Chọn một hoặc nhiều ảnh màn hình:",
        type=["png", "jpg", "jpeg", "webp"],
        accept_multiple_files=True,
        help="Bạn có thể tải lên toàn bộ luồng tương tác (UI Flow) gồm nhiều bước liên tiếp.",
    )

    if use_sample and sample_path.exists():
        sample_img = Image.open(sample_path)
        uploaded_images.append(sample_img)
        uploaded_names.append("Màn hình Mẫu (Admin User Management)")
    elif uploaded_files:
        for f in uploaded_files:
            img = Image.open(f)
            uploaded_images.append(img)
            uploaded_names.append(f.name)

    user_context = st.text_area(
        "2. Mô tả Luồng tương tác & Đối tượng người dùng:",
        placeholder="Ví dụ: Trang quản trị danh sách người dùng cho Admin; mục tiêu là tra cứu nhanh và quản lý quyền người dùng...",
        value="Trang quản lý danh sách người dùng của hệ thống học tập trực tuyến (Click-Ed). Người dùng là Quản trị viên cần tra cứu, phân quyền và duyệt tài khoản.",
        height=100,
    )

    audit_clicked = st.button("🚀 Bắt đầu phân tích (Audit UI Flow)", type="primary", use_container_width=True)

with col_right:
    st.subheader("2. Xem trước Giao diện (Screenshots Preview)")
    if uploaded_images:
        tabs = st.tabs([f"Ảnh {i+1}: {uploaded_names[i][:20]}" for i in range(len(uploaded_images))])
        for idx, tab in enumerate(tabs):
            with tab:
                st.image(uploaded_images[idx], caption=uploaded_names[idx], use_container_width=True)
    else:
        st.info("Chưa có ảnh nào được tải lên. Hãy chọn ảnh ở cột bên trái hoặc tick vào ô 'Sử dụng ảnh mẫu'.")

# Output Section
st.divider()


def render_radar_chart(scores: dict):
    """Render interactive Plotly radar chart for 5 UX dimensions."""
    categories = [
        "Tính trực quan<br>(Visibility)",
        "Phản hồi<br>(Feedback)",
        "Định hướng<br>(Affordance)",
        "Điều hướng<br>(Navigation)",
        "Tinh gọn nhận thức<br>(Cognitive Load)",
    ]

    values = [
        scores.get("visibility", 65),
        scores.get("feedback", 55),
        scores.get("affordance", 70),
        scores.get("navigation", 60),
        scores.get("cognitive_load", 75),
    ]

    # Close polygon
    categories_plot = categories + [categories[0]]
    values_plot = values + [values[0]]
    benchmark_plot = [85, 85, 85, 85, 85, 85]

    fig = go.Figure()

    # Benchmark polygon
    fig.add_trace(go.Scatterpolar(
        r=benchmark_plot,
        theta=categories_plot,
        fill='toself',
        fillcolor='rgba(16, 185, 129, 0.1)',
        line=dict(color='rgba(16, 185, 129, 0.6)', dash='dash', width=2),
        name='Tiêu chuẩn khuyến nghị (85đ)'
    ))

    # Actual scores polygon
    fig.add_trace(go.Scatterpolar(
        r=values_plot,
        theta=categories_plot,
        fill='toself',
        fillcolor='rgba(79, 70, 229, 0.25)',
        line=dict(color='#4f46e5', width=3),
        name='Điểm thực tế của UI'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10),
                gridcolor='#e2e8f0'
            ),
            angularaxis=dict(
                tickfont=dict(size=12, family="sans-serif", color="#334155")
            )
        ),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        margin=dict(l=40, r=40, t=30, b=40),
        height=380,
    )
    return fig


if audit_clicked:
    if not uploaded_images:
        st.error("⚠️ Vui lòng tải lên ít nhất một ảnh giao diện trước khi bắt đầu!")
    else:
        with st.spinner("🔍 Đang kết nối NotebookLM, đối chiếu tri thức và chấm điểm đa chiều..."):
            result = run_ux_audit(
                images=uploaded_images,
                image_names=uploaded_names,
                user_context=user_context,
                notebook_id=notebook_id,
                api_key=api_key_input if api_key_input else None,
                gemini_model=model_choice,
            )

        st.success(f"✅ Hoàn tất kiểm toán! Động cơ sử dụng: **{result.get('engine', 'Audit Engine')}**")

        data = result.get("structured_data", {})
        overall_score = data.get("ux_health_score", 68)
        verdict = data.get("verdict", "Cần cải thiện (Needs Improvement)")
        scores = data.get("scores", {})
        issues = data.get("issues", [])
        strengths = data.get("strengths", [])

        # Count issues by severity
        crit_count = sum(1 for i in issues if i.get("severity") == "Critical")
        maj_count = sum(1 for i in issues if i.get("severity") == "Major")
        min_count = sum(1 for i in issues if i.get("severity") == "Minor")

        # Top KPI Scorecard
        st.subheader("🎯 1. Bảng Điểm Khả Dụng & Chỉ Số Sức Khỏe UX (UX Scorecard)")
        kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)

        with kpi_col1:
            score_color = "#10b981" if overall_score >= 80 else ("#f59e0b" if overall_score >= 60 else "#ef4444")
            st.markdown(
                f"""
                <div class="metric-card" style="border-top: 4px solid {score_color};">
                    <div class="metric-label">UX Health Index</div>
                    <div class="metric-value" style="color: {score_color};">{overall_score}<span style="font-size: 1.1rem; color: #94a3b8;">/100</span></div>
                    <div style="font-size: 0.8rem; font-weight: 600; color: {score_color};">{verdict}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with kpi_col2:
            st.markdown(
                f"""
                <div class="metric-card" style="border-top: 4px solid #ef4444;">
                    <div class="metric-label">Lỗi Nghiêm trọng</div>
                    <div class="metric-value" style="color: #ef4444;">{crit_count}</div>
                    <div style="font-size: 0.8rem; color: #64748b;">Blocker / Critical</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with kpi_col3:
            st.markdown(
                f"""
                <div class="metric-card" style="border-top: 4px solid #f97316;">
                    <div class="metric-label">Lỗi Trung bình</div>
                    <div class="metric-value" style="color: #f97316;">{maj_count}</div>
                    <div style="font-size: 0.8rem; color: #64748b;">Major Friction</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with kpi_col4:
            st.markdown(
                f"""
                <div class="metric-card" style="border-top: 4px solid #eab308;">
                    <div class="metric-label">Lỗi Nhẹ / Cần trau chuốt</div>
                    <div class="metric-value" style="color: #ca8a04;">{min_count}</div>
                    <div style="font-size: 0.8rem; color: #64748b;">Minor / Polish</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with kpi_col5:
            st.markdown(
                f"""
                <div class="metric-card" style="border-top: 4px solid #10b981;">
                    <div class="metric-label">Điểm Sáng (Strengths)</div>
                    <div class="metric-value" style="color: #10b981;">{len(strengths)}</div>
                    <div style="font-size: 0.8rem; color: #64748b;">Cần duy trì</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

        # Radar Chart & Dimension Breakdown
        chart_col, detail_col = st.columns([1.2, 1], gap="medium")

        with chart_col:
            st.markdown("#### 📡 Biểu đồ Radar 5 Chiều kích Khả dụng")
            fig = render_radar_chart(scores)
            st.plotly_chart(fig, use_container_width=True)

        with detail_col:
            st.markdown("#### 📊 Chi tiết Điểm thành phần")
            dim_labels = [
                ("Tính trực quan (Visibility)", scores.get("visibility", 65)),
                ("Phản hồi hệ thống (Feedback)", scores.get("feedback", 55)),
                ("Định hướng hành động (Affordance)", scores.get("affordance", 70)),
                ("Điều hướng & Định vị (Navigation)", scores.get("navigation", 60)),
                ("Tinh gọn nhận thức (Cognitive Load)", scores.get("cognitive_load", 75)),
            ]
            for label, val in dim_labels:
                col_name, col_prog = st.columns([1.5, 1])
                with col_name:
                    st.write(f"**{label}**")
                with col_prog:
                    st.progress(val / 100, text=f"{val}/100")

            if strengths:
                st.markdown("##### 🌟 Điểm cộng nổi bật:")
                for s in strengths:
                    st.markdown(f"- ✅ *{s}*")

        st.divider()

        # Severity Issue Matrix
        st.subheader("⚠️ 2. Bảng Phân Cấp & Quản Trị Độ Nghiêm Trọng Của Lỗi (Issue Matrix)")
        filter_opt = st.radio(
            "Lọc lỗi theo mức độ nghiêm trọng:",
            options=["Tất cả", "🔴 Critical (Nghiêm trọng)", "🟠 Major (Trung bình)", "🟡 Minor (Nhẹ)"],
            horizontal=True,
        )

        filtered_issues = issues
        if "Critical" in filter_opt:
            filtered_issues = [i for i in issues if i.get("severity") == "Critical"]
        elif "Major" in filter_opt:
            filtered_issues = [i for i in issues if i.get("severity") == "Major"]
        elif "Minor" in filter_opt:
            filtered_issues = [i for i in issues if i.get("severity") == "Minor"]

        for item in filtered_issues:
            sev = item.get("severity", "Minor")
            card_class = "issue-critical" if sev == "Critical" else ("issue-major" if sev == "Major" else "issue-minor")
            badge_class = "badge-crit" if sev == "Critical" else ("badge-maj" if sev == "Major" else "badge-min")
            badge_icon = "🔴" if sev == "Critical" else ("🟠" if sev == "Major" else "🟡")

            st.markdown(
                f"""
                <div class="issue-card {card_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <div>
                            <span class="badge-pill {badge_class}">{badge_icon} {sev.upper()}</span>
                            <strong>Vị trí: {item.get('element', 'Phần tử UI')}</strong> 
                            <span style="color: #64748b; font-size: 0.85rem;">({item.get('screen', 'Màn hình')})</span>
                        </div>
                    </div>
                    <p style="margin: 6px 0; font-size: 0.95rem;"><strong>Mô tả lỗi:</strong> {item.get('issue', '')}</p>
                    <p style="margin: 4px 0; font-size: 0.85rem; color: #475569;"><strong>Nguyên lý vi phạm:</strong> <em>{item.get('principle', '')}</em></p>
                    <div style="margin-top: 8px; padding-top: 8px; border-top: 1px dashed rgba(0,0,0,0.1); font-size: 0.9rem; color: #0f172a;">
                        <strong>💡 Đề xuất sửa đổi:</strong> {item.get('recommendation', '')}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.divider()

        # Detailed Report Tabs
        st.subheader("📑 3. Báo Cáo Phân Tích Chuyên Sâu & Xuất Tài Liệu")
        tab_report, tab_knowledge, tab_export = st.tabs([
            "📊 Báo Cáo Chi Tiết (Full Markdown)",
            "📚 Tri Thức Đối Chiếu Từ NotebookLM",
            "📥 Xuất Báo Cáo (.md)",
        ])

        with tab_report:
            st.markdown(result.get("report", "Không có nội dung báo cáo."))

        with tab_knowledge:
            st.markdown("### 📖 Trích xuất Tri thức từ Notebook 'The Design of Everyday Creative Things'")
            nlm_ctx = result.get("notebooklm_context")
            if nlm_ctx:
                st.info(nlm_ctx)
            else:
                st.write("Tri thức tích hợp từ các nguyên lý tiêu chuẩn của Don Norman và Steve Krug.")

        with tab_export:
            st.markdown("### Tải về bản báo cáo định dạng Markdown")
            report_text = result.get("report", "")
            st.download_button(
                label="📥 Tải xuống file Markdown (UX_Audit_Report.md)",
                data=report_text,
                file_name="UX_Audit_Report.md",
                mime="text/markdown",
            )
