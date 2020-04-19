import random 
import requests
from bs4 import BeautifulSoup
dict = {
  "first":"pierwszy",
  "end":"koniec",
  "tea":"herbata",
  "dog":"pies"
}

print(dict)
word = input ("podaj wyraz\n")
if word in dict:
  print (dict[word])
else:
  print("brak słowa")
for i in range(20,0,-1):
  print(i)

for i in range(0,10):
  print("*",end='')

#print("\n")
print ("*"*10)
r = requests.get("http://www.rajkonkret.pl/")
soup = BeautifulSoup(r.content,features="html.parser")
list = soup.find_all('div')
for i in list:
  print(i.get('class'))

#print(soup.get_text)
for i in range(6):
  print(random.randrange(1,50))
url = 'https://www.pracuj.pl/praca/python;kw/lodz;wp?rd=50'
page = requests.get(url)
#print(page.content)
soup2 = BeautifulSoup(page.content,'html.parser')
print(soup2.title.string)
element = soup2.find(class_="results-header__offer-count-text-number")
print("Oferty pracy Python w Łodzi ", element.text)

