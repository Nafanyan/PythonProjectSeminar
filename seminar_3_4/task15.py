#Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]

def mult (N):
    sup = 1
    for i in range(1,N+1):
        sup *= i
    return sup

N = 6
arr = [x for x in range(1,N+1)]
res = list(map(mult,arr))
print(res)

