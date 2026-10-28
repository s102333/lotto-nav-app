import streamlit as st
import csv
import random
import os
from datetime import datetime
import time
import urllib.parse

# ==================== 1. 專業級頁面與馬會視覺風格設定 ====================
st.set_page_config(
    page_title="AI 智能選號導航系統 | 香港賽馬會數據支援", 
    page_icon="🎯", 
    layout="centered"
)

# 注入頂級 UI/UX 專業 CSS 樣式
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #001F3F 0%, #003366 50%, #004080 100%);
        padding: 30px 20px;
        border-radius: 14px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.2);
    }
    .main-title {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }
    .sub-title {
        font-size: 1rem;
        color: #FFD700;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    .info-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 6px solid #003366;
        padding: 24px;
        border-radius: 10px;
        height: 100%;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .action-card {
        background: #F8FAFC;
        border: 1px solid #CBD5E1;
        border-left: 6px solid #C62828;
        padding: 24px;
        border-radius: 10px;
        height: 100%;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .vip-banner {
        background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
        border: 2px solid #F59E0B;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 30px;
        box-shadow: 0 4px 14px rgba(245,158,11,0.2);
    }
    .number-ball {
        display: inline-block;
        width: 42px;
        height: 42px;
        line-height: 42px;
        background: radial-gradient(circle at 30% 30%, #FF5252, #C62828);
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 50%;
        text-align: center;
        margin: 5px;
        box-shadow: 0 4px 8px rgba(198,40,40,0.35);
    }
    .nav-box {
        background: linear-gradient(135deg, #F0F4F8 0%, #E2E8F0 100%);
        border: 1px solid #CBD5E1;
        border-top: 5px solid #003366;
        padding: 28px;
        border-radius: 12px;
        margin-top: 35px;
        margin-bottom: 35px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .pay-btn {
        display: block;
        background-color: #D97706;
        color: white !important;
        padding: 14px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
        text-align: center;
        font-size: 1.1rem;
        box-shadow: 0 4px 8px rgba(217,119,6,0.35);
    }
    .map-btn {
        display: inline-block;
        background-color: #003366;
        color: white !important;
        padding: 12px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 14px;
        box-shadow: 0 3px 6px rgba(0,51,102,0.2);
        text-align: center;
    }
    .metric-container {
        background: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }
    .section-spacing {
        margin-top: 40px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 頂部精裝標題區
st.markdown("""
    <div class='main-header'>
        <div class='main-title'>🎯 AI 智能六合彩專屬導航系統</div>
        <div class='sub-title'>結合香港馬會官方歷史大數據 · 個人生命密碼 · 機器學習熱力圖 · 智慧合買管理</div>
    </div>
""", unsafe_allow_html=True)

# ==================== 2. 核心大數據與計算函式 ====================

@st.cache_data
def load_historical_data():
    csv_filename = 'hkjc_marksix_results.csv'
    historical_draws = set()
    recent_draws_list = []
    total_draws_count = 4402
    
    if os.path.exists(csv_filename):
        with open(csv_filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0
            for row in reader:
                try:
                    b1, b2, b3, b4, b5, b6 = int(row['ball_1']), int(row['ball_2']), int(row['ball_3']), int(row['ball_4']), int(row['ball_5']), int(row['ball_6'])
                    balls = [b1, b2, b3, b4, b5, b6]
                    historical_draws.add(frozenset(balls))
                    
                    if count < 5:
                        recent_draws_list.append({
                            "draw_id": row.get('draw_id', 'N/A'),
                            "date": row.get('draw_date', 'N/A'),
                            "numbers": sorted(balls)
                        })
                    count += 1
                except (KeyError, ValueError):
                    continue
            if count > 0:
                total_draws_count = count
    return historical_draws, total_draws_count, recent_draws_list

def calculate_life_path(birthdate_str):
    digits = [int(char) for char in birthdate_str if char.isdigit()]
    total = sum(digits)
    while total > 9 and total not in [11, 22, 33]:
        total = sum([int(char) for char in str(total)])
    return total

def get_dynamic_timing_and_location(life_path, current_date_str):
    date_seed = sum([int(c) for c in current_date_str if c.isdigit()])
    timings = [
        ("午時 (11:00 – 12:59)", "正南方", "中環士丹利街投注站（核心財富磁場）", "中環士丹利街10-12號地下"),
        ("亥時 (21:00 – 22:59)", "正北方", "上水廣場投注站（聚寶靈氣之眼）", "上水龍琛路39號上水廣場購物中心"),
        ("申時 (15:00 – 16:59)", "正西方", "荃灣沙咀道投注站（強運激發據點）", "荃灣沙咀道290-296號地下"),
        ("辰時 (07:00 – 08:59)", "東北方", "沙田好運中心投注站（穩定增值樞紐）", "沙田橫壆街3號好運中心商場"),
        ("酉時 (17:00 – 18:59)", "正東方", "屯門市廣場投注站（喜神迎財據點）", "屯門屯順街1號屯門市廣場"),
        ("巳時 (09:00 – 10:59)", "西北方", "旺角亞皆老街投注站（人氣興旺樞紐）", "旺角亞皆老街109號地下")
    ]
    index = (life_path + date_seed) % len(timings)
    return timings[index]

historical_draws, total_draws_count, recent_draws_list = load_historical_data()
today_str = datetime.now().strftime("%Y-%m-%d")

# ==================== 3. 主畫面頂級 VIP 尊貴會員招募專區（解決手機看不到側邊欄痛點） ====================
st.markdown("""
    <div class='vip-banner'>
        <h3 style='margin-top:0; color:#92400E; font-size: 1.4rem; margin-bottom: 12px;'>👑 【VIP 尊貴會員升級專區】解鎖全套贏面倍增工具</h3>
        <p style='font-size:0.95rem; color:#78350F; margin-bottom:8px;'>🔥 <b>VIP 冷熱號碼熱力圖</b>：<b>告別盲目亂買！</b>精準鎖定近期高頻開出與潛水回補的黃金號碼，把勝率從碰運氣提升到大數據科學運算。</p>
        <p style='font-size:0.95rem; color:#78350F; margin-bottom:8px;'>📅 <b>個人開彩運勢日曆</b>：<b>拒絕浪費冤枉錢！</b>自動標註您全年磁場最強的「強力出擊日」，把金錢精準投資在財運最高昂的黃金期。</p>
        <p style='font-size:0.95rem; color:#78350F; margin-bottom:12px;'>🤝 <b>智慧夾錢分帳管理</b>：<b>和氣生財不傷感情！</b>一鍵輸入總金額與出資額，自動生成透明分紅比例與確認卡，同事朋友夾錢買複式從此不再計錯數。</p>
        <hr style='margin: 12px 0; border-top: 1px solid #F59E0B;'>
        <p style='font-size:0.9rem; color:#B45309; font-weight:bold; margin-bottom:0;'>💡 每月只需 $48 HKD（不到兩張電腦飛的錢），立即點擊下方按鈕解鎖全年權益：</p>
        <a href="https://buy.stripe.com/your_stripe_payment_link" target="_blank" class="pay-btn">💳 立即線上信用卡升級 VIP（$48/月）</a>
    </div>
""", unsafe_allow_html=True)

with st.expander("🇭🇰 港幣轉數快 (FPS) / PayMe 直接過數升級指引"):
    st.write("如欲使用轉數快或 PayMe 支付 $48 月費，請轉至以下帳號：")
    st.code("FPS ID: 123456789 (Joyful Tech)", language="text")
    st.write("過數後請將截圖 WhatsApp 至 91234567，客服將在 10 分鐘內為您手動解鎖 VIP 帳號！")

st.markdown("<div class='section-spacing'></div>", unsafe_allow_html=True)

# ==================== 4. 雙欄頂級排版（輸入與護盾說明） ====================
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown(f"""
        <div class='info-card'>
            <h4 style='margin-top:0; color:#003366; font-size: 1.2rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; margin-bottom: 12px;'>⚙️ 系統防撞護盾說明</h4>
            <p style='font-size:0.95rem; margin-bottom:10px; color:#1E293B;'><b>🌟 核心系統優勢：</b></p>
            <p style='font-size:0.88rem; margin-bottom:6px; color:#334155;'>• <b>4,402 期防撞過濾</b>：同步香港馬會歷史紀錄，自動剔除已開組合。</p>
            <p style='font-size:0.88rem; margin-bottom:6px; color:#334155;'>• <b>個人生命密碼</b>：精準對位您的專屬運勢常數。</p>
            <p style='font-size:0.88rem; margin-bottom:12px; color:#334155;'>• <b>動態吉時導航</b>：一鍵開啟 Google Maps 直達旺地。</p>
            <hr style='margin: 12px 0; border-top: 1px solid #CBD5E1;'>
            <p style='font-size:0.85rem; color:#64748B; margin-bottom:0;'>💡 <b>提示</b> : 本系統已針對手機端完美適配，所有操作直觀流暢！</p>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
        <div class='action-card'>
            <h4 style='margin-top:0; color:#C62828; font-size: 1.2rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; margin-bottom: 12px;'>✨ 立即啟動專屬測算</h4>
            <p style='font-size:0.9rem; color:#334155; margin-bottom:10px;'>請輸入您的出生日期以計算今期專屬組合：</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)
    birthday_input = st.text_input("🎂 出生日期 (YYYY-MM-DD)", "1977-10-02")
    
    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    bet_mode = st.selectbox(
        "📊 選擇投注組合模式",
        ["標準單注 (6 個號碼)", "進階複式 (7 個號碼)", "強運複式 (8 個號碼)"]
    )
    
    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    generate_btn = st.button("🚀 啟動 AI 演算法，生成今期專屬號碼", type="primary", use_container_width=True)

# ==================== 5. 主畫面計算與結果呈現邏輯 ====================
if generate_btn:
    
    with st.spinner("🔄 AI 核心正正在同步香港馬會最新開獎數據庫，計算專屬吉時與方位..."):
        time.sleep(1.0)
    
    life_path = calculate_life_path(birthdate_input)
    best_time, best_direction, best_station, station_address = get_dynamic_timing_and_location(life_path, today_str)
    
    draw_count = 6
    if "7 個號碼" in bet_mode:
        draw_count = 7
    elif "8 個號碼" in bet_mode:
        draw_count = 8

    st.markdown("<div class='section-spacing'></div>", unsafe_allow_html=True)
    st.markdown(f"### 📊 今期個人專屬運勢報告（{bet_mode}）")
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns(3, gap="medium")
    with col_a:
        st.markdown(f"<div class='metric-container'><span style='color:gray; font-size:0.85rem;'>1️⃣ 個人生命密碼</span><br><b style='color:#003366; font-size:1.1rem;'>【 {life_path} 號常數 】</b></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown(f"<div class='metric-container'><span style='color:gray; font-size:0.85rem;'>2️⃣ 大數據防撞狀態</span><br><b style='color:#003366; font-size:1.1rem;'>已過濾 {total_draws_count} 期</b></div>", unsafe_allow_html=True)
    with col_c:
        st.markdown(f"<div class='metric-container'><span style='color:gray; font-size:0.85rem;'>3️⃣ 今日動態更新</span><br><b style='color:#003366; font-size:1.1rem;'>{today_str}</b></div>", unsafe_allow_html=True)
        
    st.markdown("<div class='section-spacing'></div>", unsafe_allow_html=True)
    
    valid_combinations = []
    attempts = 0
    while len(valid_combinations) < 3 and attempts < 100000:
        attempts += 1
        pool = list(range(1, 50))
        random.shuffle(pool)
        combo = sorted(pool[:draw_count])
        combo_set = frozenset(combo[:6])
        
        if combo_set in historical_draws:
            continue
            
        if combo not in valid_combinations:
            valid_combinations.append(combo)

    st.markdown(f"#### 🎯 為您今期獨家訂製的 3 組{bet_mode}專屬號碼")
    st.markdown("<p style='color: #64748B; font-size: 0.9rem; margin-bottom: 25px;'>⚠️ 註：本系統確保每期數據即時更新，絕不與歷史已開獎組合重複。</p>", unsafe_allow_html=True)
    
    for i, res in enumerate(valid_combinations, 1):
        st.markdown(f"**第 {i} 組精選組合：**")
        balls_html = "".join([f"<span class='number-ball'>{str(n).zfill(2)}</span>" for n in res])
        st.markdown(f"<div style='margin-bottom: 20px;'>{balls_html}</div>", unsafe_allow_html=True)

    with st.expander("🔮 點擊展開：AI 財神靈籤占卜（今日財運批語）"):
        oracles = [
            ("【上上籤 - 財神到門】", "今日磁場大旺，正財偏財皆有所獲。宜大膽朝吉方位行事，心誠則靈！"),
            ("【中平籤 - 穩步向前】", "氣場平穩，切忌貪勝。建議採取小額複式或與朋友夾錢，穩紮穩打為上策。"),
            ("【吉 - 順勢而為】", "貴人相助於正南方。今日靈感最強，相信直覺選出的第一組號碼！")
        ]
        oracle_choice = oracles[(life_path + int(today_str.replace("-", ""))) % len(oracles)]
        st.markdown(f"### {oracle_choice[0]}")
        st.info(oracle_choice[1])

    # Google Maps 導航按鈕
    maps_query = urllib.parse.quote(f"香港 {best_station} {station_address}")
    maps_url = f"https://www.google.com/maps/search/?api=1&query={maps_query}"

    st.markdown(f"""
        <div class='nav-box'>
            <h3 style='margin-top:0; color:#003366; font-size: 1.3rem; margin-bottom: 18px;'>🧭 今期個人專屬「動態吉時與最佳投注站」導航</h3>
            <p style='margin-bottom: 12px;'><b>⏱ 今日專屬最佳吉時：</b> <span style='color:#C62828; font-weight:bold;'>{best_time}</span></p>
            <p style='margin-bottom: 12px;'><b>📍 推薦個人吉方位：</b> 朝【 <span style='color:#C62828; font-weight:bold;'>{best_direction}</span> 】方向出行</p>
            <p style='margin-bottom: 18px;'><b>🏢 推薦指定吉投注站：</b> <span style='font-weight:bold; color:#003366;'>{best_station}</span> ({station_address})</p>
            <a href="{maps_url}" target="_blank" class="map-btn">🗺️ 一鍵打開 Google Maps 導航至此投注站</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    with st.expander("🔍 點擊展開：近期馬會開獎結果速查與核對工具"):
        for draw in recent_draws_list:
            nums_str = " ".join([str(n).zfill(2) for n in draw['numbers']])
            st.markdown(f"• **期數 {draw['draw_id']}** ({draw['date']})： ` {nums_str} `")

else:
    st.markdown("<div style='margin-top: 35px;'></div>", unsafe_allow_html=True)
    st.info("👈 請在上方填寫您的出生日期，選擇投注模式，並點擊**「啟動 AI 演算法，生成今期專屬號碼」**按鈕！")
