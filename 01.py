import time


class TrafficLight:
    __color = ('красный', 'желтый', 'зеленый')

    def running(self, *colors, count=1):
        if self.__color != colors:
            print('Неверный порядок режимов')
            exit(1)
        for _ in range(count):
            print(self.__color[0].capitalize())
            time.sleep(7)
            print(self.__color[1].capitalize())
            time.sleep(2)
            print(self.__color[2].capitalize())
            if count > 1:
                time.sleep(5)


light = TrafficLight()
light.running('красный', 'желтый', 'зеленый', count=2)

light_2 = TrafficLight()
light_2.running('желтый', 'красный', 'зеленый', count=1)
