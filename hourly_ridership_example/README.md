# MTA Subway Hourly Ridership

## Dataset Description
This [dataset](https://github.com/ntlfi/optimization_datasets/blob/main/hourly_ridership_example/hourly_ridership_manhattan.csv) contains **hourly ridership data** for the New York City Metropolitan Transportation Authority (MTA) *subway* system. In a given period, the dataset provides the total number of riders that entered a subway complex in *Manhattan* for each hour. The dataset also includes geographical information for each subway complex, such as latitude and longitude.

## Dataset Summary

|   |   |
|:---:|:---:|
| **Data Provider** | Metropolitan Transportation Authority (MTA) |
| **Borough** | Manhattan |
| **Time Period** | July 15 - July 24, 2024 |
| **Data Last Updated** | July 31, 2024 |
| **Posting Frequency** | Weekly |
| **Number of Columns** | 6 |
| **Number of Rows** | 30914 |

## Data Dictionary

| Data Label | Data Type | Data Description |
|:---:|:---:|:---|
| **timestamp** | [floating timestamp](https://dev.socrata.com/docs/datatypes/floating_timestamp.html#,) | Timestamp payment took place in local time. All transactions here are rounded down to the nearest hour. For example, a swipe that took place at 1:37pm will be reported as having taken place at 1pm. |
| **station_id** | integer | A unique identifier for station complexes |
| **station_name** | string | The subway complex where an entry swipe or tap took place. Large subway complexes, such as *Times Square* and *Fulton Center*, may contain multiple subway lines. The subway complex name includes the routes that stop at the complex in parenthesis, such as Zerega Av (6). |
| **ridership** | integer | Total number of riders that entered a subway complex. Note that this number counts those individuals who entered a subway complex via a free bus-to-subway, or free out-of-network transfer. |
| **latitude** | float | Latitude for the specified subway complex. Note that, for those large subway complexes, such as *Times Square* and *Fulton Center*, may have multiple latitude and longitude entries. |
| **longitude** | float | Longitude for the specified subway complex. |
> Currently, `floating timestamp` is a string in the format of `YYYY-MM-DDTHH:MM:SS.SSS`. This format is subject to change in the future.

## Example Data
|    | timestamp              |   station_id | station_name      |   latitude |   longitude |   ridership |
|---:|:-----------------------|-------------:|:------------------|-----------:|------------:|------------:|
|  0 | 2024-7-15T00:00:00.000 |           10 | 49 St (N,R,W)     |    40.7599 |    -73.9841 |         267 |
|  1 | 2024-7-15T00:00:00.000 |          103 | Bowery (J,Z)      |    40.7203 |    -73.9939 |          66 |
|  2 | 2024-7-15T00:00:00.000 |          107 | Broad St (J,Z)    |    40.7065 |    -74.0111 |          24 |
|  3 | 2024-7-15T00:00:00.000 |          118 | 3 Av (L)          |    40.7328 |    -73.9861 |          97 |
|  4 | 2024-7-15T00:00:00.000 |          119 | 1 Av (L)          |    40.731  |    -73.9816 |         130 |
|  5 | 2024-7-15T00:00:00.000 |           13 | 28 St (R,W)       |    40.7455 |    -73.9887 |         127 |
|  6 | 2024-7-15T00:00:00.000 |           14 | 23 St (R,W)       |    40.7413 |    -73.9893 |          90 |
|  7 | 2024-7-15T00:00:00.000 |          143 | Inwood-207 St (A) |    40.8681 |    -73.9199 |          51 |
|  8 | 2024-7-15T00:00:00.000 |          144 | Dyckman St (A)    |    40.8655 |    -73.9273 |          28 |
|  9 | 2024-7-15T00:00:00.000 |          145 | 190 St (A)        |    40.859  |    -73.9342 |          12 |



## Data Source
This dataset is sourced from [**`NY Open Data`**](https://data.ny.gov/Transportation/MTA-Subway-Hourly-Ridership-Beginning-February-202/wujg-7c2s/about_data). See [here](https://github.com/ntlfi/optimization_datasets/blob/main/hourly_ridership_example/fetch.py) for the code used to generate this dataset.