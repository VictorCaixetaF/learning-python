import random
from lists import listx

def randon_list(x):
    rand_dict_list = {key: random.sample(range(value), 5) for key, value in x().items()}
    return rand_dict_list
