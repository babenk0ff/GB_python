import requests


def currency_rates(val):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)

