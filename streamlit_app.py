import streamlit as st
import time

# 1. إعداد واجهة روز الاحترافية
st.set_page_config(page_title="Rose Health & Fitness", page_icon="🌸", layout="centered")

# تصميم الألوان المبهجة مع ضمان وضوح الخطوط
st.markdown("""
    <style>
    .stApp { 
        background-color: #FFF0F5; 
    }
    h1, h2, h3, p, span, label { 
        color: #4B0082 !important; /* لون بنفسجي غامق جداً لضمان الوضوح التام */
        font-family: 'Arial'; 
    }
    .stButton>button { 
        background-color: #D02090; 
        color: white !important; 
        border-radius: 20px; 
    }
    /* ضمان وضوح نصوص الإدخال */
    .stNumberInput label, .stTextInput label {
        color: #4B0082 !important;
        font-weight: bold;
    }
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
st.write(f"لقد شربتِ: {st.session_state.water} من 12 كوباً.")

st.divider()

# 3. متابعة الوزن والهدف
st.subheader("📈 متابعة الوزن والهدف")
cw_col, tw_col = st.columns(2)
with cw_col:
    current_weight = st.number_input("وزنكِ الحالي (كجم):", value=60.0, step=0.1, key="cw")
with tw_col:
    target_weight = st.number_input("هدفكِ الشخصي (كجم):", value=55.0, step=0.1, key="tw")

diff = round(current_weight - target_weight, 1)
if diff > 0: st.info(f"✨ باقي لكِ {diff} كجم للوصول للرشاقة!")

st.divider()

# 4. سجل قياسات الجسم
st.subheader("📏 سجل قياسات الجسم (بالسنتمتر)")
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    waist = st.number_input("الخصر:", value=70, key="waist")
with col_m2:
    hips = st.number_input("الأرداف:", value=90, key="hips")
with col_m3:
    arm = st.number_input("الذراع:", value=25, key="arm")

st.divider()

# 5. مؤقت التمرين
st.subheader("⏱️ مؤقت التمرين")
t_col1, t_col2 = st.columns(2)
with t_col1:
    seconds = st.number_input("ثواني التمرين:", min_value=0, value=30, key="timer_sec")
with t_col2:
    if st.button("ابدأ التحدي 🚀"):
        with st.empty():
            while seconds > 0:
                st.write(f"💖 استمري.. المتبقي: {seconds} ثانية")
                time.sleep(1)
                seconds -= 1
            st.write("✅ بطلة! انتهى التمرين!")

st.divider()

# 6. سجل الوجبات
st.subheader("📸 سجل الوجبات")
tab_up, tab_cam = st.tabs(["📤 رفع من الاستوديو", "📸 تصوير مباشر"])
with tab_up:
    up_file = st.file_uploader("ارفعي صورة وجبتكِ", type=["jpg", "png"])
with tab_cam:
    pic = st.camera_input("صوري وجبتكِ")

st.divider()

# 7. مفكرة روز
st.subheader("📝 خربشات روز الصحية")
journal_entry = st.text_area("عبري عن شعوركِ اليوم...", key="journal")
if st.button("حفظ الملاحظة ✨"):
    st.toast("تم حفظ ذكرياتكِ الجميلة!")
