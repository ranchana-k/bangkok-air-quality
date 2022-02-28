# Bangkok PM2.5 Forecast
How the quantity of PM2.5 which is one of the pollutant factor of AQI (Air Quality Index) at Din Daeng district, Bangkok will be in the next 2 days? Analyze changes in PM2.5' levels over the period and forecast for the next 2 days using Vector Autoregression (VAR), Autoregression (AR) and deep learning using recurrent neuron network model.

# Project Motivation

Air quality has been concerned recently in Thailand. There were more people experienced health effects from PM2.5 
(particulate matter with less than 2.5 micrometer diameter).
Bad air quality has effects on people's health especially sensitive groups. 
They had better avoid outdoor activities or prepare their N95 respirators instead of surgical masks if needed. 
Like weather forecast, knowing how the air quality will be in the near future helps people prepare and manage their life.

# Objectives
This project aim to forecast the quantity of PM2.5 which is one of the six pollutants used in AQI calculation. The forecasts were divided into 2 sections as followings:
- Section 1: Time series analysis and forecasting using VAR and AR
- Section 2: Forecasting using RNN models (Unidirectional LSTM and Bidirectional LSTM)

# Method
The data collected for time series analysis and prediction with VAR and AR were from Dec 1, 2021 to Jan 5, 2022. As it was hourly measured, there were 864 rows in total with 815 rows (with differencing level 1) for training and 48 rows for testing. Then, the dataset was updated to Feb 23, 2022 09:00:00 (totally 864 + 1,162 = 2,026 rows) in order to train with RNN model.

# Files Description

- scrape_air4thai.py - code for scraping pollutants measurement
- report_54t_dindaeng.csv - a dataset from crawling and used for time series analysis
- cleaned_dataset.csv - 'report_54t_dindaeng.csv' after cleaning
- Bangkok PM2.5 Forecast - VAR and AR.ipynb - a python notebook illustrates how the data tidied, analysed and predicted
- Bangkok PM2.5 Forecast - RNN models - a python notebook about training RNN models and their predictions

# Summary
### Section 1
- The PACF plots showed that pollutants changes in Din Daeng District, Bangkok had insignificantly relationship with its lag 1. 
- Each pollutant seemed to have effects on each other as Vector Autoregression model gave less error than Autoregression model. However, both VAR and AR models were still not good to predict the value in the next two days (48 hours) as their RMSEs values were still high compared to their means. The RMSE of PM2.5 values for VAR and AR model (lags=1) were 15.96 and 19.48 with average at about 40.


# Licenses / Acknowledgements / References

- The raw data was crawled by the author from Air4Thai (Data resources: http://air4thai.pcd.go.th/webV2/history/)


