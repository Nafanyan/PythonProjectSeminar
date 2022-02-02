from task19 import random
#Реализовать алгоритм перемешивания списка.
def interfere(text):
    for i in range(len(text)):
        index = random(i,len(text),'int')
        temp = text[i]
        text[i] = text[index]
        text[index] = temp
    return text
array = [i for i in range(10)]
print(interfere(array))
