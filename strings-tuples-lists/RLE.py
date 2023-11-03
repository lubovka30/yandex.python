# RLE
# Формат ввода
# Строка цифр длиной не меньше 1.

# Формат вывода
# Пары: сама цифра и количество повторений цифры подряд во введённой строке

text = input()
char: int = 0
while len(text):
    count: int = 0
    i: int = 0
    tmp = text[0]
    while text[i] == tmp:
        count += 1
        i += 1
        if i >= len(text):
            break
    print(tmp, count)
    text = text[i:]
