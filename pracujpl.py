import random 
import requests
from bs4 import BeautifulSoup
lang = input("podaj język\n")
city = input ("podaj miasto\n")
#print(soup.get_text)
for i in range(6):
  print(random.randrange(1,50))
url = 'https://www.pracuj.pl/praca/'+lang+';kw/'+city+';wp?rd=50'
page = requests.get(url)
#print(page.content)
soup2 = BeautifulSoup(page.content,'html.parser')
print(soup2.title.string)
element = soup2.find(class_="results-header__offer-count-text-number")
if element is None:
  print("nie ma ofert")
else:
  print("Oferty pracy " + lang, element.text)