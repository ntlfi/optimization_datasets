# %%
import numpy as np
import pandas as pd
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# Load the data
df = pd.read_excel(f"{current_dir}/21zp33ny.xlsx")

# %%
df = df[["NEW YORK", "Unnamed: 1", "Unnamed: 2"]]
df.columns = ["ZIP code", "income group", "number of returns"]

# for each row, delete nan values
df = df.dropna()

df.drop(df.index[0], inplace=True)

df.drop(df[df["ZIP code"] == 0].index, inplace=True)
df.drop(df[df["ZIP code"] == 99999].index, inplace=True)

# reindex the dataframe
df.reset_index(drop=True, inplace=True)

# %%
list_zip_code = []
list_individual_income = []

def calculate_income(income_info):
    dict_income_group = {
        0: 12500, 
        1: 37500, 
        2: 62500, 
        3: 87500, 
        4: 150000, 
        5: 200000, 
    }

    avg_income = 0
    for i in range(6):
        avg_income += dict_income_group[i] * (income_info[i] / sum(income_info))

    return avg_income

for i in range(len(df)):
    if len(list_zip_code) == 0 or df.at[i, "ZIP code"] != list_zip_code[-1]:
        list_zip_code.append(df.at[i, "ZIP code"])
        count = 1
        income_info = [df.at[i, "number of returns"], ]
    else:
        count += 1
        income_info.append(df.at[i, "number of returns"])

    if count == 6:
        list_individual_income.append(calculate_income(income_info))

# %%
income = pd.DataFrame({"ZIP code": list_zip_code, "average income": list_individual_income})
income.to_csv(f"{current_dir}/average_income.csv", index=False)

# %%
# read the total population data
population = pd.read_csv(f"{current_dir}/../nys_pop_by_zipcode_age/population.csv")
population = population[["zipcode", "Total"]]

# %%
num = df[["ZIP code", "number of returns"]]
num = num.groupby("ZIP code").sum()

# %%
# marge the two dataframes
employment = pd.merge(num, population, left_on="ZIP code", right_on="zipcode")
employment["employment rate"] = employment["number of returns"] / employment["Total"]
employment["employment rate"] = employment["employment rate"].apply(lambda x: min(x, 0.99))
employment = employment[["zipcode", "employment rate"]]

# %%
employment.to_csv(f"{current_dir}/employment_rate.csv", index=False)