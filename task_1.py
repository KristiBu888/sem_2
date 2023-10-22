# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# from random import randint
# n = 5
# list_coins = []
# for i in range(n):
#     list_coins.append(randint(0, 1))
# print(list_coins)
# zero = list_coins.count(0)
# if len(list_coins) - zero < zero:
#     print(len(list_coins) - zero)
# else:
#     print(f'Нужно перевернуть {zero} монеток')

# Решение 2
n = int(input('Введите число монеток: '))
coins = []
count_zero = 0
count_one = 0

for coin in coins:
    if coin == 0:
        count_zero += 1
    else:
        count_one += 1

if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)
