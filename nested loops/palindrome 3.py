# Формат ввода
# В первой строке записано число N
# Во всех последующих N строках указано по одному числу.

# Формат вывода
# требуется вывести общее количество палиндромов среди введённых чисел (кроме числа N).

def check_palindrome(num):
    str1: list = list(num)
    str2 = list(num)
    str2.reverse()
    if str1 == str2:
        return True
    else:
        return False


n = int(input())
count: int = 0
for i in range(n):
    if check_palindrome(input()):
        count += 1
print(count)
