import streamlit as st
import pandas as pd
import numpy as np  # Correct import
import plotly.express as px

st.set_page_config(page_title="Bravo4All Executive Dashboard", layout="wide")

st.title("📊 Bravo4All – Hotel Workforce Performance")

# Sample KPI Data
st.subheader("Executive Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Guest Satisfaction", "4.30 / 5", "+0.10 vs Premium")
col2.metric("Total Rewards Investment", "$669,090", "")
col3.metric("Workforce Attendance", "88.9%", "-1.1% vs Industry")

# ✅ FIXED: Attendance Trends with numpy.random
st.subheader("Attendance Trends")
sample_data = pd.DataFrame({
    "Month": pd.date_range("2023-01-01", periods=12, freq="M"),
    "Hilton NY": np.random.uniform(85, 95, 12),
    "Hyatt SF": np.random.uniform(85, 95, 12),
})
st.line_chart(sample_data.set_index("Month"))

# Bar Chart
st.subheader("Training Completion Rate by Property")
bar_data = pd.DataFrame({
    "Property": ["Hilton NY", "Hyatt SF", "Marriott LA", "Sheraton Dallas"],
    "Completion %": [84.2, 82.9, 82.1, 81.7],
})
fig = px.bar(bar_data, x="Property", y="Completion %", text="Completion %", color="Property")
st.plotly_chart(fig, use_container_width=True)