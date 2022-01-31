#Найти НОК двух чисел

def nok(number_one,number_two):
    temp = 0
    for i in range(1,max(number_one,number_two)):
        if (number_one % i == 0 and number_two % i == 0): temp = i
    return int(number_one * number_two / temp)



print(nok(151,18))