from car import CarroEletrico

my_tesla = CarroEletrico('tesla', 'model s', 2015)
my_tesla.bateria.describe()
my_tesla.bateria.upgrade()
print(my_tesla.get_fullname())