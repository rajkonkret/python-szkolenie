from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os

#launch url
url = "https://www.olx.pl/oferta/wynajme-ladne-mieszkanie-z-wyposazeniem-w-cudnym-miejscu-CID3-IDCs5VG.html"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

#After opening the url above, Selenium clicks the specific agency link
python_button_cookie = driver.find_element_by_class_name('cookiesBarClose')
#python_button_cookie.focus()
driver.implicitly_wait(10)
python_button_cookie.click()
python_button = driver.find_element_by_class_name("spoiler")
python_button.click() #click fhsu link

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get('https://www.olx.pl/oferta/wynajme-ladne-mieszkanie-z-wyposazeniem-w-cudnym-miejscu-CID3-IDCs5VG.html')
python_button_cookie = driver.find_element_by_class_name('cookiesBarClose')
#python_button_cookie.focus()
driver.implicitly_wait(10)
python_button_cookie.click()
p_c = driver.find_element_by_class_name('contactitem')
p_c.click()


#python_button = driver.find_element_by_id('button inverted spoiler') #FHSU
#python_button.click() #click fhsu link
driver.implicitly_wait(10)
print(driver.page_source)
#Selenium hands the page source to Beautiful Soup
soup_level1=BeautifulSoup(driver.page_source, 'html.parser')
soup_level1.findall('strong')
print(soup_level1)