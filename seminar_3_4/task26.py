#Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
#Т е для k = 5, список будет выглядеть так: [5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5]
def fib(num):
    result = []
    temp_one = temp_two = 1
    for i in range(num*2):
        if (i < num + 1):
            temp = temp_one-temp_two
            result.append(temp)
            temp_one, temp_two = temp_two,temp
        elif(i == num + 1):
            result.reverse()
            temp_one = temp_two = 1
        else:
            temp = temp_one + temp_two
            result.append(temp)
            temp_one, temp_two = temp_two,temp
    return result

print(fib(7))
