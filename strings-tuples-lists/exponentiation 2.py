# Создадим новую программу, которая возводит в заданную степень все числа, переданные пользователем.

# Формат ввода
# В первой строке записана последовательность натуральных чисел, разделённых пробелами.
# Во второй строке записано натуральное число P — степень, в которую требуется возвести числа.

# Формат вывода
# Последовательность чисел, являющихся ответом.
# Числа вывести в одну строку через пробел.

sequence = input()
p = int(input())
tmp = sequence.split(" ")
result: str = ""
for i in range(len(tmp)):
    result += str(int(tmp[i]) ** p) + " "
print(result[:-1])