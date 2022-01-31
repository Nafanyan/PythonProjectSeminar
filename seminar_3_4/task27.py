#Строка содержит набор чисел. Показать большее и меньшее число
num_part = ['1','2','3','4','5','6','7','8','9','0']
def min_max(text):
    sup_arr = []
    temp = ''
    for el in text:
        if (el in num_part): temp += el
        else:
            if (temp != ''): sup_arr.append(int(temp))
            temp = ''
    return max(sup_arr),min(sup_arr)

numbers = '123, 24, 4212, 62'
print(min_max(numbers))