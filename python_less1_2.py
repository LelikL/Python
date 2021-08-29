list_kub = []
list_kub17 = []
all_sum = 0
all_sum17 = 0

# список из кубов нечетных чисел от 1 до 1000
for i in range(1, 1000):
    if i % 2 != 0:
        i = i ** 3
        list_kub.append(i)
for el in list_kub:
    el += 17
    list_kub17.append(el)

print(list_kub)
print(list_kub17)

# сумма чисел,сумма цифр которых // 7 (all_sum = 17485588610)
for number in list_kub:
    n_sum = 0
    num = number

    while num > 0:
        j = num % 10
        n_sum += j
        num = num // 10

    if n_sum % 7 == 0:
        all_sum += number

print(all_sum)

for number in list_kub17:
    n_sum = 0
    num = number

    while num > 0:
        k = num % 10
        n_sum += k
        num = num // 10

    if n_sum % 7 == 0:
        all_sum17 += number

# all_sum17 = 15392909930
print(all_sum17)

