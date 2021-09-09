numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


# ------------------------ num_translate --------
def num_translate(num, dict_num):
    if num in dict_num:
        print(dict_num[num])
    else:
        print(None)
# ----------------------- END num_translate -----


number = input('Enter number: ')
num_translate(number, numbers)
