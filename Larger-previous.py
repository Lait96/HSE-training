# -*- coding: utf_8 -*-

# Задача:
# Найти все числа больше предыдущего в листе и вывести их

List_a = list(map(int, input().split()))
List_b = []
previous = List_a[0]

for i in List_a:
    if i > previous:
        List_b.append(i)
    previous = i
print(*List_b)
