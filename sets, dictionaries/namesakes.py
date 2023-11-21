# Формат ввода
# В первой строке указывается количество мужчин — сотрудников организации (N).
# Затем идут N строк с фамилиями этих сотрудников в произвольном порядке.

# Формат вывода
# Количество однофамильцев в организации.

names = list()
for i in range(int(input())):
    names.append(input().split())
count: int = 0
names.sort()

for name in names:
    if names.count(name) > 1:
        count += 1
print(count)
