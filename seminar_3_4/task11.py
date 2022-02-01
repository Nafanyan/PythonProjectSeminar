#Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.
N = 5
arr = list(map(lambda arr: -3 **arr, [x for x in range(N)]))
print(arr)