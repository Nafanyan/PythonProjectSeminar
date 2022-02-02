#Найти НОК двух чисел
number_one,number_two = 151, 18
array = [i for i in range(1,min(number_one,number_two)+1)]
arr_kr = filter(lambda i : number_one % i == 0 and number_two % i == 0, array)
result = int(number_one * number_two / max(arr_kr))
print(result)
