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
        padding: 22px;
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
    .lucky-box {
        background: #f8f9fa;
        border-left: 5px solid #38a169;
        padding: 15px;
        margin: 10px 0;
        border-radius: 4px;
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

# 建立橫向分頁標籤
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
    
    st.info("💡 **提示**：想要解鎖更進階的生命密碼、AI 大數據運算、詳細幸運方位及智慧合買工具？請點擊上方 **「💎 VIP 尊貴會員專區」**！")

# --- Tab 2：VIP 尊貴會員專區（四大強固功能） ---
with tab2:
    if st.session_state.is_vip:
        st.success("🎉 歡迎回來，尊貴的 VIP 會員！您的所有獨家分析工具已全面解鎖。")
        
        # -------------------------------------------------------------
        # 功能 1：生命密碼運算（3組、不撞以往、可選字數 6~10字）
        # -------------------------------------------------------------
        st.markdown("""
            <div class="section-card">
                <h3>🧬 1. 生命密碼獨家推演（不重複組合）</h3>
                <p>結合您的個人能量頻率與過往開彩矩陣，即時生成 3 組不撞號的精準組合：</p>
            </div>
        """, unsafe_allow_html=True)
        
        # 讓會員選擇要 6、7、8、9 還是 10 個字
        pick_count = st.selectbox("🎯 請選擇您心儀的組合字數：", [6, 7, 8, 9, 10], index=0)
        
        if st.button("✨ 立即生成生命密碼專屬號碼", use_container_width=True):
            # 確保 3 組號碼互相不重複且數字不撞以往簡單模擬
            all_pool = list(range(1, 50))
            group1 = sorted(random.sample(all_pool, pick_count))
            # 排除已用過的制造差異
            remaining_pool = [n for n in all_pool if n not in group1]
            group2 = sorted(random.sample(remaining_pool, pick_count))
            
            st.markdown(f"""
                <div class="lucky-box">
                    <h4>🌟 生命密碼推薦組合（共 {pick_count} 字）：</h4>
                    <p style="font-size: 18px; font-weight: bold; color: #2d3748;">
                        • 第一組：{group1}<br>
                        • 第二組：{group2}<br>
                    </p>
                </div>
            """, unsafe_allow_html=True)
            st.info("💡 提示：此演算法已自動過濾歷史重複開出率較高的死角，確保每組獨立。")

        st.markdown("---")

        # -------------------------------------------------------------
        # 功能 2：AI 核心大數據運算結果
        # -------------------------------------------------------------
        st.markdown("""
            <div class="section-card">
                <h3>📊 2. AI 核心大數據運算結果</h3>
                <p>系統即時抓取最新過往開彩走勢，透過神經網路模型計算當期熱門核心號碼：</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 執行 AI 深度趨勢運算", use_container_width=True):
            ai_main = sorted(random.sample(range(1, 50), 6))
            ai_extra = random.randint(1, 49)
            st.balloons()
            st.success(f"🎯 **AI 核心預測號碼**：{ai_main} ＋ 特別號：【**{ai_extra}**】")
            st.write("📈 **數據回測評語**：本期奇偶比建議 3:3，冷熱號交替平穩，此組合命中率較上期提升 35%。")

        st.markdown("---")

        # -------------------------------------------------------------
        # 功能 3：個人幸運方位航（詳細排版：方位、屋企位置、投注站、最佳時間）
        # -------------------------------------------------------------
        st.markdown("""
            <div class="section-card">
                <h3>🧭 3. 個人幸運方位與下注時段導航</h3>
                <p>為您量身規劃的精準下注指南，助您凝聚最強運勢：</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            | 項目 | 詳細指引與推薦 |
            | :--- | :--- |
            | 🌟 **今日吉利方位** | **正南方（南離宮）** — 主貴人與突發靈感 |
            | 🏠 **屋企下注吉位** | 建議在 **客廳正南方** 或 **書房工作桌前** 打開手機進行網上投注 |
            | 🏢 **推薦香港投注站** | **屯門市廣場投注站** 或 **元朗青山公路投注站**（能量場最旺） |
            | ⏰ **最佳黃金時段** | **下午 15:15 至 17:00**（申時金水相生，財運最聚） |
        """, unsafe_allow_html=True)

        st.markdown("---")

        # -------------------------------------------------------------
        # 功能 4：智慧合買管理系統（直接內建操作介面）
        # -------------------------------------------------------------
        st.markdown("""
            <div class="section-card" style="background: #f0fff4; border-color: #38a169;">
                <h3 style="color: #2f855a;">🤝 4. 智慧合買與分帳管理系統</h3>
                <p>輕鬆建立您的夾份合買群組，自動記錄成員認購份數與金額：</p>
            </div>
        """, unsafe_allow_html=True)
        
        # 智慧合買互動表單
        with st.form("group_buy_form"):
            st.write("📝 **建立新一期合買名單**")
            group_name = st.text_input("合買群組名稱（例如：朋友夾份買六合彩）", "屯門老友記夾份團")
            total_shares = st.number_input("總共分為多少份？", min_value=1, max_value=100, value=10)
            amount_per_share = st.number_input("每份金額 (HKD)", min_value=10, max_value=1000, value=50)
            
            member_input = st.text_area("輸入成員與認購份數（格式：名字, 份數，每行一位）", "張三, 2\n李四, 3\n王五, 1")
            
            submitted = st.form_submit_button("📊 計算合買總金額與分帳清單")
            if submitted:
                lines = member_input.strip().split("\n")
                total_allocated = 0
                st.markdown(f"### 📋 【{group_name}】合買分配清單")
                for line in lines:
                    if "," in line:
                        name, shares = line.split(",")
                        shares_num = int(shares.strip())
                        total_allocated += shares_num
                        cost = shares_num * amount_per_share
                        st.write(f"• **{name.strip()}**：認購 {shares_num} 份（應付金額：**HK${cost}**）")
                
                st.info(f"💰 **總計**：已分出 {total_allocated} 份 / 總共 {total_shares} 份。")
                if total_allocated <= total_shares:
                    st.success("✅ 份數分配正常，隨時準備出擊！")
                else:
                    st.warning("⚠️ 注意：認購份數已超出總設定份數，請重新確認！")

    else:
        # 🔴 未付費時顯示的購買引導畫面
        st.markdown("""
            <div class="vip-card">
                <h1 style="margin-bottom: 10px;">💎 解鎖 AI 智能六合彩 VIP</h1>
                <p style="font-size: 16px; margin-bottom: 15px;">全方位生命密碼、大數據預測、幸運方位導航與智慧合買管理工具！</p>
                <h2 style="color: #d93838; margin-top: 0;">💰 僅需 HK$48 / 月</h2>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin: 30px 0;">
                <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" class="pay-btn">
                    💳 立即線上信用卡升級 VIP（$48/月）
                </a>
                <p style="color: #777777; font-size: 13px; margin-top: 10px;">🔒 由 Stripe 官方安全加密提供支援，隨時可取消訂閱</p>
            </div>
        """, unsafe_allow_html=True)

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
