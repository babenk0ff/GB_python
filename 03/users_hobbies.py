from itertools import zip_longest
import pickle

with open('users.csv', 'r', encoding='utf-8') as f:
    users = [line.strip().replace(',', ' ') for line in f.readlines()]

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobbies = [list(line.strip().split(',')) for line in f.readlines()]

if len(users) < len(hobbies):
    exit(1)

users_hobbies_dict = dict(zip_longest(users, hobbies))
print(users_hobbies_dict)

with open('users_hobbies_dict.pickle', 'wb') as f:
    pickle.dump(users_hobbies_dict, f)

with open('users_hobbies_dict.pickle', 'rb') as f:
    dict_read = pickle.load(f)

print(dict_read)