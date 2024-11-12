import random


def factory(x, y, z):
    car = x * y + 2 * z
    return car

car1 = factory(2,3,5)
print(car1)


def repair():
    global car1
    car1 = car1 + 2

repair()
print(car1)
