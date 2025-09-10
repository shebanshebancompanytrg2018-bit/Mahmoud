import streamlit as st
from datetime import datetime
import plotly.express as px
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="برنامج حساب العمر الفكاهي", page_icon="🎂", layout="centered")

# رسالة في البداية
st.markdown("<h2 style='text-align:center; color:green;'>🌹 لا تنسوا الصلاة على النبي ﷺ 🌹</h2>", unsafe_allow_html=True)

st.title("🎉 برنامج حساب العمر الفكاهي 🎂")

# رابط التطبيق (عدّله حسب رابطك الفعلي على Streamlit Cloud)
APP_URL = "https://funnyage.streamlit.app"

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

    # تقسيم العمر على أنشطة الحياة (تقديرات تقريبية)
    sleep_years = round(years * 0.33, 2)   
    work_years  = round(years * 0.25, 2)   
    eat_years   = round(years * 0.04, 2)   
    laugh_years = round(years * 0.02, 2)   
    rest_years  = max(0.0, round(years - (sleep_years + work_years + eat_years + laugh_years), 2))

    # عرض النتائج
    st.markdown(
        f"""
*🎂 عمرك الحالي:* {years} سنة  
*⏳ عشت حتى الآن:* {months} شهر – {weeks} أسبوع – {days} يوم  

*🕒 وهذا يعادل:*  
* {hours:,} ساعة  
* {minutes:,} دقيقة  
* {seconds:,} ثانية  

*🌬️ أنفاسك:* {breaths:,} نفس  
*❤️ دقات قلبك:* {heartbeats:,} نبضة  
*😂 ضحكاتك:* {laughs:,} مرة  
*🛌 نومك التقريبي:* {sleep_years} سنة  
*💼 عملك التقريبي:* {work_years} سنة  
*🍔 وقتك في تناول الطعام:* {eat_years} سنة  
""",
        unsafe_allow_html=False
    )

    # 📊 رسم دائري
    st.subheader("📊 توزيع حياتك التقريبي")
    pie_df = pd.DataFrame({
        "النشاط": ["🛌 نوم", "💼 عمل", "🍔 أكل", "😂 ترفيه/ضحك", "🌍 باقي الحياة"],
        "سنوات": [sleep_years, work_years, eat_years, laugh_years, rest_years]
    })
    fig_pie = px.pie(
        pie_df, names="النشاط", values="سنوات",
        hole=0.35, title="نظرة عامة على حياتك"
    )
    fig_pie.update_traces(textinfo="label+percent", insidetextorientation="auto")
    st.plotly_chart(fig_pie, use_container_width=True)

    # 📈 شريط زمني
    st.subheader("📈 خط حياتك الزمني (تقريبي)")
    avg_life = 75
    lived = min(years, avg_life)
    remaining = max(0, avg_life - years)
    bar_df = pd.DataFrame({
        "الجزء": ["ما عشته", "المتبقي (تقديري)"],
        "سنوات": [lived, remaining]
    })
    fig_bar = px.bar(
        bar_df, x="سنوات", y="الجزء", orientation="h",
        text="سنوات", title="مقارنة بين الماضي والمتبقي"
    )
    fig_bar.update_layout(yaxis=dict(categoryorder="array", categoryarray=["ما عشته", "المتبقي (تقديري)"]))
    st.plotly_chart(fig_bar, use_container_width=True)

    # 🔗 روابط المشاركة
    st.subheader("🔗 شارك نتيجتك مع الأصدقاء")
    whatsapp_url = f"https://wa.me/?text=🎂 عمري {years} سنة! جرّب برنامج حساب العمر الفكاهي: {APP_URL}"
    facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={APP_URL}"
    st.markdown(f"[📱 شارك على واتساب]({whatsapp_url})")
    st.markdown(f"[🌐 شارك على فيسبوك]({facebook_url})")

# توقيع
st.markdown("---")
st.markdown("✨ تم إنشاءه بواسطة *محمود ناصيف (أبو عبد الرحمن)* ✨")
