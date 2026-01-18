import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الهوية الرياضية والوضوح (حل مشكلة الفراغات والخطوط)
st.set_page_config(page_title="Rose Fitness Master", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%); }
    div[data-testid="stVerticalBlock"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 20px;
        padding: 20px;
        border-right: 8px solid #FF8C00;
    }
    h1, h2, h3, p, label, span { 
        color: #001D3D !important; 
        font-weight: 800 !important;
    }
    .stButton > button {
        background-color: #FF8C00 !important; 
        color: #FFFFFF !important;
        font-weight: bold;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Rose Smart Fitness 2026")

# 2. ميزة مزامنة خطة الذكاء الاصطناعي (مع إصلاح الروابط)
st.subheader("📝 خطة التمارين والمزامنة الذكية")
ai_plan = st.text_area("ألصقي خطتكِ هنا ليتم تحليلها وترشيح الفيديو المناسب:", 
                       placeholder="مثال: خطة لنحت الخصر...")

# هذا الجزء يضمن تغيير الفيديو بناءً على الكلمات الموجودة في خطتكِ
if ai_plan:
    st.markdown("### 🤖 نتيجة تحليل المدرب لخطتكِ:")
    
    # تحديد الرابط بناءً على المحتوى
    if any(word in ai_plan for word in ["نحت", "بيلاتس", "نيكول"]):
        target_video = "https://www.youtube.com/watch?v=NxX9p8W09I8"
        advice_msg = "خطة نحت رائعة! الأنسب لكِ هو تمارين بيلاتس نيكول."
    elif any(word in ai_plan for word in ["حرق", "كارديو", "دهون"]):
        target_video = "https://www.youtube.com/watch?v=2MoGxae-zyo"
        advice_msg = "هدفكِ الحرق؛ أرشح لكِ تمارين كلو تينج المكثفة."
    else:
        target_video = "https://www.youtube.com/watch?v=Im3PXoLmyx8"
        advice_msg = "خطة شاملة! إليكِ هذا التمرين المتكامل لشد الجسم."

    st.info(advice_msg)
    # الزر الآن مربوط بمتغير target_video الذي يتغير بتغير النص
    st.link_button("▶️ فتح فيديو التمرين المرشح الآن", target_video)

st.divider()

# 3. عرض جدول التمارين الأسبوعي (اختياري)
show_exercises = st.toggle("🏋️‍♀️ عرض جدول التمارين الأسبوعي الخاص بكِ")
if show_exercises:
    day = st.selectbox("🎯 اختاري اليوم:", ["السبت: خصر وبطن", "الاثنين: أرداف", "الأربعاء: ذراعين"])
    exercise_urls = {
        "السبت: خصر وبطن": "https://www.youtube.com/watch?v=cIuiQyfKBTg",
        "الاثنين: أرداف": "https://www.youtube.com/watch?v=hpyT2v04Bj0",
        "الأربعاء: ذراعين": "https://www.youtube.com/watch?v=Im3PXoLmyx8"
    }
    st.link_button("📺 فتح فيديو الجدول", exercise_urls[day])

st.divider()

# 4. إصلاح قسم المؤقت (منع خطأ IndentationError)
st.subheader("⏱️ مؤقت التمرين")
timer_sec = st.number_input("ثواني التمرين:", value=30)
if st.button("🏁 ابدأ العد"):
    placeholder = st.empty()
    for i in range(timer_sec, 0, -1):
        placeholder.write(f"⏳ المتبقي: {i} ثانية")
        time.sleep(1)
    placeholder.success("✅ انتهى الوقت!")
