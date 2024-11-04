class Student:
    def __init__(self, name, surname, age, grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades

    def average_rating(self):
        if not self.grades:
            return 0
        return sum(self.grades) // len(self.grades)

    def grade(self):
        average = self.average_rating()
        if average > 8:
            return "Отличник"
        elif average >= 7:
            return "Хорошист"
        elif average > 5:
            return "Учащийся"
        else:
            return "Неуспевающий"

    def __str__(self):
        achievements = self.grade()
        return f"Ученик: {self.name} {self.surname}, Возраст: {self.age}, Средний балл: {self.average_rating()}, Достижения: {achievements}"

student1 = Student("Артур", "Мельничук", 27, [9, 8, 7, 10, 10])
print(student1)