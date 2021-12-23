for number in list(range(1, 101)):
    last_digit = int(str(number)[-1])
    ending = 'ов'
    if not 11 <= number <= 19:
        if last_digit == 1:
            ending = ''
        elif 2 <= last_digit <= 4:
            ending = 'а'
    print(number, f'процент{ending}')
