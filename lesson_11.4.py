class Storage:
    # attribute
    new_storage = []

    # method
    @staticmethod
    def show_storage():
        print('Весь товар на складе: ')
        for el in Storage.new_storage:
            print(el)

    @staticmethod
    def move_storage(name, count, name_dep):
        if Storage.valid(name, count, name_dep):
            for el in Storage.new_storage:
                for key, val in el.items():
                    if name == val:
                        if count <= el['кол-во']:
                            el['кол-во'] -= count
                            if el['кол-во'] == 0:
                                Storage.new_storage.remove(el)
                            return print(f'Позиция: {name}, кол-во: {count} перемещена в подзразделение: {name_dep}')
                        else:
                            return print('На складе нет такого количества')
            return print('Данного товара нет на складе')

    """Валидация"""
    @staticmethod
    def valid(name, count, name_stor):
        if not(isinstance(name, str)):
            print('Введены некорректные данные, наименование должно быть строчным')
            return False
        elif not(isinstance(count, int)):
            print('Введены некорректные данные, количество должно быть числом')
            return False
        elif not(isinstance(name_stor, str)):
            print('Введены некорректные данные, название подразделения должно быть строчным')
            return False
        return True


class Office:
    # attribute
    new_office = []
    # method
    # Наличие оргтехники
    @staticmethod
    def show_office_eq():
        if len(Office.new_office):
            print('Здесь пусто')
        else:
            for el in Office.new_office:
                print(el)

    # Перемещение на склад
    @staticmethod
    def move_srorage():
        Storage.new_storage.extend(Office.new_office)
        print('Оргтехника перемещена на склад')

    def __init__(self, name, model, price, count):
        self.name = name
        self.model = model
        self.price = price
        self.count = count


class Printer(Office):
    # attribute
    def __init__(self, name, model, price, count):
        super().__init__(name, model, price, count)
        Storage.new_storage.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.count,
        })


class Scanner(Office):
    # attribute
    def __init__(self, name, model, price, count):
        super().__init__(name, model, price, count)
        Storage.new_storage.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.count,
        })


class Xerox(Office):
    # attribute
    def __init__(self, name, model, price, count):
        super().__init__(name, model, price, count)
        Storage.new_storage.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.count
        })


p1 = Printer('HP', 'LJ2513', 7500, 6)
s1 = Scanner('HP MFU', 'MF28a', 12000, 4)
x1 = Xerox('Samsung', 'R210', 15000, 5)
Storage.show_storage()
Office.show_office_eq()
Office.move_srorage()

Storage.move_storage('HP MFU', 2, 'Отдел логистики')
Storage.show_storage()
Storage.move_storage('Samsung', 3, 'Бухгалтерия')
Storage.show_storage()
Storage.move_storage('HP', 5, 'Отдел сбыта')
Storage.show_storage()
Storage.move_storage('HP LJ125i', '5', 'Отдел сбыта')
Storage.move_storage(123, 5, 'Отдел сбыта')
Storage.move_storage('HP LJ125i', 5, 123)