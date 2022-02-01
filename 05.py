class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')


pen = Pen('Pen')
pen.draw()

pencil = Pencil('Pencil')
pencil.draw()

handle = Handle('Handle')
handle.draw()
