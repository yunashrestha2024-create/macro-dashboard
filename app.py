import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components
from datetime import datetime

# ==========================================
# 1. ULTIMATE 2026 INTERFACE (Glassmorphism + Neon)
# ==========================================
st.set_page_config(page_title="APRF Intelligence Engine 2026", layout="wide")

# Custom CSS for the Future Interface
st.markdown("""
<style>
    /* Global Background */
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* The Title */
    .stTitle {
        color: #00ff9d;
        font-size: 3.5rem;
        text-align: center;
        text-shadow: 0px 0px 20px rgba(0, 255, 157, 0.7);
        font-family: 'Orbitron', sans-serif;
        padding-top: 20px;
    }
    
    /* The Subtitle */
    .stSubheader {
        color: #00b4d8;
        font-family: 'Orbitron', sans-serif;
        text-align: center;
    }
    
    /* Glassmorphism Cards for Metrics */
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        color: #ffffff;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    
    /* Neon Buttons */
    .stButton {
        background: linear-gradient(90deg, #00ff9d, #00b4d8);
        color: black;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
    }
    
    /* Beautiful Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 5px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #ffffff;
        font-weight: bold;
    }
    
    /* Sliders */
    .stSlider {
        background: transparent;
    }
</style>
""", unsafe_allow_html=True)

st.title("APRF Intelligence Engine 2026")
st.subheader("Embodied Policy Intelligence | National-Global System")

# ==========================================
# 2. LIVE DATA ACQUISITION (The Reality Base)
# ==========================================
def fetch_world_bank_data(indicator, country="NPL", per_page=5):
    try:
        url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page={per_page}"
        response = requests.get(url, timeout=10)
        data = response.json()
        rows = data[1]
        return {int(row['date']): row['value'] for row in rows if row['value'] is not None}
    except:
        return None

gdp_data = fetch_world_bank_data("NY.GDP.MKTP.KD.ZG")
inflation_data = fetch_world_bank_data("FP.CPI.TOTL.ZG")

if gdp_data and inflation_data:
    reality_df = pd.DataFrame({
        "Year": list(gdp_data.keys()),
        "GDP Growth (%)": list(gdp_data.values()),
        "Inflation (%)": list(inflation_data.values())
    })
    reality_df = reality_df.sort_values("Year")
    latest_gdp = reality_df.iloc[-1]['GDP Growth (%)']
    latest_inflation = reality_df.iloc[-1]['Inflation (%)']
    st.success("✅ Live World Bank data connected. System is now breathing with reality.")
else:
    st.warning("World Bank API unavailable. Using grounded sample data.")
    reality_df = pd.DataFrame({
        "Year": [2020, 2021, 2022, 2023],
        "GDP Growth (%)": [-2.0, 4.8, 5.6, 3.9],
        "Inflation (%)": [4.2, 6.4, 6.4, 6.4]
    })
    latest_gdp = 3.9
    latest_inflation = 6.4

# ==========================================
# 3. THE TRIKA STATE (System Logic)
# ==========================================
if latest_gdp > 5.0 and latest_inflation < 5.0:
    system_state = "Expansion: Growth & Stability"
elif latest_gdp > 5.0:
    system_state = "Expansion: Heat Rising"
elif latest_gdp < 3.0 and latest_inflation > 6.0:
    system_state = "Contraction: Stagnation & Inflation"
else:
    system_state = "Stability: Need Breakthrough"

# ==========================================
# 4. THE ULTIMATE TABS (Variety of Visualizations)
# ==========================================
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌐 Macro Reality", "🕊️ Well-being", "🔗 Rhizomatic Graph", "🔮 Simulation", "📜 Policy Brief"])

# --- TAB 1: MACRO REALITY (Charts & Graphs) ---
with tab1:
    st.subheader("Macroeconomic Reality (Live)")
    
    # Live Metrics Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("GDP Growth", f"{latest_gdp}%", "Target: 6.5%")
    col2.metric("Inflation", f"{latest_inflation}%", "Target: 5.0%")
    col3.metric("System State", system_state, "Trika Logic")
    
    # Variety of Charts
    st.markdown("### 📈 Growth & Inflation (Line Graph)")
    fig1 = px.line(reality_df, x="Year", y=["GDP Growth (%)", "Inflation (%)"], 
                   title="The Dance of Growth and Inflation",
                   color_discrete_sequence=["#00ff9d", "#ff4d4d"])
    st.plotly_chart(fig1, use_container_width=True)
    
    st.markdown("### 📊 Area Chart (Historical Trend)")
    st.area_chart(reality_df.set_index("Year"))
    
    st.markdown("### 📉 Scatter Chart (Correlation)")
    fig2 = px.scatter(reality_df, x="GDP Growth (%)", y="Inflation (%)", 
                      title="GDP vs Inflation Correlation",
                      color_discrete_sequence=["#00b4d8"])
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("### 🥧 Pie Chart (Revenue/Sectoral Representation)")
    pie_data = {"Sector": ["Agriculture", "Industry", "Services"], "Share": [25, 15, 60]}
    fig3 = px.pie(pie_data, names="Sector", values="Share", hole=0.4, 
                  title="Nepal's Economic Structure",
                  color_discrete_sequence=["#00ff9d", "#00b4d8", "#ff4d4d"])
    st.plotly_chart(fig3, use_container_width=True)

# --- TAB 2: WELL-BEING NODE ---
with tab2:
    st.subheader("Spirituality & Well-being Node")
    
    wellbeing_data = {
        "Indicator": ["Social Trust", "Cultural Resilience", "Mental Well-being", 
                      "Community Engagement", "Environmental Stewardship"],
        "Current (0-100)": [45, 62, 58, 50, 65],
        "Target (0-100)": [75, 80, 85, 75, 85]
    }
    wellbeing_df = pd.DataFrame(wellbeing_data)
    
    st.dataframe(wellbeing_df)
    
    st.markdown("### 🕊️ Well-being Gap Analysis")
    fig4 = px.bar(wellbeing_df, x="Indicator", y=["Current (0-100)", "Target (0-100)"],
                  barmode="group", title="Well-being Indicators: Current vs Target",
                  color_discrete_sequence=["#ff4d4d", "#00ff9d"])
    st.plotly_chart(fig4, use_container_width=True)
    
    st.caption("This is a measurable policy outcome that must be tracked alongside GDP.")

# --- TAB 3: RHIZOMATIC GRAPH (The 2026 Centerpiece) ---
with tab3:
    st.subheader("Rhizomatic Knowledge Graph (Interactive)")
    st.markdown("Drag, click, and zoom to explore how Policy, Economy, Education, and Well-being connect.")
    
    # Create Graph
    G = nx.Graph()
    
    # Nodes
    G.add_node("RSP Promises", type="Policy", color="red")
    G.add_node("MoF Budget", type="Policy", color="red")
    G.add_node("Swarnim Wagle", type="Leader", color="blue")
    G.add_node("GDP Growth", type="Macro", color="green")
    G.add_node("Inflation", type="Macro", color="green")
    G.add_node("Unemployment", type="Macro", color="green")
    G.add_node("Education", type="Education", color="orange")
    G.add_node("Well-being", type="Spiritual", color="purple")
    G.add_node("AI Capability", type="Computation", color="cyan")
    
    # Edges
    G.add_edge("RSP Promises", "MoF Budget")
    G.add_edge("MoF Budget", "GDP Growth")
    G.add_edge("GDP Growth", "Unemployment")
    G.add_edge("Education", "Unemployment")
    G.add_edge("Education", "Well-being")
    G.add_edge("Well-being", "GDP Growth")
    G.add_edge("AI Capability", "GDP Growth")
    G.add_edge("AI Capability", "Education")
    G.add_edge("Swarnim Wagle", "MoF Budget")
    
    # Visualize
    net = Network(height="600px", width="100%", bgcolor="#0e1117", font_color="#ffffff", notebook=False)
    net.from_nx(G)
    net_html = net.generate_html()
    components.html(net_html, height=600, width="100%")

# --- TAB 4: SIMULATION ENGINE (The What-If) ---
with tab4:
    st.subheader("Policy Simulation Engine")
    
    col1, col2 = st.columns(2)
    with col1:
        stimulus = st.slider("Fiscal Stimulus (% of GDP)", 0, 10, 3)
    with col2:
        education_investment = st.slider("Education Investment (% of Budget)", 0, 20, 8)
    
    # Simulation Logic (Trika)
    sim_gdp = latest_gdp + (stimulus * 0.4) + (education_investment * 0.1)
    sim_inflation = latest_inflation + (stimulus * 0.2) - (education_investment * 0.05)
    sim_wellbeing = 58 + (education_investment * 0.5)
    
    # Animated Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Simulated GDP", f"{sim_gdp:.2f}%", f"From {latest_gdp}%")
    col2.metric("Simulated Inflation", f"{sim_inflation:.2f}%", f"From {latest_inflation}%")
    col3.metric("Simulated Well-being", f"{sim_wellbeing:.2f}", "From 58")
    
    # Visualize Simulation Results
    sim_data = pd.DataFrame({
        "Indicator": ["GDP Growth", "Inflation", "Well-being"],
        "Before": [latest_gdp, latest_inflation, 58],
        "After": [sim_gdp, sim_inflation, sim_wellbeing]
    })
    fig5 = px.bar(sim_data, x="Indicator", y=["Before", "After"], barmode="group",
                  title="Policy Impact: Before vs After Simulation",
                  color_discrete_sequence=["#ff4d4d", "#00ff9d"])
    st.plotly_chart(fig5, use_container_width=True)

# --- TAB 5: POLICY BRIEF (The Research Output) ---
with tab5:
    st.subheader("Embodied Policy Brief")
    st.write(f"""
    **The Macro Reality:** 
    GDP is at **{latest_gdp}%** (target 6.5%), Inflation at **{latest_inflation}%** (target 5.0%). 
    Economy is remittance-dependent with a massive trade deficit.
    
    **The Well-being Reality:**
    Critical gaps in Social Trust (45/100) and Mental Well-being (58/100). 
    These are the foundation of a productive society.
    
    **The Simulation Insight:**
    If we increase Stimulus by **{stimulus}%** and Education Investment by **{education_investment}%**, 
    GDP rises to **{sim_gdp:.2f}%**, Inflation adjusts to **{sim_inflation:.2f}%**, 
    and Well-being improves to **{sim_wellbeing:.2f}**.
    
    **The Embodied Recommendation:**
    You cannot push a button to grow. You must **orchestrate** the Economic and Well-being nodes simultaneously. 
    Investing in Education improves both GDP and Well-being. 
    This is the **Trika Logic**: expansion through investment, contraction through discipline, stability through balance, and evolution through feedback.
    """)
    
    st.caption("APRF Intelligence Engine 2026 | Node: Macro + Well-being + Simulation + Graph")

st.caption("© 2026 APRF Intelligence Engine | Svatantrya System")
