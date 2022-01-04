import requests
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

            nominal_index_start = resp_text.find('<Nominal>', currency_index)
            nominal_index_stop = resp_text.find('</Nominal>', currency_index)
            nominal = int(resp_text[nominal_index_start + 9:nominal_index_stop])

            result = (Decimal(currency_value) / nominal).quantize(Decimal('.01'))
        else:
            return None
    else:
        return None

    return result


print(currency_rates('usd'))
print(currency_rates('EUR'))
print(currency_rates('CZK'))
