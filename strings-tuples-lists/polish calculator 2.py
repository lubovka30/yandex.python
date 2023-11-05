# Операции, которые выполняются с одним значением, называются унарными, с двумя — бинарными, с тремя — тернарными.
# Давайте улучшим наш калькулятор, добавив поддержку следующих операций:

# бинарные:
# + (сложение),
# - (вычитание),
# * (умножение),
# / (деление нацело; для отрицательных чисел работает по тем же правилам, что и в Python);
# унарные:
# ~ (унарный минус — меняет знак),
# ! (факториал),
# # (клонирование — вернуть в стек значение дважды);
# тернарные:
# @ (возвращает в стек те же три значения, но в ином порядке: второе, третье, первое).

# Формат ввода
# вводится одна строка, содержащая разделённые пробелами целые числа и знаки операций.
# Вместе они составляют корректное выражение в обратной польской нотации,
# не содержащее деления на ноль и взятия факториала от отрицательного числа.

# Формат вывода
# выводится одно целое число — результат вычисления выражения.

strInp = input()
listInp = strInp.split(" ")


def plus(massiv, j):
    result = int(massiv[j - 2]) + int(massiv[j - 1])
    massiv[j] = str(result)
    del massiv[j - 2:j]
    return massiv


def minus(massiv, j):
    result = int(massiv[j - 2]) - int(massiv[j - 1])
    massiv[j] = str(result)
    del massiv[j - 2:j]
    return massiv


def multiply(massiv, j):
    result = int(listInp[i - 2]) * int(listInp[i - 1])
    massiv[j] = str(result)
    del massiv[j - 2:j]
    return massiv


def division(massiv, j):
    result = int(listInp[i - 2]) // int(listInp[i - 1])
    massiv[j] = str(result)
    del massiv[j - 2:j]
    return massiv


def un_minus(massiv, j):
    if int(massiv[j - 1]) < 0:
        result = abs(int(massiv[j - 1]))
    elif int(massiv[j - 1]) == 0:
        result = int(massiv[j - 1])
    else:
        result = 0 - int(massiv[j - 1])
    massiv[j] = str(result)
    del massiv[j - 1]
    return massiv


def cloning(massiv, j):
    massiv[j] = str(massiv[j - 1])
    return massiv


def fatorial(massiv, j):
    p: int = 1
    if int(massiv[j - 1]) == 0:
        p = 0
    else:
        for item in range(int(massiv[j - 1])):
            p *= item + 1
    massiv[j] = str(p)
    del massiv[j - 1]
    return massiv


def mixing(massiv, j):
    massiv[j] = str(massiv[j - 3])
    del massiv[j - 3]
    return massiv


while len(listInp) > 1:
    i: int = 0
    if len(listInp) == 1:
        break
    while listInp[i].isdigit() or len(listInp[i]) > 1:
        i += 1
    else:
        tmp = listInp[i]
        if tmp == "+":
            listInp = plus(listInp, i)
        elif tmp == "-":
            listInp = minus(listInp, i)
        elif tmp == "*":
            listInp = multiply(listInp, i)
        elif tmp == "/":
            listInp = division(listInp, i)
        elif tmp == "~":
            listInp = un_minus(listInp, i)
        elif tmp == "#":
            listInp = cloning(listInp, i)
        elif tmp == "!":
            listInp = fatorial(listInp, i)
        elif tmp == "@":
            listInp = mixing(listInp, i)

print(listInp[0])
