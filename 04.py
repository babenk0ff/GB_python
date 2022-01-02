def thesaurus_adv(*names):
    surname_letters = set(man.split()[1][0] for man in names)
    result_dict = {}
    for s_letter in surname_letters:
        temp_dict = {}
        name_letters = set(man.split()[0][0] for man in names if man.split()[1][0] == s_letter)
        for n_letter in name_letters:
            temp_dict[n_letter] = [man for man in names
                                   if man.split()[0][0] == n_letter and man.split()[1][0] == s_letter]
        result_dict[s_letter] = temp_dict
    return result_dict


names_dict = thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')
print(names_dict)
