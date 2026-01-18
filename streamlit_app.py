import streamlit as st
import time

# 1. التنسيق الرياضي المتقدم
st.set_page_config(page_title="Zuhour Fitness 2026", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%); }
    div[data-testid="stVerticalBlock"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 20px; padding: 25px;
        border-right: 12px solid #FF8C00;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    h1, h2, h3, p, label { color: #000000 !important; font-weight: 900 !important; }
    .stButton > button {
        background-color: #FF8C00 !important; color: white !important;
        font-weight: bold; height: 55px; width: 100%; border: 2px solid #000;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ مدربكِ الشخصي الذكي 2026")

# 2. خانة الهدف القابلة للتغيير (التحديث الجديد)
st.subheader("🎯 حددي هدفكِ الشخصي")
col1, col2 = st.columns(2)

with col1:
    current_weight = st.number_input("الوزن الحالي (كجم):", min_value=30.0, max_value=200.0, value=65.0, step=0.1)
with col2:
    target_weight = st.number_input("الوزن المستهدف (كجم):", min_value=30.0, max_value=200.0, value=55.0, step=0.1)

# حساب المتبقي
to_lose = current_weight - target_weight

if to_lose > 0:
    st.warning(f"💪 متبقي لكِ {to_lose:.1f} كجم للوصول للهدف. أنتِ قادرة على فعلها!")
    # شريط تقدم وهمي للتحفيز
    progress = max(0, min(100, int((target_weight / current_weight) * 100)))
    st.write("مستوى القرب من الوزن المثالي:")
    st.progress(progress)
elif to_lose == 0:
    st.success("🎉 مبروك! لقد وصلتِ لوزنكِ المثالي. حافظي عليه!")
else:
    st.info(f"✨ أنتِ تحت الوزن المستهدف بـ {abs(to_lose):.1f} كجم. ركزي على بناء العضلات!")

st.divider()

# 3. ميزة الترشيح الذكي (روابط 2026 نشطة)
st.subheader("📝 ترشيح التمارين بناءً على خطتكِ")
ai_plan = st.text_area("ألصقي خطتكِ هنا لتحليلها وترشيح فيديو مناسب:", height=100)

if ai_plan:
    if any(word in ai_plan.lower() for word in ["نحت", "بيلاتس", "خصر"]):
        video_url = "https://www.youtube.com/watch?v=U4_lVjsOVBs"
        message = "✅ تمرين النحت والبيلاتس المخصص لكِ جاهز"
    elif any(word in ai_plan.lower() for word in ["حرق", "كارديو", "وزن"]):
        video_url = "https://www.youtube.com/watch?v=v2r0zYnFmxo"
        message = "✅ تمرين الكارديو وحرق الدهون المكثف جاهز"
    else:
        video_url = f"https://www.youtube.com/results?search_query={ai_plan}"
        message = "✅ تم العثور على تمارين تناسب خطتكِ"

    st.success(message)
    st.link_button("🚀 ابدئي التمرين الآن", video_url)

st.divider()

# 4. جدول التمارين الأسبوعي
if st.toggle("🏋️‍♀️ عرض الجدول الأسبوعي"):
    day = st.selectbox("🎯 اختر اليوم:", ["السبت: خصر وبطن", "الاثنين: كارديو", "الأربعاء: شد كامل"])
    urls = {
        "السبت: خصر وبطن": "https://www.youtube.com/watch?v=0cwkkKjvAjE",
        "الاثنين: كارديو": "https://www.youtube.com/watch?v=5JY9FZATqVA",
        "الأربعاء: شد كامل": "https://www.youtube.com/watch?v=W2VEUWqeS88"
    }
    st.link_button("📺 فتح الفيديو", urls[day])

st.sidebar.write(f"👤 مستخدم التطبيق الحالي")
st.sidebar.info(f"الهدف الحالي: {target_weight} كجم")
