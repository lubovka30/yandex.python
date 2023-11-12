# Формат ввода
# В первой строке задаётся количество детей в группе (N).
# В следующих N строках записана фамилия ребенка и список его любимых каш.
# В последней строке записана каша, информацию о которой хочет получить воспитатель.

# Формат вывода
# Фамилии учеников, которые любят заданную кашу, в алфавитном порядке.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».

text: list = []
textList: list = []
out: list = []
for i in range(int(input())):
    text = input().split()
    textList.append({text[0]: text[1:]})
find = input()

for j in range(len(textList)):
    for value in textList[j].values():
        if find in "".join(value):
            for key in textList[j].keys():
                out.append(key)
out.sort()  # сортируем список в алфавитном порядке

if len(out) == 0:
    print("Таких нет")
else:
    print("\n".join(out))
