from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait, Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



web =  'http://air4thai.pcd.go.th/webV2/history/'
s = Service('/usr/bin/geckodriver')

driver = webdriver.Firefox(service=s)
driver.get(web)

station = driver.find_element(By.ID, 'station_name')
station_selected = station.find_element(By.XPATH, ".//option[@value='54t']")
station_selected.click()
# to select data features needed (air pollutants)
parameters = driver.find_element(By.ID, 'parameter_name')
para1 = parameters.find_element(By.XPATH, ".//option[@value='PM25']")
# may note be used
# para2 = parameters.find_element(by.xpath, ".//option[@value='pm10']")
# para3 = parameters.find_element(by.xpath, ".//option[@value='o3']")
# para4 = parameters.find_element(by.xpath, ".//option[@value='co']")
para5 = parameters.find_element(By.XPATH, ".//option[@value='NO2']")
ActionChains(driver).key_down(Keys.SHIFT).click(para1).key_up(Keys.SHIFT).perform()
ActionChains(driver).key_down(Keys.SHIFT).click(para5).key_up(Keys.SHIFT).perform()

# click the button 'table'
table_btn = driver.find_element(By.ID, 'table_bt')
table_btn.click()

ignored_exception = (StaleElementReferenceException,)
scrape = True
report = []
while scrape:
    rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
    for row in rows:
        data = row.find_elements(By.XPATH, './/td')
        report.append([ele.text for ele in data])
    # find html element
    html_ele = driver.find_element(By.TAG_NAME, 'html')
    # Scrolls down to the bottom of the page
    html_ele.send_keys(Keys.END)
    # find the next button
    next = driver.find_element(By.XPATH, "//li[@id='table1_next']/a")
    next_parent = next.find_element(By.XPATH, "..")

    if "disabled" not in next_parent.get_attribute("class").split():

        next.click()

    else:
        scrape = False
    
driver.quit()
df = pd.DataFrame(report, columns=['No', 'date', 'time', 'PM2.5', 'PM10','O3', 'CO', 'NO2'])

df.to_csv('report_54t_dindaeng.csv', index=False)

