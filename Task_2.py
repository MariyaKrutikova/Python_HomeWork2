# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# from random import randint

S = int(input("Сумма чисел равна: "))
P = int(input("Произведение чисел равно: "))

a = True
for x in range(0,1000):
    for y in range(0,1000):
        if x + y == S and x*y == P:
            print(f"Петя загадал {x} и {y}")
            a = False
        
if a:
    print("Таких x и y нет")
