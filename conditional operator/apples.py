# У Пети было 7 яблок, а у Васи 6.
# Затем Петя отдал 3 яблока Васе, а у Толи взял 2 яблока.
# Вася попросил у Толи 5 яблок, но он отдал Гене 2.
# Затем Дима дал Пете N яблок, а Васе M.
# Так у кого в итоге яблок больше — у Пети или Васи?

# Формат ввода
# В первой строке записано натуральное число N.
# Во второй — M.

# Формат вывода
# Имя ребёнка, у которого больше яблок.

N = int(input())
M = int(input())
pete = 6 + N
vasya = 9 + M
if pete > vasya:
    print("Петя")
else:
    print("Вася")
