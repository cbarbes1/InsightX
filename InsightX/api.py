import requests
import json



def clean_commodity_json(data):
    """Cleans the JSON data for WTI crude oil price."""
    if 'data' in data:
        data['data'] = [item for item in data['data'] if item.get('value') != '.']
    return data

def fetch_gas_data(api_key):
    """Fetches WTI crude oil price data from Alpha Vantage."""
    url = f"https://www.alphavantage.co/query?function=COFFEE&interval=annual&apikey={api_key}"
    r = requests.get(url)
    data = r.json()
    data = clean_commodity_json(data)
    return data


def fetch_news_data(api_key, symbol):
    """Fetches WTI crude oil price data from Alpha Vantage."""
    url = f"https://www.alphavantage.co/query?function=COFFEE&interval=annual&apikey={api_key}"
    r = requests.get(url)
    data = r.json()
    data = clean_commodity_json(data)
    return data