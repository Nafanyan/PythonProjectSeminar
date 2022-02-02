#Задать список из N элементов, заполненных числами из [-N, N].
#Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

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

N = 10
array = [ x for x in range(-N,N+1)]
print(array)
print(sum_index(array, 'index.txt'))