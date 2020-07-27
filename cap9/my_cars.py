from car import Car
from eletric_car import CarroEletrico, Bateria

regular_car = Car('honda', 'civic', 2017)

eletric_car = CarroEletrico('tesla', 'model s', 2016)

print("Carro comum:")
print(regular_car.get_fullname())

print("Carro Eletrico: ")
print(eletric_car.get_fullname())