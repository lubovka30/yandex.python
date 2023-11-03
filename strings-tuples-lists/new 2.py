# Формат ввода
# вводится натуральное число L — необходимая длина заголовка.
# Вводится натуральное число N — количество строк в заголовке новости.
# В каждой из последующих N строк записано по одной строке заголовка.

# Формат вывода
# Сокращённый заголовок.

# Примечание
# Многоточие учитывается при подсчёте длины заголовка.
# Символ перевода строки при подсчёте длины не учитывается.

length = int(input())
text: str = ""
for i in range(n := int(input())):
    if i < n - 1:
        text += input() + "\n"
    else:
        text += input()
listInp = text.split("\n")

for j in range(len(listInp)):
    if len(listInp[j]) < length - 3:
        print(listInp[j])
        length = length - len(listInp[j])
    else:
        k = length - 3
        result = str(listInp[j])
        print(result[:k] + "...")
        break
