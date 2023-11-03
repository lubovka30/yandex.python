# Формат ввода
# В единственной строке записывается последовательность натуральных чисел, разделённых пробелами.

# Формат вывода
# требуется вывести одно натуральное число — НОД всех данных чисел.
def nod(n, m):
    if n == 0 or m == 0:
        return n + m
    if n > m:
        return nod(n - m, m)
    else:
        return nod(n, m - n)


result: int = 0
sequence = input()
sequence = sequence.lstrip(" ").rstrip(" ")
tmp = sequence.split(" ")
for i in range(len(tmp)):
    if i < len(tmp) - 1:
        result = nod(int(tmp[i]), int(tmp[i + 1]))
        tmp[i + 1] = result
print(result)
