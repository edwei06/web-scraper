import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

response = requests.get('https://www.railway.gov.tw/tra-tip-web/tip')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# find all citys
city_dict = {}
city_list = []
all_city = soup.find('div', class_ = 'line-inner')
for city in all_city.find_all(class_='btn tipCity'):
    city_list.append(city.text)
    city_dict[(city.text)] = city.get('data-type')

for city in range(len(city_list)):
    print(f'({city}){city_list[city]} ')
start_city = city_list[int(input('請輸入出發地城市代碼: '))]

start_station_list = []
all_station = soup.find('div', id = city_dict[start_city])
for station in all_station.find_all(class_="btn tipStation"):
    start_station_list.append(station.get('title'))

for station in range(len(start_station_list)):
    print(f'({station}){start_station_list[station]} ')
start_station = start_station_list[int(input('請輸入出發站代碼: '))]

for city in range(len(city_list)):
    print(f'({city}){city_list[city]} ')
end_city = city_list[int(input('請輸入抵達地城市代碼: '))]

end_station_list = []
all_station = soup.find('div', id = city_dict[end_city])
for station in all_station.find_all(class_="btn tipStation"):
    end_station_list.append(station.get('title'))

for station in range(len(end_station_list)):
    print(f'({station}){end_station_list[station]} ')
end_station = end_station_list[int(input('請輸入出發站代碼: '))]

print('請輸入日期,包含年月日,只有從今日起90天內的日期為有效日期')
year = int(input('年: '))
month = int(input('月: '))
day = int(input('日: '))

payload= {
	'_csrf': '1907d91c-036c-43de-be20-9e12f8b334c3',
	'trainTypeList': 'ALL',
	'transfer': 'ONE',
	'startStation': f'{start_station}',
	'endStation': f'{end_station}',
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
	'車種車次':trainNolist,
	'全票價格':pricelist,
	'出發時間':startTimelist,
	'抵達時間':endTimelist,
	'行駛時間':estlist
}

final_data = pd.DataFrame(data,index = False)
print(final_data)

final_data.to_csv(f'G:/vs code file/web scraper/暑期營隊python爬蟲/程式/台鐵{year}-{month}-{day} {start_station[5:]}到{end_station[5:]}.csv',index = False, encoding = 'utf-8-sig')

os.system("pause")