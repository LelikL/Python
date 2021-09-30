class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Новый автомобиль: {self.name} цветом {self.color} полицейская машина - {self.is_police}')

    def go(self):
        print(f'{self.name}: машина поехала.')

    def stop(self):
        print(f'{self.name}: машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: машина повернула {"направо" if direction == 0 else "налево"}.')

    def show_speed(self):
        return f'{self.name}: скорость машины = {self.speed}.'


class TownCar(Car):


    def show_speed(self):
        return f'{self.name}: скорость машины = {self.speed}. Внимание! Превышение скорости!' \
        if self.speed > 60 else f'{self.name}: скорость машины = {self.speed}.'


class WorkCar(Car):


    def show_speed(self):
        return f'{self.name}: скорость машины = {self.speed}. Внимание! Превышение скорости!' \
        if self.speed > 40 else f'{self.name}: скорость машины = {self.speed}.'


class PoliceCar(Car):


    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('"Полицейская"', "белый", 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Грузовой"', "'очень грязная'", 50)
work_car.go()
print(work_car.show_speed())
work_car.turn(0)
work_car.turn(1)
work_car.stop()
print()
