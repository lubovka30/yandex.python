# Давайте создадим программу, которая преобразует введённую стоку из горизонтальной записи в вертикальную.

# Формат ввода
# Одна строка.

# Формат вывода
# Вертикальное представление введённой строки.
j: int = 0
for i in (text := input()):
    print(text[j])
    j += 1
