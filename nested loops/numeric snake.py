# Формат ввода
# В первой строке записано число N — высота числового прямоугольника.
# Во второй строке указано число M — ширина числового прямоугольника.

# Формат вывода
# Нужно вывести сформированную числовую змейку требуемого размера.
# Чтобы прямоугольник был красивым, каждый его столбец следует сделать одинаковой ширины.

n = int(input())
m = int(input())

out: list = []
p: int = n * m
if p == 0:
    print("0")
    exit()


def getRank(num):
    rank: int = 0
    while num:
        num = num // 10
        rank += 1
    return rank


def chekSpace(a, b):
    s: int = 0
    if getRank(out[a][b]) != getRank(p):
        s = getRank(p) - getRank(out[a][b])
    space: str = " " * s + " "
    return space


tmp: int = 1
for i in range(n):
    out1: list = []
    k: int = 1
    while k <= m:
        out1.append(tmp)
        tmp += 1
        k += 1
    out.append(out1)

for i in range(n):
    snake: str = ""
    if float(i % 2) != 0:
        j: int = m - 1
        while j >= 0:
            snake += chekSpace(i, j) + str(out[i][j])
            j -= 1
    else:
        j: int = 0
        while j < m:
            snake += chekSpace(i, j) + str(out[i][j])
            j += 1
    print(snake[1:])
