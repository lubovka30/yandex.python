# В детском саду 2 ребенка съедают 2 куска колбасы за 2 минуты. Сколько кусков колбасы за
# N минут съедят M детей?

# Формат ввода
# В первой строке записано натуральное число N≥1
# Во второй строке записано натуральное число M≥1

# Формат вывода
# Одно натуральное число — количество кусков колбасы, съеденных детьми

N = int(input())
M = int(input())
print(int(0.5 * N * M))
