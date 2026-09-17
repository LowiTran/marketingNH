import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Cấu hình trang Streamlit
st.set_page_config(
    page_title="VIETCOMBANK LEAD MANAGER - NHÓM NOLE KPI",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Khởi tạo dữ liệu lưu trữ (st.session_state)
if "leads_data" not in st.session_state:
    st.session_state.leads_data = []

# 3. CSS Tùy chỉnh (Tông màu Trắng & Xanh Lá đặc trưng Vietcombank)
st.markdown("""
    <style>
    /* Nền ứng dụng chính */
    .stApp {
        background-color: #F8F9FA;
    }
    
    /* Thanh Sidebar bên trái */
    [data-testid="stSidebar"] {
        background-color: #004d25 !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Khung Logo màu trắng trong Sidebar */
    .logo-container {
        background-color: white;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Banner Header chính */
    .header-banner {
        background: linear-gradient(135deg, #006838 0%, #004d25 100%);
        border-radius: 12px;
        padding: 22px 28px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0, 104, 56, 0.15);
    }
    .header-banner h2 {
        color: white !important;
        margin: 0 0 6px 0;
        font-weight: 700;
        font-size: 24px;
    }
    .header-banner p {
        color: #E8F5E9 !important;
        margin: 0;
        font-size: 14px;
    }
    
    /* Tiêu đề các mục */
    .section-header {
        font-size: 18px;
        font-weight: bold;
        color: #111827;
        margin-top: 15px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Thẻ thống kê (Metric Cards) */
    .metric-card {
        background-color: white;
        padding: 16px 20px;
        border-radius: 10px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .metric-title {
        font-size: 13px;
        color: #6B7280;
        margin-bottom: 4px;
        font-weight: 500;
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #006838;
    }
    
    /* Thẻ Pipeline tiến độ */
    .pipeline-card {
        background-color: white;
        border: 1px solid #E5E7EB;
        border-radius: 10px;
        padding: 18px 10px;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .pipeline-title {
        font-size: 13px;
        color: #4B5563;
        margin-bottom: 8px;
        font-weight: 500;
    }
    .pipeline-count {
        font-size: 30px;
        font-weight: bold;
        color: #006838;
    }

    /* Box thông báo trống (Matching exact screenshot styling) */
    .empty-box {
        background-color: #1e293b;
        color: #60a5fa;
        padding: 16px 20px;
        border-radius: 8px;
        font-size: 15px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. THANH DIỀU HƯỚNG BÊN TRÁI (SIDEBAR)
# ==========================================
with st.sidebar:
    # Hiển thị file ảnh từ máy
    st.image("VCB.jpg", use_container_width=True)
    
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h3 style="margin: 0; font-size: 18px; font-weight: bold; color: white;">VIETCOMBANK</h3>
            <p style="margin: 4px 0 0 0; font-size: 12px; opacity: 0.9; font-weight: 600;">LEAD MANAGER</p>
            <p style="margin: 0; font-size: 11px; opacity: 0.7;">Nhóm NoLe KPI</p>
        </div>
        <hr style="border-color: rgba(255,255,255,0.2); margin-bottom: 20px;">
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 11px; font-weight: bold; letter-spacing: 1px; color: #9CA3AF;'>MENU CHỨC NĂNG</p>", unsafe_allow_html=True)
    
    menu_choice = st.radio(
        "Chức năng",
        options=[
            "🏠 Tổng quan",
            "👥 Khách hàng",
            "➕ Thêm khách hàng",
            "🎯 Pipeline",
            "📊 Phân tích",
            "📞 Cần chăm sóc"
        ],
        label_visibility="collapsed"
    )

# Hàm hỗ trợ hiển thị Banner Header chung
def render_header_banner():
    st.markdown("""
        <div class="header-banner">
            <h2>🏛️ VIETCOMBANK LEAD MANAGER - NHÓM LỘN XỘN</h2>
            <p>Hệ thống quản lý và chăm sóc khách hàng tiềm năng Ngân hàng Vietcombank</p>
        </div>
    """, unsafe_allow_html=True)

# Lấy DataFrame từ session_state
df_leads = pd.DataFrame(st.session_state.leads_data)

# ==========================================
# 5. XỬ LÝ GIAO DIỆN THEO MENU CHỌN
# ==========================================

# ------------------------------------------
# MENU 1: TỔNG QUAN
# ------------------------------------------
if "Tổng quan" in menu_choice:
    render_header_banner()
    
    # Tính toán các chỉ số thực tế từ dữ liệu
    total_leads = len(df_leads)
    hot_leads = len(df_leads[df_leads['Phân loại'] == '🔥 HOT']) if total_leads > 0 else 0
    warm_leads = len(df_leads[df_leads['Phân loại'] == '⚡ WARM']) if total_leads > 0 else 0
    cold_leads = len(df_leads[df_leads['Phân loại'] == '❄️ COLD']) if total_leads > 0 else 0
    
    # 1. Tổng quan khách hàng
    st.markdown('<div class="section-header">📊 Tổng quan khách hàng</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="metric-card"><div class="metric-title">👥 Tổng khách hàng</div><div class="metric-value">{total_leads}</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card"><div class="metric-title">🔥 Khách HOT</div><div class="metric-value">{hot_leads}</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-card"><div class="metric-title">⚡ Khách WARM</div><div class="metric-value">{warm_leads}</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="metric-card"><div class="metric-title">❄️ Khách COLD</div><div class="metric-value">{cold_leads}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. Pipeline tiến độ
    st.markdown('<div class="section-header">📌 Pipeline tiến độ</div>', unsafe_allow_html=True)
    p1, p2, p3, p4, p5 = st.columns(5)
    
    pipeline_stages = ["Mới tiếp nhận", "Đã liên hệ", "Đang tư vấn", "Tiềm năng", "Đã chuyển đổi"]
    cols = [p1, p2, p3, p4, p5]
    
    for stage, col in zip(pipeline_stages, cols):
        count = len(df_leads[df_leads['Trạng thái Pipeline'] == stage]) if total_leads > 0 else 0
        with col:
            st.markdown(f'<div class="pipeline-card"><div class="pipeline-title">{stage}</div><div class="pipeline-count">{count}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. Khách hàng ưu tiên xử lý (HOT Lead)
    st.markdown('<div class="section-header">🔥 Khách hàng ưu tiên xử lý (HOT Lead)</div>', unsafe_allow_html=True)
    
    if total_leads > 0 and hot_leads > 0:
        hot_df = df_leads[df_leads['Phân loại'] == '🔥 HOT']
        st.dataframe(hot_df, use_container_width=True, hide_index=True)
    else:
        st.info("💡 Chưa có dữ liệu khách hàng ưu tiên (HOT Lead) cần xử lý.")

# ------------------------------------------
# MENU 2: KHÁCH HÀNG (Ảnh image_6118cf.png)
# ------------------------------------------
elif "Khách hàng" in menu_choice:
    render_header_banner()
    st.markdown('<div class="section-header">👥 Danh sách khách hàng</div>', unsafe_allow_html=True)
    
    if len(df_leads) == 0:
        st.info("Chưa có thông tin khách hàng nào.")
    else:
        st.dataframe(df_leads, use_container_width=True, hide_index=True)

# ------------------------------------------
# MENU 3: THÊM KHÁCH HÀNG (Ảnh image_611965, image_616f7f, image_616fa4)
# ------------------------------------------
elif "Thêm khách hàng" in menu_choice:
    render_header_banner()
    st.markdown('<div class="section-header">➕ Tạo hồ sơ khách hàng mới</div>', unsafe_allow_html=True)
    st.info("💡 Hệ thống sẽ tự động tính điểm tiềm năng dựa trên thông tin thu nhập, sản phẩm và nhu cầu vay/gửi.")
    
    with st.form("create_lead_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        
        # Cột 1
        with col1:
            fullname = st.text_input("👤 Họ và tên *", placeholder="Nhập họ và tên")
            phone = st.text_input("📱 Số điện thoại *", placeholder="Nhập số điện thoại")
            email = st.text_input("📧 Email", placeholder="Nhập email")
            gender = st.selectbox("👤 Giới tính", ["Nam", "Nữ", "Khác"])
            
        # Cột 2
        with col2:
            age = st.number_input("🎂 Tuổi", min_value=18, max_value=100, value=25)
            job = st.text_input("💼 Nghề nghiệp", placeholder="Nhập nghề nghiệp")
            income = st.number_input("💰 Thu nhập/tháng (Triệu VNĐ)", min_value=0.0, value=15.00, step=1.0)
            location = st.text_input("📍 Khu vực (Quận/Huyện, Tỉnh/TP)", placeholder="Nhập khu vực")
            
        # Cột 3
        with col3:
            product = st.selectbox(
                "💳 Sản phẩm quan tâm",
                ["Vay mua nhà", "Vay mua ô tô", "Vay kinh doanh", "Thẻ tín dụng", "Gửi tiết kiệm", "Tài khoản thanh toán"]
            )
            demand_amount = st.number_input("💵 Nhu cầu dự kiến (Triệu VNĐ)", min_value=0.0, value=500.00, step=50.0)
            timeframe = st.selectbox("📅 Thời gian dự kiến", ["Trong 1 tháng", "1 - 3 tháng", "3 - 6 tháng", "Trên 6 tháng"])
            staff = st.text_input("👤 Nhân viên phụ trách", placeholder="Nhập tên nhân viên phụ trách")
            
        note = st.text_area("📝 Ghi chú chi tiết", placeholder="Nhập ghi chú thêm...")
        
        submit_btn = st.form_submit_button("🚀 LƯU VÀ PHÂN LOẠI KHÁCH HÀNG", type="primary", use_container_width=True)
        
        if submit_btn:
            if not fullname or not phone:
                st.error("⚠️ Vui lòng điền đầy đủ thông tin bắt buộc: Họ và tên và Số điện thoại!")
            else:
                # Thuật toán tự động phân loại Lead dựa trên Thu nhập & Nhu cầu
                if income >= 30.0 or demand_amount >= 1000.0 or timeframe == "Trong 1 tháng":
                    lead_type = "🔥 HOT"
                elif income >= 15.0 or demand_amount >= 300.0:
                    lead_type = "⚡ WARM"
                else:
                    lead_type = "❄️ COLD"
                
                # Lưu thông tin mới vào Session State
                new_lead = {
                    "Mã KH": f"VCB{len(df_leads) + 101}",
                    "Họ và tên": fullname,
                    "Số điện thoại": phone,
                    "Email": email,
                    "Giới tính": gender,
                    "Tuổi": age,
                    "Nghề nghiệp": job,
                    "Thu nhập (Triệu)": income,
                    "Khu vực": location,
                    "Sản phẩm quan tâm": product,
                    "Nhu cầu (Triệu)": demand_amount,
                    "Thời gian dự kiến": timeframe,
                    "Nhân viên": staff,
                    "Phân loại": lead_type,
                    "Trạng thái Pipeline": "Mới tiếp nhận",
                    "Ngày tạo": datetime.now().strftime("%d/%m/%Y"),
                    "Ghi chú": note
                }
                st.session_state.leads_data.append(new_lead)
                st.success(f"✅ Đã thêm hồ sơ khách hàng **{fullname}** thành công! Hệ thống phân loại: **{lead_type}**")

# ------------------------------------------
# MENU 4: PIPELINE (Ảnh image_611989.png)
# ------------------------------------------
elif "Pipeline" in menu_choice:
    render_header_banner()
    st.markdown('<div class="section-header">🎯 Quy trình chuyển đổi (Pipeline)</div>', unsafe_allow_html=True)
    
    if len(df_leads) == 0:
        st.info("Chưa có dữ liệu.")
    else:
        # Hiển thị dạng cột Pipeline
        cols = st.columns(5)
        stages = ["Mới tiếp nhận", "Đã liên hệ", "Đang tư vấn", "Tiềm năng", "Đã chuyển đổi"]
        
        for idx, stage in enumerate(stages):
            with cols[idx]:
                st.markdown(f"### **{stage}**")
                stage_df = df_leads[df_leads['Trạng thái Pipeline'] == stage]
                if len(stage_df) == 0:
                    st.caption("Trống")
                else:
                    for _, row in stage_df.iterrows():
                        with st.expander(f"{row['Họ và tên']} ({row['Phân loại']})"):
                            st.write(f"📱 {row['Số điện thoại']}")
                            st.write(f"💳 {row['Sản phẩm quan tâm']}")
                            st.write(f"💵 {row['Nhu cầu (Triệu)']} Triệu")

# ------------------------------------------
# MENU 5: PHÂN TÍCH (Ảnh Screenshot 2026-09-17 174454.png)
# ------------------------------------------
elif "Phân tích" in menu_choice:
    render_header_banner()
    st.markdown('<div class="section-header">📊 Phân tích dữ liệu kinh doanh</div>', unsafe_allow_html=True)
    
    if len(df_leads) == 0:
        st.info("Chưa có dữ liệu để thực hiện phân tích.")
    else:
        col_a1, col_a2 = st.columns(2)
        with col_a1:
            st.markdown("#### 💳 Phân bổ theo sản phẩm quan tâm")
            st.bar_chart(df_leads['Sản phẩm quan tâm'].value_counts())
        with col_a2:
            st.markdown("#### 🔥 Phân bổ tỷ lệ phân loại Lead")
            st.bar_chart(df_leads['Phân loại'].value_counts())

# ------------------------------------------
# MENU 6: CẦN CHĂM SÓC (Ảnh Screenshot 2026-09-17 174501.png)
# ------------------------------------------
elif "Cần chăm sóc" in menu_choice:
    render_header_banner()
    st.markdown('<div class="section-header">📞 Danh sách ưu tiên chăm sóc ngay</div>', unsafe_allow_html=True)
    
    if len(df_leads) == 0:
        st.info("Chưa có thông tin khách hàng.")
    else:
        # Ưu tiên hiển thị các khách HOT và WARM cần chăm sóc
        urgent_df = df_leads[df_leads['Phân loại'].isin(['🔥 HOT', '⚡ WARM'])]
        if len(urgent_df) > 0:
            st.dataframe(urgent_df, use_container_width=True, hide_index=True)
        else:
            st.success("🎉 Không có khách hàng cần chăm sóc khẩn cấp!")
