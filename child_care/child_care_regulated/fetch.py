import pandas as pd
from sodapy import Socrata

client = Socrata("data.ny.gov", None)
results = client.get("cb42-qumz", limit=3000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# Print out the first few rows of the data
print(results_df.head())