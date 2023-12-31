# Формат ввода
# В первой строке записано натуральное число N — количество выделенных придорожных местностей.
# В каждой из N последующих строк записано описание придорожной местности.

# Формат вывода
# вывести все найденные объекты в придорожных местностях.

textSet = set()  # создаем множество для хранения результата

for i in range(int(input())):  # циклично принимаем от пользователя строки
    textSet = textSet | set(input().split())  # преобразуем строки во множество и к textSet
for item in textSet:  # поэлементно (по слову) выводим в консоль уникальные слова
    print(item)
