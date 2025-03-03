import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def plot_wti_data(data):
    """Plots WTI crude oil price data."""
    dates = []
    values = []
    for item in data['data']:
        try:
            date = datetime.strptime(item['date'], '%Y-%m-%d')
            value = float(item['value'])
            dates.append(date)
            values.append(value)
        except ValueError:
            value = 0  # Replace with 0 or another appropriate default

        

    plt.figure(figsize=(12, 6))
    plt.plot(dates, values, marker='o', linestyle='-')
    plt.title(data['name'])
    plt.xlabel('Date')
    plt.ylabel(data['unit'])
    plt.grid(True)

    # Format the date axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gcf().autofmt_xdate()  # Rotate date labels for better readability

    plt.tight_layout()
    plt.show()