# Формат ввода
# вводится строка.

# Формат вывода
# Если введённая строка относится к палиндрому, то вывести YES, а иначе — NO.

# Примечание
# При проверке не обращайте внимания на регистр и пробелы.

def is_palindrome(text):
    text = text.lower().replace(' ', '')
    if text == text[::-1]:
        return True
    else:
        return False


if is_palindrome(input()):
    print("YES")
else:
    print("NO")
