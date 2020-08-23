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

#closing the firefox
driver.quit()
