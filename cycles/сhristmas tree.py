# Напишите программу, которая зажигает Ёлочку, когда все дети прокричат «Три!»

# Формат ввода
# Вводятся крики детей.

# Формат вывода
# Выводить «Режим ожидания...», пока дети не прокричат «Три!».
# В конце вывести «Ёлочка, гори!»

while (param := input()) != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")
