#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
import math
def mult_couple(arr):
    result = []
    for i in range(math.ceil(len(arr)/2)):
        result.append(arr[i] * arr[len(arr)-1-i])
    return result

array = [2,3,4,5,6]
print(mult_couple(array))
