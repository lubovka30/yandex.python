# Формат ввода
# В первой строке записано натуральное число N — количество выделенных придорожных местностей.
# В каждой из N последующих строках — описание придорожной местности.

# Формат вывода
# Количество строк, в которых есть зайка.

n = int(input())
count: int = 0
while n > 0:
    if ("зайка" or "ЗАЙКА") in (str := input()):
        count += 1
    n -= 1
print(count)
