import random


class Car:
    def __init__(self, color, name, is_police=False):
        self.color = color
        self.name = name
        self.speed = 0
        self.is_police = is_police

    def go(self):
        self.speed = random.randint(10, 120)
        print(f'Автомобиль разогнался до {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Автомобиль остановился')

    def turn(self, direction):
        self.speed = self.speed / 2  # типа вдвое скорость сбросил перед поворотом
        print(f'Автомобиль сбавил скорость до {self.speed} км/ч и повернул на{direction.lower()}')

    def show_speed(self):
        if self.speed != 0:
            print(f'Автомобиль движеться со скоростью {self.speed} км/ч')
        else:
            print('Автомобиль стоит на месте')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость')
        elif self.speed != 0:
            print(f'Автомобиль движеться со скоростью {self.speed} км/ч')
        else:
            print('Автомобиль стоит на месте')


class SportCar(Car):
    def go(self):
        self.speed += random.randint(20, 240)
        print(f'Автомобиль разогнался до {self.speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость')
        else:
            print(f'Автомобиль движеться со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color, name, is_police=True):
        super().__init__(color, name, )
        self.speed = 0
        self.is_police = is_police


l = SportCar('Black', 'Lancer')
r = TownCar('Gray', 'Renault')
l.go()
l.go()
r.go()
r.go()
r.go()
r.go()
r.show_speed()
l.show_speed()
l.turn('ПраВо')
r.stop()
r.show_speed()
