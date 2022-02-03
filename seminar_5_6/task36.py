#Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

def check(arr):
    temp = arr[0]
    result = [temp]
    for i in range(len(arr)):
        if (temp < arr[i]):
            result.append(arr[i])
            temp = arr[i]
    return result

array = [1, 4, 5, 2, 3, 4, 6, 1, 7]
print(check(array))