import requests, xmltodict, json

raw_data = requests.get(f'http://apis.data.go.kr/1400119/service/rest/KfniService/btncInfo?serviceKey=KTzkIv%2F6NJ%2BAVkAwqvrQAJntQ1lNEF4YPkO44kO3fYYWVvGDOrDupZBs5d4DCFIIeSs%2BxTiOHJHhs0n3upxFAA%3D%3D&q1=ZDAN000301').content

xmlObject = xmltodict.parse(raw_data)

data = xmlObject['response']['body']['items']['item']

for data in data:
    print(data['systemkorname']+'의 영문명' + data['systemname'])