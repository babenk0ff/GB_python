class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f"${self._income['wage'] + self._income['bonus']}")


worker = Position('James', 'Bond', '007', 75000, 10500)

print(worker.name)
print(worker.surname)
print(worker.position)

worker.get_full_name()
worker.get_total_income()
