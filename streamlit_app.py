import streamlit as st

# 1. إعدادات الواجهة الاحترافية 2026
st.set_page_config(page_title="Zuhour Fitness Elite", page_icon="🧘‍♀️", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    div[data-testid="stVerticalBlock"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 30px; padding: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-top: 10px solid #00d2ff;
    }
    h1, h2, h3, p, label { color: #2c3e50 !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stButton > button {
        background: linear-gradient(to right, #00d2ff, #3a7bd5) !important;
        color: white !important; font-weight: bold; border-radius: 15px;
        height: 50px; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. إضافة صورة فتاة تتمرن (شكل مبهج)
col_img, col_txt = st.columns([1, 2])
with col_img:
    # رابط لصورة متحركة لفتاة تمارس الرياضة لتعطي روحاً للموقع
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJieHlxbm5qbm5qbm5qbm5qbm5qbm5qbm5qbm5qbm5qbm5qJmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1z/3o7TKMGpxxygWvS8Y8/giphy.gif", width=150)
with col_txt:
    st.title("أهلاً بكِ في عالم الرشاقة")
    st.write("رحلتكِ نحو الـ 55 كجم تبدأ بابتسامة وإصرار! ✨")

# --- القسم 1: القياسات والوزن المثالي ---
st.subheader("📏 قياسات الجسم والهدف")
c1, c2 = st.columns(2)
with c1:
    h = st.number_input("الطول (سم):", value=160)
with c2:
    w = st.number_input("الوزن الحالي (كجم):", value=65.0)

ideal_w = h - 105
st.info(f"💡 الوزن المثالي المقترح لكِ عالمياً هو: {ideal_w} كجم")

# --- القسم 2: عداد الماء والكاميرا الخلفية ---
st.divider()
st.subheader("💧 شرب الماء وتوثيق الوجبات")
if 'water' not in st.session_state: st.session_state.water = 0

col_w, col_cam = st.columns(2)
with col_w:
    if st.button("🥤 إضافة كوب ماء"):
        st.session_state.water += 1
    st.write(f"الأكواب: {st.session_state.water} / 12")

with col_cam:
    food_photo = st.camera_input("📷 تصوير الوجبة (خلفية)")

# --- القسم 3: التمارين العالمية الموثوقة ---
st.divider()
st.subheader("🤖 ترشيح التمارين (محتوى عالمي)")
plan = st.text_area("ما هو هدف تمرين اليوم؟ (مثلاً: نحت، حرق، شد)")

if plan:
    if any(word in plan.lower() for word in ["نحت", "خصر"]):
        url = "https://www.youtube.com/watch?v=3Pr6n-nKnAA" # Emi Wong
        st.success("تم اختيار تمرين 'Emi Wong' العالمي لنحت الخصر")
    else:
        url = "https://www.youtube.com/watch?v=2MoGxae-zyo" # Chloe Ting
        st.success("تم اختيار تحدي 'Chloe Ting' لحرق الدهون")
    st.link_button("▶️ ابدأ التمرين الآن", url)

st.sidebar.markdown(f"### سجل زهور ✨\nالوزن: {w} كجم\nالهدف: {ideal_w} كجم")
