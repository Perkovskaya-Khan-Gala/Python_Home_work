# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#    -> 5

from random import randint

while True:
    numberN=int(input("Введите размер массива N: "))
    if numberN>0:
        break
    else:
        print("Введено не число или число меньшее 1. Попробуйте еще раз.")

list=[]
for i in range(numberN):
    list.append(randint(1,numberN))

numberX=int(input(f"Введите число X: "))

min=1000
for iu in list:
        if abs(numberX-iu)<min:
            min=abs(numberX-iu)
            numberCloser=iu

print(numberN)
print(list)
print(numberX)      
print(f" -> {numberCloser}") 