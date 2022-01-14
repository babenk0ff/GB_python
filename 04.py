def get_pair(lst):
    iterator = iter(lst)
    prev = next(iterator)
    for item in lst:
        yield prev, item
        prev = item


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [b for a, b in get_pair(src) if b > a]
print(result)
