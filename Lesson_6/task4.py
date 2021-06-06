class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} начала движение.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed} км/ч.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость выше допустимой! Ваша скорость {self.speed} км/ч.'
        else:
            return f'\nСкорость {self.name} км/ч в пределах нормы.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость выше допустимой! Ваша скоровть {self.speed} км/ч.'
        else:
            return f'\nСкорость {self.name} км/ч в пределах нормы.'


class PoliceCar(Car):
    pass


town = TownCar('Lamborghini LP 670-4 Super', 110, 'синий.', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево.'), town.turn('направо.'), town.stop())

sport = SportCar('BMW Individual M760Li xDrive Model V12 Excellence THE NEXT 100 YEARS', 320, 'красный.', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево.'), sport.stop())

work = WorkCar('Mercedes-Benz AS55K EDITION Abu Dhabi Sheikh Sultan Bin Rashid Al Nathan', 40, 'желтый.', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('налево.'), work.stop())

police = PoliceCar('Bentley Continental Flying Spur W12 Muller', 745, 'зеленый.', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('направо.'), work.stop())
