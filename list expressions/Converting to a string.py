# Вашему решению предоставлен список натуральных чисел numbers.

# Напишите выражение для генерации строки, представляющей собой отсортированный список чисел,
# записанных через дефис, окружённый пробелами, без повторений.

# Примечание
# В решении не должно быть ничего, кроме выражения.

# numbers = [3, 1, 2, 3, 2, 2, 1]
numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]
result = ' - '.join(map(str, sorted(set(numbers))))
print(result)
