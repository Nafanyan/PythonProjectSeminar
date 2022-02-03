#В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

def read_file(path):
    data = open(path,'r')
    result = []
    for el in data:
        result.append(el)
    data.close()
    return result

def check(arr):
    for i in range(len(arr)):
        if (arr[i] != arr[i+1] - 1): return arr[i+1]

arr = read_file('task35_num.txt')
arr = arr[0].split()
arr = list(map(lambda el: int(el),arr))
arr = check(arr)
print(arr)