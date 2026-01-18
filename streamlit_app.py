import streamlit  as st
‏#إعداد واجهة زهور احترافية
‏st.set_page_config(page_title="Zuhour Fitness 2026", page_icon="⏳", layout="centered")
st.title("⏳ تطبيق زهور لنحت القوام 2026")
st.write("---")
# عداد شرب الماء (3 لتر يومياً)
if 'water' not in st.session_state:
    st.session_state.water = 0
st.subheader(f"💧 أكواب الماء: {st.session_state.water} / 12")
if st.button("شربت كوباً جديداً 🥛"):
    st.session_state.water += 1

st.progress(min(st.session_state.water / 12, 1.0))
# جدول التمارين والـ Hip Dips
st.divider()
st.subheader("🏋️‍♀️ جدول تمارين الأسبوع المستهدف"
day = st.selectbox("🎯 اختيار يوم التمارين :",
[""السبت: خصر وبطن سفلية", "الاثنين: أرداف و Hip Dips", "الأربعاء: ذراعين وشد كامل"])
# تفاصيل التمارين والفيديوهات الأجنبية
exercise_info = {
    "السبت: خصر وبطن سفلية": {
        "text": "1. Plank (30s)\n2. Side Crunches (15x3)\n3. Side Leg Lifts (15x3)",
        "link": "https://www.youtube.com/watch?v=cIuiQyfKBTg"
    },
  "الاثنين: أرداف و Hip Dips": {
        "text": "1. Glute Bridges (15x3)\n2. Donkey Kicks (15x3)\n3. Fire Hydrants (15x3)",
        "link": "https://www.youtube.com/watch?v=hpyT2v04Bj0"
    },
    "الأربعاء: ذراعين وشد كامل": {
        "text": "1. Wall Push-ups (12x3)\n2. Curtsy Lunges (15x3)\n3. Arm Circles (1 min)",
        "link": "https://www.youtube.com/watch?v=Im3PXoLmyx8"
    }
}
st.info(exercise_info[day]["text"])
st.link_button("📺 شاهد فيديو التمرين (المدربين الأجانب)", exercise_info[day]["link"])

# نصيحة زهور اليومية
st.divider()
st.success("💡 نصيحة اليوم: التزمي بالـ 3 لتر ماء ونامي جيداً للوصول لوزن 55 كجم.")   
