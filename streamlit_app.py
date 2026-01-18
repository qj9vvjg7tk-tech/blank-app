import streamlit as st
import time

# 1. إعداد واجهة روز الاحترافية
st.set_page_config(page_title="Rose Health & Fitness", page_icon="🌸", layout="centered")

# تصميم الألوان المبهجة
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    h1, h2, h3 { color: #D02090 !important; font-family: 'Arial'; }
    .stButton>button { background-color: #D02090; color: white; border-radius: 20px; border: none; width: 100%; }
    .stProgress > div > div > div > div { background-color: #FF69B4; }
    .css-1offfwp { background-color: #D02090 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌸 الروتين الصحي مع روز")
st.write("---")

# 2. قسم شرب الماء
st.subheader("💧 عداد شرب الماء (الهدف: 3 لتر)")
if 'water' not in st.session_state: st.session_state.water = 0
col_w1, col_w2 = st.columns([2, 1])
with col_w1:
    st.progress(min(st.session_state.water / 12, 1.0))
with col_w2:
    if st.button("🥛 شربت كوباً"): st.session_state.water += 1
if st.session_state.water >= 12: st.success("🏆 بطلة الارتواء! مبروك الوسام")

st.divider()

# 3. متابعة الوزن والهدف
st.subheader("📈 متابعة الوزن والهدف")
cw_col, tw_col = st.columns(2)
with cw_col:
    current_weight = st.number_input("وزنكِ الحالي (كجم):", value=60.0, step=0.1)
with tw_col:
    target_weight = st.number_input("هدفكِ الشخصي (كجم):", value=55.0, step=0.1)

diff = round(current_weight - target_weight, 1)
if diff > 0: st.info(f"✨ باقي لكِ {diff} كجم للوصول للرشاقة!")
elif diff == 0: 
    st.balloons()
    st.success("🎉 أحسنتِ! لقد وصلتِ لهدفكِ!")

st.divider()

# 4. قسم قياسات الجسم (الجديد ✨)
st.subheader("📏 سجل قياسات الجسم (بالسنتمتر)")
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    waist = st.number_input("الخصر:", min_value=40, max_value=150, value=70)
with col_m2:
    hips = st.number_input("الأرداف:", min_value=40, max_value=150, value=90)
with col_m3:
    arm = st.number_input("الذراع:", min_value=10, max_value=60, value=25)

if st.button("حفظ القياسات الأسبوعية 📝"):
    st.toast(f"تم حفظ قياساتكِ: خصر {waist}سم، أرداف {hips}سم. واصلي التقدم!")

st.divider()

# 5. مؤقت التمرين
st.subheader("⏱️ مؤقت التمرين")
t_col1, t_col2 = st.columns(2)
with t_col1:
    seconds = st.number_input("ثواني التمرين:", min_value=0, value=30)
with t_col2:
    if st.button("ابدأ التحدي 🚀"):
        with st.empty():
            while seconds > 0:
                st.write(f"💖 استمري.. المتبقي: {seconds} ثانية")
                time.sleep(1)
                seconds -= 1
            st.write("✅ بطلة! انتهى التمرين!")

st.divider()

# 6. سجل الوجبات والكاميرا
st.subheader("📸 سجل الوجبات والسعرات")
if 'calories' not in st.session_state: st.session_state.calories = 0
c_col1, c_col2 = st.columns(2)
with c_col1:
    cal_in = st.number_input("سعرات الوجبة:", min_value=0)
    if st.button("إضافة ➕"): st.session_state.calories += cal_in
with c_col2:
    st.warning(f"مجموع السعرات: {st.session_state.calories}")

tab_up, tab_cam = st.tabs(["📤 رفع من الاستوديو", "📸 تصوير مباشر"])
with tab_up:
    up_file = st.file_uploader("ارفعي صورة وجبتكِ", type=["jpg", "png"])
with tab_cam:
    pic = st.camera_input("صوري وجبتكِ")

st.divider()

# 7. مكتبة التمارين
st.subheader("📺 مكتبة تمارين روز")
category = st.selectbox("نوع التمرين:", ["Pilates + Hip Dips", "Low-Impact Cardio", "Walk"])
st.info("اختاري الفيديو من القائمة المنسدلة واضغطي 'فتح الفيديو'.")

st.divider()

# 8. مفكرة روز
st.subheader("📝 خربشات روز الصحية")
journal_entry = st.text_area("عبري عن شعوركِ اليوم...")
if st.button("حفظ الملاحظة ✨"):
    st.toast("تم حفظ ذكرياتكِ الجميلة!")

st.sidebar.markdown("### 🌸 قائمة روز")
st.sidebar.info("💡 لا تنسي إضافة التطبيق للشاشة الرئيسية بالضغط على Share ثم Add to Home Screen.")
