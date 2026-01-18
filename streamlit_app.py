import streamlit as st

# إعداد الصفحة وإزالة المساحات الزائدة في الأعلى
st.set_page_config(page_title="Zuhour Fitness 2026", page_icon="⏳", layout="centered")

# كود لإخفاء القوائم غير الضرورية وتقليل الفراغات البيضاء
st.markdown("""
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 0rem;}
    div.stButton > button:first-child { background-color: #f0f2f6; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⏳ تطبيق زهور للرشاقة 2026")

# 1. قسم الماء (مدمج لتقليل المساحة)
if 'water' not in st.session_state:
    st.session_state.water = 0

col1, col2 = st.columns([2, 1])
with col1:
    st.write(f"💧 أكواب الماء: {st.session_state.water} / 12")
with col2:
    if st.button("➕ إضافة كوب"):
        st.session_state.water += 1
st.progress(min(st.session_state.water / 12, 1.0))

st.write("---")

# 2. قسم التمارين (جعله اختيارياً كما طلبتِ)
st.subheader("🏋️‍♀️ جدول التمارين")
show_exercises = st.toggle("عرض تفاصيل تمارين اليوم") # زر تبديل أنيق بدل المربع الأبيض

if show_exercises:
    day = st.selectbox("🎯 اختاري اليوم:", [
        "السبت: خصر وبطن سفلية", 
        "الاثنين: أرداف و Hip Dips", 
        "الأربعاء: ذراعين وشد كامل"
    ])

    exercise_info = {
        "السبت: خصر وبطن سفلية": {
            "details": "✅ Plank | ✅ Side Crunches | ✅ Side Leg Lifts",
            "url": "https://www.youtube.com/watch?v=cIuiQyfKBTg"
        },
        "الاثنين: أرداف و Hip Dips": {
            "details": "✅ Glute Bridges | ✅ Donkey Kicks | ✅ Fire Hydrants",
            "url": "https://www.youtube.com/watch?v=hpyT2v04Bj0"
        },
        "الأربعاء: ذراعين وشد كامل": {
            "details": "✅ Wall Push-ups | ✅ Curtsy Lunges | ✅ Arm Circles",
            "url": "https://www.youtube.com/watch?v=Im3PXoLmyx8"
        }
    }

    st.info(exercise_info[day]["details"])
    
    # العودة لنظام الزر المباشر لليوتيوب
    st.link_button("📺 فتح فيديو التمرين مباشرة", exercise_info[day]["url"])

st.write("---")
st.success("💡 نصيحة زهور: الاستمرارية سر النجاح!")
