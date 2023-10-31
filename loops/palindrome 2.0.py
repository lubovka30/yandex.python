# Формат ввода
# Одно натуральное число.

# Формат вывода
# YES — если число является палиндромом, иначе — NO.

n = int(input())
n1 = str(n)
n2: str = ""
while n > 0:
    n2 += str(n % 10)
    n = n // 10
if n1 == n2:
    print("YES")
else:
    print("NO")
