import streamlit as st

def show():
    st.subheader("📚 APRF Research Publications")
    
    publications = [
        {"title": "From Responsible Expansion to Rhizomatic Governance", "year": 2026, "status": "📄 Published"},
        {"title": "Policy Intelligence Lab: Nepal Macro Analysis", "year": 2026, "status": "📄 Published"},
        {"title": "AI as Infrastructure: A Development Framework", "year": 2026, "status": "✍️ Drafting"},
        {"title": "Svatantrya System: A Trika-Based Governance Model", "year": 2026, "status": "🔬 Researching"}
    ]
    
    for pub in publications:
        st.markdown(f"**{pub['title']}** ({pub['year']}) - {pub['status']}")
