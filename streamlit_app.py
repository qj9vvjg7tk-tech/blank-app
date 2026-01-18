import streamlit as st
import time

# 1. إعدادات الواجهة الرياضية
st.set_page_config(page_title="Zuhour Fitness 2026", page_icon="⚖️", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%); }
    div[data-testid="stVerticalBlock"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 20px; padding: 25px;
        border-right: 12px solid #FF8C00;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    h1, h2, h3, p, label { color: #000000 !important; font-weight: 900 !important; }
    .stButton > button {
        background-color: #FF8C00 !important; color: white !important;
        font-weight: bold; height: 50px; border-radius: 15px; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ مستشاركِ الصحي: الوزن والطول")

# --- القسم الجديد: حاسبة الوزن المثالي الذكية ---
st.subheader("📏 تنسيق الوزن المثالي بناءً على طولكِ")
col_h, col_w = st.columns(2)

with col_h:
    user_height = st.number_input("أدخلي طولكِ (سم):", min_value=120, max_value=220, value=160)
with col_w:
    user_weight = st.number_input("وزنكِ الحالي (كجم):", min_value=30.0, max_value=200.0, value=65.0)

# حساب الوزن المثالي (معادلة متوسطة للرشاقة)
ideal_weight = user_height - 105 
bmi = user_weight / ((user_height/100)**2)

st.info(f"💡 بناءً على طولكِ ({user_height} سم)، الوزن المثالي المقترح لكِ هو: {ideal_weight} كجم")

# تحليل الفرق
diff = user_weight - ideal_weight
if diff > 0:
    st.warning(f"🎯 متبقي لكِ {diff:.1f} كجم للوصول للوزن المثالي. استمري في التمارين!")
elif diff == 0:
    st.success("🎉 مذهل! أنتِ في الوزن المثالي تماماً.")
else:
    st.info(f"✨ أنتِ تحت الوزن المثالي بـ {abs(diff):.1f} كجم. ركزي على التغذية وبناء العضلات.")

# عرض مؤشر كتلة الجسم (BMI)
st.write(f"مؤشر كتلة جسمكِ الحالي: {bmi:.1f}")

st.divider()

# --- قسم شرب الماء (المستعاد) ---
st.subheader("🥤 هدف شرب الماء اليومي")
if 'water' not in st.session_state:
    st.session_state.water = 0

c1, c2 = st.columns([2, 1])
with c1:
    st.write(f"الأكواب المستهلكة: {st.session_state.water} / 12")
    st.progress(min(st.session_state.water / 12, 1.0))
with c2:
    if st.button("➕ إضافة كوب"):
        st.session_state.water += 1

st.divider()

# --- الأقسام الإضافية (الكاميرا والترشيح) ---
if st.toggle("🛠️ إظهار الأدوات الإضافية (كاميرا وترشيح AI)"):
    tab1, tab2 = st.tabs(["📸 تصوير الطعام", "🤖 ترشيح التمارين"])
    with tab1:
        st.camera_input("صوري وجبتكِ")
    with tab2:
        plan = st.text_area("ألصقي خطتكِ هنا:")
        if plan:
            st.link_button("🚀 ابدأ التمرين المناسب", "https://www.youtube.com/watch?v=v2r0zYnFmxo")

st.sidebar.markdown(f"### ملخص اليوم\n**
