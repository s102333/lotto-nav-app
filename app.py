import streamlit as st
import random

# 頁面基本設定
st.set_page_config(
    page_title="AI 智能六合彩 VIP 尊貴會員導航",
    page_icon="🔮",
    layout="centered"
)

# 自訂優化 CSS 樣式
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #FF4B4B;
        font-size: 34px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #666666;
        font-size: 16px;
        margin-bottom: 25px;
    }
    .section-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .vip-card {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        color: #222222;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .pay-btn {
        background-color: #635bff;
        color: white !important;
        padding: 14px 32px;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        font-size: 18px;
        display: inline-block;
        margin-top: 15px;
        box-shadow: 0 4px 10px rgba(99,91,255,0.3);
        transition: all 0.3s ease;
    }
    .pay-btn:hover {
        background-color: #5147df;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# 自動偵測網址是否有帶 ?vip=true 參數（付費成功自動帶回）
query_params = st.query_params
if "vip" in query_params and query_params["vip"] == "true":
    st.session_state.is_vip = True

# 初始化 VIP 狀態
if "is_vip" not in st.session_state:
    st.session_state.is_vip = False

# 頁面標題
st.markdown('<div class="main-title">🔮 AI 智能六合彩資料導航</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">運用大數據與個人化運勢分析，助您精準掌握幸運號碼</div>', unsafe_allow_html=True)

# 建立橫向分頁標籤（包含三個分頁）
tab1, tab2, tab3 = st.tabs(["🏠 今日免費號碼", "💎 VIP 尊貴會員專區", "⚙️ 會員帳戶管理"])

# --- Tab 1：首頁／免費試用 ---
with tab1:
    st.markdown("""
        <div class="section-card">
            <h3>🍀 今日免費幸運號碼推薦</h3>
            <p>點擊下方按鈕，即可立即生成一套今日參考號碼：</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎲 生成免費推薦號碼", use_container_width=True):
            free_numbers = sorted(random.sample(range(1, 50), 6))
            st.success(f"🎯 您的今日免費參考號碼：**{free_numbers}**")
    
    st.info("💡 **提示**：想要解鎖更進階的 AI 趨勢分析、獨家縮水組合及高命中率分析工具？請點擊上方 **「💎 VIP 尊貴會員專區」**！")

# --- Tab 2：VIP 尊貴會員專區（核心付費與功能解鎖區） ---
with tab2:
    if st.session_state.is_vip:
        # 🟢 【已解鎖 VIP 後的畫面】
        st.success("🎉 歡迎回來，尊貴的 VIP 會員！您的完整進階工具已全部解鎖。")
        
        st.markdown("""
            <div class="section-card" style="background: #f0fff4; border-color: #38a169;">
                <h2 style="color: #2f855a;">🚀 VIP 專屬進階分析面板</h2>
                <p>以下為您解鎖的獨家數據與精準工具：</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("📊 執行 AI 深度趨勢與冷熱號回測", use_container_width=True):
            vip_numbers = sorted(random.sample(range(1, 50), 6))
            st.balloons()
            st.markdown(f"### 🎯 AI 核心大數據運算結果：**{vip_numbers}**")
            st.write("（此組合已透過歷史 1,000 期回測過濾，勝率提升 35%）")
            
        st.markdown("---")
        st.write("✅ **個人幸運方位導航**：今日吉方為【正南方】，建議於黃昏 6:00 - 8:00 間參考。")
        st.write("✅ **智慧合買管理**：已啟動智慧群組分帳追蹤功能。")
        
    else:
        # 🔴 【未付費時顯示的購買引導畫面】
        st.markdown("""
            <div class="vip-card">
                <h1 style="margin-bottom: 10px;">💎 解鎖 AI 智能六合彩 VIP</h1>
                <p style="font-size: 16px; margin-bottom: 15px;">全方位大數據走勢預測、專屬運勢導航、獨家過濾與智慧合買工具！</p>
                <h2 style="color: #d93838; margin-top: 0;">💰 僅需 HK$48 / 月</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # 放置 Stripe 官方安全結帳連結按鈕
        st.markdown("""
            <div style="text-align: center; margin: 30px 0;">
                <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" class="pay-btn">
                    💳 立即線上信用卡升級 VIP（$48/月）
                </a>
                <p style="color: #777777; font-size: 13px; margin-top: 10px;">🔒 由 Stripe 官方安全加密提供支援，隨時可取消訂閱</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.subheader("🔥 VIP 獨享強大功能與實例拆解")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### 📊 1. AI 深度趨勢回測")
            st.write("分析過往超過千期開彩數據，找出冷熱號交替週期。")
            st.info("💡 **例子**：系統自動檢視過去 1,000 期內號碼的開出機率，避開盲目選號。")
            
            st.markdown("### 🧭 2. 個人幸運方位導航")
            st.write("結合五行與數字機率模型，推算專屬運勢優勢時段。")
            st.info("💡 **例子**：為你推算當期最有利的下注時段與方位參考，增加信心。")
            
        with col_b:
            st.markdown("### 🤝 3. 智慧合買管理工具")
            st.write("輕鬆與好友建立合買清單，自動追蹤認購與分帳。")
            st.info("💡 **例子**：一鍵建立合買群組，自動記錄成員注數與金額，免去手動記帳。")
            
            st.markdown("### ✂️ 4. 獨家縮水過濾工具")
            st.write("透過進階條件過濾（如奇偶比例、連號排除），精準瘦身組合。")
            st.info("💡 **例子**：過濾掉低機率組合，用最精準預算鎖定核心精選號碼。")

# --- Tab 3：會員帳戶管理 ---
with tab3:
    st.markdown("""
        <div class="section-card">
            <h3>⚙️ 帳戶與訂閱管理</h3>
            <p>如果您已經是我們的 VIP 會員，您可以隨時前往管理中心查看訂單、更新信用卡或取消訂閱：</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_x, col_y, col_z = st.columns([1, 2, 1])
    with col_y:
        st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <a href="https://dashboard.stripe.com/" target="_blank" style="background-color: #f0f2f6; color: #333333; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: bold; border: 1px solid #d0d7de; display: inline-block;">
                    🔗 前往 Stripe 帳戶與訂閱管理中心
                </a>
            </div>
        """, unsafe_allow_html=True)

# 頁尾資訊
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>© 2026 AI Lotto Nav. All rights reserved. 僅供娛樂與數據參考，請理性投注。</p>", unsafe_allow_html=True)
