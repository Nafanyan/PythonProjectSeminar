#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def dif_max_min(arr):
    sup = []
    for el in arr:
        sup.append(round(el - int(el),3))
    return max(sup) - min(sup)

array = [1.1, 1.2, 3.1, 5.2, 10.01]
print(dif_max_min(array))