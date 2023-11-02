# Формат ввода
# вводятся строки, пока не будет введена строка «ФИНИШ».

# Формат вывода
# выводится один символ в нижнем регистре — наиболее часто встречающийся.

# Примечания
# Пробелы в анализе не участвуют.
# Если в результате анализа получено несколько ответов,
# следует вывести первый по алфавиту.
result: str = ""
while (text := input()) != "ФИНИШ":
    count: int = 0
    for i in range(len(text)):
        tmp = text[i]
        if text.count(tmp) > count:
            count = text.count(tmp)
            result = tmp
        elif text.count(tmp) == count:
            if tmp < result:
                result = tmp
print(result.lower())
