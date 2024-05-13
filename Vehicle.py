class Vehicle:
    vehiclr_type = 'none'

class Car:
    price = 1000000

    def horse_powers(self):
        return 120


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.vehicle_type = 'Auto'
        self.price = 1500000

    def horse_powers(self):
        return 200


nissan_car = Nissan()
print(f'Vehicle type: {nissan_car.vehicle_type}')
print(f'Car price: {nissan_car.price}')
print(f'Horse powers of car: {nissan_car.horse_powers()}')