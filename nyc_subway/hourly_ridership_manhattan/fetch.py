# -*- coding: utf-8 -*-
"""

The file is for downloading and pre-processing the hourly ridership data from 
https://data.ny.gov/Transportation/MTA-Subway-Hourly-Ridership-Beginning-February-202/wujg-7c2s/about_data.

"""

# make sure to install these packages before running: sodapy
import pandas as pd # type: ignore
import os
from sodapy import Socrata # type: ignore

# Unauthenticated client only works with public data sets. Note 'None' in place of application token, and no username or password:
client = Socrata("data.ny.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.ny.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

day_list = [
    "2024-7-15",
    "2024-7-16", 
    "2024-7-17", 
    "2024-7-18", 
    "2024-7-19", 
    "2024-7-20", 
    "2024-7-21", 
    "2024-7-22", 
    "2024-7-23",
    "2024-7-24",
]

list_of_data = []
print("-" * (len(day_list) * 24))
for day in day_list:
    for hour in range(0, 24):
        # First 3000 results, returned as JSON from API / converted to Python list of dictionaries by sodapy.
        results = client.get("wujg-7c2s", transit_timestamp=f"{day}T{hour:02d}:00:00.000", transit_mode="subway", borough="Manhattan", limit=3000)
        if len(results) == 3000:
            print(f"Warning: {day}T{hour:02d}:00:00.000 has more than 3000 records")
        else:
            print("o", end="")

        # Convert to pandas DataFrame
        df = pd.DataFrame.from_records(results)

        # Modify pandas DataFrame
        df_ridership = df[["transit_timestamp", 
                        "station_complex_id", 
                        "ridership", 
                        "transfers"]]
        station_info = df[["station_complex_id", 
                        "station_complex", 
                        "latitude", 
                        "longitude"]].drop_duplicates()
        station_info = station_info.rename(columns={'station_complex_id': 'station_id', 
                                                    'station_complex': 'station_name'})
        df = df_ridership.rename(columns={'transit_timestamp': 'timestamp', 
                                        'station_complex_id': 'station_id'})
        df.reset_index(drop=True, inplace=True)
        df["ridership"] = df["ridership"].map(lambda x: int(x[:-2])) + df["transfers"].map(lambda x: int(x[:-2]))
        df = df[['station_id', 'ridership']]

        # Group by timestamp and station_id, as we care about the sum of ridership and transfers for each station at each hour
        grouped = df.groupby(["station_id"]).sum()
        grouped.reset_index(inplace=True)

        # Left join with station_info
        grouped_df = pd.merge(grouped, station_info, how="left", on="station_id")
        grouped_df["timestamp"] = f"{day}T{hour:02d}:00:00.000"

        list_of_data.append(grouped_df)

# Concatenate all the dataframes
res = pd.concat(list_of_data)

# Rearrange columns and sort by timestamp and station_id
res = res.reset_index(drop=True)
res = res[['timestamp', 'station_id', 'station_name', 'latitude', 'longitude', 'ridership']]
res = res.sort_values(by=["timestamp", "station_id"], ascending=[True, True])

# Save as CSV
current_directory = os.path.dirname(os.path.abspath(__file__))
res.to_csv(f"{current_directory}/hourly_ridership_manhattan.csv")

# Print the first 10 rows as markdown
print()
print("The number of rows in the dataset is", len(res))
print("The number of columns in the dataset is", len(res.columns))
print(res[:10].to_markdown())
