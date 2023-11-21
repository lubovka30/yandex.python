# Формат ввода
# В каждой строке записано описание придорожной местности.
# Конец ввода обозначается пустой строкой.

# Формат вывода
# Список увиденного и их количество.
# Порядок вывода не имеет значения.

out: list = []

while (text := input()) != "":
    for word in text.split():
        out.append(word)
out.sort()
while out:
    print(f"{out[0]} {out.count(out[0])}")
    tmp = out[0]
    while tmp in out:
        out.remove(tmp)
