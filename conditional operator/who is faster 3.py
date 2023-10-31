# В новом сезоне за первенство в велогонках вновь борются лучшие из лучших.
# Протяжённость заключительной трассы — 43872м, и все хотят знать,
# кто получит золотую медаль.

# Нам известны средние скорости трёх претендентов на победу –
# Пети, Васи и Толи. Кто из них победит?

# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.

# Формат вывода
# Красивый пьедестал (ширина ступеней 8 символов).

# Примечание
# В данный момент визуализация тестов работает некорректно.
# Ответ на первый тест:

#           Петя
#   Толя
#                   Вася
#    II      I      III

petya = int(input())
vasya = int(input())
tolya = int(input())

if max(petya, vasya, tolya) == petya:
    if max(vasya, tolya) == vasya:
        print(" " * 10, "Петя", " " * 10, sep="")
        print(" " * 2, "Вася", " " * 20, sep="")
        print(" " * 18, "Толя", " " * 2, sep="")
        print(" " * 3, "II", " " * 6, "I", " " * 6, "III", " " * 3, sep="")
    else:
        print(" " * 10, "Петя", " " * 10, sep="")
        print(" " * 2, "Толя", " " * 20, sep="")
        print(" " * 18, "Вася", " " * 2, sep="")
        print(" " * 3, "II", " " * 6, "I", " " * 6, "III", " " * 3, sep="")
if max(petya, vasya, tolya) == vasya:
    if max(petya, tolya) == petya:
        print(" " * 10, "Вася", " " * 10, sep="")
        print(" " * 2, "Петя", " " * 20, sep="")
        print(" " * 18, "Толя", " " * 2, sep="")
        print(" " * 3, "II", " " * 6, "I", " " * 6, "III", " " * 3, sep="")
    else:
        print(" " * 10, "Вася", " " * 10, sep="")
        print(" " * 2, "Толя", " " * 20, sep="")
        print(" " * 18, "Петя", " " * 2, sep="")
        print(" " * 3, "II", " " * 6, "I", " " * 6, "III", " " * 3, sep="")
if max(petya, vasya, tolya) == tolya:
    if max(petya, vasya) == petya:
        print(" " * 10, "Толя", " " * 10, sep="")
        print(" " * 2, "Петя", " " * 20, sep="")
        print(" " * 18, "Вася", " " * 2, sep="")
        print(" " * 3, "II", " " * 6, "I", " " * 6, "III", " " * 3, sep="")
    else:
        print(" " * 10, "Толя", " " * 10, sep="")
        print(" " * 2, "Вася", " " * 20, sep="")
        print(" " * 18, "Петя", " " * 2, sep="")
        print(" " * 3, "II", " " * 6, "I", " " * 6, "III", " " * 3, sep="")