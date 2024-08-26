import pandas as pd
from sodapy import Socrata

client = Socrata("data.ny.gov", None)
results = client.get("bg59-42xi", limit=3000)
print(len(results))

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# Save to CSV
results_df.to_csv("schedule.csv", index=False)