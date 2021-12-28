str_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

signs = ('-', '+')
i = 0
while i < len(str_list):
    word = str_list[i]
    if word[-1].isdigit():
        if len(word) == 1:
            str_list[i] = '0' + word
        elif len(word) == 2 and word[0] in signs:
            str_list[i] = word[0] + '0' + word[1]

        str_list.insert(i, '"')
        str_list.insert(i + 2, '"')
        i += 2
    else:
        i += 1

print(str_list)

final_string = ''
switch = False
i = 0
while i < len(str_list):
    if str_list[i] == '"':
        if switch:
            final_string += f'{str_list[i]}'
            switch = False
        else:
            final_string += f' {str_list[i]}'
            switch = True
    else:
        if i == 0:
            final_string += f'{str_list[i]}'
        elif i == len(str_list) - 1:
            final_string += f' {str_list[i]}'
        else:
            if switch:
                final_string += f'{str_list[i]}'
            else:
                final_string += f' {str_list[i]}'
    i += 1

print(final_string)
