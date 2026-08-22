import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

st.set_page_config(page_title="APRF Svatantrya Intelligence Engine", layout="wide")
st.title("🌐 APRF Svatantrya Intelligence Engine")
st.subheader("National-Global Policy Intelligence System (2026 Architecture)")

# ==========================================
# 1. LIVE DATA ACQUISITION (The Baseline)
# ==========================================
st.subheader("📡 Step 1: Live Data Acquisition")

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

def fetch_nrb_rates():
    try:
        url = "https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=20&from=2024-01-01&to=2024-12-31"
        response = requests.get(url, timeout=10)
        data = response.json()
        if data and data.get('data') and data['data'].get('payload'):
            payload = data['data']['payload']
            return payload[-1]['rates'], payload[-1]['date']
    except:
        return None, None
    return None, None

gdp_data = fetch_world_bank_gdp()
rates, date = fetch_nrb_rates()

if gdp_data is not None:
    st.success("✅ World Bank GDP data fetched.")
    st.line_chart(gdp_data.set_index('Year'))
else:
    st.info("Showing static baseline (World Bank unavailable).")

# ==========================================
# 2. KNOWLEDGE GRAPH NODE CREATION (Neo4j)
# ==========================================
st.subheader("🧠 Step 2: Rhizomatic Knowledge Graph (Visualizing the System)")

# Create a graph manually (can be populated from Neo4j later)
G = nx.Graph()

# Policy Nodes (RSP/MoF)
G.add_node("RSP Vacha Patra", type="Policy", color="red")
G.add_node("MoF Budget", type="Policy", color="red")
G.add_node("Swarnim Wagle (MoF)", type="Leadership", color="blue")

# Economic Nodes
G.add_node("GDP Growth", type="Macro", color="green")
G.add_node("Inflation", type="Macro", color="green")
G.add_node("Remittance", type="Macro", color="green")
G.add_node("Unemployment", type="Macro", color="green")

# Education Nodes
G.add_node("Skill Gap", type="Education", color="orange")
G.add_node("Curriculum Reform", type="Education", color="orange")

# Spirituality Node
G.add_node("Trika Principles", type="Spiritual", color="purple")

# AI Node
G.add_node("AI Capability", type="Computation", color="cyan")

# Edges (Connections)
G.add_edge("RSP Vacha Patra", "GDP Growth", weight=2)
G.add_edge("RSP Vacha Patra", "Unemployment", weight=2)
G.add_edge("MoF Budget", "Inflation", weight=1)
G.add_edge("Swarnim Wagle (MoF)", "MoF Budget", weight=1)
G.add_edge("Skill Gap", "Unemployment", weight=3)
G.add_edge("Curriculum Reform", "Skill Gap", weight=2)
G.add_edge("Trika Principles", "AI Capability", weight=1)
G.add_edge("AI Capability", "GDP Growth", weight=1)
G.add_edge("AI Capability", "Curriculum Reform", weight=2)

# Visualize the Graph using Pyvis
net = Network(height="600px", width="100%", bgcolor="#ffffff", font_color="#000000")
net.from_nx(G)
net_html = net.generate_html()

# Render the interactive graph in Streamlit
components.html(net_html, height=600, width="100%")

st.caption("Click, drag, and zoom to explore the Rhizomatic connections between Policy, Economy, Education, and AI.")

# ==========================================
# 3. SIMULATION ENGINE (The "What-If" Layer)
# ==========================================
st.subheader("🧪 Step 3: Policy Simulation Engine")

col1, col2 = st.columns(2)
with col1:
    industrial_investment = st.slider("Increase Industrial Investment (%)", 0, 20, 5)
with col2:
    tax_incentive = st.slider("Tax Incentive for SMEs (%)", 0, 15, 3)

simulated_gdp = 3.9 + (industrial_investment * 0.15) + (tax_incentive * 0.05)
simulated_inflation = 6.4 - (tax_incentive * 0.1)

st.metric("Simulated GDP Growth", f"{simulated_gdp:.2f}%", "Target: 6.5%")
st.metric("Simulated Inflation", f"{simulated_inflation:.2f}%", "Target: 5.0%")

# ==========================================
# 4. POLICY BRIEF GENERATOR
# ==========================================
st.subheader("🤖 Step 4: AI-Generated Policy Brief")
st.write(f"""
**Current Reality:** 
Nepal's GDP growth is {gdp_data.iloc[-1]['GDP Growth (%)'] if gdp_data is not None else 3.9}%, but the target is 6.5%. 
The economy is heavily dependent on remittance ({1450} billion NPR) and faces a massive trade deficit.

**Simulation Insight:** 
If we increase industrial investment by {industrial_investment}%, we can potentially add {industrial_investment * 0.15:.2f}% to GDP growth. 
However, **Real-World Constraints** must be respected: 
1. **Physical Infrastructure:** Roads, factories, and energy take 5-10 years.
2. **Skills Mismatch:** The workforce cannot be transformed overnight.
3. **Institutional Capacity:** The state must build execution capacity first.

**Recommendation:** 
Use the Rhizomatic Graph to identify the most critical connection (e.g., Skill Gap → Unemployment). 
Focus on **aligning curriculum (Education Node) with industrial needs (Economic Node)** before scaling investment. 
This is the only path to sustainable acceleration.
""")

st.caption("APRF Svatantrya Intelligence Engine | Node 0 + Graph + Simulation")
