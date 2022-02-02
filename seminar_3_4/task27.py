#Строка содержит набор чисел. Показать большее и меньшее число

numbers = '123 24 4212 62'
num = list(map(int,numbers.split()))
print(max(num), min(num))