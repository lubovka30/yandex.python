# Формат ввода
# Вводятся строки, описывающие придорожную местность.
# В конце поездки вводится «Приехали!»

# Формат вывода
# Количество строк, в которых есть зайка.

count: int = 0
while (param := input()) != "Приехали!":
    if ("зайка" or "ЗАЙКА") in param:
        count += 1
print(count)
