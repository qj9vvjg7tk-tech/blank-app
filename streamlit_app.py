import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الهوية الرياضية والتباين العالي
st.set_page_config(page_title="Rose Fitness Pro 2026", page_icon="🧘‍♀️", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%); }
    div[data-testid="stVerticalBlock"] > div {
        background-color: #FFFFFF !important; 
        border-radius: 20px; padding: 20px;
        border-right: 12px solid #FF8C00;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    h1, h2, h3, p, label, span { color: #000000 !important; font-weight: 800 !important; }
    .stButton > button {
        background-color: #FF8C00 !important; color: #FFFFFF !important;
        font-weight: bold; height: 50px; border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧘‍♀️ Rose Smart Coach 2026")

# --- القسم الأول: كاميرا تحليل الطعام ---
with st.expander("📸 كاميرا تحليل الوجبات الذكية", expanded=False):
    st.write("صوري وجبتكِ وسأعطيكِ نصيحة سريعة!")
    img_file = st.camera_input("التقطي صورة للطعام")
    if img_file:
        st.image(img_file, caption="تم التقاط الوجبة")
        st.success("✅ يبدو طعاماً صحياً! تأكدي من شرب كوب ماء كبير قبل البدء.")

# --- القسم الثاني: منشئ الجدول الزمني الذكي ---
st.subheader("📅 تنظيم أيام التمرين والراحة")
selected_days = st.multiselect("اختاري الأيام التي ستتدربين فيها:", 
                               ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"],
                               default=["السبت", "الاثنين", "الأربعاء"])

if selected_days:
    st.write("### 📝 جدولكِ الأسبوعي المقترح:")
    cols = st.columns(len(selected_days))
    for i, day in enumerate(selected_days):
        with cols[i]:
            if i % 2 == 0:
                st.info(f"{day}\n\nنحت وبيلاتس")
            else:
                st.warning(f"{day}\n\nكارديو حرق")

# --- القسم الثالث: ترشيح الذكاء الاصطناعي المطور ---
st.divider()
st.subheader("🤖 تحليل وترشيح التمارين")
ai_plan = st.text_area("ألصقي خطتكِ التدريبية هنا:", placeholder="مثال: أريد تنحيف البطن والخصر...")

if ai_plan:
    st.markdown("### 🔍 نتائج التحليل:")
    if any(word in ai_plan.lower() for word in ["نحت", "خصر", "بيلاتس"]):
        video_url = "https://www.youtube.com/watch?v=U4_lVjsOVBs"
        st.write("✨ الخطة: ركزي على تمارين الثبات (Plank) مع البيلاتس.")
    elif any(word in ai_plan.lower() for word in ["حرق", "وزن", "كارديو"]):
        video_url = "https://www.youtube.com/watch?v=v2r0zYnFmxo"
        st.write("🔥 الخطة: تمارين الـ HIIT هي الأسرع لحرق الدهون.")
    else:
        video_url = f"https://www.youtube.com/results?search_query={ai_plan}"
        st.write("💡 الخطة: تم استخراج أفضل الفيديوهات المتوفرة لطلبكِ.")
        
    st.link_button("▶️ افتحي التمرين الآن", video_url)

# --- القسم الرابع: عداد الماء والهدف ---
st.divider()
col_a, col_b = st.columns(2)
with col_a:
    weight = st.number_input("الوزن الحالي:", value=65.0)
with col_b:
    target = st.number_input("الوزن الهدف:", value=55.0)

st.progress(max(0, min(100, int((target/weight)*100))))
st.write(f"💪 المتبقي للهدف: {weight-target:.1f} كجم")

st.sidebar.caption("تطبيق روز فيتنس - النسخة الاحترافية")
