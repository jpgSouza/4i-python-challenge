import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

url = "https://br.investing.com/economic-calendar/" #web URL

#Firefox defining
option = Options()
option.headless = True
driver = webdriver.Firefox()

#getting the url and opening the Firefox
driver.get(url)

#delay to load the page
time.sleep(5)

#event click to change filters
driver.find_element_by_xpath('//*[@id="timeFrame_thisWeek"]').click()

#delay to apply the filters
time.sleep(3)

#economic table path
element = driver.find_element_by_xpath('//*[@id="economicCalendarData"]')
html_content = element.get_attribute('outerHTML')

#closing firefox
driver.quit()
