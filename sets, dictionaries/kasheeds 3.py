# Формат ввода
# В первых двух строках указывается количество детей, любящих манную и овсяную каши (N и M).
# Затем идут N+M строк — перемешанные фамилии детей.
# Гарантируется, что в группе нет однофамильцев.

# Формат вывода
# В алфавитном порядке фамилии учеников, которые любят только одну кашу.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».

n = int(input())  # количество детей
m = int(input())  # количество детей
result = set()

for i in range(n + m):
    tmp = set(input().split())
    if tmp <= result:
        result = result.difference(tmp)
    else:
        result = result.union(tmp)
if len(result) == 0:
    print("Таких нет")
else:
    result = list(result)
    result.sort()
    for letter in result:
        print(letter)
