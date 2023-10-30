# Формат ввода
# Три строки описывающих придорожную местность.
#
# Формат вывода
# Строка в которой есть зайка, а затем её длина.
# Если таких строк несколько, выбрать ту, что меньше всех лексикографически.

str1 = input()
str2 = input()
str3 = input()
if ("зайка" or "ЗАЙКА") in str1 and ("зайка" or "ЗАЙКА") in str2 and ("зайка" or "ЗАЙКА") in str3:
    print(min(str1, str2, str3), len(min(str1, str2, str3)))
elif ("зайка" or "ЗАЙКА") in str1 and ("зайка" or "ЗАЙКА") in str2:
    print(min(str1, str2), len(min(str1, str2)))
elif ("зайка" or "ЗАЙКА") in str1 and ("зайка" or "ЗАЙКА") in str3:
    print(min(str1, str3), len(min(str1, str3)))
elif ("зайка" or "ЗАЙКА") in str2 and ("зайка" or "ЗАЙКА") in str3:
    print(min(str2, str3), len(min(str2, str3)))
elif ("зайка" or "ЗАЙКА") in str1:
    print(str1, len(str1))
elif ("зайка" or "ЗАЙКА") in str2:
    print(str2, len(str2))
elif ("зайка" or "ЗАЙКА") in str3:
    print(str3, len(str3))
