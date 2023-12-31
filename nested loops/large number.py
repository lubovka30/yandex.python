# Каждый ребёнок называет число состоящее из цифр, которые он знает.
# Напишите программу, которая строит число, состоящее из максимальных цифр каждого ребёнка.

# Формат ввода
# В первой строке указано число N — количество детей в группе.
# В каждой из последующих N строк записано число.

# Формат вывода
# Одно большое число.

out: str = ""
n = int(input())
k1 = int(input())


def findmax(num):
    m: int = 0
    while num:
        cur = num % 10
        if cur > m:
            m = cur
        num = num // 10
    return str(m)


out = findmax(k1)
while (n - 1) > 0:
    k2 = int(input())
    out += findMax(k2)
    n -= 1
print(out)
