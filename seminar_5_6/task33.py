#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
def write_file(path,arr):
    file = open(path,'w')
    file.writelines(arr)
    file.close()

k = 2
arr = [f'{random.randint(0,100)}x^{i}' for i in range(100)]
print(arr)
res = list(filter(lambda el: f'^{k}' in el and len(el) - 1 - el.find('^') == len(str(k)), arr))
write_file('task33_res.txt',res)
