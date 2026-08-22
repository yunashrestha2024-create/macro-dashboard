import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# Page Config
st.set_page_config(page_title="APRF Macro Reality Engine", layout="wide")

st.title("🇳🇵 APRF Macro Reality Engine")
st.subheader("Nepal Economic Intelligence Dashboard - Live Data")

# --- FUNCTION TO FETCH WORLD BANK DATA ---
def fetch_world_bank_data():
    try:
        # World Bank API for Nepal (NPL) GDP Growth (NY.GDP.MKTP.KD.ZG)
        url = "https://api.worldbank.org/v2/country/NPL/indicator/NY.GDP.MKTP.KD.ZG?format=json&per_page=10"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # Extract the data (skip the first metadata element)
        rows = data[1]
        years = [int(row['date']) for row in rows]
        values = [row['value'] for row in rows]
        
        # Create a DataFrame
        df = pd.DataFrame({'Year': years, 'GDP Growth (%)': values})
        return df.dropna()
    except:
        return None

# --- FETCH DATA ---
gdp_data = fetch_world_bank_data()

# --- DISPLAY ---
if gdp_data is not None:
    st.success("✅ Live data fetched from World Bank API!")
    st.subheader("Nepal GDP Growth Rate (Historical)")
    fig = px.line(gdp_data, x="Year", y="GDP Growth (%)", title="Real GDP Growth (World Bank)")
    st.plotly_chart(fig, use_container_width=True)
    
    # Show latest value
    latest = gdp_data.iloc[-1]
    st.metric("Latest GDP Growth", f"{latest['GDP Growth (%)']}%", f"Year: {latest['Year']}")
else:
    st.warning("⚠️ Live API connection failed. Showing sample data.")
    # Fallback to sample data
    sample_gdp = pd.DataFrame({
        'Year': [2019, 2020, 2021, 2022, 2023],
        'GDP Growth (%)': [6.7, -2.0, 4.8, 5.6, 3.9]
    })
    st.line_chart(sample_gdp.set_index('Year'))

# --- MACRO INDICATORS (SAMPLE BUT READY FOR LIVE API) ---
st.subheader("Key Macroeconomic Indicators (Target vs Reality)")
data = {
    "Indicator": ["Inflation (CPI %)", "Remittance (Bn NPR)", "FX Reserves (Bn USD)", 
                  "Trade Deficit (Bn NPR)", "Base Rate (%)"],
    "Current": [6.4, 1450, 15.0, 1500, 10.5],
    "Target": [5.0, 1600, 20.0, 1200, 8.0]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.subheader("Current vs Target Performance")
st.bar_chart(df.set_index("Indicator"))

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

st.caption("APRF Policy Intelligence Lab | Live Data Node 0.5")
