fild = [['   |   |   '],['-----------'],['   |   |   '],['-----------'],['   |   |   ']]
#data = {[0,0]:[0,1],[0,1]:[0,5],[0,2]:[0,9],[1,0]:[2,1],[1,1]:[2,5],[1,2]:[2,9],[2,0]:[4,1],[2,1]:[4,5],[2,2]:[4,9]}
def print_fild(array):
    result = ''
    for i in range(len(array)):
        for j in range(len(array[i])):
            result += array[i][j]
        result += '\n'
    return result


def add_position(arr,pos,znak):
    result = []
    sup_str = ''
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                if (k == pos[1] and i == pos[0] ): sup_str += znak
                else: sup_str += arr[i][j][k]
        result.append(sup_str)
        sup_str = ''
    return result
print(print_fild(add_position(fild,[0,1],'x')))
