#Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
#Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9

def preparation(source):
    source = source.replace('+', ' + ')
    source = source.replace('-', ' - ')
    source = source.replace('*', ' * ')
    source = source.replace('/', ' / ')
    source = source.replace(')', ' ) ')
    source = source.replace('(', ' ( ')
    return source

def calculate(example_str):
    sup_arr = example_str.split()
    i = 0
    while(i != len(sup_arr)):
        if (sup_arr[i] == '*' ):
            sup_arr[i] = float(sup_arr[i - 1]) * float(sup_arr[i + 1])
            sup_arr.pop(i + 1)
            sup_arr.pop(i - 1)
            i = i - 2

        elif(sup_arr[i] == '/'):
            sup_arr[i] = float(sup_arr[i - 1]) / float(sup_arr[i + 1])
            sup_arr.pop(i + 1)
            sup_arr.pop(i - 1)
            i = i - 2
        i = i + 1
    i = 0
    while(i != len(sup_arr)):
        if (sup_arr[i] == '+' ):
            sup_arr[i] = float(sup_arr[i - 1]) + float(sup_arr[i + 1])
            sup_arr.pop(i + 1)
            sup_arr.pop(i - 1)
            i = i - 2
        elif(sup_arr[i] == '-'):
            sup_arr[i] = float(sup_arr[i - 1]) - float(sup_arr[i + 1])
            sup_arr.pop(i + 1)
            sup_arr.pop(i - 1)
            i = i - 2
        i = i + 1
    return float(sup_arr[0])

example = '1-2*3'
example = preparation(example)
print(calculate(example))

