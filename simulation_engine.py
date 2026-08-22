# simulation_engine.py
def simulate_policy(gdp_growth, inflation, stimulus, education_investment):
    # Calculate simulated outputs
    sim_gdp = gdp_growth + (stimulus * 0.4) + (education_investment * 0.1)
    sim_inflation = inflation + (stimulus * 0.2) - (education_investment * 0.05)
    
    return sim_gdp, sim_inflation
