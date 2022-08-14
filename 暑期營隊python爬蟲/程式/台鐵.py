import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
timenow = datetime.datetime.now()
year = timenow.year
month = timenow.month
day = timenow.day

payload= {
	'_csrf': '1907d91c-036c-43de-be20-9e12f8b334c3',
	'trainTypeList': 'ALL',
	'transfer': 'ONE',
	'startStation': '1000-臺北',
	'endStation': '0980-南港',
	'rideDate': f'{year}/{month}/{day}',
	'startOrEndTime': 'true',	
	'startTime': '01:00',
	'endTime': '23:00',
}


response = requests.post("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime", data = payload)
response.encoding="utf-8"

soup = BeautifulSoup(response.text, 'html.parser')
train = soup.findAll('tr', class_="trip-column")
pricelist =[]
trainNolist = []
startTimelist = []
endTimelist = []
estlist = []
for i in train:
	test = i.find('s')
	price_parent = test.parent
	price = price_parent.find('span').text
	pricelist.append(price)
	trainNo = i.find('a').text
	trainNolist.append(trainNo)
	first_td_tag=i.find('td')
	startTime = first_td_tag.findNext('td')
	startTimelist.append(startTime.text)
	endTime = startTime.findNext('td')
	endTimelist.append(endTime.text)
	est = endTime.findNext('td')
	estlist.append(est.text)

data ={
	'Train':trainNolist,
	'Price':pricelist,
	'startTimelist':startTimelist,
	'endTimelist':endTimelist,
	'est':estlist
}

final_data = pd.DataFrame(data,)

print(final_data)

final_data.to_csv(f'G:/vs code file/web scraper/暑期營隊python爬蟲/程式/台鐵{year}-{month}-{day}.csv',index = False, encoding = 'utf-8-sig')






