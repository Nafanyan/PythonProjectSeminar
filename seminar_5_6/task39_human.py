#Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека


no_sweets = True
num_player, sweets = 1, 40
while(no_sweets):
    print(f'Всего конфет {sweets}')
    print(f'Ход игрока номер {num_player}')
    num_sweets = int(input())
    if (num_sweets <= 0 or num_sweets > 6):
        print('Всегда нужно брать минимум 1 конфету и не больше 6')
        continue
    sweets -= num_sweets
    if (sweets <= 0):
        no_sweets = False
        break
    if(num_player == 1): num_player = 2
    else: num_player = 1

print(f'Победил игрок под номером {num_player}')

