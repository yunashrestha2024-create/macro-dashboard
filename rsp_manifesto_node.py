import streamlit as st
import pandas as pd

def show():
    st.subheader("📜 RSP Manifesto vs Reality Analysis")
    
    # The 100 Promises (Core Pillars)
    manifesto_data = {
        "Pillar": ["Governance & Integrity", "Middle-Class Expansion", "Employment & Productivity", 
                   "Connectivity & Infrastructure", "Diaspora Engagement"],
        "Promises": ["Anti-corruption, Digital State", "Tax Reform, SME Support", "1M Jobs, Skill Alignment", 
                     "Transport, Energy, Digital", "Investment Channels, Knowledge Return"],
        "Reality Status": ["🔴 Critical Gap", "🟠 High Gap", "🔴 Critical Gap", "🟡 Moderate Gap", "🟠 High Gap"],
        "Observation": ["Bureaucracy resists change", "Idle liquidity, weak investment", "High migration, low industry", 
                        "Slow execution, weak capacity", "No clear policy framework"]
    }
    
    df = pd.DataFrame(manifesto_data)
    st.dataframe(df)
    
    # Reality Check Visualization
    st.markdown("### 📊 Promises vs Reality (Gap Analysis)")
    gap_counts = df["Reality Status"].value_counts()
    st.bar_chart(gap_counts)
    
    st.write("""
    **Research Insight:**
    The RSP's 100 Promises are ambitious but lack an embedded intelligence system to track execution. 
    This Node is designed to connect each promise to real-time macro data, so the public can see exactly 
    where the government is succeeding and where it is failing.
    """)
