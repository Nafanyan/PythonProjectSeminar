import random

def bot (quantity_sweet):
    temp = 0
    if (quantity_sweet > 6 and quantity_sweet % 7 != 0):
        for i in range(1,7):
            if ((quantity_sweet - i) % 7 == 0): temp = i
    elif(quantity_sweet % 7 == 0): temp = random.randint(1,6)
    else:
        for i in range(7):
            if (quantity_sweet - i == 0): temp = i
    return temp

def who_win(player):
    if (player == 1): return 'Вы победили!'
    else:return 'Победил компьютер'

def swap(player):
    if(player == 1): return 2
    else: return 1


num_player, sweets = 1, 40
while(True):
    print(f'Всего конфет {sweets}')
    if(num_player == 1):
        print('Ваш ход:')
        num_sweets = int(input())
    else:
        print('Ход компьютера')
        num_sweets = bot(sweets)
        print(num_sweets)
    if (num_sweets <= 0 or num_sweets > 6):
        print('Всегда нужно брать минимум 1 конфету и не больше 6')
        continue
    sweets -= num_sweets
    if (sweets <= 0):
        break
    num_player = swap(num_player)


print(who_win(num_player))
