# Вашему решению будет предоставлена строка sentence слов, разделённых пробелами.

# Напишите списочное выражения для генерации списка длин слов.

# Примечание
# В решении не должно быть ничего, кроме списочного выражения.

sentence = input()
long = [len(sen) for sen in sentence.split()]
print(long)
