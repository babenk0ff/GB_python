def get_unique_list(lst):
    unique = set()
    tmp = set()
    for element in lst:
        if element not in tmp:
            unique.add(element)
        else:
            unique.discard(element)
        tmp.add(element)

    return [element for element in lst if element in unique]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(get_unique_list(src))
