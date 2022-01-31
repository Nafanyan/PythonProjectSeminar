#Вычислить число  c заданной точностью d
#	Пример: при d = 0.001,  = 3.141. 10-1d10-10
import math
def pi(accur):
    i = 0
    while (accur != 1):
        accur *= 10
        i += 1
    return round(math.pi,i)

print(pi(0.00001))