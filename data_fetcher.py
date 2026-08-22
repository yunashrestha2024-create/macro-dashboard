# data_fetcher.py
import requests
import pandas as pd

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

def fetch_world_bank_inflation():
    try:
        url = "https://api.worldbank.org/v2/country/NPL/indicator/FP.CPI.TOTL.ZG?format=json&per_page=10"
        response = requests.get(url, timeout=10)
        data = response.json()
        rows = data[1]
        years = [int(row['date']) for row in rows]
        values = [row['value'] for row in rows]
        df = pd.DataFrame({'Year': years, 'Inflation (%)': values})
        return df.dropna()
    except:
        return None
