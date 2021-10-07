class MyException(Exception):
    # attribute
    def __init__(self, txt):
        self.txt = txt


num = input("Enter number: ")

try:
    num = int(num)
    if num == 0:
        raise MyException("Деление на ноль!")
except (ValueError, MyException) as err:
    print(err)
else:
    print(1 / num)
