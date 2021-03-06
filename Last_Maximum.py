# -*- coding: utf_8 -*- 

# Задача:
# Найти максимальный элемент в массиве (и его последнюю позицию).

list_a = list(map(int, input().split()))
Max = max(list_a)
n, Last_position = 0, 0

for i in list_a:
    if i == Max and n > Last_position:
        Last_position = n
    n += 1

print(Max, Last_position)
