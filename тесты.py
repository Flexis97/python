a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("1 задание")
print(list(filter(lambda x: x % 2 == 0, a)))                   # 1) четные числа


print("2 задание")
print(list(map(lambda x: x ** 2, a)))                          # 2)возыедение в квадрат



from functools import reduce
print("3 задание")
print((reduce(lambda x, y: x + y, a, 0)))                      # 3) Сумма списка

arrey = ["a", "aaa", "aaaaaaa", "aaaaa", "aa"]
print("4 задание")
print(sorted(arrey, key=lambda s: len(s)))                     # 4) сортировка по длине


b = [1, 1, 2, 2, 3, 3, 5, 5, 10, 10]
print("5 задание")
print(list(set(b)))                                            # 5) set элементы



strings = ["hello", "world", "python", "is", "awesome"]
print("6 задание")
print(list(map(lambda x: x.upper(), strings)))                 # 6) Верхний регистр





arrey_1 = ["apple", "banana", "apricot", "cherry", "avocado"]
print("7 задание")
filter_list = list(filter(lambda x: x.startswith("b"), arrey_1)) # 7)  выбор по определеной букве
print(filter_list)

#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("8 задание")
print(sum(map(lambda x: x**2, a)))                               # 8) сумма квадратов из переменой ,а, в самом начале


Сотрудники = [
    {'Имя': 'Артур', 'Возраст': 27},
    {'Имя': 'Алексей', 'Возраст': 30},
    {'Имя': 'Генадий', 'Возраст': 50}
    ]
key_1 = "Имя"
key_2 = "Возраст"
print("9 задание")
print(list(map(lambda d: d[key_1], Сотрудники)))                  # 9 Из списка словарей выбор по ключу



data = [('Имя', 'Артур'), ('Возраст', 27), ('Гоод', 'Пинск')]
print("10 задание")
print(dict(map(lambda item: item, data)))                       # 10 Список картежей в словарь