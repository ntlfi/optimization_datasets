# New York State Population by ZIP Code and Age

## Dataset Description
This [dataset]() contains **population data** for the state of New York by **zip code** and **age**. The dataset provides the total number of individuals in each age group for each zip code in New York State. 

## Dataset Summary
|   |   |
|:---:|:---:|
| **Data Provider** | US Census Bureau |
| **Region** | New York State |
| **Time Period** | 2018 - 2022 |
| **Data Last Updated** | December 7, 2023 |
| **Posting Frequency** | 5 Years |
| **Number of Columns** |  |
| **Number of Rows** |  |

## Data Dictionary

| Data Label | Data Type | Data Description |
|:---:|:---:|:---|
| **zip_code** | string | A unique identifier for zip codes in New York State. |
| **age_group (e.g., -5)** | string | The total population for an age group. |

> * "-5" means the total population for under 5 years old; "85+" means the total population for 85 years old and older.
> * There exist some regions with a population of 0.


## Example Data




## Data Source
This dataset is extracted from the [**2018-2022 American Community Survey (ACS) 5-Year Subject Tables**](https://www.census.gov/acs/www/data/data-tables-and-tools/subject-tables/) **> S0101: Age and Sex** provided by [`US Census Bureau`](https://www.census.gov/). See, for example, one of those tables for [**ZIP code 10001**](https://data.census.gov/table?q=10001&t=Age%20and%20Sex). We used the table [**New York State ZIP Codes-County FIPS Cross-Reference**](https://data.ny.gov/Government-Finance/New-York-State-ZIP-Codes-County-FIPS-Cross-Referen/juva-r6g2/about_data) from [`NY Open Data`](https://data.ny.gov/Government-Finance/New-York-State-ZIP-Codes-County-FIPS-Cross-Referen/juva-r6g2/about_data) as reference for a list of ZIP codes in New York State. See [here]() to see how this dataset was generated. 