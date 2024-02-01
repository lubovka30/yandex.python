# Напишите программу, которая производит счёт по заданным параметрам.

# Формат ввода
# В одну строку через пробел вводятся 3 рациональных числа — начало счета, конец и шаг.

# Формат вывода
# Последовательность чисел с заданными параметрами.
from itertools import count

numbers = input().split()
for value in count(float(numbers[0]), float(numbers[2])):
    if value <= float(numbers[1]):
        print(round(value, 2))
    else:
        break
