import streamlit as st
import datetime

# Cấu hình trang
st.set_page_config(page_title="Vietcombank - Trang chủ", page_icon="🛡️", layout="wide")

# Tùy chỉnh CSS để giống màu sắc thương hiệu VCB (Xanh và Trắng)
st.markdown("""
    <style>
    /* Ẩn menu mặc định của Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Màu sắc thương hiệu */
    .vcb-green-text {color: #008345 !important; font-weight: bold;}
    .vcb-light-green-bg {background-color: #8cc63f !important; color: white !important; border-radius: 5px; padding: 8px 15px;}
    
    /* Định dạng thanh Top Nav */
    .top-nav {font-size: 13px; color: #555; display: flex; justify-content: space-between; padding-bottom: 10px; border-bottom: 1px solid #eee; margin-bottom: 15px;}
    .top-nav a {text-decoration: none; color: #555; margin-right: 15px;}
    .top-nav a:hover {color: #008345;}
    
    /* Định dạng Container chính */
    .main-container {background-color: white; padding: 20px;}
    
    /* Căn giữa các nút ở menu dưới */
    div.stButton > button {height: 80px; font-weight: bold; color: #008345; border-color: #e0e0e0; background-color: white;}
    div.stButton > button:hover {border-color: #008345; color: #008345;}
    </style>
""", unsafe_allow_html=True)

# 1. TOP NAVIGATION BAR (Cá nhân, Tổ chức, Về Vietcombank...)
st.markdown("""
    <div class="top-nav">
        <div>
            <a href="#" style="color: #008345; font-weight: bold;">Cá nhân</a>
            <a href="#">Tổ chức</a>
            <a href="#">Khách hàng Ưu tiên</a>
        </div>
        <div>
            <a href="#">Về Vietcombank</a>
            <a href="#">Tin tức</a>
            <a href="#">Nhà đầu tư</a>
            <a href="#">Mạng lưới</a>
            <a href="#">Tuyển dụng</a>
            <span style="margin-right: 15px; font-weight: bold;">📞 1900 545413</span>
            <span>🇻🇳</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 2. MAIN NAVIGATION BAR (Logo, Menu chính, Đăng nhập)
nav_cols = st.columns([2, 1.5, 1.5, 1.5, 1.5, 2, 1.5])
with nav_cols[0]:
    st.markdown("<h3 class='vcb-green-text'>🛡️ Vietcombank</h3>", unsafe_allow_html=True)
with nav_cols[1]:
    st.markdown("<p style='margin-top: 10px;'>Sản phẩm & Dịch vụ ⌄</p>", unsafe_allow_html=True)
with nav_cols[2]:
    st.markdown("<p style='margin-top: 10px;'>Công cụ & Tiện ích ⌄</p>", unsafe_allow_html=True)
with nav_cols[3]:
    st.markdown("<p style='margin-top: 10px;'>Liên hệ & Hỗ trợ ⌄</p>", unsafe_allow_html=True)
with nav_cols[4]:
    st.markdown("<p style='margin-top: 10px;'>Giao dịch an toàn</p>", unsafe_allow_html=True)
with nav_cols[5]:
    st.markdown("<p style='margin-top: 10px; color: #004a8f; font-weight: bold;'>DIY Vietcombank x HAHA</p>", unsafe_allow_html=True)
with nav_cols[6]:
    if st.button("🚪 Đăng nhập", type="primary", use_container_width=True):
        st.info("Chuyển hướng đến trang Đăng nhập VCB Digibank...")

st.markdown("<hr style='margin: 0px 0px 40px 0px; opacity: 0.2;'>", unsafe_allow_html=True)

# 3. HERO SECTION (Lời chào, Tìm kiếm, QR Code & Hình ảnh)
hero_col1, hero_col2 = st.columns([1.2, 1])

with hero_col1:
    st.markdown("<br>", unsafe_allow_html=True)
    # Tự động thay đổi lời chào theo giờ
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        greeting = "Chào buổi sáng ⛅"
    elif current_hour < 18:
        greeting = "Chào buổi chiều 🌤️"
    else:
        greeting = "Chào buổi tối 🌙"
        
    st.markdown(f"<h1 style='font-size: 3rem; color: #333;'>{greeting}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.2rem; color: #555;'>Quý khách đang tìm kiếm gì hôm nay?</p>", unsafe_allow_html=True)
    
    # Thanh tìm kiếm
    search_query = st.text_input("", placeholder="🔍 Thẻ tín dụng, vay tiêu dùng...", label_visibility="collapsed")
    if search_query:
        st.success(f"Đang tìm kiếm thông tin cho: **{search_query}**")

with hero_col2:
    # Mô phỏng khu vực QR code và bộ sưu tập thẻ
    st.markdown("""
        <div style="background-color: #f1f8f4; padding: 20px; border-radius: 15px; text-align: center; border: 1px dashed #008345;">
            <h4 style="color: #008345;">Quét để khám phá</h4>
Dưới đây là mã nguồn Streamlit hoàn chỉnh mô phỏng lại bố cục và các chức năng chính của giao diện web Vietcombank trong hình. Tôi đã thiết kế lại với tông màu xanh lá (VCB) và trắng, loại bỏ hình nền phong cảnh phức tạp để giao diện gọn gàng, mang tính ứng dụng cao.

Bạn chỉ cần lưu đoạn mã này vào một file (ví dụ: `app.py`) và chạy bằng lệnh `streamlit run app.py` trong terminal.

```python
import streamlit as st

# 1. Cấu hình trang
st.set_page_config(page_title="Vietcombank Clone", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS Tùy chỉnh (Giao diện xanh/trắng)
st.markdown("""
    <style>
    /* Tùy chỉnh màu sắc chữ */
    .vcb-green { color: #005C2B; font-weight: bold; }
    .top-bar { font-size: 13px; color: #555; }
    .nav-link { font-size: 16px; font-weight: bold; color: #005C2B; cursor: pointer; }
    
    /* Giao diện khung Hero */
    .bg-light-green { 
        background-color: #E8F5E9; 
        padding: 40px; 
        border-radius: 15px; 
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    /* Tùy chỉnh thanh tìm kiếm */
    div[data-testid="stTextInput"] input { 
        border-radius: 30px; 
        padding: 15px;
    }
    
    /* Tùy chỉnh nút bấm Đăng nhập & Utilities */
    div.stButton > button {
        border-radius: 20px;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        border-color: #005C2B;
        color: #005C2B;
    }
    .login-btn div.stButton > button {
        background-color: #8CC63F;
        color: white;
        border: none;
    }
    .login-btn div.stButton > button:hover {
        background-color: #005C2B;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Top Bar (Thanh menu trên cùng)
t1, t2, t3 = st.columns([4, 1, 4])
with t1:
    st.markdown("<span class='top-bar'><b>Cá nhân</b> &nbsp;&nbsp;|&nbsp;&nbsp; Tổ chức &nbsp;&nbsp;|&nbsp;&nbsp; Khách hàng Ưu tiên</span>", unsafe_allow_html=True)
with t3:
    st.markdown("<div style='text-align: right;'><span class='top-bar'>Về Vietcombank &nbsp;|&nbsp; Tin tức &nbsp;|&nbsp; Nhà đầu tư &nbsp;|&nbsp; Mạng lưới &nbsp;|&nbsp; Tuyển dụng &nbsp;|&nbsp; 📞 <b>1900 545413</b> &nbsp;|&nbsp; 🇻🇳</span></div>", unsafe_allow_html=True)

st.divider()

# 4. Main Navigation (Thanh điều hướng chính)
n1, n2, n3, n4, n5, n6 = st.columns([1.5, 1.2, 1.2, 1.2, 1.2, 1])
with n1:
    st.markdown("<h3 class='vcb-green'>🛡️ Vietcombank</h3>", unsafe_allow_html=True)
with n2:
    st.markdown("<div class='nav-link'>Sản phẩm & Dịch vụ ⌄</div>", unsafe_allow_html=True)
with n3:
    st.markdown("<div class='nav-link'>Công cụ & Tiện ích ⌄</div>", unsafe_allow_html=True)
with n4:
    st.markdown("<div class='nav-link'>Liên hệ & Hỗ trợ ⌄</div>", unsafe_allow_html=True)
with n5:
    st.markdown("<div class='nav-link'>Giao dịch an toàn</div>", unsafe_allow_html=True)
with n6:
    st.markdown("<div class='login-btn'>", unsafe_allow_html=True)
    st.button("➔ Đăng nhập", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Hero Section (Khu vực chào mừng, tìm kiếm và thẻ)
with st.container():
    st.markdown("<div class='bg-light-green'>", unsafe_allow_html=True)
    h1, h2, h3 = st.columns([4, 2, 4])
    
    with h1:
        st.header("Chào buổi chiều 🌤️")
        st.write("Quý khách đang tìm kiếm gì hôm nay?")
        # Thanh tìm kiếm
        search = st.text_input("", placeholder="🔍 Thẻ tín dụng, vay tiêu dùng...")
        
    with h2:
        # Giả lập mã QR
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image("[https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=vietcombank](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=vietcombank)", width=120)
        st.write("↙️ Quét để khám phá")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with h3:
        # Phần giới thiệu bộ sưu tập thẻ (thay thế ảnh bằng Text và Icon)
        st.markdown("<h3 class='vcb-green'>Vietcombank Visa HAHA Collection</h3>", unsafe_allow_html=True)
        st.write("✏️ Khởi lo chi, chỉ lo chill 🥕")
        st.info("💳 Hình ảnh minh họa các thẻ Visa (Xanh lá, Hồng, Xanh dương)")
        
    st.markdown("</div>", unsafe_allow_html=True)

# 6. Bottom Utilities Bar (Thanh tiện ích dưới cùng)
st.markdown("<br>", unsafe_allow_html=True)
b1, b2, b3, b4, b5 = st.columns(5)
with b1:
    st.button("⭐ Gợi ý sản phẩm", use_container_width=True)
with b2:
    st.button("📰 Tin nổi bật", use_container_width=True)
with b3:
    st.button("📝 Đăng ký trực tuyến", use_container_width=True)
with b4:
    st.button("🎁 VCB Loyalty", use_container_width=True)
with b5:
    st.button("🏷️ Ưu đãi", use_container_width=True)

# 7. Chatbot Icon (Nút nổi góc phải dưới)
st.markdown("""
    <div style='position: fixed; bottom: 30px; right: 30px; background-color: #8CC63F; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; box-shadow: 2px 2px 10px rgba(0,0,0,0.2); cursor: pointer;'>
        <h2 style='margin:0; padding:0;'>🤖</h2>
    </div>
""", unsafe_allow_html=True)
