import streamlit as st
import random
from datetime import datetime

# 頁面基本設定
st.set_page_config(
    page_title="AI 智能六合彩 VIP 尊貴會員導航",
    page_icon="🔮",
    layout="centered"
)

# 自訂 CSS 樣式
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #FF4B4B;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-title {
        text-align: center;
        color: #555555;
        font-size: 16px;
        margin-bottom: 30px;
    }
    .vip-card {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        color: #333333;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .pay-btn {
        background-color: #635bff;
        color: white !important;
        padding: 12px 28px;
        text-decoration: none;
        border-radius: 6px;
        font-weight: bold;
        font-size: 16px;
        display: inline-block;
        margin-top: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .pay-btn:hover {
        background-color: #5147df;
    }
    </style>
""", unsafe_allow_html=True)

# 頁面標題
st.markdown('<div class="main-title">🔮 AI 智能六合彩資料導航</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">運用大數據與個人化運勢分析，助您精準掌握幸運號碼</div>', unsafe_allow_html=True)

# 側邊欄導航
st.sidebar.title("📌 功能選單")
menu = st.sidebar.radio("選擇功能", ["🏠 首頁／免費試用", "💎 VIP 尊貴會員專區", "⚙️ 會員帳戶管理"])

# --- 1. 首頁／免費試用 ---
if menu == "🏠 首頁／免費試用":
    st.subheader("🍀 今日免費幸運號碼推薦")
    st.write("點擊下方按鈕，即可隨機生成一套今日的參考號碼：")
    
    if st.button("🎲 生成免費推薦號碼"):
        free_numbers = sorted(random.sample(range(1, 50), 6))
        st.success(f"您的今日免費參考號碼：**{free_numbers}**")
    
    st.info("💡 想要解鎖更進階的 AI 趨勢分析、熱門號碼過濾與獨家運勢導航？歡迎隨時前往左側選單升級為 VIP 會員！")

# --- 2. VIP 尊貴會員專區 ---
elif menu == "💎 VIP 尊貴會員專區":
    st.markdown("""
        <div class="vip-card">
            <h2>💎 AI 智能六合彩 VIP 尊貴會員</h2>
            <p>解鎖完整大數據走勢預測、專屬運勢導航、獨家縮水組合及高命中率分析工具！</p>
            <h3>💰 僅需 HK$48 / 月</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # 放置 Stripe 官方安全結帳連結按鈕
    st.markdown("""
        <div style="text-align: center;">
            <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" class="pay-btn">
                💳 立即線上信用卡升級 VIP（$48/月）
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("🔥 VIP 尊貴會員獨享功能預覽")
    st.write("1. **AI 深度趨勢回測**：分析過往過千期開彩數據。")
    st.write("2. **個人幸運方位與時間導航**：結合五行與數字機率。")
    st.write("3. **智慧合買管理工具**：輕鬆與好友建立合買清單與自動分帳。")

# --- 3. 會員帳戶管理 ---
elif menu == "⚙️ 會員帳戶管理":
    st.subheader("⚙️ 帳戶與訂閱管理")
    st.write("如果您已經訂閱成為 VIP，您可以透過下方連結隨時管理您的訂閱、更新信用卡資料或隨時取消訂閱：")
    
    # 這裡可以放置 Stripe 官方的客戶入口網址 (Customer Portal)
    st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://dashboard.stripe.com/" target="_blank" style="color: #635bff; font-weight: bold; text-decoration: underline;">
                🔗 前往 Stripe 帳戶與訂閱管理中心
            </a>
        </div>
    """, unsafe_allow_html=True)

# 頁尾資訊
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>© 2026 AI Lotto Nav. All rights reserved. 僅供娛樂與數據參考，請理性投注。</p>", unsafe_allow_html=True)
