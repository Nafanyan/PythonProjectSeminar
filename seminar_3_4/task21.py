#Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
def second_occur_index(list,string):
    counter = 0
    result = 0
    for i in range(len(list)):
        num_el = 0
        for j in range(len(list[i])):
            if(list[i].find(string,num_el,len(list[i])) != -1 and counter <= 1):
                num_el = list[i].find(string, num_el, len(list[i])) + 1
                result = i, num_el - 1
                counter += 1
    if (counter != 2): result = -1

    return result

source = ['12,1,34,1','sdad','sdss13fv']
print(second_occur_index(source,'sd'))



