# AQI calculation function
def calculate_AQI(pm25, pm10, o3, co, no2, so2):
    '''The AQI value is the highest value calculated for each pollutant
    Parameters:
      - PM2.5 (ug/m^3) - truncate to 1 decimal place
      - PM10 (ug/m^3) - truncate to integer
      - O3 (ppb) - have to be converted to unit 'ppm' and truncated to 3 decimals places
      - CO (ppm) - truncate to 1 decimals places
      - NO2 (ppb) - truncate to integer
      - SO2 (ppb - truncate to integer
    Return: AQI index'''
    pm25_dict = {"Ip_0_50": {"I_Hi": 50, "I_Lo": 0, "BP_Hi": 12, "BP_Lo": 0},
                 "Ip_51_100": {"I_Hi": 100, "I_Lo": 51, "BP_Hi": 35.4, "BP_Lo": 12.1},
                 "Ip_101_150": {"I_Hi": 150, "I_Lo": 101, "BP_Hi": 55.4, "BP_Lo": 35.5},
                 "Ip_151_200": {"I_Hi": 200, "I_Lo": 151, "BP_Hi": 150.4, "BP_Lo": 55.5},
                 "Ip_201_300": {"I_Hi": 300, "I_Lo": 201, "BP_Hi": 250.4, "BP_Lo": 150.5},
                 "Ip_301_400": {"I_Hi": 400, "I_Lo": 301, "BP_Hi": 350.4, "BP_Lo": 250.5},
                 "Ip_401_500": {"I_Hi": 500, "I_Lo": 401, "BP_Hi": 500.4, "BP_Lo": 350.5}}
    pm10_dict = {"Ip_0_50": {"I_Hi": 50, "I_Lo": 0, "BP_Hi": 54, "BP_Lo": 0},
                 "Ip_51_100": {"I_Hi": 100, "I_Lo": 51, "BP_Hi": 154, "BP_Lo": 55},
                 "Ip_101_150": {"I_Hi": 150, "I_Lo": 101, "BP_Hi": 254, "BP_Lo": 155},
                 "Ip_151_200": {"I_Hi": 200, "I_Lo": 151, "BP_Hi": 354, "BP_Lo": 255},
                 "Ip_201_300": {"I_Hi": 300, "I_Lo": 201, "BP_Hi": 424, "BP_Lo": 355},
                 "Ip_301_400": {"I_Hi": 400, "I_Lo": 301, "BP_Hi": 504, "BP_Lo": 425},
                 "Ip_401_500": {"I_Hi": 500, "I_Lo": 401, "BP_Hi": 604, "BP_Lo": 505}}
    o3_dict = {"Ip_101_150": {"I_Hi": 150, "I_Lo": 101, "BP_Hi": 0.164, "BP_Lo": 0.125},
               "Ip_151_200": {"I_Hi": 200, "I_Lo": 151, "BP_Hi": 0.204, "BP_Lo": 0.165},
               "Ip_201_300": {"I_Hi": 300, "I_Lo": 201, "BP_Hi": 0.404, "BP_Lo": 0.205},
               "Ip_301_400": {"I_Hi": 400, "I_Lo": 301, "BP_Hi": 0.504, "BP_Lo": 0.405},
               "Ip_401_500": {"I_Hi": 500, "I_Lo": 401, "BP_Hi": 0.604, "BP_Lo": 0.505}}
    co_dict = {"Ip_0_50": {"I_Hi": 50, "I_Lo": 0, "BP_Hi": 12, "BP_Lo": 0},
               "Ip_51_100": {"I_Hi": 100, "I_Lo": 51, "BP_Hi": 35.4, "BP_Lo": 12.1},
               "Ip_101_150": {"I_Hi": 150, "I_Lo": 101, "BP_Hi": 55.4, "BP_Lo": 35.5},
               "Ip_151_200": {"I_Hi": 200, "I_Lo": 151, "BP_Hi": 150.4, "BP_Lo": 55.5},
               "Ip_201_300": {"I_Hi": 300, "I_Lo": 201, "BP_Hi": 250.4, "BP_Lo": 150.5},
               "Ip_301_400": {"I_Hi": 400, "I_Lo": 301, "BP_Hi": 350.4, "BP_Lo": 250.5},
               "Ip_401_500": {"I_Hi": 500, "I_Lo": 401, "BP_Hi": 500.4, "BP_Lo": 350.5}}
    pm25_ind, pm10_ind, o3_ind, co_ind, no2_ind, so2_ind = 0, 0, 0, 0, 0, 0

    # calculate PM2.5 Index
    if pm10 >= 0 and pm10 <= 54:
        key = "Ip_0_50"
    elif pm10 > 54 and pm10 <= 154:
        key = "Ip_51_100"
    elif pm10 > 154 and pm10 <= 254:
        key = "Ip_101_150"
    elif pm10 > 254 and pm10 <= 354:
        key = "Ip_151_200"
    elif pm10 > 354 and pm10 <= 424:
        key = "Ip_201_300"
    elif pm10 > 54 and pm10 <= 154:
        key = "Ip_301_400"
    else:
        key = "Ip_401_500"
    pm10_ind = (pm10_dict[key]["I_Hi"] - pm10_dict[key]["I_Lo"]) * (PM10 - pm10_dict[key]["BP_Lo"]) / (
                pm10_dict[key]["BP_Hi"] - pm10_dict[key]["BP_Lo"]) + pm10_dict[key]["I_Lo"]
    return PM10_ind