# app.py
import streamlit as st
import data_fetcher
import trika_core
import simulation_engine
import policy_brief
import knowledge_graph

st.set_page_config(page_title="APRF Svatantrya Intelligence Engine", layout="wide")
st.title("🌐 APRF Svatantrya Intelligence Engine")
st.subheader("Embodied Policy Intelligence (Multi-Node System)")

# ==========================================
# STEP 1: DATA NODE (Call data_fetcher.py)
# ==========================================
st.subheader("📡 Data Node: Live Reality")
gdp_data = data_fetcher.fetch_world_bank_gdp()
inflation_data = data_fetcher.fetch_world_bank_inflation()

if gdp_data is not None and inflation_data is not None:
    st.success("✅ Live World Bank data fetched.")
    st.line_chart(gdp_data.set_index('Year'))
    st.line_chart(inflation_data.set_index('Year'))
    
    latest_gdp = gdp_data.iloc[-1]['GDP Growth (%)']
    latest_inflation = inflation_data.iloc[-1]['Inflation (%)']
else:
    st.warning("World Bank API unavailable. Using Tantric Sample Data.")
    latest_gdp = 3.9
    latest_inflation = 6.4

# ==========================================
# STEP 2: TRIKA NODE (Call trika_core.py)
# ==========================================
st.subheader("🕉️ Trika Node: Spiritual Anchor")
trika_state = trika_core.get_trika_state(latest_gdp)
st.info(trika_state)

# ==========================================
# STEP 3: GRAPH NODE (Call knowledge_graph.py)
# ==========================================
st.subheader("🔗 Rhizomatic Node: Knowledge Graph")
knowledge_graph.display_knowledge_graph()

# ==========================================
# STEP 4: SIMULATION NODE (Call simulation_engine.py)
# ==========================================
st.subheader("🔮 Simulation Node: What-If Analysis")
col1, col2 = st.columns(2)
with col1:
    stimulus = st.slider("Fiscal Stimulus (% of GDP)", 0, 10, 3)
with col2:
    education_investment = st.slider("Education Investment (% of Budget)", 0, 20, 8)

sim_gdp, sim_inflation = simulation_engine.simulate_policy(latest_gdp, latest_inflation, stimulus, education_investment)

st.metric("Simulated GDP Growth", f"{sim_gdp:.2f}%", "Target: 6.5%")
st.metric("Simulated Inflation", f"{sim_inflation:.2f}%", "Target: 5.0%")

# ==========================================
# STEP 5: POLICY BRIEF NODE (Call policy_brief.py)
# ==========================================
st.subheader("📜 Research Node: Embodied Policy Brief")
brief = policy_brief.generate_brief(trika_state, latest_gdp, sim_gdp, sim_inflation, stimulus, education_investment)
st.write(brief)
