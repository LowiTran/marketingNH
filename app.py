import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Cấu hình trang
st.set_page_config(
    page_title="VCB Digibank - Ngân hàng số",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Tùy chỉnh để giả lập giao diện VCB Digibank
def local_css():
    st.markdown("""
    <style>
        /* Màu chủ đạo của VCB là xanh lá cây đậm: #005a3c và màu phụ là xanh nhạt */
        :root {
            --vcb-green: #005a3c;
            --vcb-light-green: #67a935;
        }
        
        /* Chỉnh màu chữ sidebar */
        [data-testid="stSidebar"] {
            background-color: #f8f9fa;
        }
        [data-testid="stSidebar"] * {
            color: var(--vcb-green) !important;
        }
        
        /* Tiêu đề chính */
        h1, h2, h3 {
            color: var(--vcb-green) !important;
            font-weight: bold;
        }
        
        /* Thẻ hiển thị số dư tài khoản */
        .account-card {
            background: linear-gradient(135deg, #005a3c, #67a935);
            border-radius: 15px;
            padding: 25px;
            color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            margin-bottom: 25px;
        }
        .account-card p {
            color: white !important;
            margin: 0;
            padding: 0;
        }
        .account-balance {
            font-size: 36px;
            font-weight: bold;
            margin: 10px 0 !important;
            color: white !important;
        }
        
        /* Nút thao tác nhanh ở trang chủ */
        .stButton>button {
            width: 100%;
            background-color: white;
            color: var(--vcb-green) !important;
            border: 1.5px solid var(--vcb-green);
            border-radius: 10px;
            height: 70px;
            font-weight: bold;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: var(--vcb-green);
            color: white !important;
            border: 1.5px solid var(--vcb-green);
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        
        /* Nút Primary (Lưu / Tiếp tục) */
        button[data-testid="baseButton-primary"] {
            background-color: var(--vcb-green) !important;
            color: white !important;
        }
        
        /* Ẩn footer mặc định của Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

local_css()

# Biến dữ liệu giả lập
USER_NAME = "NGUYỄN VĂN A"
ACCOUNT_NUMBER = "1012345678"
BALANCE = "125,450,000 VND"

# ==========================================
# GIAO DIỆN SIDEBAR (THANH ĐIỀU HƯỚNG TRÁI)
# ==========================================
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Vietcombank_logo.svg/1200px-Vietcombank_logo.svg.png", 
    width=220
)
st.sidebar.markdown("---")
st.sidebar.markdown(f"**👤 Xin chào,**\n### **{USER_NAME}**")
st.sidebar.markdown("---")

menu = ["🏠 Trang chủ", "💸 Chuyển tiền", "💰 Gửi tiết kiệm", "🧾 Thanh toán hóa đơn", "💳 Dịch vụ thẻ", "⚙️ Cài đặt"]
choice = st.sidebar.radio("DANH MỤC CHỨC NĂNG", menu)

st.sidebar.markdown("---")
st.sidebar.button("Đăng xuất", type="primary")

# ==========================================
# GIAO DIỆN MAIN CONTENT (NỘI DUNG CHÍNH)
# ==========================================

if choice == "🏠 Trang chủ":
    st.title("VCB Digibank")
    
    # Khu vực thẻ tài khoản
    st.markdown(f"""
    <div class="account-card">
        <p style="font-size: 16px;">Tài khoản thanh toán VND</p>
        <p style="font-size: 22px; font-weight: bold; letter-spacing: 2px;">{ACCOUNT_NUMBER}</p>
        <div class="account-balance">{BALANCE}</div>
        <p style="font-size: 14px; opacity: 0.9;">Chi nhánh Thăng Long</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ⚡ Chức năng nổi bật")
    
    # Khu vực các nút bấm tiện ích nhanh
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("💸\nChuyển tiền VCB")
    with col2:
        st.button("⚡\nChuyển nhanh 24/7")
    with col3:
        st.button("📱\nNạp tiền điện thoại")
    with col4:
        st.button("🧾\nThanh toán hóa đơn")
        
    st.markdown("---")
    
    # Bảng lịch sử giao dịch gần đây
    st.markdown("### 🕒 Lịch sử giao dịch gần đây")
    
    now = datetime.now()
    transactions = pd.DataFrame({
        "Thời gian": [
            (now).strftime("%d/%m/%Y %H:%M"),
            (now - timedelta(days=1)).strftime("%d/%m/%Y %H:%M"),
            (now - timedelta(days=2)).strftime("%d/%m/%Y %H:%M"),
            (now - timedelta(days=3)).strftime("%d/%m/%Y %H:%M"),
            (now - timedelta(days=5)).strftime("%d/%m/%Y %H:%M")
        ],
        "Diễn giải": [
            "Chuyển tiền đến NGUYEN VAN B",
            "Thanh toán hóa đơn tiền điện",
            "Nhận lương tháng",
            "Phí duy trì dịch vụ VCB Digibank",
            "Nạp tiền điện thoại Viettel"
        ],
        "Số tiền": [
            "- 500,000 VND",
            "- 1,250,000 VND",
            "+ 25,000,000 VND",
            "- 11,000 VND",
            "- 100,000 VND"
        ]
    })
    
    st.dataframe(transactions, use_container_width=True, hide_index=True)

elif choice == "💸 Chuyển tiền":
    st.title("Chuyển tiền")
    st.info("Quý khách vui lòng chọn hình thức chuyển tiền, nhập thông tin người nhận và số tiền.")
    
    with st.form("transfer_form"):
        st.selectbox("Hình thức chuyển:", ["Chuyển tiền trong Vietcombank", "Chuyển nhanh Napas 24/7 ngoài VCB"])
        
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Ngân hàng thụ hưởng")
            st.text_input("Số tài khoản người nhận")
        with col2:
            st.text_input("Tên người nhận (Hệ thống tự động tra cứu)", disabled=True, value="Vui lòng nhập STK...")
            st.number_input("Số tiền (VND)", min_value=0, step=50000)
            
        st.text_input("Nội dung chuyển tiền", value=f"{USER_NAME} chuyen tien")
        st.form_submit_button("Tiếp tục", type="primary")

elif choice == "💰 Gửi tiết kiệm":
    st.title("Tiền gửi tiết kiệm trực tuyến")
    st.success("🌟 Lãi suất gửi góp trực tuyến hiện tại đang áp dụng lên đến 5.5%/năm.")
    
    st.metric(label="Tổng số dư tiết kiệm (VND)", value="50,000,000", delta="+2,500,000 VND so với tháng trước")
    
    st.markdown("---")
    st.markdown("### Mở tài khoản tiết kiệm mới")
    with st.form("saving_form"):
        st.selectbox("Kỳ hạn gửi", ["1 tháng (Lãi suất 3.0%)", "3 tháng (Lãi suất 3.5%)", "6 tháng (Lãi suất 4.5%)", "12 tháng (Lãi suất 5.5%)"])
        st.number_input("Số tiền gửi (VND)", min_value=1000000, step=1000000)
        st.selectbox("Phương thức đáo hạn", ["Tự động quay vòng gốc và lãi", "Tự động quay vòng gốc, lãi chuyển vào TK thanh toán", "Đóng tài khoản, gốc và lãi chuyển vào TK thanh toán"])
        st.form_submit_button("Mở sổ tiết kiệm", type="primary")

else:
    st.title(choice)
    st.warning("🚧 Chức năng này hiện đang được mô phỏng và nâng cấp trong phiên bản sắp tới.")
