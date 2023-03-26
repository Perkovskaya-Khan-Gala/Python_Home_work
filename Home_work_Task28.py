# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# # 2 2
#    4 


def NumberInput(message):
    while True:
        result=int(input(message))
        if result>=0:
            return result
        else:
            print("Введено отрицательное число. Попробуйте еще раз.")

def SummRequrcy(first, second):
    if second>0:
        return 1 + SummRequrcy(first, second-1)
    return first

numberA=NumberInput("Введите число а>0: ")
numberB=NumberInput("Введите число b>0: ")
print(numberA,numberB)
print(SummRequrcy(numberA, numberB))