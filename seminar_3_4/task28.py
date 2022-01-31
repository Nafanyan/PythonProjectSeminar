#Найти корни квадратного уравнения Ax² + Bx + C = 0
#Математикой
#Используя дополнительные библиотеки*
num_arr = ['1','2','3','4','5','6','7','8','9','0']

def dis(text):
    sup_arr = []
    temp = ''
    flag = False
    if (text[0] in num_arr): flag = True
    for i in range(len(text)):
        if(text[i] in num_arr and flag): temp += text[i]
        elif(text[i] == '^'): flag = False
        elif(text[i] == '+' or text[i] == '-' or text[i] == '='):
            flag = True
            if (temp != ''): sup_arr.append(int(temp))
            temp= ''
            temp += text[i]
    return sup_arr[1] * sup_arr[1] + sup_arr[0] * sup_arr[2] * (- 4), sup_arr

def math_square(text):
    diskrem, num_arr = dis(text)
    if (diskrem < 0): return False
    elif(diskrem == 0): return -num_arr[1] / (2 * num_arr[0])
    elif(diskrem > 0): return round((-num_arr[1] + diskrem**0.5)/(2 * num_arr[0]),2),\
                              round((-num_arr[1] - diskrem**0.5)/(2 * num_arr[0]),2)

print(math_square('-3x^2 -7x - 3 = 0'))



