from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        
        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            
            with open('dict_user_hobby.json', 'w', encoding='utf-8') as f:
                list = zip_longest((' '.join(user.split(',')) for user in users), hobby)
                my_dict = {str(num[0]).strip(): str(num[1]).strip() for num in list}
                dump(my_dict, f, ensure_ascii=False, indent=4)

            print(my_dict)
        else:
            exit(1)