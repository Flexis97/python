# print("ЗАДАНИЕ 1")
# a = 1, 2, 3, 4, 5, 6, 7
# print (a)
# b = list(a)
# print(b)
#
#
# print("ЗАДАНИЕ 2")
#
# a = int(input("Введите число: "))
# if a/2 == 0:
#    print("четное")
# else:
#     print("нечетное")
# #print("ЗАДАНИЕ 3")
# print("Ведены числа: " "1 2 3 4 5 6 7 8 9")
# строка = "1 2 3 4 5 6 7 8 9"
# строка1 =(строка.rsplit())
# print("Из них :" )
# print("Миниальное: " + min(строка1))
# print("Миаксимальноее: " + max(строка1))
#
#
# print("ЗАДАНИЕ 4")
#
# число = input("Введиье натуральное число: ")
# число1 = float(число)
# if число != float:
#     print("Это число является не натуральным")
#     print("Введиье натуральное число")
# elif num <= 0:
#     print("Это число является не натуральным")
#     print("Введиье натуральное число")
# else:
#     print("Это число является натуральным")
#
#     print("минимальное число и введеных"+ min(число))
#     print("максимальное число и введеных"+ max(число))
# #if число <= 0:
#     #print("Это число является не 111натуральным")
#     #print("Введиье натуральное число")
#
#
#     #print("здесь наибольшая цифра: " )
#     #exit(0)
# #else:if :
#     #print("Это число является натуральным")
#     #exit(0)
# #
#     #print("Это число является не натуральным")
#     #if num > 0:
#             #elif num < 0:
#             #print("Это число является не натуральным")
#            # print(num)
#
#                 #else:
#                 #print("Это число является натуральным")
#
# #print("ЗАДАНИЕ 5")
#
#
#
#
#
#
#
#
#
# print("ЗАДАНИЕ 6")
# слово = input("Введиье слово: ")
# a = len(слово)
# b = set(слово)
# c = len(b)
# if a == c:
#     print("слово не изограмма :","в нем" , a,"уникальных элементов"  )
# else:
#     print("слово изограмма :","в нем" , a, "элементов", ",", "из них" ,c, "уникальных элементов" )
#
# print("ЗАДАНИЕ 7")
#
# год = int(input("Введите год: "))
# small = "Не высокосный год"
# big = "Высокосный год"
# if год % 4 != 0:
#     print(small)
# elif год % 100 == 0:
#     if год % 400 == 0:
#         print(big)
#     else:
#         print(small)
# else:
#     print("Высокосный")
#
# print("ЗАДАНИЕ 8")
print("Введите длины катетов трекгольника: ")
a = float(input("Катет а: = "))
b = float(input("Катет в: = "))
c = float(input("Катет с: = "))

if   a + b < c:
    print("Не существующий треугольник")
elif a + c < b:
    print("Не существующий треугольник")
elif b + c < a:
    print("Не существующий треугольник")
else:
    print("Треугольник возможно построить")