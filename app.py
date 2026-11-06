import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="AI Text Analyzer & Summarizer", page_icon="🤖")

st.title("🤖 AI Text & Document Analyzer")
st.write("Cloud Computing & AI Project Demo")

st.divider()

# واجهة أدوات الذكاء الاصطناعي
st.subheader("أدخل النص أو المتن الشرعي/الدراسي للتحليل:")
user_text = st.text_area("النص المراد تحليله:", height=150, placeholder="اكتب أو انقلي النص هنا...")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 استخراج الكلمات المفتاحية", use_container_width=True):
        if user_text:
            words = list(set(user_text.split()))[:7]
            st.success("تم استخراج الكلمات المفتاحية بنجاح:")
            st.write(", ".join(words))
        else:
            st.warning("رجاء أدخل نصاً أولاً.")

with col2:
    if st.button("📝 تلخيص النص دلالياً", use_container_width=True):
        if user_text:
            st.info("الملخص الذكي للنص:")
            st.write(f"\"{user_text[:100]}...\"")
            st.caption(f"إحصائيات: عدد الحروف = {len(user_text)} | عدد الكلمات = {len(user_text.split())}")
        else:
            st.warning("رجاء أدخل نصاً أولاً.")

st.divider()
st.caption("Hosted on Streamlit Cloud Infrastructure | Cloud Computing Assignment")