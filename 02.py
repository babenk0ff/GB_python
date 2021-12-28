str_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
signs = ('-', '+')

for word in str_list:
    new_word = ''
    if word[-1].isdigit():
        if len(word) == 1:
            new_word = '0' + word
        elif len(word) == 2:
            if word[0] in signs:
                new_word = word[0] + '0' + word[1]
            else:
                new_word = word

        new_list.append('"')
        new_list.append(new_word)
        new_list.append('"')
    else:
        new_list.append(word)

print(new_list)

final_string = ''
switch = False
i = 0
while i < len(new_list):
    if new_list[i] == '"':
        if switch:
            final_string += f'{new_list[i]}'
            switch = False
        else:
            final_string += f' {new_list[i]}'
            switch = True
    else:
        if i == 0:
            final_string += f'{new_list[i]}'
        elif i == len(new_list) - 1:
            final_string += f' {new_list[i]}'
        else:
            if switch:
                final_string += f'{new_list[i]}'
            else:
                final_string += f' {new_list[i]}'
    i += 1

print(final_string)
