import streamlit as st

# إعداد واجهة روز الجديدة
st.set_page_config(page_title="Rose Health & Fitness", page_icon="✨", layout="centered")

# الاسم الجديد للتطبيق
st.title("✨ الروتين الصحي مع روز")
st.write("---")

# 1. قسم شرب الماء
st.subheader("💧 عداد شرب الماء (الهدف: 3 لتر)")
if 'water' not in st.session_state:
    st.session_state.water = 0

col1, col2 = st.columns([2, 1])
with col1:
    st.progress(min(st.session_state.water / 12, 1.0))
with col2:
    if st.button("🥛 شربت كوباً"):
        st.session_state.water += 1

st.write(f"لقد شربتِ: {st.session_state.water} من 12 كوباً.")

st.divider()

# 2. عداد السعرات والكاميرا
st.subheader("🍎 عداد السعرات وتصوير الوجبات")

# خيار تصوير الوجبة
picture = st.camera_input("صوري وجبتكِ لتوثيقها 📸")
if picture:
    st.image(picture, caption="تم تسجيل الوجبة بنجاح!")

if 'calories' not in st.session_state:
    st.session_state.calories = 0

cal_input = st.number_input("أدخلي عدد سعرات الوجبة (تقديرياً):", min_value=0, step=50)
if st.button("إضافة السعرات ➕"):
    st.session_state.calories += cal_input

st.warning(f"إجمالي السعرات المستهلكة اليوم: {st.session_state.calories} سعرة.")

st.divider()

# 3. وجبات صحية مقترحة
st.subheader("🥗 وجبات صحية مقترحة")
meal_type = st.selectbox("اكتشفي وجبات لـ:", ["الفطور", "الغداء", "العشاء"])

meals = {
    "الفطور": "2 بيضة مسلوقة + نصف حبة أفوكادو + خيار.",
    "الغداء": "صدر دجاج مشوي + 5 ملاعق أرز أسمر + سلطة خضراء كبيرة.",
    "العشاء": "علبة تونة مصفاة من الزيت + سلطة جرجير + زبادي يوناني."
}
st.info(meals[meal_type])

st.divider()

# 4. جدول التمارين
st.subheader("🏋️‍♀️ جدول تمارين روز")
day = st.selectbox("اختاري اليوم:", ["السبت: خصر وبطن سفلية", "الاثنين: أرداف و Hip Dips", "الأربعاء: ذراعين وشد كامل"])

exercise_info = {
    "السبت: خصر وبطن سفلية": {"text": "1. Plank (30s)\n2. Side Crunches (15x3)", "link": "https://www.youtube.com/watch?v=cIuiQyfKBTg"},
    "الاثنين: أرداف و Hip Dips": {"text": "1. Glute Bridges (15x3)\n2. Donkey Kicks (15x3)", "link": "https://www.youtube.com/watch?v=hpyT2v04Bj0"},
    "الأربعاء: ذراعين وشد كامل": {"text": "1. Wall Push-ups (12x3)\n2. Arm Circles (1 min)", "link": "https://www.youtube.com/watch?v=Im3PXoLmyx8"}
}

st.success(exercise_info[day]["text"])
st.link_button("📺 فيديو التمرين", exercise_info[day]["link"])

st.divider()
st.info("💡 نصيحة روز: الالتزام هو سر الوصول لوزن 55 كجم. استمري!")
