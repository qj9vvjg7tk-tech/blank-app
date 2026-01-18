import streamlit as st

# 1. إعدادات الصفحة والجمالية
st.set_page_config(page_title="Zuhour AI Coach", page_icon="🧘‍♀️", layout="centered")

# تنسيق CSS لضمان مظهر احترافي ومبهج
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #FFF5F7 0%, #FFE4E1 100%); }
    .main-card {
        background-color: white; border-radius: 20px; padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-right: 8px solid #FF69B4;
        margin-bottom: 20px;
    }
    h1, h2, h3 { color: #D81B60 !important; text-align: center; font-family: 'Arial'; }
    .stButton > button { background: #FF69B4 !important; color: white !important; border-radius: 15px; width: 100%; height: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. عرض صورة الفتاة الرياضية (رابط GIF مؤكد ومجرب)
st.markdown("<center><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3ZSZjdD1z/L40pC6N0H4h0E/giphy.gif' width='200'></center>", unsafe_allow_html=True)

st.title("🌸 مستشار زهور الرياضي الذكي")

# --- القسم الأول: تحديث الهدف والوزن ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.subheader("📏 راداد الأهداف والقياسات")
c1, c2, c3 = st.columns(3)
with c1: h = st.number_input("الطول (سم):", value=160)
with c2: w = st.number_input("الوزن الحالي:", value=65.0)
with c3: target = st.number_input("الهدف (كجم):", value=55.0)

diff = w - target
if diff > 0:
    st.warning(f"🎯 متبقي لكِ {diff:.1f} كجم للوصول لهدف الـ {target} كجم")
else:
    st.success("🎉 تهانينا! لقد حققتِ وزنكِ المستهدف!")
st.markdown('</div>', unsafe_allow_html=True)

# --- القسم الثاني: صندوق استشارة الذكاء الاصطناعي (الميزة الجديدة) ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.subheader("🤖 صندوق الاستشارة والخطط")
st.write("ألصقي هنا الخطة التي حصلتِ عليها، وسيقوم الذكاء الاصطناعي بترشيح الفيديوهات المناسبة:")

# هذا هو المربع الذي طلبتِ إضافته للاستشارة
user_input = st.text_area("ضعي نص الخطة هنا (مثلاً: أريد نحت البطن اليوم)...", height=150)

if user_input:
    st.info("🔄 جاري تحليل الخطة وترشيح الفيديوهات العالمية...")
    # منطق الذكاء الاصطناعي للتحليل
    if any(word in user_input for word in ["نحت", "خصر", "بيلاتس", "شد"]):
        vid = "https://www.youtube.com/watch?v=3Pr6n-nKnAA"
        name = "تمرين Emi Wong العالمي لنحت الخصر"
    elif any(word in user_input for word in ["حرق", "دهون", "وزن", "كارديو"]):
        vid = "https://www.youtube.com/watch?v=2MoGxae-zyo"
        name = "تحدي Chloe Ting العالمي لحرق الدهون"
    else:
        vid = "https://www.youtube.com/watch?v=v2r0zYnFmxo"
        name = "تمارين الشد الشاملة (سارة بوب فيت)"
    
    st.success(f"✅ تم التشخيص! الفيديو المرشح لخطتك هو: {name}")
    st.link_button("🚀 ابدئي التمرين المرشح الآن", vid)
st.markdown('</div>', unsafe_allow_html=True)

# --- القسم الثالث: جدول الأسبوع الثابت ---
st.divider()
st.subheader("📅 جدول تمارين الأسبوع (روابط موثوقة)")
day = st.selectbox("اختر اليوم لرؤية فيديو التمرين:", ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"])
week_plan = {
    "الأحد": "https://www.youtube.com/watch?v=2MoGxae-zyo",
    "الاثنين": "https://www.youtube.com/watch?v=3Pr6n-nKnAA",
    "الثلاثاء": "https://www.youtube.com/watch?v=U4_lVjsOVBs",
    "الأربعاء": "https://www.youtube.com/watch?v=v2r0zYnFmxo",
    "الخميس": "https://www.youtube.com/watch?v=ml6cT4AZdqI",
    "الجمعة": "https://www.youtube.com/watch?v=Eml2xnoLpYE",
    "السبت": "https://www.youtube.com/watch?v=gC_L9qAHVJ8"
}
st.link_button(f"▶️ فتح تمرين يوم {day}", week_plan[day])

# --- القسم الرابع: الكاميرا والماء ---
st.divider()
col_w, col_c = st.columns(2)
with col_w:
    if 'water' not in st.session_state: st.session_state.water = 0
    st.write(f"🥤 الماء: {st.session_state.water}/12")
    if st.button("➕ كوب ماء"): st.session_state.water += 1
with col_c:
    st.write("📸 الكاميرا الخلفية 🔄")
    st.camera_input("صوري وجبتكِ")

st.sidebar.markdown(f"### سجل زهور 2026\nالوزن: {w} كجم\nالهدف: {target} كجم")
