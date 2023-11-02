# В детском саду ежедневно подают новую кашу на завтрак.
# Каши чередуются в следующем порядке:
# Манная;
# Гречневая;
# Пшённая;
# Овсяная;
# Рисовая.
# Напишите программу, которая строит расписание каш на ближайшие дни.

# Формат ввода
# вводится натуральное число N — количество дней.

# Формат вывода
# вывести список каш в порядке подачи.

menu: list = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
k: int = 0
for i in range(n := int(input())):
    if n > len(menu):
        if k == len(menu) - 1:
            print(menu[k])
            k = 0
        else:
            print(menu[k])
            k += 1
    else:
        print(menu[k])
        k += 1
