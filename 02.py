str_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_str_list = []
for i in range(len(str_list)):
    is_digit = False
    digit_count = 0
    for char in str_list[i]:
        if char.isdigit():
            is_digit = True
            digit_count += 1

    if digit_count == 1:
        temp_list = list(str_list[i])
        temp_list.insert(-1, '0')
        str_list[i] = ''.join(temp_list)

    if is_digit:
        new_str_list.append('"')
        new_str_list.append(str_list[i])
        new_str_list.append('"')
    else:
        new_str_list.append(str_list[i])

print(new_str_list)
