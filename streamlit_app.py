import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الهوية الرياضية الزاهية (Vibrant Sports Mode)
st.set_page_config(page_title="Rose Fitness Master 2026", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    /* تقليل المساحات الزائدة */
    .block-container {padding-top: 1.5rem; padding-bottom: 1rem;}
    
    /* خلفية رياضية حيوية (تدرج أزرق رياضي) */
    .stApp { 
        background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%); 
    }
    
    /* بطاقات بيضاء ناصعة جداً بظلال خفيفة لضمان وضوح النص الأسود */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 10px;
        border-right: 8px solid #FF8C00; /* حافة برتقالية محفزة */
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* النصوص: لون كحلي داكن جداً (قريب للأسود) لتباين فائق ووضوح تام */
    h1, h2, h3, p, label, span, div { 
        color: #001D3D !important; 
        font-family: -apple-system, sans-serif;
        font-weight: 800 !important;
    }

    /* أزرار رياضية زاهية (برتقالي محفز) */
    .stButton > button {
        background-color: #FF8C00 !important; 
        color: #FFFFFF !important;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        height: 48px;
        width: 100%;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #E67E22 !important;
        transform: translateY(-2px);
    }

    /* شريط التقدم: أخضر فسفوري رياضي */
    .stProgress > div > div > div > div {
        background-color: #39FF14 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Rose Smart Fitness 2026")
st.write(f"🚀 انطلقي اليوم يا روز: {datetime.now().strftime('%d %B, %Y')}")

# 2. قسم شرب الماء
if 'water' not in st.session_state:
    st.session_state.water = 0

st.subheader("💧 عداد الهيدرات اليومي")
col_w1, col_w2 = st.columns([2, 1])
with col_w1:
    st.write(f"الأكواب المستهلكة: {st.session_state.water} / 12")
with col_w2:
    if st.button("🥤 إضافة كوب"):
        st.session_state.water += 1
st.progress(min(st.session_state.water / 12, 1.0))

st.divider()

# 3. تحليل بيانات الجسم (الطول، الوزن، السعرات)
st.subheader("📊 التحليل البدني الذكي")
c1, c2, c3 = st.columns(3)
with c1: height = st.number_input("طولكِ (سم):", value=160, step=1)
with c2: current_w = st.number_input("وزنكِ الحالي:", value=60.0, step=0.1)
with c3: target_w = st.number_input("وزنكِ المستهدف:", value=55.0, step=0.1)

bmi = current_w / ((height / 100) ** 2)
calories = (current_w * 22) - 300 # معادلة تقريبية لخسارة الوزن

st.success(f"🤖 الحالة: {bmi:.1f} BMI | السعرات المقترحة: {int(calories)} سعرة")

st.divider()

# 4. دمج الخطط الخارجية (AI) وجدول التمارين
st.subheader("📝 خطة التمارين والمزامنة")
ai_plan = st.text_area("ألصقي خطتكِ من (ChatGPT) أو أي برنامج ذكاء اصطناعي هنا:", placeholder="مثلاً: أريد التركيز على البطن والأرداف...")

if ai_plan:
    st.markdown("### 🤖 تحليل المدرب لخطتكِ:")
    if any(word in ai_plan.lower() for word in ["نحت", "بيلاتس", "خصر", "نيكول"]):
        rec_txt = "خطة نحت رائعة! الأنسب لكِ هو تمارين بيلاتس نيكول."
        vid_url = "https://www.youtube.com/watch?v=NxX9p8W09I8"
    elif any(word in ai_plan.lower() for word in ["حرق", "كارديو", "دهون", "وزن"]):
        rec_txt = "هدف الحرق واضح؛ أرشح لكِ كارديو حرق الدهون أو تمارين كلو تينج."
        vid_url = "https://www.youtube.com/watch?v=2MoGxae-zyo"
    else:
        rec_txt = "خطة متوازنة! يمكنكِ البدء بتمارين الشد كاملة."
        vid_url = "https://www.youtube.com/watch?v=Im3PXoLmyx8"
    
    st.info(rec_txt)
    st.link_button("▶️ ابدأ التمرين المرشح لخطتكِ", vid_url)

st.write("")
show_exercises = st.toggle("🏋️‍♀️ عرض جدول التمارين الأسبوعي الخاص بكِ")

if show_exercises:
    day = st.selectbox("🎯 اختاري اليوم:", [
        "السبت: خصر وبطن سفلية", 
        "الاثنين: أرداف و Hip Dips", 
        "الأربعاء: ذراعين وشد كامل"
    ])
    exercise_info = {
        "السبت: خصر وبطن سفلية": {"details": "✅ Plank | ✅ Side Crunches", "url": "https://www.youtube.com/watch?v=cIuiQyfKBTg"},
        "الاثنين: أرداف و Hip Dips": {"details": "✅ Glute Bridges | ✅ Fire Hydrants", "url": "https://www.youtube.com/watch?v=hpyT2v04Bj0"},
        "الأربعاء: ذراعين وشد كامل": {"details": "✅ Wall Push-ups | ✅ Arm Circles", "url": "https://www.youtube.com/watch?v=Im3PXoLmyx8"}
    }

    st.warning(exercise_info[day]["details"])
    st.link_button("📺 فتح فيديو الجدول المباشر", exercise_info[day]["url"])

st.divider()

# 5. الأدوات اليومية (القياسات والمؤقت)
t1, t2 = st.tabs(["📏 سجل القياسات", "⏱️ مؤقت التمرين"])

with t1:
    st.number_input("محيط الخصر (سم):", value=70, key="w_rose")
    st.number_input("محيط الأرداف (سم):", value=90, key="h_rose")
    if st.button("💾 حفظ السجل"):
        st.toast("تم حفظ قياساتكِ بنجاح!")

with t2:
    sec = st.number_input("ثواني التحدي:", value=30)
    if st.button("🏁 ابدأ العد التنازلي"):
        ph = st.empty()
        for i in range(sec, 0, -1):
            ph.write(f"⏳ المتبقي: {i} ثانية")
            time.sleep(1)
        ph.success("✅ بطلة! أنجزتِ المهمة.")

st.sidebar.caption("نسخة 2026 الذهبية • وضعية رياضية زاهية")
