#Определить, присутствует ли в заданном списке строк, некоторое число
stop = ['1','2','3','4','5','6','7','8','9','0']

def search_num(list, num):
    result = False
    num_str = str(num)
    for i in range(len(list)):
        number_el = 0
        for j in range(len(list[i])):
            if(list[i].find(num_str,number_el,len(list[i])) != -1):
                num_el = list[i].find(num_str,number_el,len(list[i])) + 1
                if(num_el - 1 == 0 and not(list[i][len(num_str)] in stop)):
                    result = True
                    break
                elif(num_el + len(num_str) - 2 == len(list[i]) and not(list[num_el-2] in stop)):
                    result = True
                    break
                elif(not(list[i][num_el - 2] in stop) and not(list[i][num_el - 1 + len(num_str)] in stop)):
                    result = True
                    break

    return result

source = ['22,12,31,12344,2354', 'asd', 'sa21']
print(search_num(source,'2'))

