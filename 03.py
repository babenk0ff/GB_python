def thesaurus(*names):
    name_letters = set(name[0].lower() for name in names)
    result_dict = {}
    for letter in name_letters:
        result_dict[letter.upper()] = [name for name in names if name[0].lower() == letter]
    return result_dict


names_dict = thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Ариэль')
print(names_dict)

for key in sorted(names_dict.keys()):
    print(key, names_dict[key])
