"""Я не могу понять как вывести данные по авто"""
class Auto:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def start_eng(self):
        print(f"{self.brand} {self.model} завел двигатель.")


my_car = Auto("Toyota", "Camry", 2021, "черный")
print(my_car.brand, my_car.model, my_car.year, my_car.color)
my_car.start_eng()



