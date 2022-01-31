#Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.
def peresech(one_str,two_str):
    if (one_str in two_str):
        count = 0
        setting = ''
        for i in range(len(two_str)-len(one_str)+1):
            for j in range(len(one_str)):
                setting = setting + two_str[i+j]
            if (setting == one_str): count += 1
            setting = ''
        return count
    else: return False

one_string = input()
two_string = input()

print(peresech(one_string,two_string))