# Напишите программу, которая избавляется от:
# Двух символов # в начале информационных сообщений;
# Строк, заканчивающихся тремя символами @.

# Формат ввода
# вводятся строки отчёта. Признаком завершения ввода считается пустая строка.

# Формат вывода
# Очищенные данные.

while (text := input()) != "":
    result = text.lstrip("##")
    if text.endswith("@@@"):
        continue
    print(result)
