import re


def email_parse(email_address):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    email = pattern.match(email_address)
    if not email_address:
        raise ValueError('email указан не верно')
    return email.groupdict()                   # подсмотрел в разборе ДЗ


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
