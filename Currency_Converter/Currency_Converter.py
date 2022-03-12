from unicodedata import decimal

from bs4 import BeautifulSoup
from decimal import Decimal
import requests
import xmltodict
import json
import pprint


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(f'https://cbr.ru/scripts/XML_daily.asp?date_req={date}')
    data = json.dumps(xmltodict.parse(response.text))
    data = json.loads(data)
    #print(data)
    #pprint.pprint(data['ValCurs']['Valute'])

    new_map = {}
    for map_ in data['ValCurs']['Valute']:
        new_map[map_['CharCode']] = map_
    #pprint.pprint(new_map)
    if cur_from == 'RUR':
        cur_from = {'CharCode': 'RUR', 'Nominal': '1', 'Name': 'Русских рублей', 'Value': '1,0000'}
    else:
        cur_from = new_map[cur_from]
    if cur_to == 'RUR':
        cur_to = {'CharCode': 'RUR', 'Nominal': '1', 'Name': 'Русских рублей', 'Value': '1,0000'}
    else:
        cur_to = new_map[cur_to]

    # rate_from = cur_from['Value'] / cur_from['Nominal']
    # rate_to = cur_to['Value'] / cur_to['Nominal']

    #print(Decimal((cur_to['Value'].replace(',','.'))))


    result = amount * ((Decimal(cur_to['Nominal'].replace(',', '.')) / Decimal(cur_from['Value'].replace(',', '.'))) / (
                Decimal(cur_from['Value'].replace(',', '.')) * Decimal(cur_to['Nominal'].replace(',', '.'))))
    return result


#convert(27,'AUD', 'AZN',"10.03.2022")


# Чем выше курс в то что переходишь тем меньше той нужно она в знаменателе,
# чем выше курс исходной валюты тем больше нужно другой курс исходной в числителе.
# А номинал в дроби обратный курсу того чего он номинал.
