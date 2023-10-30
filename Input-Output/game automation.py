# Напишите программу для робота-няни, которая из числа вида abcd составляет число badc.
#
# Формат ввода
# Одно четырёхзначное число.
#
# Формат вывода
# Одно четырёхзначное число — результат перестановки.

number = int(input())
number_1 = str(number // 1000)
number_2 = str(number // 100 % 10)
number_3 = str(number // 10 % 10)
number_4 = str(number % 10)
number_2143 = number_2 + number_1 + number_4 + number_3
print(int(number_2143))
