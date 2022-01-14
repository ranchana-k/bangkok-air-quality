# Bangkok AQI (Air Quality Index) Forecast
What the AQI index at Din Daeng district, Bangkok will be in the next 5 days? Analyze changes in air pollutants' levels over the period and forecast the AQI index in the next 5 days using Vector Autoregression (VAR) compared to individual SARIMA.

# Project Motivation

Air quality has been concerned recently in Thailand. There were more people experienced health effects from PM2.5 
(particulate matter with less than 2.5 micrometer diameter).
Bad air quality has effects on people's health especially sensitive groups. 
They had better avoid outdoor activities or prepare their N95 respirators instead of surgical masks if needed. 
Like weather forecast, knowing how the air quality will be in the near future helps people prepare and manage their life.

# Files Description

- scrape_air4thai.py - code for scraping pollutants measurement
- report_54t_dindaeng.csv - a dataset from crawling and used for time series analysis
- Bangkok Air Quality Index Forecast.ipynb - a python notebook illustrates how the data tidied, analysed and predicted

# Licenses / Acknowledgements / References

The raw data was crawled by the author from Air4Thai (Data resources: http://air4thai.pcd.go.th/webV2/history/)
