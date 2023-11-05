# Напишите программу, которая производит вычисление выражения, записанного в обратной польской нотации (ОПН).

# Формат ввода
# вводится одна строка, содержащая разделённые пробелами целые числа и знаки операций +, -, *,
# которые вместе составляют корректное выражение в обратной польской нотации.

# Формат вывода
# выводится одно целое число — результат вычисления выражения.

result: int = 0
strInp = input()
listInp = strInp.split(" ")

while len(listInp) > 1:
    i: int = 0
    result = 0
    if len(listInp) == 1:
        break
    while listInp[i].isdigit() or len(listInp[i]) > 1:
        i += 1
    else:
        tmp = listInp[i]
        if tmp == "+":
            result = int(listInp[i - 2]) + int(listInp[i - 1])
        elif tmp == "-":
            result = int(listInp[i - 2]) - int(listInp[i - 1])
        elif tmp == "*":
            result = int(listInp[i - 2]) * int(listInp[i - 1])
        listInp[i] = str(result)
        del listInp[i - 2:i]

print(result)

