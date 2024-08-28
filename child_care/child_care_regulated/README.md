# New York State Child Care Regulated Programs

## Dataset Description
This [dataset](https://github.com/ntlfi/optimization_datasets/blob/main/child_care/child_care_regulated/child_care_regulated.csv) contains basic information for facilities of **regulated child care programs** in New York State, including the location and capacity of each facility, for each age group.

The data does not include any information regarding day care center programs in New York City, as those programs are regulated by the New York City Department of Health and Mental Hygiene. The inspection data reflects only reflects inspections that were conducted where violations were cited. It does not reflect inspections where no violations are cited.


## Dataset Summary
|   |   |
|:---:|:---:|
| **Data Provider** | NYS Office of Children and Family Services (OCFS) |
| **Region** | New York State |
| **Time Period** | Up-to-date |
| **Data Last Updated** | August 24, 2024 |
| **Posting Frequency** | Daily |
| **Number of Columns** | 13 |
| **Number of Rows** | 15540 |

## Data Dictionary

| Data Label | Data Type | Data Description |
|:---:|:---:|:---|
| **facility_id** | int64 | Unique number automatically generated at Children and Family Services to identify an individual facility |
| **program_type** | object | Type of child care program |
| **facility_status** | object | Status of the facility |
| **facility_name** | object | DBA (legal entity/doing business as) name or Legal Name (last name, first name) |
| **city** | object | City the program is located in. |
| **zip_code** | int64 | Zip code of the city the program is located in |
| **school_district_name** | object | Name of School District in which Program is located |
| **infant_capacity** | int64 | For DCC, total number of children up to 18 months of age |
| **toddler_capacity** | int64 | For DCC, total number of children ages 18 months to 36 months |
| **preschool_capacity** | int64 | For DCC, total number of children at least 3 years of age who are not yet enrolled in kindergarten or a higher grade |
| **school_age_capacity** | int64 | For DCC and SACC, total number of children who are under 13 years of age who are enrolled in kindergarten or a higher grade |
| **children_capacity** | int64 | For FDC and GFDC, the total number of children ages 6 weeks to 12 years |
| **total_capacity** | int64 | Total capacity of the facility |

> Data types above are subject to change. 

> **[Abbreviation Notes]** 
> * **Program types**: *FDC* = Family Day Care; *GFDC* = Group Family Day Care; *SACC* = School Age Child Care; *DCC* = Day Care Center; *SDCC* = Small Day Care Center;
> * **Facility status**: *License* = GFDC or DCC; *Registration* = FDC, SACC, SDCC; *Pending Revocation* = recommended for revocation; *Pending Revocation & Denial* = recommended for revocation/denial; *Pending Denial* = recommended for denial; *Suspended* = may not care for children.


## Example Data
|    |   facility_id | program_type   | facility_status   | facility_name                                     | city         |   zip_code | school_district_name   |   infant_capacity |   toddler_capacity |   preschool_capacity |   school_age_capacity |   children_capcity |   total_capacity |
|---:|--------------:|:---------------|:------------------|:--------------------------------------------------|:-------------|-----------:|:-----------------------|------------------:|-------------------:|---------------------:|----------------------:|-------------------:|-----------------:|
|  0 |            14 | GFDC           | License           | Levine, Rosemarie                                 | Albany       |      12203 | Albany                 |                 0 |                  0 |                    0 |                     2 |                 12 |               14 |
|  1 |          5555 | FDC            | Registration      | Matey, Sally                                      | Jamestown    |      14701 | Jamestown              |                 0 |                  0 |                    0 |                     2 |                  6 |                8 |
|  2 |         40414 | DCC            | License           | Early Childhood Cooperative Experience            | Harris       |      12742 | nan                    |                24 |                 36 |                   38 |                     0 |                  0 |               98 |
|  3 |         40542 | DCC            | License           | The New Rochelle Day Nursery                      | New Rochelle |      10801 | New Rochelle           |                 0 |                 38 |                   74 |                     0 |                  0 |              112 |
|  4 |         44327 | DCC            | License           | St. Lawrence County Community Development Program | Ogdensburg   |      13669 | Ogdensburg             |                 0 |                  0 |                   17 |                     0 |                  0 |               17 |
|  5 |         44774 | DCC            | License           | Haverstraw Head Start                             | Haverstraw   |      10927 | Haverstraw-Stony Pt    |                 0 |                  0 |                  120 |                     0 |                  0 |              120 |
|  6 |        107869 | DCC            | License           | Parsons Child and Family Center                   | Schenectady  |      12304 | Schenectady            |                 0 |                  0 |                   95 |                     0 |                  0 |               95 |
|  7 |        134735 | DCC            | License           | St. Lawrence County Community Development Program | Potsdam      |      13676 | Potsdam                |                 0 |                  0 |                   42 |                     0 |                  0 |               42 |
|  8 |        162378 | SACC           | Registration      | Committee for Hispanic Children and Families, Inc | Bronx        |      10453 | Bronx 10               |                 0 |                  0 |                    0 |                   269 |                  0 |              269 |
|  9 |        226129 | GFDC           | License           | Daddy's Day Care Limited Liability Company        | Elmont       |      11003 | Elmont                 |                 0 |                  0 |                    0 |                     4 |                 12 |               16 |



## Data Source
This dataset is sourced from [**NY Open Data**](https://data.ny.gov/Human-Services/Child-Care-Regulated-Programs/cb42-qumz/about_data). See [here](https://github.com/ntlfi/optimization_datasets/blob/main/child_care/child_care_regulated/fetch.py) to see how this dataset was generated. 