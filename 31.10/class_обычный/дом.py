print("книга")
class book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


    def __str__(self):
        return (f"Книга: {self.title}, автор: {self.author}, страниц: {self.pages}, год: {self.year}")



Book = book("1984", "арт", 328, 1949)
print(Book)




print("Авто")
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
my_car.start_eng()
print(my_car.brand, my_car.model, my_car.year, my_car.color)


print("Холодильник")
class Refrigerator:
    def __init__(self, manufacturer, capacity, model_name):
        self.manufacturer = manufacturer  # Производитель
        self.capacity = capacity            # Емкость (в литрах)
        self.model_name = model_name        # Название модели
        self.door_open = False              # Состояние дверцы (открыта/закрыта)

    def open_door(self):
        if not self.door_open:
            self.door_open = True
            print(f"Дверца холодильника {self.model_name} открыта.")
        else:
            print(f"Дверца холодильника {self.model_name} уже открыта.")

    def close_door(self):
        if self.door_open:
            self.door_open = False
            print(f"Дверца холодильника {self.model_name} закрыта.")
        else:
            print(f"Дверца холодильника {self.model_name} уже закрыта.")

    def turn_on(self):
        print(f"Холодильник {self.model_name} включен.")


my_fridge = Refrigerator("Samsung", 300, "35AAAAa")
my_fridge.turn_on()
my_fridge.open_door()
my_fridge.close_door()



class Person:
    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number
        self.is_standing = False

    def stand_up(self):
        if not self.is_standing:
            self.is_standing = True
            print(f"{self.name} {self.surname} встал.")
        else:
            print(f"{self.name} {self.surname} уже стоит.")

    def sit_down(self):
        if self.is_standing:
            self.is_standing = False
            print(f"{self.name} {self.surname} сел.")
        else:
            print(f"{self.name} {self.surname} уже сидит.")


person1= Person("артур", "Мельничук", 27, "+375292265739")
person1.stand_up()  # Вывод: Иван Иванов встал.
person1.sit_down()  # Вывод: Иван Иванов сел.
print(person1.name)


class House:
    def __init__(self, floors, square, rooms):
        self.floors = floors
        self.square = square
        self.rooms = rooms

    def calculate_price(self, cost_per_meter):
        total_price = self.square * cost_per_meter
        return total_price


house1 = House(2, 120, 5)
cost_per_meter = 1200
total_price = house1.calculate_price(cost_per_meter)

print(f"Стоимость дома: {total_price} бел.рублей.")



class Student:
    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades

    def average_rating(self):
        if not self.grades:  # Проверка на наличие оценок
            return 0
        return sum(self.grades) / len(self.grades)

    def get_achievements(self):
        """Метод для получения информации о достижениях ученика."""
        average = self.average_rating()
        if average >= 8:
            return "Отличник"
        elif average >= 7:
            return "Хорошист"
        elif average >= 5:
            return "Учащийся"
        else:
            return "Неуспевающий"

    def __str__(self):
        achievements = self.get_achievements()
        return f"Ученик: {self.first_name} {self.last_name}, Возраст: {self.age}, Средний балл: {self.calculate_average():.2f}, Достижения: {achievements}"

student1 = Student("Артур", "Мельничук", 27, [9, 8, 7, 10, 10])
print(student1)

