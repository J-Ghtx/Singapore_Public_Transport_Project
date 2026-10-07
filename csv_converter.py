import pandas as pd
import matplotlib.pyplot as plt
import os
csv_file = "data/national_day_2026.csv"
df = pd.read_csv(csv_file)
base_name = os.path.splitext(os.path.basename(csv_file))[0]
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
plt.plot(df["Timestamp"], df["TaxiCount"])
plt.title("Taxi Availability Over Time")
plt.xlabel("Time")
plt.ylabel("Available Taxis")
plt.xticks(rotation=45)
plt.savefig(f"figures/{base_name}.png")
plt.show()