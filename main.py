import json
print("Taxi Tracker Started")
import requests
import csv
import time
from datetime import datetime
url = "https://api.data.gov.sg/v1/transport/taxi-availability"
def collect_data():
    response = requests.get(url)
    data = response.json()
    coordinates = data["features"][0]["geometry"]["coordinates"]
    taxi_count = len(coordinates)
    timestamp = datetime.now()
    print(f"{timestamp}: {taxi_count} taxis available")
    with open("data/taxi_counts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, taxi_count])
    print(f"{timestamp}: {taxi_count} taxis recorded")
collect_data()