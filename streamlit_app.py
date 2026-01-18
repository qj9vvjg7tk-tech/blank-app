import streamlit as st

# 1. إعدادات الصفحة والجمالية
st.set_page_config(page_title="Zuhour Fitness AI 2026", page_icon="🧘‍♀️", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #FFF5F7 0%, #FFE4E1 100%); }
    .main-card {
        background-color: white; border-radius: 20px; padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-bottom: 5px solid #FF69B4;
    }
    h1, h2, h3 { color: #D81B60 !important; font-family: 'Arial'; text-align: center; }
    .stButton > button {
        background: #FF69B4 !important; color: white !important; border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. صورة فتاة رياضية مبهجة (GIF احترافي)
st.markdown("<center><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3ZSZjdD1z/L40pC6N0H4h0E/giphy.gif' width='250'></center>", unsafe_allow_html=True)

st.title("🌸 مدرب زهور الذكي: خطة الرشاقة")

# --- القسم 1: التشخيص الذكي بناءً على القياسات ---
with st.container():
    st.subheader("🔍 تشخيص الذكاء الاصطناعي لحالتك")
    col1, col2 = st.columns(2)
    with col1:
        h = st.number_input("الطول (سم):", value=160)
    with col2:
        w = st.number_input("الوزن الحالي (كجم):", value=65.0)
    
    bmi = w / ((h/100)**2)
    ideal_w = h - 105
    
    if bmi > 25:
        status = "تركيز على حرق الدهون (Cardio)"
        recommendation = "ننصحكِ باتباع تمارين عالية الكثافة اليوم."
    else:
        status = "تركيز على النحت والشد (Sculpting)"
        recommendation = "حالتكِ ممتازة، ركزي على بيلاتس ونحت الخصر."
    
    st.info(f"🚩 التشخيص: {status}\n\n🎯 الهدف للوصول للمثالي: {ideal_w} كجم")

# --- القسم 2: جدول تمارين الأسبوع الذكي ---
st.divider()
st.subheader("📅 جدول التمارين الأسبوعي")
day = st.selectbox("اختر اليوم لرؤية تمرينك المرشح:", ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"])

training_plan = {
    "الأحد": {"type": "حرق دهون كامل الجسم", "url": "https://www.youtube.com/watch?v=2MoGxae-zyo"},
    "الاثنين": {"type": "نحت الخصر والبطن", "url": "https://www.youtube.com/watch?v=3Pr6n-nKnAA"},
    "الثلاثاء": {"type": "بيلاتس لشد القوام", "url": "https://www.youtube.com/watch?v=U4_lVjsOVBs"},
    "الأربعاء": {"type": "راحة إيجابية (مشط وتمدد)", "url": "https://www.youtube.com/watch?v=v2r0zYnFmxo"},
    "الخميس": {"type": "كارديو مكثف", "url": "https://www.youtube.com/watch?v=ml6cT4AZdqI"},
    "الجمعة": {"type": "يوجا واسترخاء", "url": "https://www.youtube.com/watch?v=Eml2xnoLpYE"},
    "السبت": {"type": "تمارين القوة المنزلية", "url": "https://www.youtube.com/watch?v=gC_L9qAHVJ8"}
}

st.success(f"💪 تمرين يوم {day} هو: {training_plan[day]['type']}")
st.link_button(f"▶️ افتحي فيديو تمرين {day} (عالمي ومجرب)", training_plan[day]['url'])

# --- القسم 3: الكاميرا الخلفية وسجل الماء ---
st.divider()
st.subheader("📸 سجل الوجبات (كاميرا خلفية)")
st.write("💡 ملاحظة: عند فتح الكاميرا، اضغطي على أيقونة التبديل 🔄 في متصفحك للتحويل للكاميرا الخلفية.")
st.camera_input("التقطي صورة الوجبة")

if 'glasses' not in st.session_state: st.session_state.glasses = 0
st.subheader(f"🥤 شرب الماء: {st.session_state.glasses} / 12")
if st.button("اضافة كوب"): st.session_state.glasses += 1

st.sidebar.markdown(f"### ملخص زهور\nالوزن: {w}\nالهدف: {ideal_w}")
