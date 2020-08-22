import requests                 #request in web
from bs4 import BeautifulSoup   #data format
import asyncio                  #async
from pyppeteer import launch    #manipulations and filters

url = "https://br.investing.com/economic-calendar/" #web URL
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

#function to access de url and apply "thisWeek" filter
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)

    await page.click('#timeFrame_thisWeek')

    await page.screenshot({'path': 'example.png'})

    await browser.close()

asyncio.get_event_loop().run_until_complete(main()) #calling the function

#--------------- [Data request] --------

result = requests.get(url, headers=headers)

# result status code
print(result)

soup = BeautifulSoup(result.text, 'lxml')

table = soup.find_all('table', id='economicCalendarData')

for table_header in table:
    columns = table_header.find_all('th')
    for columns_data in columns:
        print(columns_data.text)

for table_content in table:
    list = table_content.find_all('td')
    for list_data in list:
        print(list_data.text)
