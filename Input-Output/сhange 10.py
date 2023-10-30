# Формат ввода
# Цена покупки — двоичное число, выданное кассовым аппаратом.
# Номинал купюры пользователя — десятичное число (≥100).

# Формат вывода
# Одно десятичное число — сдача, которую требуется отдать пользователю.

cost = input()
nominal = int(input())
i: int = 0
cost_dec: int = 0
cost_i = int(cost)
for item in cost:
    cost_dec = cost_dec + (cost_i % 10 * (2 ** i))
    cost_i = cost_i // 10
    i += 1
print(nominal - cost_dec)
