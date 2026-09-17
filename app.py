import streamlit as st
import pandas as pd

# 1. Cấu hình trang
st.set_page_config(
    page_title="VIETCOMBANK LEAD MANAGER - NHÓM LỘN XỘN",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Tùy chỉnh (Tông màu Trắng & Xanh Lá đặc trưng của Vietcombank)
st.markdown("""
    <style>
    /* Nền ứng dụng màu trắng sáng */
    .stApp {
        background-color: #F8F9FA;
    }
    
    /* Thanh Sidebar bên trái - Màu xanh Vietcombank */
    [data-testid="stSidebar"] {
        background-color: #004d25 !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Khung Logo màu trắng trong Sidebar */
    .logo-container {
        background-color: white;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Header Banner chính */
    .header-banner {
        background: linear-gradient(135deg, #006838 0%, #004d25 100%);
        border-radius: 12px;
        padding: 25px 30px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0, 104, 56, 0.15);
    }
    .header-banner h2 {
        color: white !important;
        margin: 0 0 8px 0;
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
        color: #1A1A1A;
        margin-top: 20px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Thẻ thống kê tổng quan (Cards) */
    .metric-card {
        background-color: white;
        padding: 15px 20px;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .metric-title {
        font-size: 13px;
        color: #64748B;
        margin-bottom: 5px;
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
        border: 1px solid #E0E0E0;
        border-radius: 12px;
        padding: 20px 10px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: transform 0.2s;
    }
    .pipeline-card:hover {
        border-color: #006838;
        transform: translateY(-2px);
    }
    .pipeline-title {
        font-size: 14px;
        color: #555555;
        margin-bottom: 10px;
        font-weight: 500;
    }
    .pipeline-count {
        font-size: 32px;
        font-weight: bold;
        color: #006838;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. THANH DIỀU HƯỚNG BÊN TRÁI (SIDEBAR)
# ==========================================
with st.sidebar:
    # Ô logo Vietcombank nền trắng
    st.markdown("""
        <div class="logo-container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Vietcombank_logo.svg/1200px-Vietcombank_logo.svg.png" width="160">
        </div>
        <div style="text-align: center; margin-bottom: 20px;">
            <h3 style="margin: 0; font-size: 18px; font-weight: bold; color: white;">VIETCOMBANK</h3>
            <p style="margin: 5px 0 0 0; font-size: 12px; opacity: 0.8; font-weight: 600;">LEAD MANAGER</p>
            <p style="margin: 0; font-size: 11px; opacity: 0.7;">Nhóm Lộn Xộn</p>
        </div>
        <hr style="border-color: rgba(255,255,255,0.2); margin-bottom: 20px;">
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 12px; font-weight: bold; letter-spacing: 1px; color: #A0AEC0;'>MENU CHỨC NĂNG</p>", unsafe_allow_html=True)
    
    # Danh sách chức năng đầy đủ từ hình ảnh
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

# ==========================================
# 4. NỘI DUNG CHÍNH (MAIN CONTENT AREA)
# ==========================================

if "Tổng quan" in menu_choice:
    # 4.1 Header Banner chính
    st.markdown("""
        <div class="header-banner">
            <h2>🏛️ VIETCOMBANK LEAD MANAGER - NHÓM LỘN XỘN</h2>
            <p>Hệ thống quản lý và chăm sóc khách hàng tiềm năng Ngân hàng Vietcombank</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 4.2 Tổng quan khách hàng
    st.markdown('<div class="section-header">📊 Tổng quan khách hàng</div>', unsafe_allow_html=True)
    
    col_k1, col_k2, col_k3, col_k4 = st.columns(4)
    
    with col_k1:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">👥 Tổng khách hàng</div>
                <div class="metric-value">0</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_k2:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">🔥 Khách HOT</div>
                <div class="metric-value">0</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_k3:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">⚡ Khách WARM</div>
                <div class="metric-value">0</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_k4:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">❄️ Khách COLD</div>
                <div class="metric-value">0</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 4.3 Pipeline tiến độ
    st.markdown('<div class="section-header">📌 Pipeline tiến độ</div>', unsafe_allow_html=True)
    
    p1, p2, p3, p4, p5 = st.columns(5)
    
    stages = [
        ("Mới tiếp nhận", "0", p1),
        ("Đã liên hệ", "0", p2),
        ("Đang tư vấn", "0", p3),
        ("Tiềm năng", "0", p4),
        ("Đã chuyển đổi", "0", p5)
    ]
    
    for title, count, col in stages:
        with col:
            st.markdown(f"""
                <div class="pipeline-card">
                    <div class="pipeline-title">{title}</div>
                    <div class="pipeline-count">{count}</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 4.4 Khách hàng ưu tiên xử lý (HOT Lead)
    st.markdown('<div class="section-header">🔥 Khách hàng ưu tiên xử lý (HOT Lead)</div>', unsafe_allow_html=True)
    
    # Bảng hiển thị danh sách HOT Lead
    df_empty = pd.DataFrame({
        "Mã KH": [],
        "Họ và tên": [],
        "Số điện thoại": [],
        "Nhu cầu sản phẩm": [],
        "Mức độ ưu tiên": [],
        "Trạng thái": [],
        "Ngày tiếp nhận": []
    })
    
    st.dataframe(
        df_empty,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Mã KH": "Mã KH",
            "Họ và tên": "Họ và tên",
            "Số điện thoại": "Số điện thoại",
            "Nhu cầu sản phẩm": "Nhu cầu sản phẩm",
            "Mức độ ưu tiên": "Mức độ ưu tiên",
            "Trạng thái": "Trạng thái",
            "Ngày tiếp nhận": "Ngày tiếp nhận"
        }
    )
    st.info("💡 Chưa có dữ liệu khách hàng ưu tiên (HOT Lead) cần xử lý.")

elif "Khách hàng" in menu_choice:
    st.title("👥 Quản lý danh sách Khách hàng")
    st.write("Chức năng tra cứu và phân loại khách hàng.")

elif "Thêm khách hàng" in menu_choice:
    st.title("➕ Thêm mới Khách hàng tiềm năng")
    with st.form("add_lead_form"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.text_input("Họ và tên khách hàng")
            st.text_input("Số điện thoại")
            st.selectbox("Phân loại Lead", ["🔥 HOT Lead", "⚡ WARM Lead", "❄️ COLD Lead"])
        with col_f2:
            st.selectbox("Nhu cầu sản phẩm VCB", ["Thẻ tín dụng", "Vay tiêu dùng", "Gửi tiết kiệm", "Mở tài khoản số đẹp", "Khác"])
            st.selectbox("Trạng thái Pipeline", ["Mới tiếp nhận", "Đã liên hệ", "Đang tư vấn", "Tiềm năng", "Đã chuyển đổi"])
            st.text_area("Ghi chú thêm")
        st.form_submit_button("Lưu khách hàng", type="primary")

elif "Pipeline" in menu_choice:
    st.title("🎯 Quản lý Tiến độ Pipeline")
    st.write("Chức năng theo dõi hành trình chuyển đổi khách hàng.")

elif "Phân tích" in menu_choice:
    st.title("📊 Báo cáo & Phân tích")
    st.write("Biểu đồ và chỉ số hiệu quả chuyển đổi Lead.")

elif "Cần chăm sóc" in menu_choice:
    st.title("📞 Danh sách Khách hàng Cần chăm sóc")
    st.write("Lịch nhắc gọi lại và chăm sóc định kỳ.")
