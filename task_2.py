# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


# 1
import random
import os

os.system("cls")

N = int(input("Введите число арбузов "))
max = 0
min = 999

for i in range(N):
    mass = random.randint(1, 10)
    print(mass, end=' ')
    if mass <= min:
        min = mass
    if mass >= max:
        max = mass
print()
print("Самый тяжелый арбуз весит: ", max)
print("Самый легкий арбуз весит: ", min)


# 2
N = int(input("количество арбузов "))
i, array = 1, []
while i <= N:
    array.append(int(input("Введите вес арбузов ")))
i += 1


# 3
array = [5, 1, 6, 5, 9]
print("Теще мы дали арбуз ", {min(array)},
      "кг, а себе взяли абрбуз", {max(array)}, "кг")


# 4
print("Enter N")
array = [random.randint(1, 20) for i in range(int(input()))]

light = array[0]
heavy = array[0]

print(array)
for watermelon in array[1:]:
    if watermelon > heavy:
        heavy = watermelon
    elif watermelon < light:
        light = watermelon

print(f'{light} {heavy}')
