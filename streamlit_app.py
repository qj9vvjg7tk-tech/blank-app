import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الهوية البصرية (Apple Style) - نصوص واضحة جداً
st.set_page_config(page_title="Rose Smart Fitness", page_icon="🌸", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #FDFCFB 0%, #E2D1C3 100%); }
    /* نصوص كحلية داكنة جداً لضمان الوضوح التام */
    h1, h2, h3, p, label, span, div { 
        color: #1A2E35 !important; 
        font-family: -apple-system, sans-serif;
        font-weight: 700 !important;
    }
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 25px;
        padding: 20px;
        margin-bottom: 15px;
        border: 1px solid rgba(255,255,255,0.5);
    }
    .stButton > button {
        background-color: #F3C3B2 !important; 
        color: #1A2E35 !important;
        border-radius: 20px;
        border: 2px solid #1A2E35;
        font-weight: bold;
        width: 100%;
    }
    .stProgress > div > div > div > div { background-color: #99CDD8 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌸 مدرب روز المتكامل")

# 2. قسم المدخلات الذكية (قابلة للتغيير بالكامل)
st.subheader("📊 ملفكِ البدني الشخصي")
c1, c2, c3 = st.columns(3)
with c1:
    height = st.number_input("طولكِ (سم):", value=160, step=1)
with c2:
    current_w = st.number_input("وزنكِ الحالي (كجم):", value=60.0, step=0.1)
with c3:
    target_w = st.number_input("هدفكِ (كجم):", value=55.0, step=0.1)

# --- العمليات الحسابية الذكية ---
# 1. مؤشر كتلة الجسم (BMI)
bmi = current_w / ((height / 100) ** 2)
# 2. السعرات الحرارية التقريبية (BMR مبسط) للحفاظ على الوزن
calories = (10 * current_w) + (6.25 * height) - (5 * 25) + 5 # تقدير لسن 25
# 3. السعرات المطلوبة لخسارة الوزن بأمان
target_calories = calories - 400

# 3. لوحة التحليل الذكي
st.markdown("### 🤖 تحليل المدرب")
col_bmi, col_cal = st.columns(2)

with col_bmi:
    if bmi < 18.5: status = "نحافة"; rec_cat = "تمارين نيكول (Move With Nicole)"
    elif 18.5 <= bmi < 25: status = "مثالي"; rec_cat = "تمارين كلو تينج (Chloe Ting)"
    else: status = "زيادة بسيطة"; rec_cat = "كارديو ومشي منزلي"
    st.metric("مؤشر الكتلة (BMI)", f"{bmi:.1f}", status)

with col_cal:
    st.metric("السعرات المقترحة", f"{int(target_calories)} سعرة", "-400 يومياً")

st.info(f"💡 نصيحة روز: للوصول إلى {target_w} كجم، ركزي على {rec_cat} واشربي الكثير من الماء!")

st.divider()

# 4. قسم الإحماء والتمدد (Safety First)
st.subheader("🧘 تمدد وإحماء (قبل البدء)")
warmups = {
    "إحماء كامل الجسم (Nicole)": "https://www.youtube.com/watch?v=i9Yp99S9-hU",
    "تمدد سريع (5 دقائق)": "https://www.youtube.com/watch?v=2MoGxae-zyo"
}
sel_warm = st.selectbox("اختاري الإحماء:", list(warmups.keys()))
st.link_button("▶️ ابدأ الإحماء المباشر", warmups[sel_warm])

st.divider()

# 5. مكتبة التمارين الشاملة
st.subheader("📺 تمارينكِ المخصصة اليوم")
all_videos = {
    "تمارين كلو تينج (Chloe Ting)": {
        "تحدي عضلات البطن": "https://www.youtube.com/watch?v=2MoGxae-zyo",
        "شد الجسم بالكامل": "https://www.youtube.com/watch?v=2pLT-olgUJs"
    },
    "تمارين نيكول (Move With Nicole)": {
        "بيلاتس نحت الجسم": "https://www.youtube.com/watch?v=NxX9p8W09I8",
        "بيلاتس كامل الجسم": "https://www.youtube.com/watch?v=K-PpDUpniz4"
    },
    "كارديو ومشي منزلي": {
        "كارديو حرق الدهون": "https://www.youtube.com/watch?v=gC_L9qAHVJ8",
        "مشي سريع - Leslie": "https://www.youtube.com/watch?v=enYITYwvPAQ"
    }
}

# اختيار الفئة بناءً على التحليل أو الاختيار الشخصي
final_cat = st.selectbox("الفئة:", list(all_videos.keys()), index=list(all_videos.keys()).index(rec_cat))
sel_main = st.selectbox("التمرين الأساسي:", list(all_videos[final_cat].keys()))
st.link_button(f"🚀 فتح {sel_main} في يوتيوب", all_videos[final_cat][sel_main])

st.divider()
# 6. الأدوات اليومية (الماء، القياسات، المؤقت)
tabs = st.tabs(["💧 الماء", "📏 القياسات", "⏱️ المؤقت"])
with tabs[0]:
    if 'water' not in st.session_state: st.session_state.water = 0
    if st.button("🥤 إضافة كوب"): st.session_state.water += 1
    st.write(f"الهدف اليومي: {st.session_state.water}/12")
    st.progress(min(st.session_state.water / 12, 1.0))
with tabs[1]:
    st.number_input("الخصر (سم):", value=70)
    st.number_input("الأرداف (سم):", value=90)
with tabs[2]:
    sec = st.number_input("المؤقت (ثواني):", value=30)
    if st.button("🏁 ابدأ الآن"):
        ph = st.empty()
        for i in range(sec, 0, -1):
            ph.write(f"⏳ المتبقي: {i} ثانية")
            time.sleep(1)
        ph.success("✅ بطلة يا روز! انتهى الوقت.")

st.sidebar.caption("روز فيتنس • تحليل ذكي • روابط مباشرة")
