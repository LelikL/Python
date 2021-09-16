src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [n for n in src if src.count(n) == 1]

print(result)


def optimiz_count(list):
    my_dict = {i: 0 for i in list}

    for i in list:
        my_dict[i] += 1

    print('Код оптимизирован!')
    print([i for i in my_dict if my_dict[i] == 1])


optimiz_count(src)
