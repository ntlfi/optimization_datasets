# New York State Child Care Regulated Programs

## Dataset Description
This [dataset]() contains basic information for facilities of **regulated child care programs** in New York State. The dataset provides information on the capacity of each facility, for each age group.

> The data does not include any information regarding day care center programs in New York City, as those programs are regulated by the New York City Department of Health and Mental Hygiene. The inspection data reflects only reflects inspections that were conducted where violations were cited. It does not reflect inspections where no violations are cited.


## Dataset Summary
|   |   |
|:---:|:---:|
| **Data Provider** | NYS Office of Children and Family Services |
| **Region** | New York State |
| **Time Period** | Update to date |
| **Data Last Updated** | August 24, 2024 |
| **Posting Frequency** | Daily |
| **Number of Columns** | 13 |
| **Number of Rows** | 15540 |

## Data Dictionary

 0   facility_id           15540 non-null  int64 
 1   program_type          15540 non-null  object
 2   facility_status       15540 non-null  object
 3   facility_name         15540 non-null  object
 4   city                  15540 non-null  object
 5   zip_code              15540 non-null  int64 
 6   school_district_name  15492 non-null  object
 7   infant_capacity       15540 non-null  int64 
 8   toddler_capacity      15540 non-null  int64 
 9   preschool_capacity    15540 non-null  int64 
 10  school_age_capacity   15540 non-null  int64 
 11  children_capcity      15540 non-null  int64 
 12  total_capacity        15540 non-null  int64 


| Data Label | Data Type | Data Description |
|:---:|:---:|:---|
| **facility_id** | int64 | Unique number automatically generated at Children and Family Services to identify an individual facility. |
| **program_type** | object | Type of child care program. |
| **facility_status** | object | Status of the facility. |
| **facility_name** | object | DBA (legal entity/doing business as) name or Legal Name (last name, first name). |
| **city** | object | City the program is located in. |
| **zip_code** | int64 | Zip code of the city the program is located in. |
| **school_district_name** | object | Name of School District in which Program is located. |
| **infant_capacity** | int64 | For DCC, total number of children up to 18 months of age. |
| **toddler_capacity** | int64 | For DCC, total number of children ages 18 months to 36 months |
| **preschool_capacity** | int64 | For DCC, total number of children at least 3 years of age who are not yet enrolled in kindergarten or a higher grade |
| **school_age_capacity** | int64 | For DCC and SACC, total number of children who are under 13 years of age who are enrolled in kindergarten or a higher grade |
| **children_capacity** | int64 | For FDC and GFDC, the total number of children ages 6 weeks to 12 years. |
| **total_capacity** | int64 | Total capacity of the facility |
> Program Types: *FDC* = Family Day Care; *GFDC* = Group Family Day Care; *SACC* = School Age Child Care; *DCC* = Day Care Center; *SDCC* = Small Day Care Center
> Facility Status: *License* = GFDC or DCC; *Registration* = FDC, SACC, SDCC; *Pending Revocation* = recommended for revocation; *Pending Revocation & Denial* = recommended for revocation/denial; *Pending Denial* = recommended for denial; *Suspended* = may not care for children


## Example Data




## Data Source
This dataset is extracted from the . See [here]() to see how this dataset was generated. 