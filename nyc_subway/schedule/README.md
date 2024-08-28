# MTA Subway Service Delivered 

## Dataset Description
This [dataset](https://github.com/ntlfi/optimization_datasets/blob/main/nyc_subway/schedule/schedule.csv) contains **service delivered data** for the New York City Metropolitan Transportation Authority (MTA) subway system. One can read the scheduled and actual number of trains that ran for each subway line during **peak hours** on **weekdays** (7 AM to 10 AM and 4 PM to 7 PM) and **weekends** (10 AM to 6 PM) from this dataset. 



## Dataset Summary

|   |   |
|:---:|:---:|
| **Data Provider** | Metropolitan Transportation Authority (MTA) |
| **Region** | New York City |
| **Time Period** | Since 2020 |
| **Data Last Updated** | August 22, 2024 |
| **Posting Frequency** | Monthly |
| **Number of Columns** | 7 |
| **Number of Rows** | 2610 |

## Data Dictionary

| Data Label | Data Type | Data Description |
|:---:|:---:|:---|
| **month** | object (yyyy-mm) | The month of the service delivered |
| **division** | object | Represents the division of the subway line (A Division or B Division) | 
| **line** | object | Represents each subway line | 
| **day_type** | int | Represents the type of day (weekday or weekend) | 
| **num_sched_trains** | int | The number of trains scheduled to run | 
| **num_actual_trains** | int | The number of trains that actually ran | 
| **service_delivered** | float | The percentage of service delivered based on scheduled and actual trains |



## Example Data
|    | month   | division   |   line |   day_type |   num_sched_trains |   num_actual_trains |   service_delivered |
|---:|:--------|:-----------|-------:|-----------:|-------------------:|--------------------:|--------------------:|
|  0 | 2024-07 | A DIVISION |      1 |          1 |               1848 |                1738 |            0.940476 |
|  1 | 2024-07 | A DIVISION |      1 |          2 |                959 |                 948 |            0.98853  |
|  2 | 2024-07 | A DIVISION |      2 |          1 |               2439 |                2284 |            0.936449 |
|  3 | 2024-07 | A DIVISION |      2 |          2 |               1270 |                1213 |            0.955118 |
|  4 | 2024-07 | A DIVISION |      3 |          2 |               1280 |                1241 |            0.969531 |
|  5 | 2024-07 | A DIVISION |      3 |          1 |               2266 |                2116 |            0.933804 |
|  6 | 2024-07 | A DIVISION |      4 |          2 |               1904 |                1791 |            0.940651 |
|  7 | 2024-07 | A DIVISION |      4 |          1 |               3036 |                2876 |            0.947299 |
|  8 | 2024-07 | A DIVISION |      5 |          1 |               2836 |                2633 |            0.92842  |
|  9 | 2024-07 | A DIVISION |      5 |          2 |                768 |                 736 |            0.958333 |

## Data Source
This dataset is sourced from [**`NY Open Data`**](https://data.ny.gov/Transportation/MTA-Subway-Service-Delivered-Beginning-2020/bg59-42xi/about_data). See [here](https://github.com/ntlfi/optimization_datasets/blob/main/nyc_subway/schedule/fetch.py) for the code used to generate this dataset.




