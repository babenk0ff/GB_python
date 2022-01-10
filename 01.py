def odd_nums(num):
    for i in range(1, num + 1, 2):
        yield i


odd_to_10 = odd_nums(10)
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
