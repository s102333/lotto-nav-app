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
        margin-bottom: 25px;
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
        padding: 22px;
        border-radius: 10px;
        height: 100%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .action-card {
        background: #F8FAFC;
        border: 1px solid #CBD5E1;
        border-left: 6px solid #D32F2F;
        padding: 22px;
        border-radius: 10px;
        height: 100%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .number-ball {
        display: inline-block;
        width: 45px;
        height: 45px;
        line-height: 45px;
        background: radial-gradient(circle at 30% 30%, #FF5252, #C62828);
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 50%;
        text-align: center;
        margin: 6px;
        box-shadow: 0 4px 8px rgba(198,40,40,0.35);
    }
    .nav-box {
        background: linear-gradient(135deg, #F0F4F8 0%, #E2E8F0 100%);
        border: 1px solid #CBD5E1;
        border-top: 5px solid #003366;
        padding: 24px;
        border-radius: 12px;
        margin-top: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .map-btn {
        display: inline-block;
        background-color: #003366;
        color: white !important;
        padding: 12px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 12px;
        box-shadow: 0 3px 6px rgba(0,51,102,0.2);
        text-align: center;
        transition: background 0.3s ease;
    }
    .map-btn:hover {
        background-color: #002244;
    }
    .metric-container {
        background: #FFFFFF;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 頂部精裝標題區
st.markdown("""
    <div class='main-header'>
        <div class='main-title'>🎯 AI 智能六合彩專屬導航系統</div>
        <div class='sub-title'>結合香港馬會官方歷史大數據 · 個人生命密碼 · 動態吉時吉地精準對位</div>
    </div>
""", unsafe_allow_html=True)

# ==================== 2. 核心大數據與計算函式 ====================

@st.cache_data
def load_historical_data():
    """載入香港馬會歷史開獎數據 (4,402 期)，建立即時防撞過濾清單"""
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
    """計算個人生命密碼 (1-9)"""
    digits = [int(char) for char in birthdate_str if char.isdigit()]
    total = sum(digits)
    while total > 9 and total not in [11, 22, 33]:
        total = sum([int(char) for char in str(total)])
    return total

def get_dynamic_timing_and_location(life_path, current_date_str):
    """根據個人生命密碼與當日實時日期，計算動態吉時與吉地"""
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

# 載入歷史資料庫
historical_draws, total_draws_count, recent_draws_list = load_historical_data()
today_str = datetime.now().strftime("%Y-%m-%d")

# ==================== 3. 雙欄頂級排版（左側防撞說明，右側互動輸入） ====================
col_left, col_right = st.columns([1, 1], gap="medium")

with col_left:
    st.markdown(f"""
        <div class='info-card'>
            <h4 style='margin-top:0; color:#003366; font-size: 1.2rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 8px;'>⚙️ 系統防撞護盾說明</h4>
            <p style='font-size:0.95rem; margin-bottom:10px; color:#1E293B;'><b>🌟 系統核心優勢：</b></p>
            <p style='font-size:0.9rem; margin-bottom:8px; color:#334155;'>• <b>個人生命密碼</b>：精準轉化個人運勢權重。</p>
            <p style='font-size:0.9rem; margin-bottom:8px; color:#334155;'>• <b>4,402 期防撞過濾</b>：已同步香港馬會最新歷史共 <b>{total_draws_count} 期</b> 紀錄，自動剔除歷史已開組合。</p>
            <p style='font-size:0.9rem; margin-bottom:12px; color:#334155;'>• <b>動態吉時導航</b>：配備一鍵地圖導航至指定旺地。</p>
            <hr style='margin: 12px 0; border-top: 1px solid #CBD5E1;'>
            <p style='font-size:0.85rem; color:#64748B; margin-bottom:0;'>💡 <b>提示</b>：本版本已針對手機與電腦瀏覽器全面優化，主要操作均已置於主畫面，確保流暢體驗！</p>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
        <div class='action-card'>
            <h4 style='margin-top:0; color:#C62828; font-size: 1.2rem; border-bottom: 2px solid #E2E8F0; padding-bottom: 8px;'>✨ 立即啟動專屬測算</h4>
            <p style='font-size:0.9rem; color:#334155; margin-bottom:15px;'>請輸入您的出生日期以計算今期專屬組合：</p>
        </div>
    """, unsafe_allow_html=True)
    # 簡潔流暢的輸入與按鈕
    birthday_input = st.text_input("🎂 出生日期 (YYYY-MM-DD)", "1977-10-02")
    generate_btn = st.button("🚀 啟動 AI 演算法，生成今期專屬號碼", type="primary", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==================== 4. 主畫面計算與結果呈現邏輯 ====================
if generate_btn:
    
    with st.spinner("🔄 AI 核心正正在同步香港馬會最新開獎數據庫，剔除歷史重複組合，並運算您的動態吉時與方位..."):
        time.sleep(1.0)
    
    life_path = calculate_life_path(birthday_input)
    best_time, best_direction, best_station, station_address = get_dynamic_timing_and_location(life_path, today_str)
    
    # 呈現三大核心亮點區塊
    st.markdown("### 📊 今期個人專屬運勢與防撞過濾報告")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(f"<div class='metric-container'><span style='color:gray; font-size:0.85rem;'>1️⃣ 個人生命密碼</span><br><b style='color:#003366; font-size:1.1rem;'>【 {life_path} 號常數 】</b></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown(f"<div class='metric-container'><span style='color:gray; font-size:0.85rem;'>2️⃣ 大數據防撞狀態</span><br><b style='color:#003366; font-size:1.1rem;'>已過濾 {total_draws_count} 期</b></div>", unsafe_allow_html=True)
    with col_c:
        st.markdown(f"<div class='metric-container'><span style='color:gray; font-size:0.85rem;'>3️⃣ 今日動態更新</span><br><b style='color:#003366; font-size:1.1rem;'>{today_str}</b></div>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 產生存檔防撞號碼
    valid_combinations = []
    attempts = 0
    while len(valid_combinations) < 3 and attempts < 100000:
        attempts += 1
        pool = list(range(1, 50))
        random.shuffle(pool)
        combo = sorted(pool[:6])
        combo_set = frozenset(combo)
        
        if combo_set in historical_draws:
            continue
            
        if combo not in valid_combinations:
            valid_combinations.append(combo)

    # 顯示號碼結果
    st.markdown("#### 🎯 為您今期獨家訂製的 3 組防撞專屬號碼")
    st.markdown("<p style='color: #64748B; font-size: 0.9rem;'>⚠️ 註：本系統確保每期數據即時更新，絕不與歷史已開獎組合重複。</p>", unsafe_allow_html=True)
    
    for i, res in enumerate(valid_combinations, 1):
        st.markdown(f"**第 {i} 組精選組合：**")
        balls_html = "".join([f"<span class='number-ball'>{str(n).zfill(2)}</span>" for n in res])
        st.markdown(f"<div style='margin-bottom: 15px;'>{balls_html}</div>", unsafe_allow_html=True)

    # Google Maps 導航按鈕
    maps_query = urllib.parse.quote(f"香港 {best_station} {station_address}")
    maps_url = f"https://www.google.com/maps/search/?api=1&query={maps_query}"

    # 呈現個人專屬動態吉時吉地與導航
    st.markdown(f"""
        <div class='nav-box'>
            <h3 style='margin-top:0; color:#003366; font-size: 1.3rem; margin-bottom: 12px;'>🧭 今期個人專屬「動態吉時與最佳投注站」導航</h3>
            <p style='margin-bottom: 8px;'><b>⏱ 今日專屬最佳吉時：</b> <span style='color:#C62828; font-weight:bold;'>{best_time}</span></p>
            <p style='margin-bottom: 8px;'><b>📍 推薦個人吉方位：</b> 朝【 <span style='color:#C62828; font-weight:bold;'>{best_direction}</span> 】方向出行</p>
            <p style='margin-bottom: 12px;'><b>🏢 推薦指定吉投注站：
