import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الهوية البصرية (Ultra-Clear Apple Style)
st.set_page_config(page_title="Rose Smart Coach", page_icon="🌸", layout="centered")

st.markdown("""
    <style>
    /* خلفية التطبيق العامة هادئة جداً */
    .stApp { 
        background: linear-gradient(180deg, #FDFCFB 0%, #E2D1C3 100%); 
    }
    
    /* حل مشكلة وضوح الخط: بطاقة بيضاء ناصعة 100% */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 12px;
        border: 1px solid #DDDDDD;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }
    
    /* الخطوط: سوداء صريحة وسميكة لضمان الوضوح التام */
    h1, h2, h3, p, label, span, .stMarkdown { 
        color: #000000 !important; 
        font-family: -apple-system, system-ui, sans-serif;
        font-weight: 800 !important;
        line-height: 1.5;
    }

    /* تحسين شكل صناديق الإدخال */
    .stNumberInput input, .stSelectbox select, .stTextArea textarea {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    /* الأزرار بلون السلمون المعتمد مع خط أسود واضح */
    .stButton > button {
        background-color: #F3C3B2 !important; 
        color: #000000 !important;
        border-radius: 15px;
        border: 2px solid #000000;
        font-weight: bold;
        height: 50px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌸 مدرب روز الذكي المتكامل")
st.write(f"📅 تاريخ اليوم: {datetime.now().strftime('%Y-%m-%d')}")

# 2. ميزة دمج الخطط الخارجية والذكاء الاصطناعي
st.subheader("📝 مزامنة خطتكِ الخارجية")
st.markdown("انسخي خطة التمارين من أي برنامج ذكاء اصطناعي هنا، وسأقوم بترشيح التمارين المناسبة لكِ:")
ai_plan = st.text_area("ألصقي خطتكِ هنا:", placeholder="مثال: أريد التركيز على نحت الخصر والكارديو...")

if ai_plan:
    st.markdown("### 🤖 مقترحات المدرب لخطتكِ:")
    # تحليل ذكي للكلمات المفتاحية
    if any(word in ai_plan.lower() for word in ["نحت", "خصر", "بيلاتس", "نيكول"]):
        rec_text = "بناءً على خطتك، التمارين الأنسب هي بيلاتس نيكول لنحت الجسم."
        vid_url = "https://www.youtube.com/watch?v=NxX9p8W09I8"
        btn_label = "▶️ ابدأ تمرين النحت (Nicole)"
    elif any(word in ai_plan.lower() for word in ["حرق", "وزن", "كارديو", "دهون"]):
        rec_text = "خطتكِ تركز على الحرق؛ أرشح لكِ تمارين الكارديو المكثف."
        vid_url = "https://www.youtube.com/watch?v=gC_L9qAHVJ8"
        btn_label = "▶️ ابدأ تمرين الحرق (Cardio)"
    else:
        rec_text = "خطة شاملة! تمارين كلو تينج ستساعدكِ في الوصول لهدفكِ."
        vid_url = "https://www.youtube.com/watch?v=2MoGxae-zyo"
        btn_label = "▶️ ابدأ تمرين (Chloe Ting)"
    
    st.info(rec_text)
    st.link_button(btn_label, vid_url)

st.divider()

# 3. تحليل بيانات الجسم (الطول، الوزن، السعرات)
st.subheader("📊 القياسات البدنية الذكية")
col_h, col_cw, col_tw = st.columns(3)
with col_h:
    h = st.number_input("الطول (سم):", value=160)
with col_cw:
    cw = st.number_input("الوزن الحالي:", value=60.0)
with col_tw:
    tw = st.number_input("الهدف:", value=55.0)

# الحسابات
bmi = cw / ((h/100)**2)
calories_to_lose = (cw * 22) - 300 # معادلة بسيطة لخسارة الوزن

c1, c2 = st.columns(2)
with c1:
    st.metric("مؤشر الكتلة (BMI)", f"{bmi:.1f}")
with c2:
    st.metric("السعرات اليومية", f"{int(calories_to_lose)} kcal")

st.divider()

# 4. أدوات المتابعة اليومية
st.subheader("⚙️ أدوات روز اليومية")
tab1, tab2, tab3 = st.tabs(["💧 الماء", "📏 القياسات", "⏱️ المؤقت"])

with tab1:
    if 'water' not in st.session_state: st.session_state.water = 0
    if st.button("🥤 شربت كوباً"): st.session_state.water += 1
    st.write(f"لقد شربتِ {st.session_state.water} من أصل 12 كوباً")
    st.progress(min(st.session_state.water/12, 1.0))

with tab2:
    st.number_input("محيط الخصر (سم):", value=70, key="waist")
    st.number_input("محيط الأرداف (سم):", value=90, key="hips")
    if st.button("💾 حفظ القياسات"):
        st.toast("تم حفظ القياسات بنجاح!")
        with tab3:
    timer_sec = st.number_input("ثواني التمرين:", value=30)
    if st.button("🏁 ابدأ المؤقت"):
        ph = st.empty()
        for i in range(timer_sec, 0, -1):
            ph.markdown(f"### ⏳ المتبقي: {i} ثانية")
            time.sleep(1)
        ph.success("✅ عمل رائع! انتهى الوقت.")

st.sidebar.caption("نسخة روز النهائية • وضوح فائق • روابط مباشرة")
