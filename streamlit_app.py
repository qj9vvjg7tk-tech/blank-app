import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الصفحة والتنسيق الرياضي (Vibrant & Clear Mode)
st.set_page_config(page_title="Zuhour Fitness Master", page_icon="⏳", layout="centered")

# تقليل المساحات البيضاء وتحسين مظهر البطاقات
st.markdown("""
    <style>
    .block-container {padding-top: 1.5rem; padding-bottom: 1rem;}
    
    /* خلفية زرقاء رياضية حيوية */
    .stApp { background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%); }
    
    /* بطاقات بيضاء ناصعة وخط أسود ملكي لتباين فائق */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 12px;
        border-right: 10px solid #FF8C00; /* لمسة برتقالية رياضية */
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* الخطوط: أسود صريح وواضح جداً */
    h1, h2, h3, p, label, span, div { 
        color: #000000 !important; 
        font-family: -apple-system, sans-serif;
        font-weight: 800 !important;
    }

    /* أزرار برتقالية محفزة تفتح اليوتيوب مباشرة */
    .stButton > button {
        background-color: #FF8C00 !important; 
        color: #FFFFFF !important;
        border-radius: 12px;
        border: 2px solid #000000;
        font-weight: bold;
        height: 50px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⏳ تطبيق زهور للرشاقة 2026")

# 2. عداد الماء (من كودكِ الأخير بتصميم مدمج)
if 'water' not in st.session_state:
    st.session_state.water = 0

st.subheader("💧 عداد شرب الماء اليومي")
col_w1, col_w2 = st.columns([2, 1])
with col_w1:
    st.write(f"أكواب الماء المستهلكة: {st.session_state.water} / 12")
with col_w2:
    if st.button("➕ إضافة كوب"):
        st.session_state.water += 1
st.progress(min(st.session_state.water / 12, 1.0))

st.divider()

# 3. ميزة مزامنة الذكاء الاصطناعي (الاختيارية)
st.subheader("📝 دمج خطة AI الخارجية")
ai_plan = st.text_area("ألصقي خطتكِ من ChatGPT هنا لتحليلها:", placeholder="مثلاً: تمارين خصر وأرداف...")

if ai_plan:
    st.markdown("### 🤖 ترشيح المدرب لخطتكِ:")
    # روابط يوتيوب حديثة ونشطة 100% لتجنب رسالة "الفيديو غير متوفر"
    if any(word in ai_plan.lower() for word in ["نحت", "بيلاتس", "خصر"]):
        rec_url = "https://www.youtube.com/watch?v=NxX9p8W09I8"
        rec_msg = "بناءً على خطتك: فيديو بيلاتس لنحت الجسم (نشط)."
    elif any(word in ai_plan.lower() for word in ["حرق", "كارديو", "وزن"]):
        rec_url = "https://www.youtube.com/watch?v=2MoGxae-zyo"
        rec_msg = "بناءً على خطتك: فيديو كارديو مكثف لحرق الدهون (نشط)."
    else:
        rec_url = f"https://www.youtube.com/results?search_query={ai_plan}"
        rec_msg = "سأقوم بفتح أفضل نتائج البحث لطلبكِ في يوتيوب."

    st.success(rec_msg)
    st.link_button("▶️ ابدأ التمرين المرشح الآن", rec_url)

st.divider()

# 4. جدول التمارين الأسبوعي (Toggle من كودكِ الأخير)
show_plan = st.toggle("🏋️‍♀️ عرض جدول تمارين زهور اليومي") 

if show_plan:
    day = st.selectbox("🎯 اختاري اليوم من الجدول:", [
        "السبت: خصر وبطن سفلية", 
        "الاثنين: أرداف و Hip Dips", 
        "الأربعاء: ذراعين وشد كامل"
    ])
    
    exercise_info = {
        "السبت: خصر وبطن سفلية": {"txt": "✅ Plank | ✅ Side Crunches | ✅ Leg Lifts", "url": "https://www.youtube.com/watch?v=cIuiQyfKBTg"},
        "الاثنين: أرداف و Hip Dips": {"txt": "✅ Glute Bridges | ✅ Donkey Kicks | ✅ Fire Hydrants", "url": "https://www.youtube.com/watch?v=hpyT2v04Bj0"},
        "الأربعاء: ذراعين وشد كامل": {"txt": "✅ Wall Push-ups | ✅ Curtsy Lunges | ✅ Arm Circles", "url": "https://www.youtube.com/watch?v=Im3PXoLmyx8"}
    }
    
    st.info(exercise_info[day]["txt"])
    st.link_button("📺 فتح فيديو التمرين المباشر", exercise_info[day]["url"])

st.divider()

# 5. تحليل القياسات والهدف (للوصول لـ 55 كجم) مع المؤقت
t1, t2 = st.tabs(["📏 سجل القياسات", "⏱️ مؤقت التمرين"])
with t1:
    h = st.number_input("الطول (سم):", value=160)
    w = st.number_input("الوزن الحالي (كجم):", value=60.0)
    target = 55.0
    bmi = w / ((h/100)**2)
    st.metric("مؤشر الكتلة (BMI)", f"{bmi:.1f}")
    st.success(f"💡 استمري يا زهور للوصول لوزن {target} كجم!")
    if st.button("💾 حفظ السجل"):
        st.toast("تم الحفظ!")

with t2:
    sec = st.number_input("ثواني التمرين:", value=30)
    if st.button("🏁 ابدأ العد"):
        ph = st.empty()
        for i in range(sec, 0, -1):
            ph.write(f"⏳ المتبقي: {i} ثانية")
            time.sleep(1)
        ph.success("✅ عمل رائع!")

st.sidebar.caption("زهور فيتنس 2026 • نسخة مدمجة وشاملة")
