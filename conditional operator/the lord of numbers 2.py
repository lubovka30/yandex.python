# Чтобы поделить трёхзначное число,
# нужно составить из него минимально и максимально возможные двухзначные числа.

# Формат ввода
# Одно трёхзначное число.

# Формат вывода
# Два защитных числа для каждого отряда, записанные через пробел.

num = int(input())
a: int = num // 100
b: int = num // 10 % 10
c: int = num % 10
num1: int = max(a, b, c)
num2: int = min(a, b, c)
num3: int = a + b + c - num1 - num2
if num2 != 0:
    one = int(str(num2) + str(num3))
else:
    one = int(str(num3) + str(num2))
two = int(str(num1) + str(num3))
print(one, two, sep=" ")
