import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os
article_url = []
titles = []
num = 0

url = 'https://www.photos18.com/?q=DJAWA'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')
cards = soup.find_all(class_ = 'card-body p-2')
for i in cards:
    article_url.append([i.find('a')['href'],num])
    titles.append(i.find('a').string)
    num += 1

url = 'https://www.photos18.com/q/DJAWA?page=2'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')
cards = soup.find_all(class_ = 'card-body p-2')
for i in cards:
    article_url.append([i.find('a')['href'],num])
    titles.append(i.find('a').string)
    num += 1

def check_image(url):
    print(titles[url[1]])
    if not os.path.exists(f'//nas/prohub/DJAWA/{article_url[links][0][3:]}'):
        aritical_web = requests.get(f'https://www.photos18.com{url[0]}')
        soup = BeautifulSoup(aritical_web.text,'html.parser')
        img = soup.findAll(class_ = 'my-2 imgHolder')
        name = 0
        img_urls = []
        for i in img:
            try:
                imgurl = i.find_all('a')
            except KeyError:
                continue
            for j in imgurl:
                img_urls.append([j['href'],name])
                name += 1
        os.makedirs(f'//nas/prohub/DJAWA/{article_url[links][0][3:]}')
        executor = ThreadPoolExecutor()          
        with ThreadPoolExecutor() as executor:
            executor.map(download_image, img_urls)   

def download_image(url):
    jpg = requests.get(url[0])
    f = open(f'//nas/prohub/DJAWA/{article_url[links][0][3:]}/{url[1]}.jpg','wb')
    f.write(jpg.content)
    f.close()
    print(url)

for links in range(len(titles)):
    print(article_url[links][0][3:])
    check_image(article_url[links])