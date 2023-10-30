# Формат ввода
# Одно четырёхзначное число

# Формат вывода
# YES если число является палиндромом, иначе — NO.

number = int(input())

if number % 10 == number // 1000 and number // 10 % 10 == number // 100 % 10:
    print("YES")
else:
    print("NO")
