import random


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        if self.speed == 0:
            self.speed = 5
            print('Машина поехала')
        else:
            print('Машина уже едет')

    def stop(self):
        if self.speed == 0:
            print('Машина уже стоит')
        else:
            self.speed = 0
            print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        max_speed = 60
        msg = f'Текущая скорость {self.speed}'
        print(msg if self.speed <= max_speed
              else msg + f'. Превышение максимально допустимой ({max_speed})')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        max_speed = 40
        msg = f'Текущая скорость {self.speed}'
        print(msg if self.speed <= max_speed
              else msg + f'. Превышение максимально допустимой ({max_speed})')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


def test_car(car_obj):
    print('class name:', car_obj.__class__.__name__)
    print('атрибут name:', car_obj.name)
    print('атрибут color', car_obj.color)
    car_obj.go()
    print('атрибут speed:', car_obj.speed)

    car_obj.show_speed()
    car_obj.speed = 41
    car_obj.show_speed()
    car_obj.speed = 65
    car_obj.show_speed()

    print('атрибут is_police:', car_obj.is_police)
    direction = random.choice(['налево', 'направо'])
    car_obj.turn(direction)
    car_obj.stop()


town_car = TownCar(0, 'yellow', 'Taxi')
test_car(town_car)
print()

work_car = WorkCar(10, 'blue', 'Truck')
test_car(work_car)
print()

police_car = PoliceCar(20, 'black', 'Interceptor')
test_car(police_car)
print()

sport_car = SportCar(100, 'red', 'Porsche')
test_car(sport_car)
