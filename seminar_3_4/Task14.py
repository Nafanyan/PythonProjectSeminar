#Подсчитать сумму цифр в вещественном числе

def sum_numb_real(num):
    result = 0
    for i in str(num):
        if(i != '.'): result += int(i)
    return result

number = float(input())
print(sum_numb_real(number))
