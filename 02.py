def num_translate(word):
    dictionary = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
        'eleven': 'одиннадцать',
        'twelve': 'двенадцать',
        'thirteen': 'тринадцать',
        'fourteen': 'четырнардцать',
        'fifteen': 'пятнадцать',
        'sixteen': 'шестнадцать',
        'seventeen': 'семнадцать',
        'eighteen': 'восемнадцать',
        'nineteen': 'девятнадцать',
        'twenty': 'двадцать',
    }
    temp = word.lower()
    if temp in dictionary.keys():
        if 65 <= ord(word[0]) <= 90:
            return dictionary[temp].capitalize()
        return dictionary[temp]
    return None


while True:
    user_input = input('Введите числительное от 1 до 20 по-английски (exit - для выхода): ')

    if user_input.lower() == 'exit':
        break
    else:
        translate = num_translate(user_input)

        if translate is None:
            print('Неизвестное число\n')
        else:
            print(f'"{user_input}" переводится как "{translate}"\n')
