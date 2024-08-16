## MTA Subway Hourly Ridership: Beginning February 2022
---

### Dataset Description
This dataset contains hourly ridership data for the New York City Metropolitan Transportation Authority (MTA) subway system. 

### Dataset Summary

|   |   |
|:---:|:---:|
| **Data Provider** | Metropolitan Transportation Authority (MTA) |
| **Time Period** | July 16 - July 31, 2024 |
| **Data Last Updated** | July 31, 2024 |
| **Posting Frequency** | August 15, 2024 |
| **Number of Rows** |  |
| **Number of Columns** |  |

### Data Dictionary

| Data Label | Data Type | Data Description |
|:---:|:---:|:---|
| timestamp | [floating timestamp](https://dev.socrata.com/docs/datatypes/floating_timestamp.html#,) | Timestamp payment took place in local time. All transactions here are rounded down to the nearest hour. For example, a swipe that took place at 1:37pm will be reported as having taken place at 1pm. |
| station_id | alphanumeric | A unique identifier for station complexes |
| station_name | string | The subway complex where an entry swipe or tap took place. Large subway complexes, such as Times Square and Fulton Center, may contain multiple subway lines. The subway complex name includes the routes that stop at the complex in parenthesis, such as Zerega Av (6). |
| fare_class_category | string | The class of fare payment used for the trip. The consolidated categories are: <br> • MetroCard – Fair Fare <br> • MetroCard – Full Fare <br> • MetroCard – Other <br> • MetroCard – Senior & Disability <br> • MetroCard – Students <br> • MetroCard – Unlimited 30-Day <br> • MetroCard – Unlimited 7-Day <br> • OMNY – Full Fare <br> • OMNY – Other <br> • OMNY – Seniors & Disabilities |
| ridership | integer | Total number of riders that entered a subway complex via OMNY or MetroCard at the specific hour and for that specific fare type. |
| transfers | integer | Number of individuals who entered a subway complex via a free bus-to-subway, or free out-of-network transfer. This represents a subset of total ridership, meaning that these transfers are already included in the preceding ridership column. Transfers that take place within a subway complex (e.g., individuals transferring from the 2 to the 4 train within Atlantic Avenue) are not captured here. |
| latitude | float | Latitude for the specified subway complex. |
| longitude | float | Longitude for the specified subway complex. |

### Example Data
|    | timestamp               |   station_id | station_name   | fare_class_category         |   ridership |   transfers |   latitude |   longitude |
|---:|:------------------------|-------------:|:---------------|:----------------------------|------------:|------------:|-----------:|------------:|
|  0 | 2023-12-27T09:00:00.000 |          228 | 23 St (F,M)    | OMNY - Seniors & Disability |           2 |           0 |    40.7429 |    -73.9928 |
|  1 | 2023-12-27T09:00:00.000 |          162 | 50 St (C,E)    | Metrocard - Full Fare       |          87 |           1 |    40.7625 |    -73.986  |
|  2 | 2023-12-27T09:00:00.000 |          333 | Wall St (2,3)  | OMNY - Full Fare            |         165 |           2 |    40.7068 |    -74.0091 |
|  3 | 2023-12-27T09:00:00.000 |          477 | 72 St (Q)      | Metrocard - Fair Fare       |           7 |           0 |    40.7688 |    -73.9584 |
|  4 | 2023-12-27T09:00:00.000 |          144 | Dyckman St (A) | Metrocard - Full Fare       |          44 |           0 |    40.8655 |    -73.9273 |

### Data Source
>  [**NY Open Data**](https://data.ny.gov/Transportation/MTA-Subway-Hourly-Ridership-Beginning-February-202/wujg-7c2s/about_data)