import requests
import datetime as dt
from decimal import Decimal


def currency_rates(currency):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    resp_text = response.text

    if currency.upper() in resp_text:
        currency_index = resp_text.find(currency.upper())
        value_start_index = resp_text.find('<Value>', currency_index)
        value_end_index = resp_text.find('</Value>', currency_index)
        currency_value = resp_text[value_start_index + 7:value_end_index].replace(',', '.')
        currency_value = Decimal(currency_value).quantize(Decimal('.01'))
    else:
        return None

    date_index = resp_text.find('Date')
    date_str = resp_text[date_index + 6:date_index + 16]
    date = dt.datetime.strptime(date_str, '%d.%m.%Y').date()

    return currency_value, date
