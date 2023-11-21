# Формат ввода
# В каждой строке записано описание придорожной местности.
# Конец ввода обозначается пустой строкой.

# Формат вывода
# определите список увиденного рядом с зайками без повторений.
# Порядок вывода не имеет значения.

# Примечание
# Считается, что объект находится рядом, если он записан справа или слева от требуемого.

out = set()
description = list()
while (text := input()) != "":
    description = text.lower().split()
    if "зайка" in description:
        while "зайка" in description:
            index = description.index("зайка")
            if index > 0:
                out.add(description[index - 1])
            if index < len(description) - 1:
                out.add(description[index + 1])
            description.pop(index)
print("\n".join(out))
