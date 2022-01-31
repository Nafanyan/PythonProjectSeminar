#Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

def sum_sequence(n):
    result = 0
    for i in range(1, n+1):
        result = result + (1+1/i) ** i
    return result

print(sum_sequence(4))