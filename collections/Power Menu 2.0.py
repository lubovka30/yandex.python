# В детском саду ежедневно подают новую кашу на завтрак.

# Напишите программу, которая строит расписание каш на ближайшие дни.

# Формат ввода.
# Вводится натуральное число M — количество каш в меню.
# В каждой из последующих M строк записано одно название каши.
# В конце передается натуральное число N — количество дней.

# Формат вывода.
# Вывести список каш в порядке подачи.

# Примечание
# Советуем изучить документацию на функцию itertools.islice, которая реализует срезы на основе итераторов.

from itertools import islice
from itertools import cycle

names = []  # объявление списка с названиями каш
for item in range(int(input())):  # итеративное добавление каш в список
    names.append(input())
days = int(input())  # число дней
count = 0  # счетчик итераций
for value in islice(cycle(names), 0, days):  # выбор среза islice из зацикленного names
    print(value)
    count += 1
    if count == days:
        break
