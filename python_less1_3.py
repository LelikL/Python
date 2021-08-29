# склонение слова
for proc in range(1, 101):
    if 1 <= proc <= 10 or 20 <= proc <= 100:
        if proc == 1 or proc % 10 == 1:
            print(f'{proc} процент')
        elif 2 <= proc % 10 <= 4:
            print(f'{proc} процента')
        else:
            print(f'{proc} процентов')
    else:
        print(f'{proc} процентов')
