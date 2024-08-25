#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

client = Socrata("data.ny.gov", None)
results = client.get("uhf3-t34z", limit=3000)
# Currently, partially copied from child_care/child_care_regulated/fetch.py


# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# Save to CSV
results_df.to_csv("origin_destination_estimate.csv", index=False)