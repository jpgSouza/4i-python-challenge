# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

converted_rating_list = []
url = "https://br.investing.com/economic-calendar/" #web URL

#Firefox defining
option = Options()
#background manipulation
option.headless = True
driver = webdriver.Firefox(options=option)

#getting the url and opening the Firefox
print('Loading...')
driver.get(url)

#delay to load the page
time.sleep(5)

#filter button path and event click to change filters
driver.find_element_by_xpath('//*[@id="timeFrame_thisWeek"]').click()

#delay to apply the filters
time.sleep(3)

#economic table path
element = driver.find_element_by_xpath('//*[@id="economicCalendarData"]')
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')

# getting economics rating data
ratings = soup.findAll("td",{"class":"left textNum sentiment noWrap"})

for rating_data in ratings:
    #saving rating titles
    titles = rating_data.get('title')
    #converting rating titles to Integer
    if titles == 'Volatilid. Esperada Baixa':
        converted_rating_list.append("1")
    elif titles == 'Volatilid. Esperada Moderada':
        converted_rating_list.append("2")
    else:
        converted_rating_list.append("3")

table = soup.find(name='table')

df_full = pd.read_html(str(table))[0]

# getting columns data
df = df_full[['Hora', 'Moeda', 'Import.', 'Evento', 'Atual', 'Projeção', 'Prévio']]

# creating columns
df.columns = ['Hour', 'Currency', 'Import.', 'Event', 'Current', 'Projection', 'Previous']

# filtering data
filtered_df = df.loc[(df['Currency'] == 'USD') | (df['Currency'] == 'BRL')]

# casting dataframe to .csv
filtered_df.to_csv('economic_calendar.csv', encoding='utf-8-sig')

print('Scraping Successfully')

#closing firefox
driver.quit()
