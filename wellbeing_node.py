import streamlit as st
import pandas as pd  # <--- ADD THIS
import plotly.express as px  # <--- ADD THIS

def show():
    st.subheader("🕊️ Spirituality & Well-being Node")
    
    wellbeing = {
        "Indicator": ["Social Trust", "Cultural Resilience", "Mental Well-being", "Community Engagement"],
        "Current": [45, 62, 58, 50],
        "Target": [75, 80, 85, 75]
    }
    df = pd.DataFrame(wellbeing)
    st.dataframe(df)
    
    fig = px.bar(df, x="Indicator", y=["Current", "Target"], barmode="group")
    st.plotly_chart(fig)
