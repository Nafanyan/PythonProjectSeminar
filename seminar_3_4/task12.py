#Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.
def dictionary_create(N):
    res_dic = {}
    for i in range(N):
        res_dic[i] = 3 * i + 1
    return res_dic

print(dictionary_create(6))

