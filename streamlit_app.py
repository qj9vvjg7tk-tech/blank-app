import streamlit as st
import random

# --- إعدادات الصفحة ---
st.set_page_config(page_title="مدرب روز الذكي 2026", page_icon="🧘‍♀️", layout="centered")

# --- CSS المطور للألوان والتأثيرات ---
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #FFF5F7 0%, #FFE4E1 100%); }
h1,h2,h3 { color:#D81B60 !important; text-align:center; font-family:'Arial'; }
.main-card {
    background-color: white; border-radius: 20px; padding: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-bottom: 5px solid #FF69B4; margin-bottom: 20px;
}
.stButton>button { 
    background: linear-gradient(90deg,#FF69B4,#FFB6C1)!important; color:white!important; border-radius:25px;
    font-weight:bold; width: 100%; transition: 0.3s;
}
</style>
""", unsafe_allow_html=True)

# --- صورة الفتاة الرياضية (GIF الرئيسي) ---
st.markdown("<center><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3ZSZjdD1z/L40pC6N0H4h0E/giphy.gif' width='220'></center>", unsafe_allow_html=True)

st.title("🌸 نظام روز للتشخيص الرياضي")

# --- القسم 1: التشخيص الذكي والترشيح ---
with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("🔍 تشخيص الحالة وترشيح الفيديو")
    c1, c2 = st.columns(2)
    with c1: h = st.number_input("الطول (سم):", value=160)
    with c2: w = st.number_input("الوزن الحالي (كجم):", value=65.0)
    
    bmi = w / ((h/100)**2)
    ideal_w = h - 105
    
    # محرك الذكاء الاصطناعي للترشيح
    if bmi > 25:
        status = "تحتاجين حرق دهون مكثف (Cardio)"
        suggested_video = "https://www.youtube.com/watch?v=2MoGxae-zyo" # Chloe Ting
        video_name = "تحدي كلو تينغ العالمي للحرق"
    else:
        status = "تحتاجين نحت وشد (Sculpting)"
        suggested_video = "https://www.youtube.com/watch?v=3Pr6n-nKnAA" # Emi Wong
        video_name = "تمرين إيمي ونغ لنحت الخصر"

    st.warning(f"🚩 تشخيص الـ AI: {status}")
    st.info(f"✨ فيديو مرشح خصيصاً لحالتكِ: {video_name}")
    st.link_button("▶️ ابدئي تمرين التشخيص الآن", suggested_video)
    st.markdown('</div>', unsafe_allow_html=True)

# --- القسم 2: جدول الأيام (اختياري) ---
st.divider()
with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("📅 جدول التمارين الأسبوعي")
    day = st.selectbox("اختر اليوم:", ["الأحد","الاثنين","الثلاثاء","الأربعاء","الخميس","الجمعة","السبت"])
    
    # روابط عالمية موثوقة (أجنبية وعربية)
    links = {
        "الأحد": "https://www.youtube.com/watch?v=ml6cT4AZdqI",
        "الاثنين": "https://www.youtube.com/watch?v=3Pr6n-nKnAA",
        "الثلاثاء": "https://www.youtube.com/watch?v=U4_lVjsOVBs",
        "الأربعاء": "https://www.youtube.com/watch?v=v2r0zYnFmxo",
        "الخميس": "https://www.youtube.com/watch?v=gC_L9qAHVJ8",
        "الجمعة": "https://www.youtube.com/watch?v=Eml2xnoLpYE",
        "السبت": "https://www.youtube.com/watch?v=2MoGxae-zyo"
    }
    st.link_button(f"فتح تمرين يوم {day}", links[day])
    st.markdown('</div>', unsafe_allow_html=True)

# --- القسم 3: الكاميرا والماء ---
st.divider()
with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("📸 سجل الوجبات (خلفية)")
    st.write("💡 لفتح الكاميرا الخلفية: اضغطي على زر التبديل 🔄 الذي سيظهر أعلى شاشة الكاميرا.")
    st.camera_input("التقطي صورة وجبتكِ")
    
    if 'water' not in st.session_state: st.session_state.water = 0
    st.subheader(f"🥤 الماء: {st.session_state.water} / 12")
    if st.button("💧 إضافة كوب"): st.session_state.water += 1
    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.markdown(f"### ملخص روز\nالوزن: {w}\nالهدف: {ideal_w}")
