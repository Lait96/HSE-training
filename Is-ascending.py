# -*- coding: utf_8 -*-

# Задача:
# Проверить является ли список монотонно возрастающим
# Доп. условия:
# Решение в виде функции с одним циклом while без вложенных условий и циклов в данный цикл

List_a = list(map(int, input().split()))


def IsAscending(A):
    i, size = 1, len(A)
    while i < size and A[i - 1] < A[i]:
        i += 1
    return "YES" if i == size else "NO"


result = IsAscending(List_a)
print(result)
