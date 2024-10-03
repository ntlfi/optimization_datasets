import numpy as np
import pandas as pd
import re
from sodapy import Socrata

client = Socrata("data.ny.gov", None)
len_results = 3000
list_data = []
start = 0
while len_results == 3000:
    results = client.get("cb42-qumz", offset=start * 3000, limit=3000)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    list_data.append(results_df)

    len_results = len(results)
    start += 1
results_df = pd.concat(list_data).reset_index(drop=True)

df = results_df[['facility_id', 'program_type', 'region_code', 'county', 'facility_status', 'facility_name', 'city', 'state', 'zip_code', 'school_district_name', 'capacity_description', 'infant_capacity', 'toddler_capacity', 'preschool_capacity', 'school_age_capacity', 'total_capacity', 'latitude', 'longitude']]

seq = df["capacity_description"]
list = []
for string in seq:
    if str(string) != 'nan':
        list_cap = re.split(' AND ', string)
        if " children, ages 6 weeks to 12 years" in list_cap[0]:
            list.append(int(list_cap[0].replace(" children, ages 6 weeks to 12 years", "")))
        else:
            list.append(0)
    else: 
        list.append(0)
df["children_capcity"] = pd.Series(list, copy=False)
df = df.astype({'children_capcity': 'int64', 
                'infant_capacity': 'int64', 
                'toddler_capacity': 'int64', 
                'preschool_capacity': 'int64', 
                'school_age_capacity': 'int64', 
                'total_capacity': 'int64'})

# check if sum('children_capacity', 'infant_capacity', 'toddler_capacity', 'preschool_capacity', 'school_age_capacity') == 'total_capacity'
df['sum'] = df['children_capcity'] + df['infant_capacity'] + df['toddler_capacity'] + df['preschool_capacity'] + df['school_age_capacity']

for i in range(len(df)):
    try: 
        assert df.loc[i]['sum'] == df.loc[i]['total_capacity']
    except AssertionError:
        print(i, df.loc[i]['sum'], df.loc[i]['total_capacity'])

# do this manually and carefully
i = 12790
print(df.loc[i]['facility_id'])
df.at[i, 'total_capacity'] = df.loc[i]['sum']

df = df[['facility_id', 'program_type', 'facility_status', 'facility_name', 'city' , 'zip_code', 'school_district_name', 'infant_capacity', 'toddler_capacity', 'preschool_capacity', 'school_age_capacity', 'children_capcity', 'total_capacity', 'latitude', 'longitude']]

df.to_csv("child_care_regulated.csv", index=False)