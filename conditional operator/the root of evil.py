# Формат ввода
# Вводится 3 вещественных числа a, b, c — коэффициенты уравнения вида:
# ax^2+bx+c=0.

# Формат вывода
# Если у уравнения нет решений — следует вывести «No solution».
# Если корней конечное число — их нужно вывести через пробел в порядке возрастания с точностью до сотых.
# Если корней неограниченное число — следует вывести «Infinite solutions».

a = float(input())
b = float(input())
c = float(input())
if a == b == c == 0:
    print("Infinite solutions")
    exit()
elif a == 0 and b != 0 and c != 0:
    x: float = -c / b
    print("{0:.2f}".format(x))
    exit()
elif b == 0 and ((a > 0 and c > 0) or (a < 0 and c < 0)):
    x: float = (abs(c) / abs(a)) ** 0.5
    print("{0:.2f}".format(x))
    exit()
elif a == b == 0:
    print("No solution")
    exit()
D: float = b ** 2 - 4 * a * c
if D == 0:
    x: float = -b / (2 * a)
    print("{0:.2f}".format(x))
elif D < 0:
    print("No solution")
elif D > 0:
    x1: float = (-b + D ** 0.5) / (2 * a)
    x2: float = (-b - D ** 0.5) / (2 * a)
    if x1 > x2:
        print("{0:.2f}".format(x2), "{0:.2f}".format(x1))
    else:
        print("{0:.2f}".format(x1), "{0:.2f}".format(x2))
