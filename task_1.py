# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
import random

n = 5
money_front = 0
money_back = 0
money_list = []
for i in range(n):
    money_list(random.randint(1, 10))
print(money_list)

for i in range(n):
    if i == 0:
        money_front += 1
        print(money_front)
    else:
        i == 1
        money_back += 1
        print(money_back)
        if money_front > money_back:
            money_result = money_back
        else:
            money_back > money_front
            money_result = money_front
print(money_result)
