def thesaurus(*names, sort=False):
    name_letters = set(name[0] for name in names)
    result_dict = {}
    for letter in name_letters:
        result_dict[letter] = [name for name in names if name[0] == letter]

    if sort:
        return dict(sorted(result_dict.items()))
    return result_dict


names_dict = thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Ариэль', sort=True)
print(names_dict)
