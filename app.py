import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="APRF Macro Reality Engine", layout="wide")

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #f5f5f5; }
    .stTitle { color: #0E7C3F; text-align: center; }
    .stSubheader { color: #333; }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🇳🇵 APRF Macro Reality Engine")
st.subheader("Nepal Economic Intelligence Dashboard")

# --- SAMPLE DATA (Replace with live scraping later) ---
data = {
    "Indicator": ["GDP Growth (%)", "Inflation (CPI %)", "Remittance Inflow (Billion NPR)", 
                  "Foreign Exchange Reserves (Billion USD)", "Trade Deficit (Billion NPR)", 
                  "Unemployment Rate (%)", "Interest Rate (Base Rate %)"],
    "2023/24": [3.9, 6.4, 1450, 15.0, 1500, 11.4, 10.5],
    "Target (MoF/RSP)": [6.5, 5.0, 1600, 20.0, 1200, 8.0, 8.0]
}
df = pd.DataFrame(data)

# --- DISPLAY METRICS ---
st.subheader("Key Macroeconomic Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("GDP Growth", "3.9%", "Target: 6.5%")
col2.metric("Inflation", "6.4%", "Target: 5.0%")
col3.metric("Remittance", "Rs 1,450 B", "Target: Rs 1,600 B")

# --- CHARTS ---
st.subheader("Current vs Target Performance")
chart_data = df.melt(id_vars=["Indicator"], var_name="Year", value_name="Value")
fig = px.bar(chart_data, x="Indicator", y="Value", color="Year", barmode="group",
             title="Nepal Macro Indicators: Current Reality vs Policy Target")
st.plotly_chart(fig, use_container_width=True)

# --- DATA TABLE ---
st.subheader("Raw Data")
st.dataframe(df)

# --- POLICY GAP ANALYSIS ---
st.subheader("📊 Policy Gap Analysis (RSP / MoF Alignment)")
gap_data = {
    "Policy Area": ["Job Creation", "Fiscal Reform", "Capital Mobilization", "Industrialization"],
    "Current Status": ["High Migration", "Low Revenue", "Idle Liquidity", "Low Output"],
    "Target Status": ["1M Jobs", "Efficient Spending", "Investment Flow", "High Productivity"],
    "Gap Level": ["Critical", "High", "High", "Critical"]
}
gap_df = pd.DataFrame(gap_data)
st.dataframe(gap_df)
st.caption("APRF Policy Intelligence Lab | Prototype Node 0")
