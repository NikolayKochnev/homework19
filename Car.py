class Car:
    price = 100000

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} - цена:{}'.format(
            self.__class__.__name__, self.price
        )
    def horse_powers(self):
        print('100 лошадинных сил')


class Nissan(Car):
    price = 650000

    def horse_powers(self):
        print('110 лошадинных сил')


class Kia(Car):
    price = 2000000

    def horse_powers(self):
        print('200 лошадинных сил')


car_1 = Nissan(name=None)
car_2 = Kia(name=None)
print(car_1)
car_1.horse_powers()
print(car_2)
car_2.horse_powers()