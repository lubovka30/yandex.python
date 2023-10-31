# Формат ввода
# Вводится одно натуральное число.

# Формат вывода
# Требуется вывести сообщение YES если число простое, иначе — NO.

n = int(input())
if n == 1:
    print("NO")
    exit()
k: int = int(n / 2)
for item in range(2, k + 1):
    if n % item == 0 and n != item:
        print("NO")
        exit()
print("YES")
