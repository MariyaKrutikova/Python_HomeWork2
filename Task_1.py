# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной 
# и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

N = int(input("Укажите колличество монет: "))

count = 0
TailCount = 0
HeadCount = 0
while count < N:
    CoinSide = randint(0,1)
    if CoinSide == 0:
        TailCount += 1
    elif CoinSide == 1:
        HeadCount += 1

if TailCount < HeadCount:
    print(f"Необходимо перевернуть {TailCount} монет")
else:
    print(f"Необходимо перевернуть {HeadCount} монет")