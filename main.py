import json
print("Taxi Tracker Started")
import requests
import csv
import time
from datetime import datetime
import os
url = "https://api.data.gov.sg/v1/transport/taxi-availability"
def collect_data():
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    coordinates = data["features"][0]["geometry"]["coordinates"]
    taxi_count = len(coordinates)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp}: {taxi_count} taxis available")
    file_exists = os.path.exists("data/taxi_counts.csv")
    with open("data/taxi_counts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "TaxiCount"])
        writer.writerow([timestamp, taxi_count])
    print(f"{timestamp}: {taxi_count} taxis recorded")
while True:
    try:
        collect_data()
    except Exception as e:
        print("Error:", e)
    time.sleep(1200)