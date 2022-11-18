import random
from lists import listx

y = input('How many exercices do you want? ')

try:
    if (y != int(y)) or (y <= 0) or (y == '') or (y >= key.listx):
        print('Thanks!!!!')
        print()
except:
    print('Write only int Numbers!!!!!')
    print()
finally:
    y = int(y)
    
def randon_list(x):
    rand_dict_list = {key: random.sample(range(value), y) for key, value in x().items()}
    return rand_dict_list
