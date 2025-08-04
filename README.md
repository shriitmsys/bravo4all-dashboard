# bravo4all-dashboard
Dashboarding prototype


Section
Description
Streamlit Component
Executive Summary
Overall metrics (attendance %, guest sat., investment)
st.metric, st.columns
Workforce Trends
Attendance / guest satisfaction over time
altair or plotly line chart
Performance Rankings
Properties ranked by score, with color highlights
st.dataframe + gradient
Warnings
Properties below threshold in training or attendance
st.markdown with emojis
Charts
Bubble chart (score vs sat), stacked bars, histograms
plotly, altair, matplotlib
Export Section
Export to CSV/PDF (dummy button for now)
st.download_button
