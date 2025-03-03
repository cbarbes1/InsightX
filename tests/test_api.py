import InsightX as insightx
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def main():
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
    if not api_key:
        raise ValueError("Please set the ALPHAVANTAGE_API_KEY environment variable.")

    data = insightx.fetch_gas_data(api_key)
    insightx.save_json(data)
    insightx.plot_wti_data(data)

if __name__ == "__main__":
    main()