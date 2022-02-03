#Напишите программу, удаляющую из текста все слова содержащие "абв".
text_delet = 'как'
text_S = 'так вот тут должен быть текст, никак иначе, как что-то умное, как-то наверное...'

text_S = text_S.split()
text_S = list(filter(lambda el: el.find(text_delet) == -1, text_S))
result = " ".join(text_S)
print(result)

