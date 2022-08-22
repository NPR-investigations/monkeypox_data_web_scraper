![](https://github.com/NPR-investigations/monkeypox_data_web_scraper/blob/main/repo_media/NPRLogo_CMYK_Medium.jpg)

# Monkey Pox Data Webscraper
This repository scrapes and archives the following:
  1. [Jynneos vaccine allocation data from the U.S. Department of Health and Human Services’ (HHS) Administration for Strategic Preparedness and Response (ASPR)](https://aspr.hhs.gov/SNS/Pages/JYNNEOS-Distribution.aspx)

  2.[Monkeypox case count by state from the CDC](https://www.cdc.gov/poxvirus/monkeypox/response/2022/us-map.html)
  
 ## Scraping Schedule
 The webscraper runs everyday at 2:00 p.m. EST
  
 ## Data Structure
 
```
.
├── data
│   └── cases_by_state_data
|     └── cases_by_state_table_current.csv
|     └── cases_by_state_text_current.txt
|     └── daily
|       └── 2022-08-22
|         └── cases_by_state_table_2022-08-22.csv
|         └── cases_by_state_text_2022-08-22.txt
|       └── 2022-xx-xx
|         └── cases_by_state_table_2022-xx-xx.csv
|         └── cases_by_state_text_2022-xx-xx.txt
│   └── doses_by_state_data
|     └── doses_by_state_table_current.csv
|     └── doses_by_state_text_current.txt
|     └── daily
|       └── 2022-08-22
|         └── doses_by_state_table_2022-08-22.csv
|         └── doses_by_state_text_2022-08-22.txt
|       └── 2022-xx-xx
|         └── doses_by_state_table_2022-xx-xx.csv
|         └── doses_by_state_text_2022-xx-xx.txt

```

- `cases_by_state_data`
  - This is the directory that contains CDC data of monkeypox cases by state
  - `cases_by_state_data/cases_by_state_table_current.csv`
    - The latest monkeypox cases by state data that the webscraper downloaded
  - `cases_by_state_data/cases_by_state_text_current.txt`
    - The explanatory text accompanying the latest monkeypox cases by state data that the webscraper downloaded
  - `cases_by_state_data/daily`
    - This is the directory that contains the CDC data of monkeypox cases by state broken down by each day the web scraper ran
    - `cases_by_state_data/daily/cases_by_state_table_2022-xx-xx.csv`
      - The monkeypox cases by state data that the webscraper downloaded on the date listed in the file name
    - `cases_by_state_data/daily/cases_by_state_text_2022-xx-xx.txt`
      - The explanatory text accompanying the monkeypox cases by state data that the webscraper downloaded  on the date listed in the file name

- `doses_by_state_data`
  - This is the directory that contains the U.S. Department of Health and Human Services’ (HHS) Administration for Strategic Preparedness and Response (ASPR) data on Jynneos vaccine allocation by state.
  - `doses_by_state_data/doses_by_state_table_current.csv`
    - The latest Jynneos vaccine allocation by state data that the webscraper downloaded
  - `doses_by_state_data/doses_by_state_text_current.txt`
    - The explanatory text accompanying the latest Jynneos vaccine allocation by state data that the webscraper downloaded
  - `doses_by_state_data/daily`
    - This is the directory that contains U.S. Department of Health and Human Services’ (HHS) Administration for Strategic Preparedness and Response (ASPR) data on Jynneos vaccine allocation by state broken down by each day the web scraper ran
    - `doses_by_state_data/daily/doses_by_state_table_2022-xx-xx.csv`
      - The Jynneos vaccine allocation by state data that the webscraper downloaded on the date listed in the file name
    - `doses_by_state_data/daily/doses_by_state_text_2022-xx-xx.txt`
      - The explanatory text accompanying the Jynneos vaccine allocation by state data that the webscraper downloaded on the date listed in the file name

## Contact
Please contact @nmcmillan@npr.org with any questions

