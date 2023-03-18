# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.  
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
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

while True:
    numberX=int(input(f"Введите число X, меньшее или равно N={numberN}: "))
    if numberX<=numberN:
        break
    else:
        print(f"Введено не число или число больше N={numberN}. Попробуйте еще раз.") 

count=0
for iu in list:
    if iu==numberX:
        count+=1

print(numberN)
print(list)
print(numberX)      
print(f" -> {count}") 