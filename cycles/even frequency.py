# программа, которая убирает все чётные цифры из числа.

# Формат ввода
# Одно натуральное число.

# Формат вывода
# Одно натуральное число — результат очистки.

n = input()
n1 = int(n)
n2: str = ""
while n1:
    if ((n1 % 10) % 2) != 0:
        n2 = str(n1 % 10) + n2
    n1 = n1 // 10
print(n2)
