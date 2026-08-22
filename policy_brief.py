# policy_brief.py
def generate_brief(trika_state, current_gdp, simulated_gdp, simulated_inflation, stimulus, education_investment):
    brief = f"""
    **The System Speaks:**
    
    We are currently in a state of **{trika_state}**. 
    The latest GDP growth is **{current_gdp}%**.
    
    **The Tantric Action:**
    If we increase Fiscal Stimulus by **{stimulus}%** of GDP, our simulation shows GDP rises to **{simulated_gdp:.2f}%**, 
    but inflation risks rising to **{simulated_inflation:.2f}%**. 
    
    **The Embodiment Principle:**
    *   **Expansion:** Invest in Industry.
    *   **Contraction:** Control Inflation by investing in Skills (Education).
    *   **Stability:** The system remains balanced.
    *   **Evolution:** The system learns from every feedback loop.
    
    **Final Recommendation:** 
    You cannot simply push a button to grow. You must **orchestrate** the Education Node and Economic Node simultaneously.
    """
    return brief
