import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os


def check_image(url):
    if os.path.exists(f'//nas/prohub/{actress.string}/{titles[url[1]].string}') == False:
        aritical_web = requests.get(url[0])
        soup = BeautifulSoup(aritical_web.text,'html.parser')
        img = soup.findAll('img')
        name = 0
        img_urls = []
        for i in img:
            try:
                img_urls.append([i['data-src'],name])
                name += 1
            except KeyError:
                pass
        try:
            os.makedirs(f'//nas/prohub/{actress.string}/{titles[url[1]].string}')
        except OSError:
            pass
        executor = ThreadPoolExecutor()          
        with ThreadPoolExecutor() as executor:
            executor.map(download_image, img_urls)   

        
def download_image(url):
    jpg = requests.get(url[0])
    f = open(f'//nas/prohub/{actress.string}/{titles[links].string}/{url[1]}.jpg','wb')
    f.write(jpg.content)
    f.close()
    print(f'{url},{titles[url[1]].string}')

actresses = ['mei-tao-jiang','yu-zi-jiang-fish','zhi-zhi-booty','lu-xuan-xuan','wang-yu-chun',
            'li-zi-xi','dou-ban-jiang','zhou-yu-xi-dummy','chen-ruo-yi','wang-xin-yao','yun-er'
            ,'xuan-zi','jiu-shi-a-zhu-a','zhou-yan-xi','cheng-cheng-cheng','xu-yuan-yuan','zhang-si-yun',
            'mi-ni'
            ]

for act in actresses:
    url = f'https://f6mm.com/tag/{act}'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, 'html.parser')
    page = soup.findAll('a',class_='page-link')
    try:
        for j in range(int(page[len(page)-2].string)):
            url = f'https://f6mm.com/tag/{act}/{j+1}'
            web = requests.get(url)
            soup = BeautifulSoup(web.text, 'html.parser')
            titles = soup.find_all('div', class_='item-link-text')
            titlelinks = soup.find_all(class_='item-link')
            actress = soup.find('p')
            article_url = []
            num = 0
            for i in titlelinks:
                article_url.append([i['href'],num])
                num += 1 

            for links in range(len(titles)):    
                check_image(article_url[links])
    except IndexError:
        pass
