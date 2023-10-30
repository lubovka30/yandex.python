# Все строки должны быть длиной в 35 символов.

# Формат ввода
# Название товара;
# цена товара;
# вес товара;
# количество денег у пользователя.

# Формат вывода
# Красивый чек в формате:

# ================Чек================
# Товар:                    <продукт>
# Цена:     <число>кг * <число>руб/кг
# Итого:                   <число>руб
# Внесено:                 <число>руб
# Сдача:                   <число>руб
# ===================================

name = input()
cost = int(input())
weight = int(input())
user_money = int(input())
n = len(name)
n1 = len(str(cost)) + len(str(weight))
n2 = len(str(cost * weight))
n3 = len(str(user_money))
n4 = len(str(user_money - weight * cost))

print("=" * 16, "Чек", "=" * 16, sep="")
print("Товар:", " " * (29 - n), name, sep="")
print("Цена:", " " * (19 - n1), weight, "кг * ", cost, "руб/кг", sep="")
print("Итого:", " " * (26 - n2), weight * cost, "руб", sep="")
print("Внесено:", " " * (24 - n3), user_money, "руб", sep="")
print("Сдача:", " " * (26 - n4), user_money - weight * cost, "руб", sep="")
print("=" * 35)
