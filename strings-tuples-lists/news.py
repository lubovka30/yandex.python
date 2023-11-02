# Напишите программу, которая сокращает длинные заголовки до требуемой длины
# и завершает их многоточием ... при необходимости.

# Формат ввода
# вводится натуральное число L — необходимая длина заголовка.
# Вводится натуральное число N — количество заголовков, которые требуется сократить.
# В каждой из последующих N строк записано по одному заголовку.

# Формат вывода
# Сокращённые заголовки.

# Примечание
# Многоточие учитывается при подсчёте длины заголовка.

length = int(input())
n = int(input())
for i in range(n):
    text = input()
    if len(text) <= length:
        print(text)
    else:
        k = length - 3
        print(f"{text[:k]}...")