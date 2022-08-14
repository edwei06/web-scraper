
from matplotlib.pyplot import new_figure_manager
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os
my_header = {'useragent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'Referer':'https://www.mksh.phc.edu.tw/home'}

web = requests.get('https://www.mksh.phc.edu.tw/home',headers = my_header)
soup = BeautifulSoup(web.text, 'html.parser')
imgs = soup.find_all('img')

name = 0
img_urls = []
for i in imgs:
    try : 
        img_urls.append((i['src']))
    except KeyError:
        pass
new_img_url = []
for item in img_urls:
    try :
        if item[0] == 'h':
            new_img_url.append([item,name])
            name += 1
    except IndexError:
        continue
# print(new_img_url)

def download_image(url):
    jpg = requests.get(url[0])
    if os.path.exists(f'D:/image test folder/mksh') == False:
        os.mkdir(f'D:/image test folder/mksh')
        print('good')
    if os.path.exists(f'D:/image test folder/mksh/{url[1]}.png') !=True :
        f = open(f'D:/image test folder/mksh/{url[1]}.png', 'wb')
        f.write(jpg.content)
        f.close()
        print(url)


executor = ThreadPoolExecutor()          
with ThreadPoolExecutor() as executor:
    executor.map(download_image, new_img_url)     















