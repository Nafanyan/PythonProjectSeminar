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

def calculate(sup_arr):
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

def prioritet(example_str):
    support = example_str.split()
    i = 0
    temp = 0
    while i!= len(support):
        if (support[i] == '('):
            temp = i
        elif (support[i] == ')'):
            support[i] = calculate(support[temp + 1:i])
            del support[temp:i]
            i = 0
        i = i + 1
    return calculate(support)




example = '1-2*3+(21+(10-9*2)-1)'
example = preparation(example)
print(prioritet(example))

