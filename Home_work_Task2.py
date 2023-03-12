# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
 
while True:
    number=int(input("Введите трехзначное положительное число:"))
    if number>99 and number<1000:
        break
    else: 
        print("Вы ввели не число или не трехзачное число. Попробуйте еще раз.")

num=number
sum=0
r=range(3)
for i in r:
    sum+=num%10
    num//=10
print(f"{number} -> {sum}")
