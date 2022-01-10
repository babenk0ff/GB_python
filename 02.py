def odd_nums(num):
    gen = (i for i in range(1, num + 1, 2))
    return gen


odd_to_10 = odd_nums(10)
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
