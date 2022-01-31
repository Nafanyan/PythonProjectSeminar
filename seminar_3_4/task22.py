#Найти сумму чисел списка стоящих на нечетной позиции
def sum_odd(array):
    result = 0
    for i in range(1,len(array),2):
        result += array[i]
    return result

arr = [1,2,3,4,5,6,7,8]
print(sum_odd(arr))

