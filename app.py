# --- Tab 2：VIP 尊貴會員專區（內含詳細例子） ---
with tab2:
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
    
    # 採用 2 欄式圖文卡片排版，讓客戶看得更清楚
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
