#Составить список простых множителей натурального числа N
def simple_num(num):
    list = []
    for i in range(1,num+1):
        if num % i == 0: list.append(i)
    if (len(list) == 2): return list
    else:
        sup_list = []
        i = 1
        while num != 1:
            if(num % list[i] == 0):
                sup_list.append(list[i])
                num = num / list[i]
            else: i = i + 1
        return sup_list

print(simple_num(999))

