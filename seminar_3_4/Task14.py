#Подсчитать сумму цифр в вещественном числе
array = (filter(lambda arr: arr !='.',input()))
array_int = map(lambda arr: int(arr),array)
sum = sum(array_int)
print(sum)
