# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Укажите число: "))

i = 0
while 2**i < N:
    print(2**i)
    i+=1
