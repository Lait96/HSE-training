# -*- coding: utf_8 -*-

# Задача:
# Перевернуть список.

# Переворот списка без создания нового

print(*list(map(int, input().split()[::-1])))

# Переворот списка без среза
list_a = list(input().split())

for i in range(len(list_a) // 2):
    list_a[i], list_a[(-i-1)] = list_a[(-i-1)], list_a[i]

print(*list_a)
