import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الواجهة الاحترافية (علاج مشكلة الوضوح والفراغات)
st.set_page_config(page_title="Rose Smart Coach", page_icon="🌸", layout="centered")

st.markdown("""
    <style>
    /* خلفية التطبيق هادئة */
    .stApp { background: linear-gradient(180deg, #FDFCFB 0%, #E2D1C3 100%); }
    
    /* حل مشكلة الوضوح: بطاقة بيضاء ناصعة وخط أسود صريح */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 12px;
        border: 2px solid #EEEEEE;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* الخطوط: سوداء صريحة وواضحة جداً للقراءة */
    h1, h2, h3, p, label, span, .stMarkdown { 
        color: #000000 !important; 
        font-family: -apple-system, sans-serif;
        font-weight: 800 !important;
    }

    /* الأزرار بلون السلمون المعتمد وخط أسود */
    .stButton > button {
        background-color: #F3C3B2 !important; 
        color: #000000 !important;
        border-radius: 15px;
        border: 2px solid #000000;
        font-weight: bold;
        height: 50px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌸 مدرب روز الذكي المتكامل")

# 2. ميزة دمج الخطط الخارجية (الذكاء الاصطناعي)
st.subheader("📝 مزامنة خطتكِ الخارجية")
st.markdown("انسخي خطتكِ من أي برنامج ذكاء اصطناعي هنا وسيقوم التطبيق بترشيح التمرين المناسب:")
ai_plan = st.text_area("ألصقي خطتكِ هنا:", placeholder="مثال: يوم 1 كارديو، يوم 2 بيلاتس...")

if ai_plan:
    st.markdown("### 🤖 تحليل المدرب:")
    if any(word in ai_plan.lower() for word in ["نحت", "بيلاتس", "خصر"]):
        advice = "خطة رائعة للنحت! أرشح لكِ تمارين بيلاتس نيكول اليوم."
        vid_url = "https://www.youtube.com/watch?v=NxX9p8W09I8"
    elif any(word in ai_plan.lower() for word in ["حرق", "كارديو", "وزن"]):
        advice = "بما أن هدفكِ الحرق؛ الأفضل لكِ هو كارديو حرق الدهون."
        vid_url = "https://www.youtube.com/watch?v=gC_L9qAHVJ8"
    else:
        advice = "خطة متوازنة! تمارين كلو تينج هي الإضافة المثالية لكِ."
        vid_url = "https://www.youtube.com/watch?v=2MoGxae-zyo"
    
    st.success(f"✅ {advice}")
    st.link_button("▶️ ابدأ التمرين المرشح الآن", vid_url)

st.divider()

# 3. بيانات الجسم (الطول والوزن)
st.subheader("📊 القياسات والتحليل")
col_h, col_cw, col_tw = st.columns(3)
with col_h: height = st.number_input("طولكِ (سم):", value=160)
with col_cw: current_w = st.number_input("وزنكِ الحالي:", value=60.0)
with col_tw: target_w = st.number_input("هدفكِ:", value=55.0)

bmi = current_w / ((height / 100) ** 2)
st.info(f"مؤشر الكتلة: {bmi:.1f} | السعرات المقترحة: {int(current_w * 24)} سعرة")

st.divider()

# 4. أدوات المتابعة (تم إصلاح خطأ الإزاحة هنا)
st.subheader("⚙️ أدوات المتابعة")
tab1, tab2, tab3 = st.tabs(["💧 الماء", "📏 القياسات", "⏱️ المؤقت"])

with tab1:
    if 'water' not in st.session_state: st.session_state.water = 0
    if st.button("🥤 إضافة كوب ماء"): st.session_state.water += 1
    st.write(f"المجموع: {st.session_state.water} / 12")
    st.progress(min(st.session_state.water / 12, 1.0))

with tab2:
    st.number_input("الخصر (سم):", value=70, key="w_meas")
    st.number_input("الأرداف (سم):", value=90, key="h_meas")
    st.button("💾 حفظ القياسات")

with tab3:
    # تم التأكد من الإزاحة الصحيحة هنا لمنع خطأ IndentationError
    timer_sec = st.number_input("ثواني التمرين:", value=30)
    if st.button("🏁 ابدأ المؤقت"):
        ph = st.empty()
        for i in range(timer_sec, 0, -1):
            ph.write(f"⏳ المتبقي: {i} ثانية")
            time.sleep(1)
        ph.success("✅ بطلة!")

st.sidebar.caption("نسخة روز النهائية • وضوح فائق • روابط مباشرة")
