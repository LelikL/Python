duration = int(input('Введите время в секундах: '))
sec = 0
min = 0
hour = 0
day = 0

if duration < 60:
    sec = duration

    print(f'duration =  {duration}')
    print(f'{duration} сек')

elif 60 <= duration < 3600:
    min = duration // 60
    sec = duration % 60

    print(f'duration =  {duration}')
    print(f'{min} мин {sec} сек')

elif 3600 <= duration < 86400:
    hour = duration // 3600
    min = (duration - (hour * 3600)) // 60
    sec = duration - (hour * 3600) - (min * 60)

    print(f'duration =  {duration}')
    print(f'{hour} час {min} мин {sec} сек')

else:
    day = duration // 86400
    hour = (duration - (day * 86400)) // 3600
    min = (duration - (day * 86400) - (hour * 3600)) // 60
    sec = duration - (day * 86400) - (hour * 3600) - (min * 60)

    print(f'duration =  {duration}')
    print(f'{day} дн, {hour} час, {min} мин, {sec} сек')
