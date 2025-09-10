import streamlit as st
from datetime import datetime

st.title("🎉 برنامج حساب العمر الفكاهي 🎂")

# إدخال تاريخ الميلاد
birth_date = st.date_input("📅 أدخل تاريخ ميلادك:")

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

    # تقديرات حياتية
    breaths = minutes * 16
    heartbeats = minutes * 70
    laughs = days * 13
    sleep_years = years // 3
    food_tons = years * 1

    # نص فكاهي
    story = f"""
    🎂 عمرك اليوم: {years} سنة  
    ⏳ هذا يعني أنك عشت: {months} شهر – {weeks} أسبوع – {days} يوم  

    🕒 أي ما يعادل:  
    - {hours:,} ساعة  
    - {minutes:,} دقيقة  
    - {seconds:,} ثانية  

    🌬️ تنفست حوالي: {breaths:,} نفس  
    ❤️ قلبك دق: {heartbeats:,} مرة (آه يا قلبي ♥)  
    😂 ضحكت تقريبًا: {laughs:,} مرة  
    🛌 نمت حوالي: {sleep_years} سنوات  
    🍔 أكلت ما يعادل: {food_tons} طن طعام  

    🚀 رحلة حياة طويلة، بس الأجمل أنها مستمرة بالحمد لله 🤍
    """

    st.markdown(story)
