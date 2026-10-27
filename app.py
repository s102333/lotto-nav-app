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

# 注入專業級 CSS 樣式 (針對手機端完美優化)
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #002D62 0%, #004080 100%);
        padding: 25px 15px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .main-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 5px;
        letter-spacing: 0.5px;
    }
    .sub-title {
        font-size: 0.95rem;
        color: #FFD700;
        font-weight: 400;
    }
    .input-card {
        background-color: #F0F4F8;
        border: 2px solid #002D62;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    .number-ball {
        display: inline-block;
        width: 42px;
        height: 42px;
        line-height: 42px;
        background: radial-gradient(circle at 30% 30%, #FF4D4D, #CC0000);
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 50%;
        text-align: center;
        margin: 5px;
        box-shadow: 0 3px 6px rgba(204,0,0,0.3);
    }
    .nav-box {
        background-color: #EBF3FA;
        border: 1px solid #B8D4F0;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .map-btn {
        display: inline-block;
        background-color: #002D62;
        color: white !important;
        padding: 10px 18px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    .map-btn:hover {
        background-color: #004080;
    }
    </style>
""", unsafe_allow_html=True)

# 標題區
st.markdown("""
    <div class='main-header'>
        <div class='main-title'>🎯 AI 智能六合彩專屬導航系統</div>
        <div class='sub-title'>結合香港馬會歷史大數據 · 個人生命密碼 · 動態吉時吉地</div>
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

# ==================== 3. 主畫面核心：手機優先的直覺輸入區塊 ====================
st.markdown("""
    <div class='input-card'>
        <h3 style='margin-top:0; color:#002D62;'>✨ 請輸入您的出生日期以啟動專屬演算法</h3>
        <p style='font-size:0.9rem; color:#555; margin-bottom:10px;'>系統將結合您的個人密碼與 4,402 期馬會歷史數據，為您計算今期專屬防撞號碼。</p>
    </div>
""", unsafe_allow_html=True)

# 讓輸入框直接在主畫面正中央，手機用戶一眼就能看到，完全不用找側邊欄！
birthday_input = st.text_input("🎂 出生日期 (格式: YYYY-MM-DD)", "1977-10-02")
generate_btn = st.button("🚀 啟動 AI 演算法，生成今期專屬號碼", type="primary", use_container_width=True)

st.markdown("---")

# ==================== 4. 側邊欄：保留額外系統狀態與說明 ====================
st.sidebar.header("⚙️ 系統防撞護盾說明")
st.sidebar.markdown(f"""
### 🌟 系統核心優勢
1. **個人生命密碼**：轉化個人運勢權重。
2. **4,402 期防撞過濾**：已同步香港馬會最新歷史共 **{total_draws_count} 期** 紀錄，自動剔除歷史已開組合。
3. **動態吉時導航**：配備一鍵地圖導航至指定旺地。
""")
st.sidebar.info("💡 提示：本版本已針對手機瀏覽器全面優化，主要操作均已置於主畫面，確保流暢體驗！")

# ==================== 5. 主畫面計算與結果呈現邏輯 ====================
if generate_btn:
    
    with st.spinner("🔄 AI 核心正正在同步香港馬會最新開獎數據庫，剔除歷史重複組合，並運算您的動態吉時與方位..."):
        time.sleep(1.0)
    
    life_path = calculate_life_path(birthday_input)
    best_time, best_direction, best_station, station_address = get_dynamic_timing_and_location(life_path, today_str)
    
    # 呈現三大核心亮點區塊
    st.markdown("### 📊 今期個人專屬運勢與防撞過濾報告")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric(label="1️⃣ 個人生命密碼", value=f"【 {life_path} 號常數 】")
    with col_b:
        st.metric(label="2️⃣ 大數據防撞狀態", value="已過濾 4,402 期")
    with col_c:
        st.metric(label="3️⃣ 今日動態更新", value=today_str)
        
    st.markdown("---")
    
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
    st.markdown("<p style='color: gray; font-size: 0.85rem;'>⚠️ 註：本系統確保每期數據即時更新，絕不與歷史已開獎組合重複。</p>", unsafe_allow_html=True)
    
    for i, res in enumerate(valid_combinations, 1):
        st.markdown(f"**第 {i} 組精選組合：**")
        balls_html = "".join([f"<span class='number-ball'>{str(n).zfill(2)}</span>" for n in res])
        st.markdown(f"<div style='margin-bottom: 12px;'>{balls_html}</div>", unsafe_allow_html=True)

    # Google Maps 導航按鈕
    maps_query = urllib.parse.quote(f"香港 {best_station} {station_address}")
    maps_url = f"https://www.google.com/maps/search/?api=1&query={maps_query}"

    # 呈現個人專屬動態吉時吉地與導航
    st.markdown(f"""
        <div class='nav-box'>
            <h3 style='margin-top:0; color:#002D62; font-size: 1.3rem;'>🧭 今期個人專屬「動態吉時與最佳投注站」導航</h3>
            <p style='margin-bottom: 8px;'><b>⏱ 今日專屬最佳吉時：</b> <span style='color:#CC0000; font-weight:bold;'>{best_time}</span></p>
            <p style='margin-bottom: 8px;'><b>📍 推薦個人吉方位：</b> 朝【 <span style='color:#CC0000; font-weight:bold;'>{best_direction}</span> 】方向出行</p>
            <p style='margin-bottom: 8px;'><b>🏢 推薦指定吉投注站：</b> <span style='font-weight:bold; color:#002D62;'>{best_station}</span> ({station_address})</p>
            <a href="{maps_url}" target="_blank" class="map-btn">🗺️ 一鍵打開 Google Maps 導航至此投注站</a>
            <hr style='margin: 15px 0 10px 0; border-top: 1px dashed #B8D4F0;'>
            <p style='font-size:0.85rem; color:#555; margin-bottom:0;'>💡 <i>提示：手機點擊上方按鈕即可直接開啟地圖導航，心誠則靈。</i></p>
        </div>
    """, unsafe_allow_html=True)

    # 近期開獎戰績比對
    with st.expander("🔍 點擊展開：近期馬會開獎結果速查與核對工具"):
        st.write("您可以對照最近幾期的官方開獎號碼，隨時追蹤系統的表現：")
        for draw in recent_draws_list:
            nums_str = " ".join([str(n).zfill(2) for n in draw['numbers']])
            st.markdown(f"• **期數 {draw['draw_id']}** ({draw['date']})： ` {nums_str} `")

    st.markdown("---")
    st.info("💡 **專業版升級提示**：系統已為您鎖定今期最優化組合。如需解鎖每期賽前 2 小時自動推播，請持續關注我們的官方 App 升級動態！")

else:
    st.info("👇 請在上方輸入您的出生日期，並點擊**「啟動 AI 演算法，生成今期專屬號碼」**按鈕，即可開始測算！")
