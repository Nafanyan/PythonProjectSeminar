import time

def random(min,max, mode='real'):
    setting = 0.01 * int((time.time()*10000) % 100)
    if(mode == 'real'): result = min + setting * (max - min)
    else:result = int(min + setting * (max - min))

    return result

print(random(10,300,'int'))
