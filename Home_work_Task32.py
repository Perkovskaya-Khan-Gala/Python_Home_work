# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
from random import randint
list=[randint(-5,20) for i in range(25)]
print(list)
numberMin=int(input("Введите минимум: "))
numberMax=int(input("Введите максимум: "))
list2=[i for i in range(len(list)) if numberMin<=list[i]<=numberMax]
print(list2)

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
# if min_number <= list_1[i] <= max_number:
# print(i)