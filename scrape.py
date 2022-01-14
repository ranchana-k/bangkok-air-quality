from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait, Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.support.select import Select


web =  'https://bangkokairquality.com/bma/report?lang=en'
driver_path = '/usr/bin/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get(web)
station = Select(driver.find_element_by_xpath('//select[@class="boxsec01"]'))
station.select_by_value('56')
start_date = '16-10-2021'
end_date = '30-11-2021'

start = driver.find_element_by_id('date_from')
start.clear()
start.send_keys(start_date)

start_time_dropdown = Select(driver.find_element_by_name('time_from'))
start_time_dropdown.select_by_value('0:00')

end = driver.find_element_by_id('date_to')
end.clear()
end.send_keys(end_date)

end_time_dropdown = Select(driver.find_element_by_name('time_to'))
end_time_dropdown.select_by_value('23:00')

table_button = driver.find_element_by_xpath('//button[@value="table"]')
table_button.click()

ignored_exception = (StaleElementReferenceException,)
scrape = True
report = []
while scrape:
    rows = driver.find_elements_by_xpath('//table[@id="example"]/tbody/tr')
    for row in rows:
        data = row.find_elements_by_xpath('.//td')
        report.append([ele.text for ele in data])
    next = driver.find_element_by_id("example_next")
    if "disabled" not in next.get_attribute("class").split():
        next.click()

    else:
        scrape = False
    
driver.quit()
df = pd.DataFrame(report, columns=['datetime', 'PM10', 'PM2.5','CO', 'NO2', 'NO', 'NOX'])
df.to_csv('report_bangkhunthain.csv', index=False)

