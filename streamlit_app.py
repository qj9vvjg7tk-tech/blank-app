import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Zuhour AI Fitness 2026", page_icon="🌸", layout="centered")

# تنسيق CSS احترافي
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #FFF5F7 0%, #FFE4E1 100%); }
    .main-card {
        background-color: white; border-radius: 20px; padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-right: 8px solid #FF69B4;
        margin-bottom: 20px;
    }
    h1, h2, h3 { color: #D81B60 !important; text-align: center; }
    .stButton > button { background: #FF69B4 !important; color: white !important; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 2. عرض صورة الفتاة الرياضية (رابط جديد ومباشر)
st.markdown("<center><img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3ZSZjdD1z/L40pC6N0H4h0E/giphy.gif' width='220' alt='Fitness Girl'></center>", unsafe_allow_html=True)

st.title("🌸 مدرب زهور الخاص")

# --- القسم الأول: قياسات الهدف ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.subheader("📏 تحديث الوزن والهدف")
c1, c2, c3 = st.columns(3)
with c1: h = st.number_input("الطول:", value=160)
with c2: w = st.number_input("الوزن الحالي:", value=65.0)
with c3: target = st.number_input("الهدف:", value=55.0)

diff = w - target
st.write(f"💪 متبقي لكِ {diff:.1f} كجم للوصول للهدف!")
st.markdown('</div>', unsafe_allow_html=True)

# --- القسم الثاني: مستشار الذكاء الاصطناعي (المربع الذي طلبتِه) ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.subheader("🤖 مستشار التمارين الذكي")
st.write("ألصقي خطتكِ التي حصلتِ عليها أو صفي حالتكِ هنا، وسأرشح لكِ الفيديو الأنسب فوراً:")
user_plan = st.text_area("مثال: خطتي اليوم هي نحت البطن والخصر...", placeholder="اكتبي هنا...")

if user_plan:
    st.write("🔍 جاري تحليل خطتكِ وترشيح التمارين...")
    # محرك تحليل النص الذكي
    if any(word in user_plan for word in ["نحت", "خصر", "بيلاتس", "شد"]):
        vid_url = "https://www.youtube.com/watch?v=3Pr6n-nKnAA"
        vid_name = "تمرين Emi Wong لنحت الخصر (المطابق لخطتك)"
    elif any(word in user_plan for word in ["حرق", "دهون", "كارديو", "سريع"]):
        vid_url = "https://www.youtube.com/watch?v=2MoGxae-zyo"
        vid_name = "تحدي Chloe Ting لحرق الدهون (المطابق لخطتك)"
    else:
        vid_url = "https://www.youtube.com/watch?v=v2r0zYnFmxo"
        vid_name = "تمرين شامل للياقة الجسم"
    
    st.success(f"✅ تم تحليل خطتك بنجاح! الفيديو المرشح: {vid_name}")
    st.link_button("🚀 ابدئي التمرين الآن", vid_url)
st.markdown('</div>', unsafe_allow_html=True)

# --- القسم الثالث: جدول الأسبوع ---
st.divider()
st.subheader("📅 جدول تمارين الأسبوع المعتمد")
day = st.selectbox("اختر اليوم:", ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"])
week_videos = {
    "الأحد": "https://www.youtube.com/watch?v=2MoGxae-zyo",
    "الاثنين": "https://www.youtube.com/watch?v=3Pr6n-nKnAA",
    "الثلاثاء": "https://www.youtube.com/watch?v=U4_lVjsOVBs",
    "الأربعاء": "https://www.youtube.com/watch?v=v2r0zYnFmxo",
    "الخميس": "https://www.youtube.com/watch?v=ml6cT4AZdqI",
    "الجمعة": "https://www.youtube.com/watch?v=Eml2xnoLpYE",
    "السبت": "https://www.youtube.com/watch?v=gC_L9qAHVJ8"
}
st.link_button(f"▶️ فتح تمرين يوم {day}", week_videos[day])

# --- القسم الرابع: الكاميرا والماء ---
st.divider()
c_water, c_cam = st.columns(2)
with c_water:
    if 'w' not in st.session_state: st.session_state.w = 0
    if st.button("🥤 إضافة ماء"): st.session_state.w += 1
    st.write(f"الماء: {st.session_state.w}/12")
with c_cam:
    st.camera_input("📸 تصوير الوجبة (خلفية 🔄)")

st.sidebar.markdown(f"### 📊 سجل روز\nالحالي: {w}\nالهدف: {target}")
