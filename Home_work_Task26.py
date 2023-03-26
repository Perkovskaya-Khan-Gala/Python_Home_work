# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
 #    A = 2; B = 3 -> 8 

numberA=int(input("Введите число А: "))
numberB=int(input("Введите число B: "))
def degreeRequrcy(foundation, degree):
    if degree>0:
        return foundation*degreeRequrcy(foundation, degree-1)
    return 1

print(f"A={numberA}; B={numberB} -> {degreeRequrcy(numberA, numberB)}")