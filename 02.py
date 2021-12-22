cubes = [number**3 for number in range(1, 1001, 2)]

# a
result = 0
for cube in cubes:
    digits = list(str(cube))
    sum_of_digits = 0
    for digit in digits:
        sum_of_digits += int(digit)
    if sum_of_digits % 7 == 0:
        result += cube

print(result)

# b
cubes_plus_17 = []
for cube in cubes:
    cubes_plus_17.append(cube + 17)

result = 0
for number in cubes_plus_17:
    digits = list(str(number))
    sum_of_digits = 0
    for digit in digits:
        sum_of_digits += int(digit)
    if sum_of_digits % 7 == 0:
        result += number

print(result)

# c
cubes = list(map(lambda x: x + 17, cubes))

result = 0
for cube in cubes:
    digits = list(str(cube))
    sum_of_digits = 0
    for digit in digits:
        sum_of_digits += int(digit)
    if sum_of_digits % 7 == 0:
        result += cube

print(result)
