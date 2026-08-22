# knowledge_graph.py
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

def display_knowledge_graph():
    G = nx.Graph()
    
    # Nodes
    G.add_node("RSP Promises", type="Policy", color="red")
    G.add_node("MoF Budget", type="Policy", color="red")
    G.add_node("GDP Growth", type="Macro", color="green")
    G.add_node("Unemployment", type="Macro", color="green")
    G.add_node("Education", type="Education", color="orange")
    G.add_node("Spiritual Anchor", type="Spiritual", color="purple")
    
    # Edges
    G.add_edge("RSP Promises", "MoF Budget")
    G.add_edge("MoF Budget", "GDP Growth")
    G.add_edge("GDP Growth", "Unemployment")
    G.add_edge("Education", "Unemployment")
    G.add_edge("Spiritual Anchor", "Education")
    
    # Visualize
    net = Network(height="500px", width="100%", bgcolor="#ffffff", font_color="#000000")
    net.from_nx(G)
    net_html = net.generate_html()
    components.html(net_html, height=500, width="100%")
