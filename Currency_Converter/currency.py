from decimal import Decimal
from bs4 import BeautifulSoup
import requests



def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(f'https://cbr.ru/scripts/XML_daily.asp?date_req={date}')

    soup = BeautifulSoup(response.text, "html.parser")
    valute_all = soup.find_all('valute')

    data = {}
    for item in valute_all:
        mapa_in = {}
        for i in item.children:
            mapa_in.update({i.name:i.string})
        data[item.find('charcode').string] = mapa_in
    if cur_from == 'RUR':
        cur_from = {'charCode': 'RUR', 'nominal': '1', 'name': 'Русских рублей', 'value': '1,0000'}
    else:
        cur_from = data[cur_from]
    if cur_to == 'RUR':
        cur_to = {'charCode': 'RUR', 'nominal': '1', 'name': 'Русских рублей', 'value': '1,0000'}
    else:
        cur_to = data[cur_to]

    #result = amount * ((Decimal(cur_to['nominal'].replace(',', '.')) / Decimal(cur_from['value'].replace(',', '.'))) / (
    #            Decimal(cur_from['value'].replace(',', '.')) * Decimal(cur_to['nominal'].replace(',', '.'))))
    result = amount * ( (Decimal(cur_from['value'].replace(',', '.')) * Decimal(cur_to['nominal'].replace(',', '.'))) /
                Decimal(cur_to['value'].replace(',', '.')) / Decimal(cur_from['nominal'].replace(',', '.')))

    return result.quantize(Decimal("1.0000"))


