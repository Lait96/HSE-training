# -*- coding: utf_8 -*-

# Задача:
# Найти соседние числа с одинаковым знаком


List_a = list(map(int, input().split()))
List_b, i, size = [], 1, len(List_a)

while i < size and len(List_b) < 2:
    if List_a[i - 1] == List_a[i] \
            or (List_a[i - 1] - 1) == List_a[i] \
            or (List_a[i - 1] + 1) == List_a[i]:
        List_b.append(List_a[i - 1])
        List_b.append(List_a[i])
    i += 1
print(*List_b)
