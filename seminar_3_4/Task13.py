#Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.
def peresech(one_str,two_str):
    return (two_str.count(one_str))

one_string = input()
two_string = input()

print(peresech(one_string,two_string))