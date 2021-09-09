def thesaurus(*args):
    my_dict = {}
    for i in sorted(args):
        key = i[0]
        if key in my_dict:
            my_dict[key] += [i]
        else:
            my_dict[key] = [i]
    return my_dict

print(thesaurus("Иван", "Мария", "Анна", "Алена", "Илья"))
