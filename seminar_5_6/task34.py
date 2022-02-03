#Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
import re
def read_file(path):
    data = open(path,'r')
    result = []
    for el in data:
        result.append(el)
    data.close()
    return result


one_file = read_file('task34_one.txt')
two_file = read_file('task34_two.txt')
res = one_file + two_file
res = list(map(lambda el:el.replace(' - ',' -'),res ))
res = list(map(lambda el: re.split(' \+ | ',el),res))
result = []
for i in range(len(res)):
    result += list(map(lambda el: el.split('x^'),res[i]))
print(result)


