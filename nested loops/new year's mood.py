# Формат ввода
# Вводится одно натуральное число — количество чисел в математической ёлке.

# Формат вывода
# Требуемая новогодняя ёлка.

n = int(input())
k: int = 1
count: int = 1
while k <= n:
    i: int = 1
    out: str = ""
    while (i <= count) and (k <= n):
        out += str(k) + " "
        i += 1
        k += 1
    count += 1
    print(out[:-1])
