import streamlit as st

# 1. إعدادات الهوية البصرية (ثيم روز الرياضي)
st.set_page_config(page_title="Zuhour AI Coach 2026", page_icon="🧘‍♀️", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #FFF5F7 0%, #FFE4E1 100%); }
    .main-card {
        background-color: white; border-radius: 20px; padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-left: 8px solid #FF69B4;
        margin-bottom: 20px;
    }
    h1, h2, h3 { color: #D81B60 !important; text-align: center; }
    .stButton > button { background: #FF69B4 !important; color: white !important; border-radius: 20px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# صورة الفتاة الرياضية (GIF)
st.markdown("<center><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3eXF4c3c3ZSZjdD1z/L40pC6N0H4h0E/giphy.gif' width='200'></center>", unsafe_allow_html=True)
st.title("🌸 مدرب زهور الذكي")

# --- القسم الأول: محرك الذكاء الاصطناعي للتشخيص والهدف ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.subheader("🔍 تشخيص الحالة وتحديد الهدف")
c1, c2 = st.columns(2)
with c1:
    h = st.number_input("الطول (سم):", value=160)
with c2:
    w = st.number_input("الوزن الحالي (كجم):", value=65.0)

target_w = st.number_input("الوزن المستهدف الذي تريدين الوصول إليه (كجم):", value=55.0)

# حسابات الذكاء الاصطناعي
diff = w - target_w
bmi = w / ((h/100)**2)

if diff > 0:
    st.warning(f"🎯 متبقي لكِ {diff:.1f} كجم للوصول لهدفك ({target_w} كجم).")
else:
    st.success(f"🎉 مذهل! لقد وصلتِ لهدفكِ المستهدف.")

# تشخيص الذكاء الاصطناعي للفيديو المناسب
if bmi > 24:
    ai_status = "حالة حرق دهون (Cardio Focus)"
    rec_video = "https://www.youtube.com/watch?v=2MoGxae-zyo" # Chloe Ting
    rec_name = "تحدي حرق الدهون العالمي (كلو تينغ)"
else:
    ai_status = "حالة نحت وشد (Sculpting Focus)"
    rec_video = "https://www.youtube.com/watch?v=3Pr6n-nKnAA" # Emi Wong
    rec_name = "تمرين نحت الخصر العالمي (إيمي ونغ)"

st.markdown(f"🤖 ترشيح الذكاء الاصطناعي بناءً على حالتكِ:")
st.info(f"الحالة المكتشفة: {ai_status}")
st.link_button(f"▶️ ابدئي التمرين المرشح: {rec_name}", rec_video)
st.markdown('</div>', unsafe_allow_html=True)

# --- القسم الثاني: جدول الأسبوع الشامل (الفيديوهات المرفوعة سابقاً) ---
st.divider()
st.subheader("📅 قائمة تمارين الأسبوع (المحتوى الموثوق)")
day = st.selectbox("اختر اليوم لرؤية الفيديو الخاص به:", ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"])

training_data = {
    "الأحد": {"type": "حرق كامل للجسم", "url": "https://www.youtube.com/watch?v=2MoGxae-zyo"},
    "الاثنين": {"type": "نحت الخصر والبطن", "url": "https://www.youtube.com/watch?v=3Pr6n-nKnAA"},
    "الثلاثاء": {"type": "بيلاتس ومرونة", "url": "https://www.youtube.com/watch?v=U4_lVjsOVBs"},
    "الأربعاء": {"type": "راحة إيجابية", "url": "https://www.youtube.com/watch?v=v2r0zYnFmxo"},
    "الخميس": {"type": "كارديو مكثف", "url": "https://www.youtube.com/watch?v=ml6cT4AZdqI"},
    "الجمعة": {"type": "يوجا واسترخاء", "url": "https://www.youtube.com/watch?v=Eml2xnoLpYE"},
    "السبت": {"type": "تمارين قوة", "url": "https://www.youtube.com/watch?v=gC_L9qAHVJ8"}
}

st.success(f"💪 تمرين {day}: {training_data[day]['type']}")
st.link_button(f"▶️ فتح فيديو يوم {day}", training_data[day]['url'])

# --- القسم الثالث: الماء والكاميرا ---
st.divider()
cw, cc = st.columns(2)
with cw:
    if 'glasses' not in st.session_state: st.session_state.glasses = 0
    st.write(f"🥤 الماء: {st.session_state.glasses}/12")
    if st.button("➕ كوب"): st.session_state.glasses += 1
with cc:
    st.write("📸 سجل الوجبات")
    st.camera_input("التقطي صورة (خلفية 🔄)", key="cam")

st.sidebar.markdown(f"### 📊 ملخص روز\nالحالي: {w} كجم\nالمستهدف: {target_w} كجم\nالفرق: {diff:.1f} كجم")
