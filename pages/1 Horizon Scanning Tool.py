import streamlit as st

from database import init_db, add_user, get_all_users
from news_engine import fetch_news
from email_service import send_alert_email

init_db()

st.set_page_config(page_title="Supply Chain Alerts", layout="centered")

st.title("Horizon Scanning Generator")

st.write("Receive automated supply chain disruption alerts.")

with st.form("signup"):

    name = st.text_input("Name")

    email = st.text_input("Email")

    frequency = st.selectbox(
        "Alert Frequency",
        ["Daily", "Weekly"]
    )

    submitted = st.form_submit_button("Generate")

if submitted:

    if not name or not email:

        st.error("Please fill all required fields")

    else:

        add_user(name, email, frequency)

        articles = fetch_news(frequency)

        send_alert_email(email, name, articles)

        st.success("Subscription successful! You will receive alerts.")
