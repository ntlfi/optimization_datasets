import requests
import pandas as pd
from sodapy import Socrata

client = Socrata("data.ny.gov", None)
results = client.get("juva-r6g2", limit=3000)
results_df = pd.DataFrame.from_records(results)
all_zipcodes = sorted(results_df["zip_code"].unique())
print(all_zipcodes)


list_data = []
for zipcode in all_zipcodes:
    url = f"https://api.census.gov/data/2022/acs/acs5/subject?get=group(S0101)&ucgid=860Z200US{zipcode}"
    # url = "https://api.census.gov/data/2022/acs/acs5/subject?get=group(S0101)&ucgid=860Z200US11361"
    try:
        response = requests.get(url)
        data = response.json()

        # 
        df = pd.DataFrame(data, columns=data[0]).drop(0)
        list_columns = [
            "S0101_C01_001E",
            "S0101_C01_002E",
            "S0101_C01_003E",
            "S0101_C01_004E",
            "S0101_C01_005E",
            "S0101_C01_006E",
            "S0101_C01_007E",
            "S0101_C01_008E",
            "S0101_C01_009E",
            "S0101_C01_010E",
            "S0101_C01_011E",
            "S0101_C01_012E",
            "S0101_C01_013E",
            "S0101_C01_014E",
            "S0101_C01_015E",
            "S0101_C01_016E",
            "S0101_C01_017E",
            "S0101_C01_018E",
            "S0101_C01_019E",
        ]
        df = df[list_columns]
        df = df.rename(columns={
            "S0101_C01_001E": "Total",
            "S0101_C01_002E": "-5", 
            "S0101_C01_003E": "5-9",
            "S0101_C01_004E": "10-14",
            "S0101_C01_005E": "15-19",
            "S0101_C01_006E": "20-24",
            "S0101_C01_007E": "25-29",
            "S0101_C01_008E": "30-34",
            "S0101_C01_009E": "35-39",
            "S0101_C01_010E": "40-44",
            "S0101_C01_011E": "45-49",
            "S0101_C01_012E": "50-54",
            "S0101_C01_013E": "55-59",
            "S0101_C01_014E": "60-64",
            "S0101_C01_015E": "65-69",
            "S0101_C01_016E": "70-74",
            "S0101_C01_017E": "75-79",
            "S0101_C01_018E": "80-84",
            "S0101_C01_019E": "85+",
        })
        df["zipcode"] = zipcode
        print(df)
        list_data.append(df)
    except:
        print(f"Missing: {zipcode}")

final_df = pd.concat(list_data)
final_df.to_csv("population.csv", index=False)