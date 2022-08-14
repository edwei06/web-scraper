import requests
from bs4 import BeautifulSoup



def geturl(url, my_headers):
    response = requests.get(url, headers = my_headers)
    response.encoding = "utf-8"
    return response.text

my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"}

url='http://hr.mcu.edu.tw/zh-hant/content/%E8%A1%A8%E6%A0%BC%E4%B8%8B%E8%BC%89downloadable-forms'


htmldata = geturl(url, my_headers)
soup = BeautifulSoup(htmldata,'html.parser')
tab = soup.find(class_ = 'col-md-6 col-lg-6')
tb = tab.find('p')
link = tb.find('a')
href = ('http://hr.mcu.edu.tw'+str(link['href']))
print(href)
odt = requests.get(href, my_headers)
file = open('D:/image test folder/first file test.odt','a')
file.write(odt.content)
file.close()
print(link['href'])







