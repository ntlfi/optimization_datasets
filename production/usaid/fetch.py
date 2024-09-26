import pandas as pd
from sodapy import Socrata
import os

client = Socrata("data.usaid.gov", None)
results = client.get("a3rc-nmf6", limit=30000)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)
df.set_index('id', inplace=True)
df = df[["country", "shipment_mode", "scheduled_delivery_date", "delivered_to_client_date", "product_group", "sub_classification", "unit_of_measure_per_pack", "line_item_quantity", "line_item_value", "pack_price", "unit_price", "weight_kilograms", "freight_cost_usd", "dosage"]]
# Get the directory of the current file
pwd = os.path.dirname(os.path.realpath(__file__))

# Save the data to a CSV file
df.to_csv(f'{pwd}/supply_chain_pricing.csv')





# countries = df['country'].unique()
# # Save country specific data to CSV files
# airports = pd.DataFrame({"country": countries})
# airports.to_csv(f'{pwd}/airports/airports.csv')

countries = df['country'].unique()
# Save country specific data to CSV files
ports = pd.DataFrame({"country": countries})
ports.to_csv(f'{pwd}/ports/ports.csv')
