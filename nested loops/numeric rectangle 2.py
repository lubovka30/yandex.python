# Формат ввода
# В первой строке записано число N — высота числового прямоугольника.
# Во второй строке указано число M — ширина числового прямоугольника.

# Формат вывода
# Нужно вывести сформированный числовой прямоугольник требуемого размера.
# Чтобы прямоугольник был красивым, каждый его столбец должен обладать одинаковой шириной.

n = int(input())
m = int(input())
k: int = 1
n1: int = 1
p: int = n * m


def rank(num):
    count: int = 0
    while num > 0:
        num = num // 10
        count += 1
    return count


while n1 <= n:
    out: str = ""
    i: int = 1
    while i <= m:
        out += str(" " * (rank(p) - rank(k))) + str(k) + " "
        i += 1
        k += n
    n1 += 1
    k = n1
    print(out[:-1])