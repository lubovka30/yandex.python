# Формат ввода
# Вводится одно натуральное число — требуемый размер таблицы.

# Формат вывода
# Таблица умножения заданного размера.

n = int(input())
n1: int = n
flag = True
k: int = 0
while flag:
    i: int = 1
    out: str = ""
    count: int = 1
    while i <= n1:
        out += str(i + count * k) + " "
        i += 1
        count += 1
    print(out)
    k += 1
    n -= 1
    if n == 0:
        flag = False
