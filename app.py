import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="APRF Policy Intelligence Lab", layout="wide")
st.title("🇳🇵 APRF Policy Intelligence Lab")
st.subheader("Macro Reality + Policy Simulation Engine")

# --- 1. Baseline Data (Static/CBS/NRB data) ---
baseline = {
    "GDP Growth (%)": 3.9,
    "Inflation (CPI %)": 6.4,
    "Unemployment Rate (%)": 11.4,
    "Industrial Output Share (%)": 15.0,
    "Remittance (Bn NPR)": 1450
}

# --- 2. THE SIMULATION ENGINE ---
st.subheader("🧪 Policy Simulation Engine (What-If Analysis)")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏭 Fiscal & Industrial Levers")
    industrial_investment = st.slider("Increase Industrial Investment (%)", 0, 20, 5)
    tax_incentive = st.slider("Tax Incentive for SMEs (%)", 0, 15, 3)
    
with col2:
    st.markdown("### 💼 Labor & External Levers")
    job_creation_target = st.slider("Target Job Creation (Thousands)", 100, 1000, 500)
    remittance_dependency = st.slider("Reduce Remittance Dependency (%)", 0, 30, 10)

# --- 3. Simulation Logic ---
st.subheader("📊 Simulated Outcomes")

# Logic: Industrial investment boosts GDP, tax incentives boost SMEs
simulated_gdp = baseline["GDP Growth (%)"] + (industrial_investment * 0.15) + (tax_incentive * 0.05)
simulated_jobs = (job_creation_target / 10) + (industrial_investment * 2)
simulated_inflation = baseline["Inflation (CPI %)"] - (tax_incentive * 0.1) - (remittance_dependency * 0.05)
simulated_unemployment = baseline["Unemployment Rate (%)"] - (simulated_jobs / 100)

# Prevent inflation from going too low (just for realism)
simulated_inflation = max(simulated_inflation, 2.0)

# --- 4. Display Simulated Metrics ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Simulated GDP Growth", f"{simulated_gdp:.2f}%", f"Baseline: {baseline['GDP Growth (%)']}%")
col2.metric("Simulated Inflation", f"{simulated_inflation:.2f}%", f"Baseline: {baseline['Inflation (CPI %)']}%")
col3.metric("Jobs Created", f"{simulated_jobs:.0f}K", f"Target: {job_creation_target}K")
col4.metric("Unemployment", f"{simulated_unemployment:.2f}%", f"Baseline: {baseline['Unemployment Rate (%)']}%")

# --- 5. Compare Baseline vs Simulated ---
st.subheader("📈 Baseline vs Simulated Outcomes")
comparison_df = pd.DataFrame({
    "Indicator": ["GDP Growth (%)", "Inflation (CPI %)", "Unemployment Rate (%)"],
    "Baseline": [baseline["GDP Growth (%)"], baseline["Inflation (CPI %)"], baseline["Unemployment Rate (%)"]],
    "Simulated": [simulated_gdp, simulated_inflation, simulated_unemployment]
})

fig = px.bar(comparison_df, x="Indicator", y=["Baseline", "Simulated"], barmode="group",
             title="Policy Impact: Baseline vs Simulated")
st.plotly_chart(fig, use_container_width=True)

# --- 6. AI-Generated Policy Brief ---
st.subheader("🤖 AI Policy Brief (Real-time Simulation Insight)")
st.write(f"""
**Policy Brief:** 
If the government increases industrial investment by {industrial_investment}% and provides a {tax_incentive}% SME tax incentive, 
Nepal's GDP growth could potentially reach **{simulated_gdp:.2f}%** (up from 3.9% baseline). 
This could create approximately **{simulated_jobs:.0f} thousand jobs**, 
reducing unemployment to **{simulated_unemployment:.2f}%**. 

**However, critical constraints must be noted:**
*   **Structural Lag:** Physical infrastructure and skill development take 5-10 years. 
    Instant job creation is not realistic without accompanying skills training.
*   **Institutional Capacity:** The current state machinery may struggle to execute 
    these reforms without an integrated intelligence system (like this dashboard).
*   **Capital Flow:** The banking sector currently has idle liquidity, but investment 
    confidence must be restored before capital mobilizes into the industrial sector.

**Recommendation:** 
This simulation suggests that a **phased, multi-year approach** is required. 
Start with targeted industrial zones, align skills training with upcoming industry needs, 
and use this simulation engine to test fiscal policies *before* implementation.
""")

st.caption("APRF Policy Intelligence Lab | Node 1: Simulation Engine")
