from matplotlib.pyplot import cla
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os

url = 'https://www.photos18.com/?q=DJAWA'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')
cards = soup.find(class_ = 'card-body p-2')
articleurl = cards.find('a')['href']
print(articleurl)
web = requests.get(f'https://www.photos18.com{articleurl}')
soup = BeautifulSoup(web.text, 'html.parser')
title = soup.find(class_ = 'title py-1')
imgurl = soup.find_all(class_ = 'my-2 imgHolder')
for i in imgurl:
    imgurl = i.find_all('a')
    for j in imgurl:
        url = j['href']
        print(url)