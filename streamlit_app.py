import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الواجهة (تجعل التطبيق يتكيف مع الشاشات المختلفة)
st.set_page_config(page_title="Rose Health", page_icon="🌸", layout="centered")

# تطبيق لغة التصميم (Apple Style - Soft UI)
st.markdown("""
    <style>
    /* خلفية متدرجة ناعمة تناسب جميع الأجهزة */
    .stApp {
        background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
    }
    
    /* تصميم البطاقات "Floating Cards" بلمسة آيفون */
    div.stButton > button, div.stSelectbox, div.stNumberInput, .stTextArea, .stAlert {
        background-color: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(10px); /* تأثير الزجاج الضبابي المشهور في آيفون */
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07) !important;
        transition: all 0.3s ease;
    }

    /* العناوين بلون داكن فخم وواضح */
    h1, h2, h3 { 
        color: #333333 !important; 
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        letter-spacing: -0.5px;
    }

    /* تخصيص الأزرار لتكون بارزة وسهلة الضغط بالأصابع */
    .stButton>button {
        background: #FF007F !important; /* لون فوشيا قوي */
        color: white !important;
        font-weight: 600 !important;
        padding: 12px !important;
    }

    /* جعل شريط التقدم أنحف وأكثر أناقة */
    .stProgress > div > div > div > div {
        background-color: #FF007F !important;
        height: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ترويسة التطبيق ---
st.title("🌸 الروتين الصحي مع روز")
day_name = datetime.now().strftime("%A")
st.caption(f"✨ مرحباً بكِ اليوم {day_name} في رحلة الـ 55 كجم")

# 2. نصيحة اليوم (بطاقة ذكية)
st.info("💡 هدف اليوم الصغير: حاولي تقليل الملح في وجباتكِ لتجنب حبس السوائل.")

# 3. قسم النشاط اليومي (مرتب في أعمدة تتغير حسب حجم الشاشة)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💧 الهيدرات")
    if 'water' not in st.session_state: st.session_state.water = 0
    c1, c2 = st.columns([1, 1])
    with c1:
        if st.button("🥤 إضافة"): st.session_state.water += 1
    with c2:
        st.write(f"{st.session_state.water} / 12")
    st.progress(min(st.session_state.water / 12, 1.0))

with col2:
    st.markdown("### 📈 الميزان")
    cw = st.number_input("الحالي:", value=60.0, step=0.1, key="weight_input")
    target = st.number_input("الهدف:", value=55.0, step=0.1, key="target_input")

st.divider()

# 4. سجل القياسات (تخطيط مرن)
st.markdown("### 📏 قياسات الجسم الأسبوعية")
m1, m2, m3 = st.columns(3)
with m1: st.number_input("الخصر (سم):", value=70)
with m2: st.number_input("الأرداف (سم):", value=90)
with m3: st.number_input("الذراع (سم):", value=25)

st.divider()

# 5. مكتبة الفيديو (القائمة الكاملة بقوة بصرية)
st.markdown("### 📺 مكتبة التمارين المحدثة")
cat = st.selectbox("اكتشفي الفئات:", ["Pilates + Hip Dips", "Low-Impact Cardio", "Walk"])

videos = {
    "Pilates + Hip Dips": {
        "Move With Nicole – 20 Min Pilates Abs": "https://www.youtube.com/watch?v=NxX9p8W09I8",
        "Move With Nicole – Side Leg Lifts": "https://www.youtube.com/watch?v=v76L87Xq1E0",
        "Move With Nicole – Pilates Booty": "https://www.youtube.com/watch?v=0_37Lh_XFmE",
        "Move With Nicole – Glute Bridges": "https://www.youtube.com/watch?v=f639W1Xf3wM",
        "Blogilates – Pilates Arms": "https://www.youtube.com/watch?v=hAGfBjvIRFI",
        "Blogilates – Curtsy Lunges": "https://www.youtube.com/watch?v=Lp_9m2M7mS4"
    },
    "Low-Impact Cardio": {
        "Grow With Jo – Cardio": "https://www.youtube.com/watch?v=gC_L9qAHVJ8",
        "Grow With Jo – Walk & Dance": "https://www.youtube.com/watch?v=8p_h2L_L8X8"
    },
    "Walk": {
        "Leslie – 30 Min Walk": "https://www.youtube.com/watch?v=enYITYwvPAQ"
    }
}

selected_vid = st.selectbox("اختاري الفيديو المفضل:", list(videos[cat].keys()))
st.link_button(f"▶️ تشغيل: {selected_vid}", videos[cat][selected_vid])

st.divider()
# 6. الأدوات (Tabs مرتبة للموبايل)
st.markdown("### ⚙️ الأدوات المساعدة")
t_timer, t_cam, t_note = st.tabs(["⏱️ مؤقت", "📸 وجبة", "📝 مفكرة"])

with t_timer:
    sec = st.number_input("ثواني التمرين:", value=30)
    if st.button("🚀 ابدأ الآن"):
        ph = st.empty()
        for i in range(sec, 0, -1):
            ph.write(f"⌛ المتبقي: {i}")
            time.sleep(1)
        ph.write("🔥 انتهى الوقت! بطلة!")

with t_cam:
    st.file_uploader("ارفعي صورة (خلفية)", type=["jpg", "png"])
    st.camera_input("تصوير مباشر (أمامية)")

with t_note:
    st.text_area("عن ماذا تفكرين اليوم؟")
    if st.button("✅ حفظ"): st.toast("تم الحفظ!")

st.sidebar.markdown("---")
st.sidebar.info("💡 تطبيق روز: مصمم ليعمل بكفاءة على جميع أجهزتكِ.")
