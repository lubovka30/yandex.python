# Формат ввода
# В первой строке записано число N
# Во всех последующих N строках — по одному числу.

# Формат вывода
# Требуется вывести общее количество простых чисел среди введённых (кроме N).

count: int = 0
n = int(input())
while n > 0:
    k = int(input())
    i: int = 2
    flag = True
    if k == 1:
        flag = False
    for i in range(2, (k // 2) + 1):
        if k % i == 0 and k != i or k == 1:
            flag = False
            break
    if flag is True:
        count += 1
    n -= 1
print(count)
