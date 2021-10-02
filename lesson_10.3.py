class Cell:
    # attribute
    def __init__(self, count_cell):
        self.count_cell = count_cell

    # method
    def __str__(self):
        return f'{self.count_cell}'

    # сложение
    def __add__(self, other):
        print("\nСложение \t= ", end='')
        return Cell(self.count_cell + other.count_cell)

    # вычитание
    def __sub__(self, other):
        print("Вычитание \t= ", end='')
        return Cell(self.count_cell - other.count_cell) if self.count_cell - other.count_cell > 0 \
                    else "Внимание! Из меньшей клетки вычитается большая!"

    # умножение
    def __mul__(self, other):
        print("Умножение \t= ", end='')
        return Cell(self.count_cell * other.count_cell)

    # деление
    def __floordiv__(self, other):
        print("Деление \t= ", end='')
        return Cell(self.count_cell // other.count_cell)

    # организация рядов
    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.count_cell // rows)]) + '\n' + '*' * (self.count_cell % rows)


cell_1 = Cell(15)
cell_2 = Cell(22)
count = 5
print(f' \tКлетка_1({cell_1}) + Клетка_2({cell_2}) = {cell_1 + cell_2}')
print(f' \tКлетка_1({cell_1}) - Клетка_2({cell_2}) = {cell_1 - cell_2}')
print(f' \tКлетка_1({cell_1}) * Клетка_2({cell_2}) = {cell_1 * cell_2}')
print(f' \tКлетка_1({cell_1}) / Клетка_2({cell_2}) = {cell_1 // cell_2}')

print(f'\nКоличество ячеек {cell_2.count_cell} в ряду должно быть по {count} яч.\n{cell_2.make_order(count)}')