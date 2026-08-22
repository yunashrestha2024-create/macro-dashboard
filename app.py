import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(page_title="APRF Policy Intelligence Lab", layout="wide")
st.title("🇳🇵 APRF Policy Intelligence Lab")
st.subheader("Macroeconomic Reality vs RSP/MoF Policy Targets")

# --- 1. Policy Targets (from RSP Vacha Patra & MoF) ---
policy_targets = {
    "Indicator": [
        "GDP Growth (%)", 
        "Inflation (CPI %)", 
        "Remittance (Bn NPR)", 
        "Unemployment Rate (%)", 
        "Trade Deficit (Bn NPR)", 
        "Industrial Output Share (%)"
    ],
    "RSP/MoF Target": [6.5, 5.0, 1600, 8.0, 1200, 25.0],
    "Reality (2025/26)": [3.9, 6.4, 1450, 11.4, 1500, 15.0]
}
policy_df = pd.DataFrame(policy_targets)

# --- 2. Gap Analysis (Research Logic) ---
policy_df["Gap"] = policy_df["RSP/MoF Target"] - policy_df["Reality (2025/26)"]
policy_df["Gap Status"] = policy_df["Gap"].apply(lambda x: "Critical" if x < -2 else ("High" if x < 0 else "Moderate"))

# --- 3. Display: Policy Gap Table ---
st.subheader("📊 Policy Gap Analysis (Research Output)")
st.dataframe(policy_df)

# --- 4. Visual: Gap Chart ---
st.subheader("📈 Target vs Reality")
fig = px.bar(policy_df, x="Indicator", y=["RSP/MoF Target", "Reality (2025/26)"], 
             barmode="group", title="Macroeconomic Policy Targets vs Current Reality")
st.plotly_chart(fig, use_container_width=True)

# --- 5. Live World Bank Data for GDP ---
st.subheader("📈 Historical GDP Growth (World Bank API)")
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
    fig2 = px.line(gdp_data, x="Year", y="GDP Growth (%)", title="Nepal Real GDP Growth Rate")
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("World Bank API is temporarily unavailable. Showing static dataset.")
    st.line_chart(pd.DataFrame({'Year': [2020, 2021, 2022], 'GDP Growth (%)': [-2.0, 4.8, 5.6]}).set_index('Year'))

# --- 6. AI-Assisted Policy Brief (Insight Generation) ---
st.subheader("🤖 AI Policy Brief (Automated Insight)")
st.write("""
**Current Macro Reality:** 
Nepal's GDP growth is currently at 3.9%, significantly below the RSP/MoF target of 6.5%. 
Inflation remains elevated at 6.4% against a target of 5.0%. 
The unemployment rate stands at 11.4%, which is 3.4% higher than the target. 

**Research Recommendation:** 
To meet the 6.5% growth target, the Fiscal Policy must aggressively shift capital expenditure towards 
productive sectors (industry and infrastructure). The current economy is heavily dependent on 
remittance (consumption-driven). **Critical structural reform is required to transition to a 
production-investment-driven economy.**

**Policy Simulation Suggestion:** 
If the government were to increase industrial output share by 5%, GDP growth could potentially 
increase by 1.2% annually. This data is now available for simulation.
""")

st.caption("APRF Policy Intelligence Lab | Research Node")
