import requests, xmltodict, json

raw_data = requests.get(f'http://apis.data.go.kr/1400119/service/rest/KfniService/btncInfo?

xmlObject = xmltodict.parse(raw_data)

data = xmlObject['response']['body']['items']['item']

for data in data:
    print(data['systemkorname']+'의 영문명' + data['systemname'])
