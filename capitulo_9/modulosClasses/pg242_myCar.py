# import da classe pg242_car.py
'''
from pg242_car import Car, EletricCar


# instanciando a classe Car()
my_new_car = Car('toyota', 'corola', '2019')
print(my_new_car.get_describe())

# chamando os metodos
my_new_car.odometer_reading = 30
my_new_car.read_odometer()



# instanciando a classe EletricCar()
my_car_tesla = EletricCar('tesla', 'roadster', '2020')

# chamando os metodos
my_car_tesla.battery_size.describe_battery()
'''




# para importar  o modulo todo 
# import nome_do_arquvo

import pg242_car as car

# instanciando a classe 
new_car = car.Car('toyota', 'corola', 2020)
print(new_car.get_describe())