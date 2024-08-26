# MTA Subway Service Delivered: Beginning 2020

## Dataset Description
Service Delivered measures the percentage of scheduled trains that are actually provided during **peak hours on weekdays** (7 AM to 10 AM and 4 PM to 7 PM) and **weekends** (10 AM to 6 PM) for a given month. This dataset covers data from 2020 and on. For data between 2015 and 2019, use dataset https://data.ny.gov/Transportation/MTA-Subway-Service-Delivered-2015-2019/32ch-sei3.

## Dataset Summary

|   |   |
|:---:|:---:|
| **Data Provider** | Metropolitan Transportation Authority (MTA) |
| **Region** | New York City |
| **Time Period** | 2020 - 2024 |
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




