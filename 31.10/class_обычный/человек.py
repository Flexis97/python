class Person:
    def __init__(self, name, surname, age, number):
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number
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
person1.stand_up()
person1.sit_down()
print(f"Имя: {person1.name}, Фамилия: {person1.surname}, Возраст {person1.age}, моб.телефон: {number} ")

# я незнаю почему номер выбивает ошибку
