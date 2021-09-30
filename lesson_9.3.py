class Worker:
    # attribute
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    # method
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


worker_1 = Position('Ivan', 'Ivanov', 'programmer', 60000, 5000)
print(worker_1.get_full_name())
print(worker_1.position)
print(worker_1.get_total_income())
