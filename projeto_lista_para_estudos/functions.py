import random
from lists import listx

try:
    y = int(input('How many exercices do you want? '))
    if (y != int(y)) or (y <= 0) or (y == '') or (y >= key.listx):
        print('Invalid Number!')
        print()
except:
    print('Write only int Numbers!!!!!')
    print()
finally:
    exit()
    
def randon_list(x):
    rand_dict_list = {key: random.sample(range(value), y) for key, value in x().items()}
    return rand_dict_list
