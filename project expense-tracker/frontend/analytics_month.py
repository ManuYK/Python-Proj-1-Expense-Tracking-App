import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"


def analytics_month_tab():
    st.title("Month-wise Expense Analytics")

    # User inputs for Year and Month
    col1, col2 = st.columns(2)
    with col1:
        year = st.number_input("Year", min_value=2000, max_value=2100, value=2024, step=1)
    with col2:
        month = st.number_input("Month", min_value=1, max_value=12, value=8, step=1)

    # Button to trigger analytics fetch
    if st.button("Get Month-wise Analytics"):
        payload = {
            "year": year,
            "month": month
        }
        response = requests.post(f"{API_URL}/analytics/monthwise/", json=payload)

        # Process response
        if response.status_code == 200:
            response = response.json()
            data = {
                "Category": list(response.keys()),
                "Total": [response[category]["total"] for category in response],
                "Percentage": [response[category]["percentage"] for category in response]
            }

            df = pd.DataFrame(data)
            df_sorted = df.sort_values(by="Percentage", ascending=False)

            st.title(f"Expense Breakdown By Category - {year}-{month}")
            st.bar_chart(data=df_sorted.set_index("Category")['Percentage'], use_container_width=True)
            df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
            df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)
            st.table(df_sorted)
        else:
            st.error("No data found for the specified month or an error occurred.")

