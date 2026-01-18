import streamlit as st

# إعدادات الواجهة
st.set_page_config(page_title="Zuhour AI Coach", page_icon="🤖", layout="centered")

# تنسيق مبهج مع الفتاة الرياضية
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #e0f7fa 0%, #80deea 100%); }
    .main-box {
        background-color: white; border-radius: 25px; padding: 25px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1); border-top: 8px solid #FF8C00;
    }
    </style>
    """, unsafe_allow_html=True)

# عرض الفتاة الرياضية في المقدمة بشكل مبهج
st.markdown("<center><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3ZSZjdD1z/3o7TKVUn7iM8FMEU24/giphy.gif' width='180'></center>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #00796b;'>🤖 نظام التشخيص الرياضي الذكي</h1>", unsafe_allow_html=True)

# --- محرك التشخيص (المدخلات) ---
with st.container():
    st.subheader("🔍 تشخيص الحالة البدنية")
    col1, col2 = st.columns(2)
    with col1:
        h = st.number_input("الطول (سم):", value=160)
    with col2:
        w = st.number_input("الوزن (كجم):", value=65.0)

    ideal_w = h - 105
    bmi = w / ((h/100)**2)

    # ذكاء اصطناعي لتشخيص الحالة
    if bmi > 25:
        diagnosis = "تحتاجين لتركيز عالي على حرق الدهون (Cardio)."
        advice = "يرجى اختيار تمارين الحرق المكثف."
    elif 18.5 <= bmi <= 24.9:
        diagnosis = "جسمك في حالة ممتازة ومثالية!"
        advice = "ركزي على نحت العضلات ومرونة الجسم."
    else:
        diagnosis = "تحتاجين لزيادة الكتلة العضلية والتغذية."
        advice = "ركزي على التمارين الهادئة والقوة."

    st.info(f"📋 تشخيص الـ AI: {diagnosis}\n\n💡 نصيحة المدرب: {advice}")

# --- قسم ترشيح الفيديوهات الذكي ---
st.divider()
st.subheader("🎯 اطلبي من الـ AI تمرينك اليوم")
user_input = st.text_input("صفي شعورك أو هدفك اليوم (مثلاً: أريد نحت الخصر أو حرق دهون البطن):")

if user_input:
    st.write("🔄 جاري تحليل حالتك وترشيح الفيديو الأنسب...")
    
    # محرك الترشيح بناءً على التشخيص والكلمات
    if any(x in user_input for x in ["نحت", "خصر", "بيلاتس", "جمال"]):
        video_url = "https://www.youtube.com/watch?v=3Pr6n-nKnAA"
        video_title = "تمرين Emi Wong العالمي لنحت القوام (الأكثر ملاءمة لحالتك)"
    elif any(x in user_input for x in ["حرق", "دهون", "وزن", "كارديو"]):
        video_url = "https://www.youtube.com/watch?v=2MoGxae-zyo"
        video_title = "تحدي Chloe Ting العالمي لحرق الدهون (المناسب لتشخيصك)"
    else:
        video_url = "https://www.youtube.com/watch?v=v2r0zYnFmxo"
        video_title = "تمارين الشد الشاملة للمدربة سارة"

    st.success(f"✅ تم العثور على أفضل تطابق: {video_title}")
    st.link_button("▶️ ابدئي التمرين الآن", video_url)

# --- بقية الميزات (الماء والكاميرا) ---
st.divider()
col_w, col_cam = st.columns(2)
with col_w:
    if 'w' not in st.session_state: st.session_state.w = 0
    if st.button("💧 إضافة كوب ماء"): st.session_state.w += 1
    st.write(f"الماء: {st.session_state.w}/12")

with col_cam:
    st.camera_input("📷 سجل الوجبات (خلفية)")

st.sidebar.markdown(f"### 📊 ملخص زهور\nالوزن: {w}\nالمثالي: {ideal_w}\nالحالة: {diagnosis.split(' ')[0]}")
