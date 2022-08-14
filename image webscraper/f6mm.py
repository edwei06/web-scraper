from ast import Pass
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os


url = 'https://f6mm.com/tag/yu-zi-jiang-fish'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')
title = soup.find('div', class_='item-link-text')
actress = soup.find('p')
print(actress.string)



titlelinks = soup.find(class_='item-link')
aritical_web = requests.get(titlelinks['href'])
soup = BeautifulSoup(aritical_web.text, 'html.parser')
img = soup.findAll('img')
print(img)
img_urls = []
name = 0
for i in img:
    try:
        img_urls.append([i['data-src'],name])
        name += 1
    except KeyError:
        Pass
# print(img_urls)
def download_image(url):
    print(url)
    jpg = requests.get(url[0])
    if os.path.exists(f'D:/image test folder/{title.string}') == False:
        os.mkdir(f'D:/image test folder/{title.string}')
    if os.path.exists(f'D:/image test folder/{title.string}/{url[1]}.jpg') !=True :
        f = open(f'D:/image test folder/{title.string}/{url[1]}.jpg', 'wb')
        f.write(jpg.content)
        f.close()


executor = ThreadPoolExecutor()          
with ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)     



titlelinks = soup.findAll(class_='item-link')
articles = []
for link in titlelinks:
    articles.append(link['href'])
print(articles)

for link in articles:
    img_urls = []
    soup = BeautifulSoup(link,'html.parser')
    imgs = soup.find_all('img')
    for i in imgs:
        img_urls.append([i['data-src']])
    print(f'the img urls  in {link} are {img_urls}')

























