# New York State Population by ZIP Code and Age

## Dataset Description
This [dataset](https://github.com/ntlfi/optimization_datasets/blob/main/child_care/nys_pop_by_zipcode_age/population.csv) contains **population data** for the state of New York by **zip code** and **age**. The dataset provides the total number of individuals in each age group for each zip code in New York State. 

## Dataset Summary
|   |   |
|:---:|:---:|
| **Data Provider** | US Census Bureau |
| **Region** | New York State |
| **Time Period** | 2018 - 2022 |
| **Data Last Updated** | December 7, 2023 |
| **Posting Frequency** | 5 Years |
| **Number of Columns** | 20 |
| **Number of Rows** | 1646 |

## Data Dictionary

| Data Label | Data Type | Data Description |
|:---:|:---:|:---|
| **zip_code** | string | A unique identifier for zip codes in New York State. |
| **-5** | string | The total population for under 5 years old |
| **-10** | string | The total population for 5 to 9 years old |
| **10-14** | string | The total population for 10 to 14 years old |
| **15-19** | string | The total population for 15 to 19 years old |
| **20-24** | string | The total population for 20 to 24 years old |
| **25-29** | string | The total population for 25 to 29 years old |
| **30-34** | string | The total population for 30 to 34 years old |
| **35-39** | string | The total population for 35 to 39 years old |
| **40-44** | string | The total population for 40 to 44 years old |
| **45-49** | string | The total population for 45 to 49 years old |
| **50-54** | string | The total population for 50 to 54 years old |
| **55-59** | string | The total population for 55 to 59 years old |
| **60-64** | string | The total population for 60 to 64 years old |
| **65-69** | string | The total population for 65 to 69 years old |
| **70-74** | string | The total population for 70 to 74 years old |
| **75-79** | string | The total population for 75 to 79 years old |
| **80-84** | string | The total population for 80 to 84 years old |
| **85+** | string | The total population for 85 years old and older |

> * There exist some regions with a population of 0.


## Example Data
|    |   zipcode |   Total |   -5 |   5-9 |   10-14 |   15-19 |   20-24 |   25-29 |   30-34 |   35-39 |   40-44 |   45-49 |   50-54 |   55-59 |   60-64 |   65-69 |   70-74 |   75-79 |   80-84 |   85+ |
|---:|----------:|--------:|-----:|------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|------:|
|  0 |      6390 |      53 |    0 |     1 |       5 |       0 |       6 |       0 |       9 |      18 |       0 |      12 |       2 |       0 |       0 |       0 |       0 |       0 |       0 |     0 |
|  1 |     10001 |   27004 |  744 |   784 |     942 |    1035 |    2296 |    3806 |    3588 |    2524 |    1702 |    1903 |    1704 |    1225 |    1323 |     933 |     815 |     616 |     488 |   576 |
|  2 |     10002 |   76518 | 2142 |  3046 |    3198 |    2652 |    4528 |    6988 |    6278 |    5157 |    4962 |    4822 |    4410 |    6106 |    4548 |    4815 |    4748 |    2531 |    2793 |  2794 |
|  3 |     10003 |   53877 | 1440 |  1034 |     953 |    7013 |    6344 |    7100 |    6427 |    3221 |    2907 |    1988 |    2698 |    2350 |    2274 |    2793 |    1854 |    1646 |     779 |  1056 |
|  4 |     10004 |    4579 |  433 |   182 |     161 |     108 |     109 |     601 |     724 |     490 |     241 |     313 |     549 |     279 |     199 |     173 |       2 |      15 |       0 |     0 |
|  5 |     10005 |    8801 |  484 |   204 |     229 |      53 |     989 |    2604 |    1144 |     945 |     685 |     351 |     652 |     218 |      85 |      92 |      66 |       0 |       0 |     0 |
|  6 |     10006 |    3736 |  128 |    96 |      75 |     242 |     258 |     593 |     778 |     445 |     428 |     316 |     172 |      58 |      56 |       6 |      65 |       0 |       0 |    20 |
|  7 |     10007 |    7506 |  605 |   451 |     290 |     188 |     414 |     760 |    1074 |     750 |     505 |    1042 |     489 |     126 |     171 |     369 |     172 |       0 |      65 |    35 |
|  8 |     10009 |   58418 | 1896 |  1658 |    1835 |    1322 |    4892 |    7440 |    7784 |    3980 |    3624 |    2841 |    2963 |    4957 |    4078 |    2858 |    2368 |    1489 |    1256 |  1177 |
|  9 |     10010 |   32410 | 1422 |  1592 |     948 |    1921 |    2640 |    3364 |    3516 |    3145 |    1839 |    1874 |    1467 |    1247 |    1870 |    1694 |    1621 |     898 |     760 |   592 |



## Data Source
This dataset is extracted from the [**2018-2022 American Community Survey (ACS) 5-Year Subject Tables**](https://www.census.gov/acs/www/data/data-tables-and-tools/subject-tables/) **> S0101: Age and Sex** provided by [`US Census Bureau`](https://www.census.gov/). See, for example, one of those tables for [**ZIP code 10001**](https://data.census.gov/table?q=10001&t=Age%20and%20Sex). We used the table [**New York State ZIP Codes-County FIPS Cross-Reference**](https://data.ny.gov/Government-Finance/New-York-State-ZIP-Codes-County-FIPS-Cross-Referen/juva-r6g2/about_data) from [`NY Open Data`](https://data.ny.gov/Government-Finance/New-York-State-ZIP-Codes-County-FIPS-Cross-Referen/juva-r6g2/about_data) as reference for a list of ZIP codes in New York State. See [here](https://github.com/ntlfi/optimization_datasets/blob/main/child_care/nys_pop_by_zipcode_age/fetch.py) to see how this dataset was generated. 