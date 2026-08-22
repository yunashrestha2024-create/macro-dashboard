# trika_core.py
def get_trika_state(gdp_growth):
    if gdp_growth > 5.0:
        return "🧘 **Expansion** (Growth Mode: The system is expanding, but must watch for overheating)"
    elif gdp_growth < 3.0:
        return "🧘 **Contraction** (Recession Mode: The system is contracting, need immediate stimulus)"
    else:
        return "🧘 **Stability** (Steady State: The system is stable, but must break inertia to reach target)"
