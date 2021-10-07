class MyComplex:
    # attribute
    def __init__(self, num, j):
        self.num = num
        self.j = j

    # method12
    def __add__(self, obj):
        print("Sum is: ")
        return MyComplex(self.num + obj.num, self.j + obj.j)

    def show(self):
        print(f"{self.num} + {self.j}i")

    def __mul__(self, obj):
        print("Mul is: ")
        return MyComplex(self.num * obj.num - (self.j * obj.j), self.num * obj.j + obj.num * self.j)


num1 = MyComplex(int(input("Введите вещественную часть первого числа: ")),
                 int(input("Введите мнимую часть первого числа: ")))
num2 = MyComplex(int(input("Введите вещественную часть второго числа: ")),
                 int(input("Введите мнимую часть второго числа: ")))
result = num1 + num2
result.show()
result1 = num1 * num2
result1.show()
