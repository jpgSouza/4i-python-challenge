import requests
from bs4 import BeautifulSoup

url = "https://br.investing.com/economic-calendar/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

result = requests.get(url, headers=headers)

# result status code
print(result)

soup = BeautifulSoup(result.text, 'lxml')

table = soup.find_all('table', id='economicCalendarData')

for table_content in table:
    list = table_content.find_all("td")
    for list_data in list:
        print(list_data.next_element)

