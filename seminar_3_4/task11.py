#Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.

def set_create(N):
    result = []
    for i in range(N):
        result.append((-3)**i)
    return result

print(set_create(5))
