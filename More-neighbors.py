# -*- coding: utf_8 -*-

# Задача:
# Найти количество чисел больше своих соседей

List_A = list(map(int, input().split()))
result = 0

for i in range(1, len(List_A) - 1):
    if List_A[i - 1] < List_A[i] > List_A[i + 1]:
        result += 1

print(result)
