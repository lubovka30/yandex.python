# Формат ввода
# Вводится одно натуральное число.

# Формат вывода
# Требуется составить математическое выражение — произведение простых неубывающих чисел,
# которое в результате даёт исходное.

n = int(input())
if n == 1:
    print(n)
    exit()
cur: int = 2
out: str = ""
while n > 1:
    k: int = int(cur / 2)
    for item in range(2, k + 1):
        if cur % item == 0 and cur != item:
            pass
    if n % cur == 0:
        out += str(cur) + " * "
        n = n // cur
    else:
        cur += 1
print(out[:-3])
