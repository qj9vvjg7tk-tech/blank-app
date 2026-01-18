import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الواجهة الرياضية والوضوح العالي
st.set_page_config(page_title="Zuhour Fitness 2026", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .block-container {padding-top: 1.5rem;}
    .stApp { background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%); }
    
    /* بطاقات بيضاء وخط أسود داكن جداً للوضوح */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 12px;
        border-right: 10px solid #FF8C00;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    h1, h2, h3, p, label, span, div { 
        color: #000000 !important; 
        font-weight: 900 !important;
    }

    .stButton > button {
        background-color: #FF8C00 !important; 
        color: #FFFFFF !important;
        border-radius: 12px;
        border: 2px solid #000000;
        font-weight: bold;
        height: 50px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ تطبيق زهور للرشاقة 2026")

# 2. عداد الماء
if 'water' not in st.session_state:
    st.session_state.water = 0

st.subheader("💧 عداد شرب الماء")
c1, c2 = st.columns([2, 1])
with c1: st.write(f"أكواب الماء: {st.session_state.water} / 12")
with c2: 
    if st.button("➕ إضافة كوب"): st.session_state.water += 1
st.progress(min(st.session_state.water / 12, 1.0))

st.divider()

# 3. ميزة ذكاء اصطناعي (ترشيح الفيديوهات)
st.subheader("📝 دمج خطة AI الخارجية")
ai_plan = st.text_area("ألصقي خطتكِ هنا لتحليلها:", placeholder="مثلاً: تمارين خصر وأرداف...")

if ai_plan:
    st.markdown("### 🤖 ترشيح المدرب:")
    if any(word in ai_plan.lower() for word in ["نحت", "بيلاتس", "خصر"]):
        url = "https://www.youtube.com/watch?v=NxX9p8W09I8"
        msg = "تم ترشيح فيديو بيلاتس لنحت الجسم."
    elif any(word in ai_plan.lower() for word in ["حرق", "كارديو", "وزن"]):
        url = "https://www.youtube.com/watch?v=2MoGxae-zyo"
        msg = "تم ترشيح فيديو كارديو مكثف."
    else:
        url = f"https://www.youtube.com/results?search_query={ai_plan}"
        msg = "سأبحث لكِ عن أفضل التمارين لخطتكِ."
    
    st.success(msg)
    st.link_button("▶️ ابدأ التمرين المرشح الآن", url)

st.divider()

# 4. جدول التمارين (Toggle)
show_plan = st.toggle("🏋️‍♀️ عرض جدول التمارين اليومي") 
if show_plan:
    day = st.selectbox("🎯 اختر اليوم:", ["السبت: خصر وبطن", "الاثنين: أرداف", "الأربعاء: شد كامل"])
    exercise_urls = {
        "السبت: خصر وبطن": "https://www.youtube.com/watch?v=cIuiQyfKBTg",
        "الاثنين: أرداف": "https://www.youtube.com/watch?v=hpyT2v04Bj0",
        "الأربعاء: شد كامل": "https://www.youtube.com/watch?v=Im3PXoLmyx8"
    }
    st.link_button("📺 فتح فيديو الجدول", exercise_urls[day])

st.divider()

# 5. القياسات والهدف
h = st.number_input("الطول (سم):", value=160)
w = st.number_input("الوزن الحالي (كجم):", value=60.0)
st.success("💡 استمري يا زهور للوصول لوزن 55 كجم!")

st.sidebar.info("زهور فيتنس 2026 • وضوح فائق وروابط نشطة")
