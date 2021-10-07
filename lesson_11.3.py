class MyException(Exception):
    # attribute
    def __init__(self, txt):
        self.txt = txt


dic = []
while True:
    num = input("Введите данные / Для выхода наберите 'Stop': ")

    num = str(num)
    if num == 'Stop':
        break
    else:
        try:
            num = int(num)
            dic.append(num)
        except (ValueError, MyException) as err:
            print(err)

print(dic)
