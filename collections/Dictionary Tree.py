# Напишите программу, которая преобразует строку слов в ёлку как показано в примере.

# Формат ввода
# В одну строку через пробел вводятся слова разделенные пробелом.

# Формат вывода
# Несколько строк. В каждой следующей строке на одно слово больше.

# Примечание
# accumulate «складывает» не только числа.

from itertools import accumulate

from itertools import accumulate

text = input().split()
text1 = list()
for item in text:
    text1.append(item + " ")
for value in accumulate(text1):
    print(value[:-1])

# # Чтение ввода
# words = input().split()
#
# # Формирование и вывод строк ёлки
# for i in range(1, len(words) + 1):
#     print(' '.join(words[:i]))

