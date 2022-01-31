#Строка содержит набор чисел. Показать большее и меньшее число
def min_max(text):
    text = text.split()
    sup_arr = []
    for el in text:
        sup_arr.append(int(el))
    return max(sup_arr),min(sup_arr)

numbers = '123 24 4212 62'
print(min_max(numbers))