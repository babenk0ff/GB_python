def get_full_prices(price_list):
    result = []
    for price in price_list:
        r, kk = str(float(price)).split('.')
        result.append('{} руб {:02} коп'.format(r, kk))
    return result


prices = [
    19.79, 106.8, 30.29, 96, 75.93,
    152.11, 60.1, 179.1, 159.9, 77.6,
    155.71, 172, 102.53, 14.28, 100.79
]

print('ID исходного списка: ', id(prices))
print(*get_full_prices(prices), sep=', ')

prices.sort()
print('ID отсортированного списка: ', id(prices))
print(*get_full_prices(prices), sep=', ')

sorted_prices = sorted(prices, reverse=True)
print('ID нового отсортированного списка: ', id(sorted_prices))
print(*get_full_prices(sorted_prices), sep=', ')

print(*get_full_prices(sorted_prices[0:5]), sep=', ')

print(*get_full_prices(sorted_prices[4::-1]), sep=', ')

