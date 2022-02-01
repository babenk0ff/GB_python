class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self, thickness, verb=0):
        mass_square = 25
        mass = round(self._length * self._width * mass_square * thickness / 1000)
        if verb == 0:
            print(f'{mass}т')
        else:
            print(f'{self._length}м * {self._width}м * {mass_square}кг * {thickness}см = {mass}т')


road_1 = Road(5000, 20)
road_1.mass_calc(5)

road_2 = Road(1000, 5)
road_2.mass_calc(4, verb=1)
