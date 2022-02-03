def max_num(arr):
    sup = []
    res = []
    for i in range(len(arr)):
        temp = arr[i]
        sup.append(temp)
        for j in range(i,len(arr)):
            if(temp < arr[j]):
                sup.append(arr[j])
                temp = arr[j]
        res.append(sup)
        sup = []
    return res
def maxi(arr):
    temp = 0
    res = []
    for el in arr:
        if (temp < len(el)):
            temp = len(el)
            res = el
    return res


arr = [5, 2, 3, 4, 6, 1, 7]
arr = max_num(arr)
print(maxi(arr))