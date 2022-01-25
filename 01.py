import re


def email_parse(email):
    pattern = re.compile(r'([a-z0-9._-]+)@([a-z0-9-]+[^-]\.[a-zA-Z]{2,}$)')
    if not pattern.match(email):
        raise ValueError(f'wrong email: {email}')
    return dict(zip(('username', 'domain'), *map(list, pattern.findall(email))))


print(email_parse('some.one@geekbrains.ru'))
print(email_parse('someone@gmailcom'))
