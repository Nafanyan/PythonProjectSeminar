#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
def write_file(path,arr):
    file = open(path,'w')
    file.writelines(arr)
    file.close()

def filt(arr):
    res = []
    for el in arr:
        if ('^1' in el):
            temp = el.find('^')
            el = el[:temp]
        elif ('^0' in el):
            temp = el.find('^')
            el = el[:temp-1]
        if (el[0] == '0'):
            el = ''
        if ( el != arr[len(arr)-1]): el += ' + '
        res.append(el)
    res_str = "".join(res)

    return res_str


k = 5
arr = [f'{random.randint(0,100)}x^{i}' for i in range(k+1)]
print(arr)
write_file('task33_res.txt',filt(arr))
