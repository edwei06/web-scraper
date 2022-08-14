#import the necessary libraries ans fuction
from turtle import title
import urllib.request as req
from matplotlib.pyplot import tick_params
from requests import request
import bs4
#enter the wanted url
url = 'https://www.ptt.cc/bbs/Stock/index.html'

#build a request object, using the request headers info
request = req.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.0.43 Safari/537.36'
})

with req.urlopen(request) as response:
    data = response.read().decode('utf-8')
# print(data)

#analyze the source code and get the title of every article

root = bs4.BeautifulSoup(data, 'html.parser')
# print(root.title.string)
titles = root.find_all('div', class_="title") # search for every title with div tag
print(titles)

for title in titles:
    if title.a != None:
        print(title.a.string)





















