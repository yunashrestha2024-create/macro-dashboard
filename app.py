import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="APRF Macro Reality Engine", layout="wide")
st.title("🇳🇵 APRF Macro Reality Engine")
st.subheader("Live Macroeconomic Intelligence Dashboard")

# --- Refresh Button ---
if st.button("🔄 Refresh Live Data"):
    st.rerun()

# --- Function to fetch NRB Forex Rates (Robust) ---
def fetch_nrb_rates():
    try:
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        url = f"https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=20&from={start_date}&to={end_date}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data and data.get('data') and data['data'].get('payload'):
            payload = data['data']['payload']
            latest_rates = payload[-1]['rates']
            return latest_rates, payload[-1]['date']
    except Exception as e:
        return None, None
    return None, None

# --- Display: Live Forex Table ---
st.subheader("💱 Live Exchange Rates (Nepal Rastra Bank)")
rates, date = fetch_nrb_rates()

if rates:
    st.success(f"✅ Live NRB data fetched from {date}")
    df_rates = pd.DataFrame(rates)
    
    # Display all available columns (instead of hardcoding)
    st.dataframe(df_rates)
else:
    st.warning("⚠️ NRB API unavailable. Showing sample data.")
    sample_rates = pd.DataFrame({
        'Currency': ['USD', 'EUR', 'INR'], 
        'Buy (NPR)': [133.5, 145.2, 1.6],
        'Sell (NPR)': [133.7, 145.4, 1.62]
    })
    st.dataframe(sample_rates)

# --- Display: World Bank GDP Chart ---
st.subheader("📈 GDP Growth Rate (World Bank Data)")
gdp_data = None

# This is safer - we define a function but call it manually
def fetch_world_bank_gdp():
    try:
        url = "https://api.worldbank.org/v2/country/NPL/indicator/NY.GDP.MKTP.KD.ZG?format=json&per_page=10"
        response = requests.get(url, timeout=10)
        data = response.json()
        rows = data[1]
        years = [int(row['date']) for row in rows]
        values = [row['value'] for row in rows]
        df = pd.DataFrame({'Year': years, 'GDP Growth (%)': values})
        return df.dropna()
    except:
        return None

gdp_data = fetch_world_bank_gdp()

if gdp_data is not None:
    st.success("✅ Live World Bank data fetched!")
    fig = px.line(gdp_data, x="Year", y="GDP Growth (%)", title="Real GDP Growth for Nepal")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ World Bank API unavailable. Showing sample data.")
    sample_gdp = pd.DataFrame({'Year': [2020, 2021, 2022], 'GDP Growth (%)': [-1.5, 4.5, 5.0]})
    st.line_chart(sample_gdp.set_index('Year'))

# --- Policy Targets (Manual Input) ---
st.subheader("📊 Key Macro Targets (MoF/RSP Vision)")
targets = {
    "Indicator": ["GDP Growth (%)", "Inflation (CPI %)", "Remittance (Bn NPR)"], 
    "Target": [6.5, 5.0, 1600]
}
st.dataframe(pd.DataFrame(targets))
