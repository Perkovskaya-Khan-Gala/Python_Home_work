# Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N, состоящий из нулей, а по главной диагонали - единицы. 
# (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла). Результат вывести в виде таблицы чисел как показано в примере ниже.

# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

number=int(input("Введите натуральное число N: "))
""""
mas=[]
for i in range(number):
    mas.append([1]*number)
print(mas)
mas = [[0] * number for j in range(number)]
"""
mas=[]
for j in range(number):
    mas.append([1 if x==j else 0 for x in range(number)])

for i in range(0, len(mas)):
    for i2 in range(0, len(mas[i])):
        print(mas[i][i2], end=' ')
    print()
