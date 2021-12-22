cubes = [number**3 for number in range(1, 1001, 2)]

# a
result = 0
for cube in cubes:
    new_number = cube
    sum_of_digits = 0
    while new_number != 0:
        last = new_number % 10
        sum_of_digits += last
        new_number //= 10
    if sum_of_digits % 7 == 0:
        result += cube

print(result)

# b
cubes_plus_17 = []
for cube in cubes:
    cubes_plus_17.append(cube + 17)

result = 0
for cube in cubes_plus_17:
    new_number = cube
    sum_of_digits = 0
    while new_number != 0:
        last = new_number % 10
        sum_of_digits += last
        new_number //= 10
    if sum_of_digits % 7 == 0:
        result += cube

print(result)

# c
cubes = list(map(lambda x: x + 17, cubes))

result = 0
for cube in cubes:
    new_number = cube
    sum_of_digits = 0
    while new_number != 0:
        last = new_number % 10
        sum_of_digits += last
        new_number //= 10
    if sum_of_digits % 7 == 0:
        result += cube

print(result)
