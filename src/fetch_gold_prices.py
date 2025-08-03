import requests
import csv
from datetime import datetime

API_KEY = "goldapi-pi9smdvlpx-io"  
url = "https://www.goldapi.io/api/XAU/EUR"
headers = {
    "x-access-token": API_KEY,
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()

if response.status_code == 200:
    print("Gold price (EUR/oz):", data.get("price"))
    print("Open price:", data.get("open_price"))
    print("High price:", data.get("high_price"))
    print("Low price:", data.get("low_price"))
    print("Timestamp:", data.get("timestamp"))

    # Save to CSV
    with open("data/gold_price_eur.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.utcfromtimestamp(data["timestamp"]).strftime('%Y-%m-%d %H:%M:%S'),
            data.get("price"),
            data.get("open_price"),
            data.get("high_price"),
            data.get("low_price")
        ])
    print("Saved to data/gold_price_eur.csv")
else:
    print("Error:", data)
