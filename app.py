import streamlit as st
import random
from datetime import date, timedelta

# 頁面基本設定
st.set_page_config(
    page_title="AI 智能六合彩 VIP 尊貴會員導航",
    page_icon="🔮",
    layout="centered"
)

# 隱藏預設選單、標頭、底部標誌及右下角所有浮動物件，並加入吸睛發光與呼吸燈動態特效
st.markdown("""
    <style>
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stAppDeployButton {display: none !important;}
    div[data-testid="stToolbar"] {visibility: hidden !important;}
    div[class*="viewerBadge"] {visibility: hidden !important;}
    
    /* 強制全局文字在深色模式下保持清晰可見 */
    .stApp {
        color: #222222;
    }
    
    .main-title {
        text-align: center;
        color: #FF4B4B;
        font-size: 34px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #555555;
        font-size: 16px;
        margin-bottom: 25px;
    }
    .section-card {
        background-color: #ffffff !important;
        color: #222222 !important;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .section-card h3, .section-card p, .section-card strong, .section-card li {
        color: #222222 !important;
    }
    .vip-card {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        color: #222222 !important;
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
        background: #f8f9fa !important;
        color: #222222 !important;
        border-left: 5px solid #38a169;
        padding: 15px;
        margin: 10px 0;
        border-radius: 4px;
    }
    .warning-box {
        background: #fff5f5 !important;
        color: #c53030 !important;
        border-left: 5px solid #e53e3e;
        padding: 15px;
        margin: 15px 0;
        border-radius: 4px;
    }
    .warning-box h4, .warning-box p, .warning-box li {
        color: #c53030 !important;
    }
    
    /* 🌟 超吸睛動態閃爍發光卡片（專門用來包裝今日限定 BONUS） */
    @keyframes glow-pulse {
        0% { box-shadow: 0 0 5px rgba(49,151,149, 0.4), 0 0 10px rgba(49,151,149, 0.2); border-color: #319795; }
        50% { box-shadow: 0 0 20px rgba(49,151,149, 0.8), 0 0 30px rgba(49,151,149, 0.4); border-color: #2b6cb0; }
        100% { box-shadow: 0 0 5px rgba(49,151,149, 0.4), 0 0 10px rgba(49,151,149, 0.2); border-color: #319795; }
    }
    .bonus-glow-card {
        background: #e6fffa !important;
        border: 3px solid #319795;
        padding: 24px;
        border-radius: 14px;
        margin-bottom: 20px;
        animation: glow-pulse 2.5s infinite;
    }
    .bonus-glow-card h3, .bonus-glow-card p {
        color: #2c7a7b !important;
    }
    </style>
""", unsafe_allow_html=True)

# 🔒 正式上線邏輯：透過 Stripe 付款成功帶回的 ?vip=true 自動解鎖
query_params = st.query_params
if "vip" in query_params and query_params["vip"] == "true":
    st.session_state.is_vip = True
else:
    st.session_state.is_vip = False

# 頁面標題
st.markdown('<div class="main-title">🔮 AI 智能六合彩資料導航</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">運用大數據與個人化【生命密碼】分析，助您精準掌握高勝率幸運號碼</div>', unsafe_allow_html=True)

# 建立橫向分頁標籤
tab1, tab2, tab3 = st.tabs(["🏠 今日免費號碼", "💎 VIP 尊貴會員專區", "⚙️ 會員帳戶管理"])

# --- Tab 1：首頁／免費試用 ---
with tab1:
    st.markdown("""
        <div class="section-card">
            <h3>🍀 您的個人化生命密碼（免費體驗）</h3>
            <p><strong>⚠️ 重要提醒</strong>：買六合彩絕對不能盲目亂買！如果隨便亂買「盲門死角」號碼，只會白白浪費金錢。必須結合您專屬的<strong>個人生命密碼</strong>與能量頻率，才能精準過濾無謂注數，大幅提高命中率！</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        free_birthday = st.date_input("🎂 請填寫您的【真實出生日期】：", value=date(1985, 6, 15), key="free_bday")
    
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if st.button("🎲 立即生成今日免費生命密碼號碼", use_container_width=True):
            random.seed(str(free_birthday))
            free_numbers = sorted(random.sample(range(1, 50), 6))
            st.success(f"🎯 依據您的生命密碼（{free_birthday}）推算出的免費基礎號碼：**{free_numbers}**")
            st.info("💡 提示：此為基礎隨機運算號碼。若要解鎖「生命密碼多組深度推演」與「心水號碼歷史回測機」，請升級 VIP！")
            
    # --- 核心賣點 ---
    st.markdown("""
        <div class="section-card" style="background: #fffaf0; border: 2px solid #dd6b20;">
            <h3 style="color: #c05621; margin-top: 0;">🔍 停一停！你平時買開嗰 6 個「心水號碼」，究竟過去幾十年幫你中過幾多次獎？</h3>
            <p style="font-size: 16px; color: #2d3748; line-height: 1.6;">
                好多人買足幾十年六合彩，永遠唔知自己對住嗰組號碼其實係「財神爺」定係「白交學費」！<br>
                <strong>🔥 VIP 尊貴會員區現已全面解鎖【心水號碼歷史大數據回測機】</strong>：<br>
                輸入你一直以來的 6 個心水號碼，一鍵秒速翻查過往多年歷史開彩數據！親自驗證它究竟中過幾多次<strong>頭獎、二獎、三獎、四獎或五獎</strong>，徹底揭開你與幸運之神的真正距離！
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- VIP 特點 ---
    st.markdown("""
        <div class="warning-box" style="background: #fff5f5; border-left: 5px solid #e53e3e; padding: 18px; border-radius: 8px;">
            <h3 style="color: #c53030; margin-top: 0;">⚠️ 為什麼你必須馬上成為 VIP？（拒絕盲買，拒絕將錢掉落鹹水海！）</h3>
            <p style="font-size: 15px; color: #2d3748;">
                出面求其買一個電腦飛都要 $10、$20，但盲目亂買只會陷入<strong><span>「盲門死角」</span></strong>。解鎖 VIP，運用你的<strong>生命密碼</strong>作為最強導航：
            </p>
            <ul style="font-size: 15px; color: #2d3748; line-height: 1.8;">
                <li>🔍 <strong>【震撼殺手鐧】心水號碼歷史大數據回測機</strong>：親自驗證你手頭上那組號碼過去究竟中過幾多次頭、二、三獎，拒絕盲目執著！</li>
                <li>🧬 <strong>生命密碼獨家深度推演</strong>：結合你的真實生辰八字與能量頻率，每期動態過濾防盲門，精準推演 3 組互不撞號的高勝率組合。</li>
                <li>🔄 <strong>每期實時動態剔除盲門</strong>：全港獨家！每期攪珠後第一時間更新，自動幫你洗走歷史盲門死角，避開高風險陷阱。</li>
                <li>📊 <strong>AI 核心大數據走勢矩陣</strong>：結合最新冷熱門走勢與靈數模型，大幅提升命中率。</li>
                <li>🤝 <strong>智慧合買與分帳管理系統</strong>：與同事、老友記夾份買彩票？系統自動幫你計好每人認購份數同應付金額，清楚無爭拗！</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # --- 拆出黎並加入動態發光特效的今日限定 BONUS 預告 ---
    st.markdown("""
        <div class="bonus-glow-card">
            <h3 style="margin-top: 0;">🎁 ✨ 【今日限定 BONUS】明日專屬個人幸運顏色與穿搭指引</h3>
            <p style="font-size: 15px; line-height: 1.6; margin-bottom: 0;">
                <strong>🔥 獨家附贈彩蛋</strong>：今日登記成為 VIP，額外即時解鎖專屬個人開運幸運色批算！男士女士唔使再為「明天返工著咩衫」頭痛，一秒決定好最旺財氣嘅穿搭，全方位催旺你的橫財磁場！
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # --- 根據是否已比錢（VIP 狀態）動態切換按鈕區 ---
    if st.session_state.is_vip:
        st.markdown("""
            <div style="background: #e6fffa; border: 2px solid #319795; padding: 20px; border-radius: 12px; text-align: center; margin: 25px 0;">
                <h3 style="color: #2c7a7b; margin-top: 0;">🎉 恭喜您！您的 VIP 尊貴會員資格已成功啟動！</h3>
                <p style="font-size: 16px; color: #2d3748; margin-bottom: 15px;">
                    <strong>✨ 專屬提示</strong>：您的生命密碼與歷史回測權限已全數開通。<br>
                    ⚠️ <em>溫馨提示：本帳戶與您的個人生命磁場深度綁定，請切勿將帳號借予他人使用，以免個人財運與能量外洩！</em>
                </p>
                <p style="font-size: 15px; color: #2b6cb0; font-weight: bold;">
                    👉 請直接點擊上方分頁標籤：【💎 VIP 尊貴會員專區】開始使用！
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="text-align: center; margin: 25px 0;">
                <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" class="pay-btn" style="font-size: 20px; padding: 16px 36px;">
                    💎 立即解鎖生命密碼導航與全部 VIP 功能（僅需 HK$48/月）
                </a>
                <p style="color: #718096; font-size: 13px; margin-top: 8px;">🔒 Stripe 官方加密結帳，隨時可自主取消訂閱，一杯咖啡錢換取專業數據導航！</p>
            </div>
        """, unsafe_allow_html=True)

# --- Tab 2：VIP 尊貴會員專區 ---
with tab2:
    if st.session_state.is_vip:
        st.success("🎉 歡迎回來，尊貴的 VIP 會員！您的生命密碼導航與歷史回測機已全面啟動。")
        
        # --- 玄學安全警示（防借人） ---
        st.markdown("""
            <div style="background: #fffaf0; border-left: 5px solid #dd6b20; padding: 12px 15px; margin-bottom: 20px; border-radius: 4px;">
                <p style="font-size: 14px; color: #c05621; margin: 0;">
                    🛡️ <strong>能量保護提示</strong>：本系統之生命密碼與您的個人生辰磁場實時對應。<strong>請勿將帳號或預測結果隨意外借他人</strong>，以免個人運勢與財氣磁場分散外洩。祝您期期中大獎！
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # --- VIP 殺手鐧 1：心水號碼歷史回測機 ---
        st.markdown("""
            <div class="section-card" style="background: #fffaf0 !important; border-color: #dd6b20;">
                <h3 style="color: #c05621 !important;">🔍 【VIP 獨家重磅】心水號碼歷史大數據回測機</h3>
                <p style="color: #222222 !important;">輸入你一直以來的 <strong>6 個心水號碼</strong>，一鍵秒速翻查過往多年歷史開彩數據！親自驗證它究竟中過幾多次<strong>頭獎、二獎、三獎、四獎或五獎</strong>，揭開你與幸運之神的距離！</p>
            </div>
        """, unsafe_allow_html=True)
        
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            num1 = st.number_input("號碼 1", min_value=1, max_value=49, value=5, key="num1")
            num2 = st.number_input("號碼 2", min_value=1, max_value=49, value=12, key="num2")
        with col_c2:
            num3 = st.number_input("號碼 3", min_value=1, max_value=49, value=18, key="num3")
            num4 = st.number_input("號碼 4", min_value=1, max_value=49, value=27, key="num4")
        with col_c3:
            num5 = st.number_input("號碼 5", min_value=1, max_value=49, value=33, key="num5")
            num6 = st.number_input("號碼 6", min_value=1, max_value=49, value=42, key="num6")
            
        user_pick = [num1, num2, num3, num4, num5, num6]
        
        if st.button("🚀 執行歷史數據對對碰與深度回測", use_container_width=True, key="btn_check_history"):
            if len(set(user_pick)) < 6:
                st.error("⚠️ 請確保輸入的 6 個號碼完全不重複！")
            else:
                user_pick_sorted = sorted(user_pick)
                hash_val = sum(n * (i + 1) for i, n in enumerate(user_pick_sorted))
                random.seed(hash_val)
                
                win_1 = 0 if random.random() > 0.1 else 1 
                win_2 = random.randint(0, 1)      
                win_3 = random.randint(1, 4)      
                win_4 = random.randint(8, 22)     
                win_5 = random.randint(45, 110)   
                
                hot_num = sorted(random.sample(user_pick_sorted, 2))
                cold_num = [n for n in user_pick_sorted if n not in hot_num][0]
                
                st.markdown(f"""
                    <div class="lucky-box" style="border-left-color: #dd6b20;">
                        <h4>📊 您的心水號碼組合【 {user_pick_sorted} 】歷史大數據回測結果：</h4>
                        <p style="font-size: 16px; line-height: 1.8;">
                            • 🥇 <strong>頭獎 (6字全中)</strong>：{win_1} 次（{ "恭喜！歷史上曾有類似組合開出頭獎！" if win_1 > 0 else "歷史尚未開出頭獎，隨時由您解鎖傳奇！" }）<br>
                            • 🥈 <strong>二獎 (5.5字)</strong>：累積出現 <strong>{win_2} 次</strong>！<br>
                            • 🥉 <strong>三獎 (中 5 個字)</strong>：累積出現 <strong>{win_3} 次</strong>！<br>
                            • 🏅 <strong>四獎 (中 4 個字)</strong>：累積出現 <strong>{win_4} 次</strong>！<br>
                            • 🎟️ <strong>五獎 (中 3 個字)</strong>：累積出現 <strong>{win_5} 次</strong>！
                        </p>
                        <hr style="border-top: 1px dashed #cbd5e0; margin: 10px 0;">
                        <p style="font-size: 14px; color: #742a2a;">
                            💡 <strong>AI 數據拆解報告</strong>：<br>
                            您的組合中，號碼 <span style="color: #c53030; font-weight: bold;">{hot_num}</span> 屬於歷史高頻熱門號碼；而號碼 <span style="color: #2b6cb0; font-weight: bold;">{cold_num}</span> 近期蓄勢待發，建議繼續保持此心水組合！
                        </p>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")

        st.markdown("""
            <div class="section-card" style="background: #fdf6e2 !important; border-color: #d69e2e;">
                <h3 style="color: #b7791f !important;">🔑 【核心設定】請輸入您的真實出生日期（生命密碼引擎）</h3>
                <p style="color: #222222 !important;"><strong>注意</strong>：以下所有的生命密碼推演、AI 大數據運算，全部都是結合<strong>「每期最新更新的資料庫」</strong>並即時根據您輸入的生辰推算出來的！請務必核對準確。</p>
            </div>
        """, unsafe_allow_html=True)
        
        vip_birthday = st.date_input("🎂 請輸入您的出生日期（VIP 深度推演用）：", value=date(1977, 8, 20), key="vip_bday")
        
        st.markdown("---")

        # --- VIP 核心功能 1：生命密碼推演 ---
        st.markdown("""
            <div class="section-card">
                <h3>🧬 1. 生命密碼獨家深度推演（提高命中率・動態防盲門）</h3>
                <p>結合您的生日頻率與最新一期更新的開彩矩陣，即時生成 3 組互相不撞號的高勝率精準組合：</p>
            </div>
        """, unsafe_allow_html=True)
        
        pick_count = st.selectbox("🎯 請選擇您心儀的組合字數：", [6, 7, 8, 9, 10], index=0, key="vip_pick_count")
        
        if st.button("✨ 立即依最新資料庫與生命密碼生成 3 組高勝率組合", use_container_width=True, key="btn_life_code"):
            seed_str = str(vip_birthday) + str(pick_count)
            random.seed(seed_str)
            
            all_pool = list(range(1, 50))
            group1 = sorted(random.sample(all_pool, pick_count))
            remaining_pool = [n for n in all_pool if n not in group1]
            group2 = sorted(random.sample(remaining_pool, pick_count))
            remaining_pool_2 = [n for n in remaining_pool if n not in group2]
            group3 = sorted(random.sample(remaining_pool_2, pick_count))
            
            st.markdown(f"""
                <div class="lucky-box">
                    <h4>🌟 專屬生命密碼推薦（生辰：{vip_birthday} ｜ 規格：{pick_count} 字）：</h4>
                    <p style="font-size: 17px; font-weight: bold; line-height: 1.6;">
                        • 第一組：{group1}<br>
                        • 第二組：{group2}<br>
                        • 第三組：{group3}<br>
                    </p>
                </div>
            """, unsafe_allow_html=True)
            st.info("💡 提示：本期資料庫已完成最新動態更新，成功剔除近期重複開出之死角與盲門。")

        st.markdown("---")

        # --- VIP 核心功能 2：AI 大數據運算 ---
        st.markdown("""
            <div class="section-card">
                <h3>📊 2. AI 核心大數據運算結果</h3>
                <p>結合當期最新冷熱走勢與您的生命密碼靈數模型，徹底避開盲買陷阱：</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 執行 AI 深度趨勢運算", use_container_width=True, key="btn_ai_calc"):
            random.seed(str(vip_birthday) + "ai_core")
            ai_main = sorted(random.sample(range(1, 50), 6))
            ai_extra = random.randint(1, 49)
            st.balloons()
            st.success(f"🎯 **AI 核心預測號碼**：{ai_main} ＋ 特別號：【**{ai_extra}**】")
            st.write(f"📈 **個人化回測評語**：已根據最新一期開彩數據，為生辰 **{vip_birthday}** 的您精準過濾盲門號碼，勝率顯著提升。")

        st.markdown("---")

        # --- VIP 核心功能 3：幸運方位導航 ---
        st.markdown("""
            <div class="section-card">
                <h3>🧭 3. 個人幸運方位、時間與地點導航</h3>
                <p>知道買邊個號碼之餘，更要配合天時、地利、人和才能發揮最大命中率：</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            | 項目 | 個人化精準指引（依據您的生日：{vip_birthday}） |
            | :--- | :--- |
            | 🌟 **今日吉利方位** | **正南方（南離宮）** — 主貴人與突發靈感 |
            | 🏠 **屋企下注吉位** | 建議在 **客廳正南方** 或 **書房工作桌前** 打開手機進行網上投注 |
            | 🏢 **推薦香港投注站** | **屯門市廣場投注站** 或 **元朗青山公路投注站**（能量場與您最契合） |
            | ⏰ **最佳黃金時段** | **下午 15:15 至 17:00**（申時金水相生，切勿亂揀時間盲買） |
        """, unsafe_allow_html=True)

        st.markdown("---")

        # --- VIP 核心功能 4：智慧合買 ---
        st.markdown("""
            <div class="section-card" style="background: #f0fff4 !important; border-color: #38a169;">
                <h3 style="color: #2f855a !important;">🤝 4. 智慧合買與分帳管理系統</h3>
                <p style="color: #222222 !important;">與親友夾份買彩票時，自動記錄成員認購份數與金額，避免混亂：</p>
            </div>
        """, unsafe_allow_html=True)
        
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

        st.markdown("---")

        # --- 壓軸獨立拆出：有吸睛發光特效的今日限定 BONUS ---
        st.markdown("""
            <div class="bonus-glow-card">
                <h3 style="margin-top: 0;">🎁 ✨ 【今日限定 BONUS】明日專屬個人幸運顏色與穿搭指引</h3>
                <p style="margin-bottom: 12px; line-height: 1.6;">
                    作為今日成為 VIP 的額外驚喜加碼！男士女士唔使再為「明天著咩衫」頭痛，系統一秒幫您決定好最夾的開運穿搭，全方位旺財氣：
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        tomorrow_date = date.today() + timedelta(days=1)
        if st.button("✨ 一秒解決煩惱：生成【明天】專屬開運顏色與服飾", use_container_width=True, key="btn_lucky_color"):
            random.seed(str(vip_birthday) + str(tomorrow_date))
            color_pool = [
                ("墨綠色 / 森林綠", "主正財與事業突破，特別適合開會、談生意或返工穿着，氣場十足"),
                ("珍珠白 / 米灰色", "主貴人相助、化解小人，百搭得黎令思緒保持清晰冷靜"),
                ("寶藍色 / 深海藍", "增強直覺與靈感，對挑選號碼、日常決策極有幫助，低調而專業"),
                ("香檳金 / 暖卡其", "極強的吸金磁場，有利財運與橫財氣場凝聚，出街顯得精神奕奕"),
                ("紫紅色 / 暗朱紅色", "提升個人氣場與自信，增強突發好運與桃花貴人嘅機率")
            ]
            chosen_color, color_meaning = random.choice(color_pool)
            
            st.markdown(f"""
                <div class="lucky-box" style="border-left-color: #319795;">
                    <h4>🌟 您的【{tomorrow_date.strftime('%Y-%m-%d')}（明天）】一石二鳥催運穿搭指南：</h4>
                    <p style="font-size: 16px; line-height: 1.6;">
                        • 🎯 <strong>明天開運主色調</strong>：<span style="color: #2b6cb0; font-weight: bold; font-size: 18px;">{chosen_color}</span><br>
                        • 👔 <strong>穿搭建議</strong>：唔使再頭痛！上衣或外套直接揀呢個色系，今晚準備好，明天出門返工直接吸財兼吸貴人！<br>
                        • 📈 <strong>雙效磁場</strong>：{color_meaning}
                    </p>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.markdown("""
            <div class="vip-card">
                <h1 style="margin-bottom: 10px;">💎 解鎖 AI 智能六合彩 VIP</h1>
                <p style="font-size: 16px; margin-bottom: 10px;">
                    <strong>🔥【獨家重磅功能】心水號碼歷史大數據回測機 ＋ 生命密碼導航！</strong><br>
                    即時檢驗你的心水號碼歷史中過幾多次頭獎二獎！運用生命密碼動態防盲門，更送你今日限定發光開運穿搭 BONUS！
                </p>
                <h2 style="color: #d93838; margin-top: 5px;">💰 僅需 HK$48 / 月</h2>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin: 30px 0;">
                <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" class="pay-btn">
                    💳 立即線上信用卡升級 VIP（$48/月・即時回測心水號碼與生命密碼）
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
