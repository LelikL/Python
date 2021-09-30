class Stationery():
    def __init__(self, title='Я не умею рисовать'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск перерисовки карандашом {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки шариковой ручкой {self.title}.')


class Marker(Stationery):
    def draw(self):
        print(f'Запуск дорисовки маркером {self.title}.')


stat = Stationery()
stat.draw()
pen = Pen("'Простой'")
pen.draw()
pencil = Pencil("Herz")
pencil.draw()
marker = Marker("ТолстячОК")
marker.draw()