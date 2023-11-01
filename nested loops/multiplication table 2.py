# Формат ввода
# В первой строке записан требуемый размер таблицы.
# Во второй строке — ширина столбцов.

# Формат вывода
# Таблица умножения заданного размера и вида.

size = int(input())
width = int(input())

for i in range(size):
    count: int = 0
    out: str = ""
    k: int = 1
    while k <= size:
        n = len(str(k * (i + 1)))
        space = " " * ((width - n) // 2)
        out += space + str(k * (i + 1)) + space
        if (width - n) % 2 == 1:
            out += " "
        if k != size:
            out += "|"
            count += 1
        k += 1
    print(out)
    if i < size - 1:
        print("-" * (width * size + count))
