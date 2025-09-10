import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

st.set_page_config(page_title="برنامج حساب العمر الفكاهي", page_icon="🎂", layout="centered")

st.title("🎉 برنامج حساب العمر الفكاهي 🎂")

# إدخال تاريخ الميلاد
birth_date = st.date_input(
    "📅 أدخل تاريخ ميلادك:",
    min_value=datetime(1900, 1, 1),
    max_value=datetime.today()
)

if birth_date:
    today = datetime.today().date()
    delta = today - birth_date

    # حساب العمر
    years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1

    months = years * 12 + (today.month - birth_date.month)
    days = delta.days
    weeks = days // 7
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    # تقديرات حياتية تقريبية
    breaths = minutes * 16
    heartbeats = minutes * 70
    laughs = days * 13
    sleep_years = years // 3
    work_years = years // 4
    food_tons = years * 1.2

    # نص فكاهي
    story = f"""
    🎂 عمرك الحالي: {years} سنة  
    ⏳ هذا يعني أنك عشت: {months} شهر – {weeks} أسبوع – {days} يوم  

    🕒 أي ما يعادل:  
    - {hours:,} ساعة  
    - {minutes:,} دقيقة  
    - {seconds:,} ثانية  

    🌬️ تنفست حوالي: {breaths:,} نفس  
    ❤️ قلبك دق: {heartbeats:,} مرة  
    😂 ضحكت تقريبًا: {laughs:,} مرة  
    🛌 نمت حوالي: {sleep_years} سنوات  
    💼 قضيت في العمل: {work_years} سنوات  
    🍔 أكلت ما يعادل: {food_tons:.1f} طن طعام  

    🚀 رحلة حياة طويلة، والأجمل أنها مستمرة بالحمد لله 🤍
    """

    st.markdown(story)

    # 📊 رسم بياني لحياتك
    st.subheader("📊 حياتك موزعة هكذا:")
    labels = ["نوم 🛌", "عمل 💼", "ضحك 😂", "أكل 🍔", "باقي الحياة 🌍"]
    sizes = [sleep_years, work_years, years * 0.5, years * 0.3, years - (sleep_years + work_years)]
    colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFD966", "#D9B3FF"]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    # 🔗 روابط المشاركة
    st.subheader("🔗 شارك نتيجتك مع الأصدقاء:")
    whatsapp_url = f"https://wa.me/?text=🎂 عمري {years} سنة! جرب برنامج حساب العمر الفكاهي هنا: https://funnyage.streamlit.app"
    facebook_url = f"https://www.facebook.com/sharer/sharer.php?u=https://funnyage.streamlit.app"
    st.markdown(f"[📱 شارك على واتساب]({whatsapp_url})")
    st.markdown(f"[🌐 شارك على فيسبوك]({facebook_url})")

# توقيع في الأسفل
st.markdown("---")
st.markdown("✨ تم إنشاؤه بواسطة *محمود ناصيف (أبو عبد الرحمن)* ✨")
