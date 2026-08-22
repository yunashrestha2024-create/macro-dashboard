import streamlit as st
import macro_reality_node
import rsp_manifesto_node
import publications_node
import wellbeing_node
import simulation_node
import knowledge_graph

st.set_page_config(page_title="APRF Intelligence Engine 2026", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); color: white; }
    .stTitle { color: #00ff9d; font-size: 3rem; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("APRF Intelligence Engine 2026")
st.subheader("National-Global Policy Intelligence System")

# Navigation Sidebar (The Rhizomatic Nodes)
st.sidebar.title("🧭 System Navigation")
node = st.sidebar.radio(
    "Select Node",
    ["🌐 Macro Reality", "📜 RSP Manifesto Analysis", "📚 Publications", 
     "🕊️ Well-being", "🔮 Simulation", "🔗 Knowledge Graph"]
)

# Route to the appropriate Node
if node == "🌐 Macro Reality":
    macro_reality_node.show()
elif node == "📜 RSP Manifesto Analysis":
    rsp_manifesto_node.show()
elif node == "📚 Publications":
    publications_node.show()
elif node == "🕊️ Well-being":
    wellbeing_node.show()
elif node == "🔮 Simulation":
    simulation_node.show()
elif node == "🔗 Knowledge Graph":
    knowledge_graph.show()

st.caption("© 2026 APRF Intelligence Engine | Svatantrya System")
