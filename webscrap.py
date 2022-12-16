from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome(r"C:\Users\reach\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('https://www.typingbaba.com/translator/english-to-tamil-translation.php')
time.sleep(2)

driver.find_element(By.ID,"english_text").send_keys("My name is ankith")
driver.find_element(By.ID,"_trans").click()
time.sleep(10)
tt = driver.find_element(By.ID,"hindi_text")
print(tt.get_attribute('text'))


print("இன்று வானிலை என்ன")

# button = driver.find_element_by_link_text("Sign In")
# button.click()

# import requests
# from bs4 import BeautifulSoup
# import csv

# URL = "https://www.typingbaba.com/translator/english-to-tamil-translation.php"
# r = requests.get(URL)

# soup = BeautifulSoup(r.content, 'html5lib')
# # print(soup.prettify().encode("utf-8"))
# quotes=[] # a list to store quotes

# table = soup.find('div', attrs = {'class':'w-100  p-2  hindi-font no-change   border border-secondary'})
# print(table)

# for row in table.findAll('div',attrs = {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
# 	print(row)
# 	quote = {}
# 	quote['theme'] = row.h5.text
# 	quote['url'] = row.a['href']
# 	quote['img'] = row.img['src']
# 	quote['lines'] = row.img['alt'].split(" #")[0]
# 	quote['author'] = row.img['alt'].split(" #")[1]
# 	quotes.append(quote)

# filename = 'inspirational_quotes.csv'
# with open(filename, 'w', newline='',encoding="utf-8") as f:
# 	w = csv.DictWriter(f,['theme','url','img','lines','author'])
# 	w.writeheader()
# 	for quote in quotes:
# 		w.writerow(quote)
# print("இன்று வானிலை என்ன".encode('utf-8'))
