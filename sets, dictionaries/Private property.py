# Формат ввода
# В первой строке задается количество детей в группе (N).
# В каждой из следующих N строк записано имя ребенка и его игрушки в формате:
# Имя: игрушка1, игрушка2, ....

# Формат вывода
# Список игрушек, которые есть только у одного из детей в алфавитном порядке.

# создание списка с игрушками
toys_list = list()
out = list()
# цикл обхода вводимых строк
for i in range(int(input())):
    text = input()
    index = text.find(":") + 1
    toys = text[index:]
    # Удаляем пробелы из строки с игрушками
    toys = toys.replace(" ", "")
    # Добавляем игрушки в список
    toys_list.extend(list(set(toys.split(','))))

    # Удаляем пробелы из строки с игрушками и добавляем игрушки в список
    # toys_list.extend(map(str.strip, toys.split(',')))

for toy in toys_list:
    if toys_list.count(toy) == 1:
        out.append(toy)
print("\n".join(sorted(out)))
