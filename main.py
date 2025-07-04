import streamlit as st
import requests

st.title("Live Currency Convertor")
amount = st.number_input("Amount (INR): ", min_value=1)

target_currency = st.selectbox("Convert to", ["USD", "GBP", "EUR", "JPY"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        converted_rate = rate * amount
        st.success(f"{amount} INR = {converted_rate:2f} {target_currency}")
    else:
        st.error("Failed to convert")