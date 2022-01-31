#Написать программу преобразования десятичного числа в двоичное

def ten_in_two(number):
    result = ''
    while(number >= 1):
        if(number % 2 == 0): result += '0'
        else: result +='1'
        number = int(number/2)
    return ''.join(reversed(result))

print(ten_in_two(16))