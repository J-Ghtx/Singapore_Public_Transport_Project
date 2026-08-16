import requests
import csv
import os
from datetime import datetime, timedelta
print("Starting collection for August 15, 2026...")
url = "https://api.data.gov.sg/v1/transport/taxi-availability"
os.makedirs("data", exist_ok=True)
csv_path = "data/august_15_2026.csv"
start_time = datetime(2026, 8, 15, 0, 0, 0)
end_time = datetime(2026, 8, 16, 0, 0, 0)
with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "TaxiCount"])
current_time = start_time
while current_time < end_time:
    timestamp_string = current_time.strftime("%Y-%m-%dT%H:%M:%S")
    params = {
        "date_time": timestamp_string
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        coordinates = data["features"][0]["geometry"]["coordinates"]
        taxi_count = len(coordinates)
        with open(csv_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp_string, taxi_count])
        print(f"{timestamp_string}: {taxi_count} taxis")
    except Exception as e:
        print(f"{timestamp_string}: ERROR - {e}")
    current_time += timedelta(minutes=20)
print("Finished collecting August 15, 2026 data.")
print(f"Saved to: {csv_path}")