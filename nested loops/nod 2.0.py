# Формат ввода
# В первой строке записано одно число N — количество данных.
# В каждой из последующих N строк записано по одному натуральному числу.

# Формат вывода
# требуется вывести одно натуральное число — НОД всех данных чисел (кроме N).

n = int(input())
nod: int = 0
if n == 1:
    print(input())
    exit()
k1 = int(input())
while (n - 1) > 0:
    k2 = int(input())
    if k1 >= k2:
        while k1 != k2:
            k1 = k1 - k2
            nod = k1
            if k1 < k2:
                count = k1
                k1 = k2
                k2 = count
    else:
        while k2 != k1:
            k2 = k2 - k1
            nod = k2
            if k2 < k1:
                count = k2
                k2 = k1
                k1 = count
    k1 = nod
    n -= 1
print(nod)
