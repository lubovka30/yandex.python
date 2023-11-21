# Формат ввода
# В первой строке указывается количество мужчин — сотрудников организации (N).
# Затем идут N строк с фамилиями этих сотрудников в произвольном порядке.

# Формат вывода
# Список однофамильцев в организации с указанием их количества в алфавитном порядке.
# Если таковых нет — вывести «Однофамильцев нет».

names = dict()
count: int = 0
for i in range(int(input())):
    name = input()
    if name not in names:
        names[name] = 1
    else:
        names[name] += 1
namesSorted = dict(sorted(names.items()))
for key, value in namesSorted.items():
    if value > 1:
        print(f"{key} - {value}")
        count += 1
if count == 0:
    print("Однофамильцев нет")
