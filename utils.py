import requests
import datetime as dt
from decimal import Decimal


def currency_rates(currency):
    if len(currency) == 3:
        url = 'http://www.cbr.ru/scripts/XML_daily.asp'
        response = requests.get(url)
        resp_text = response.text

        if currency.upper() in resp_text:
            currency_index = resp_text.find(currency.upper())
            value_start_index = resp_text.find('<Value>', currency_index)
            value_end_index = resp_text.find('</Value>', currency_index)
            currency_value = resp_text[value_start_index + 7:value_end_index].replace(',', '.')
            currency_value = Decimal(currency_value).quantize(Decimal('.01'))

            nominal_index_start = resp_text.find('<Nominal>', currency_index)
            nominal_index_stop = resp_text.find('</Nominal>', currency_index)
            nominal = int(resp_text[nominal_index_start + 9:nominal_index_stop])

            result = (Decimal(currency_value) / nominal).quantize(Decimal('.01'))
        else:
            return None

        date_index = resp_text.find('Date')
        date_str = resp_text[date_index + 6:date_index + 16]
        date = dt.datetime.strptime(date_str, '%d.%m.%Y').date()
    else:
        return None

    return result, date
