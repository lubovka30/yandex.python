# Вашему решению будет предоставлена строка text.

# Напишите выражение для генерации словаря, который содержит информацию о частоте употребления букв в заданной строке.

# При анализе не учитывайте регистр, а ключами словаря сделайте использованные в строке буквы в нижнем регистре.

# Примечание
# В решении не должно быть ничего, кроме выражения.

# text = 'Мама мыла раму!'

text = '''Ехали медведи
На велосипеде.

А за ними кот
Задом наперёд.'''
stat = {i: text.lower().count(i) for i in text.replace(" ", "").lower() if i.isalpha()}
print(stat)
