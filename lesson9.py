# class Car:
#     def __init__(self, color, brand, speed):
#         self.color = color
#         self.brand = brand
#         self.speed = speed
#
#
#
#     def __str__(self):
#         return f'Color - {self.color}\n' \
#                f'Brand- {self.brand}\n' \
#                f'Speed - {self.speed}'
#
#
# class FuelCar(Car):
#     def __init__(self, color, brand, speed):
#         super().__init__(color, brand, speed)
#
#     def benzin(self, name):
#         return f'я заправляюсь бензином {name}'
#
#     def __str__(self):
#         return super(FuelCar, self).__str__()
#
# car1 = FuelCar(color='black', brand='Golf4', speed=200)
# print(car1.benzin('Gazprom'))
# print(car1)
# print('-----')
#
# class ElectroCar(Car):
#     def __init__(self, color, brand, speed):
#         super().__init__(color, brand, speed)
#
#     def batteryy(self, volume):
#         return f'Battery-{volume}'
#
# car2 = ElectroCar(color='White', brand='Tesla', speed=300)
# print(car2.batteryy('100%'))
# print(car2)
# print('---------')
#
# class HybridCar(FuelCar, ElectroCar):
#     def __init__(self, color, brand, speed):
#         super().__init__(color, brand, speed)
#
#     def __str__(self):
#         return super(HybridCar, self).__str__()
#
# hybrid = HybridCar(color='Blue', brand='Prius', speed=250)
# print(hybrid.benzin('Red Petrolium'), hybrid.batteryy('98%'))
# print(hybrid)
#
#




# class Phone:
#     def __init__(self, name, cost, color, memory, cpu, camera, size):
#         self.name = name
#         self.cost = cost
#         self.color = color
#         self.memory = memory
#         self.cpu = cpu
#         self.camera = camera
#         self.size = size
#
#     def calling_people(self, number):
#         return f'This phone calling to this number{number}'
#
#
#
#     def __str__(self):
#         return f'Name-{self.name}\n' \
#                f'Cost-{self.cost}$\n' \
#                f'Color-{self.color}\n' \
#                f'Memory-{self.memory}\n' \
#                f'Camera-{self.camera}\n' \
#                f'Size-{self.size}'
#
# class Iphone(Phone):
#     def __init__(self, name, cost, color, memory, cpu, camera, size):
#         super().__init__(name, cost, color, memory, cpu, camera, size)
#
#     def location(self, place):
#         return f'My location-{place}'
#
#
#     def info(self):
#         if self.name == 'Iphone13':
#             return f'Best Camera at moment'
#         elif self.name == 'Iphone4':
#             return f'This phone Legend'
#         elif self.name == 'Iphone6':
#             return  f'Awful desingn'
#
#     def __str__(self):
#         return super(Iphone, self).__str__()
#
#
# iphone13 = Iphone(name='Iphone13', cost=1000,color= 'black' , memory=1024, cpu=2.0, camera=4, size=3.4)
# print(iphone13.calling_people('+996550777888'), iphone13.location('Bishkek'))
# print(iphone13)
#
# class Samsung(Phone):
#     def __init__(self, name, cost, color, memory, cpu, camera, size):
#         super().__init__(name, cost, color, memory, cpu, camera, size)
#
#
#     def __str__(self):
#         return super(Samsung, self).__str__()
#
# samsung = Samsung(name='Samsung A6', cost=300, color='Black White', memory=64, cpu=1.3, camera=1, size=2.4)
# print(samsung.calling_people('+9964477555'))
# print(samsung)