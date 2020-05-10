# crawling, scraping
# requests do połączenia z stroną
# beautifulsoup4 do wyszukania z odpowiedzi elementu html
import requests as r
from bs4 import BeautifulSoup
url = 'https://pogoda.onet.pl/prognoza-pogody/warszawa-357732'
response = r.get(url)
# int() - zamieniamy na liczbe całkowitą
soup = BeautifulSoup(response.text,'html.parser')
temp = soup.select('.temp')
print(temp[0].text)
