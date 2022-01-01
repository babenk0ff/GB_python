def thesaurus_adv(*names):
    people = [name.split() for name in names]
    # people = {name.lower(): surname.lower() for name, surname in (name.split() for name in names)}
    # print(people)
    # name_letters = set(name[0][0] for name in people)
    surname_letters = set(name[1][0] for name in people)
    print(surname_letters)
    result_dict = {}
    for s_letter in surname_letters:
        surnames_list = [man for man in names if man.split()[1][0] == s_letter]
        name_letters = set(man.split()[0][0] for man in surnames_list)
        print(name_letters)
        temp_dict = {}
        for n_letter in name_letters:
            temp_dict[n_letter] = [man for man in surnames_list if man.split()[0][0] == n_letter]
            print(temp_dict)

        # result_dict[s_letter] = [' '.join(man) for man in people if man[0][0].lower() == n_letter]
        # result_dict[n_letter.upper()] = [name for name in names if name[0].lower() == n_letter]
    return result_dict


names_dict = thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')
print(names_dict)

# for key in sorted(names_dict.keys()):
#     print(key, names_dict[key])
