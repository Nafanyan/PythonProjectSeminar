#Задать список из N элементов, заполненных числами из [-N, N].
#Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
def create_ar(N):
    arr =[]
    for i in range(-N,N+1):
        arr.append(i)
    return arr

def file_index(name_file):
    sup_ar = []
    source = open(name_file,'r')
    for line in source:
        sup_ar.append(int(line))
    source.close()
    return sup_ar

def sum_index(arr, name_file):
    result = 0
    array_index = file_index(name_file)
    for i in array_index:
        result += arr[i]
    return result


array = create_ar(10)
print(array)
print(file_index('seminar_3_4/index.txt'))
print(sum_index(array, 'seminar_3_4/index.txt'))