import streamlit as st
import time

# 1. إعدادات الواجهة الرياضية والوضوح العالي
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

st.title("⚖️ حاسبة الرشاقة والوزن المثالي")

# --- القسم الجديد: حساب الوزن المثالي بناءً على الطول ---
st.subheader("📏 تنسيق الوزن المثالي")
col_h, col_w = st.columns(2)

with col_h:
    h = st.number_input("أدخلي طولكِ (سم):", min_value=120, max_value=220, value=160)
with col_w:
    w = st.number_input("وزنكِ الحالي (كجم):", min_value=30.0, value=65.0)

# معادلة الوزن المثالي والـ BMI
ideal_w = h - 105
bmi = w / ((h/100)**2)

st.info(f"💡 الوزن المثالي المقترح لطولكِ هو: {ideal_w} كجم")

# تحليل النتيجة
if w > ideal_w:
    st.warning(f"🎯 متبقي لكِ {w - ideal_w:.1f} كجم للوصول للمثالي. استمري!")
elif w == ideal_w:
    st.success("🎉 مذهل! أنتِ في الوزن المثالي تماماً.")
else:
    st.info(f"✨ أنتِ تحت الوزن المثالي بـ {abs(w - ideal_w):.1f} كجم.")

st.divider()

# --- قسم شرب الماء ---
st.subheader("🥤 عداد شرب الماء")
if 'water' not in st.session_state:
    st.session_state.water = 0

c1, c2 = st.columns([2, 1])
with c1:
    st.write(f"الأكواب: {st.session_state.water} / 12")
    st.progress(min(st.session_state.water / 12, 1.0))
with c2:
    if st.button("🥤 إضافة كوب"):
        st.session_state.water += 1

st.divider()

# --- قسم ترشيح التمارين AI ---
st.subheader("🤖 ترشيح تمارين الذكاء الاصطناعي")
plan = st.text_area("ألصقي خطتكِ التدريبية هنا:")
if plan:
    # روابط 2026 نشطة
    if any(word in plan.lower() for word in ["نحت", "بيلاتس", "خصر"]):
        v_url = "https://www.youtube.com/watch?v=U4_lVjsOVBs"
    else:
        v_url = "https://www.youtube.com/watch?v=v2r0zYnFmxo"
    st.link_button("🚀 ابدأ التمرين المرشح الآن", v_url)

# --- إصلاح شريط المعلومات الجانبي (حل مشكلة الخطأ) ---
st.sidebar.markdown(f"### ملخص البيانات\nالطول: {h} سم\nالوزن: {w} كجم\nالهدف: {ideal_w} كجم")
