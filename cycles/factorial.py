# Формат ввода
# Вводится одно неотрицательное число.

# Формат вывода
# Требуется вывести одно натуральное число — факториал заданного числа.

k = int(input())
fact: int = 1
while k > 0:
    fact = fact * k
    k -= 1
print(fact)