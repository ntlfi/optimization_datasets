import pandas as pd
from sodapy import Socrata

client = Socrata("data.usaid.gov", None)
results = client.get("a3rc-nmf6", limit=3000, country="Vietnam")

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)
df.set_index('id', inplace=True)
df = df[["country", "shipment_mode", "scheduled_delivery_date", "delivered_to_client_date", "product_group", "sub_classification", "unit_of_measure_per_pack", "line_item_quantity", "line_item_value", "pack_price", "unit_price", "weight_kilograms", "freight_cost_usd", "dosage"]]

# Save the data to a CSV file
df.to_csv('supply_chain_pricing.csv')

countries = df['country'].unique()

# Save country specific data to CSV files
countries.to_csv('./airports/airports.csv')
