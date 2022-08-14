#import the necessary libraries ans fuction
import urllib.request as req
from matplotlib.pyplot import get
from requests import request
import bs4
#def a getdata function to get data from one page
def getdata(url):
    #build a request object, using the request headers info
    request = req.Request(url, headers={
        'cookie': 'over18=1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.0.43 Safari/537.36'
    })

    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')
    # print(data)

    #analyze the source code and get the title of every article

    root = bs4.BeautifulSoup(data, 'html.parser')
    # print(root.title.string)
    titles = root.find_all('div', class_="title") # search for every title with div tag
    # print(titles)

    for title in titles:
        if title.a != None:
            print(title.a.string)

    #get the link for the next page
    nextLink = root.find('a',string='‹ 上頁') # search for next link with string in a tag
    return print(nextLink['href'])

#enter the wanted url
pageurl = 'https://www.ptt.cc/bbs/Beauty/index.html'
pageurl = f'https://www.ptt.cc{getdata(pageurl)}'
print(pageurl)








