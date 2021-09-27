import re

emails = ['someone@geekbrains.ru', 'someone@geekbrainsru']


def email_parse(name_address):
    re_addres = re.compile(r'(?P<user>([^.]+))@(?P<domain>(.*)+\.\w+)')
    # valid
    if not re_addres.match(name_address):
        raise ValueError(f'не корректный адрес: {name_address}')
    print(re_addres.match(name_address).groupdict())


for email in emails:
    try:
        email_parse(email)
    except ValueError as error:
        print(error)
