import random
from lists import listx

def randon_list(list_exercises, num_exe):
    rand_dict_list = {key: random.sample(range(value), num_exe) for key, value in list_exercises.items()}
    return rand_dict_list


def execute_generate_list():
    exercises_quantity = input('How many exercices do you want? ')
        
    if exercises_quantity == '': 
        raise Exception("The value is empty, try again!")

    number_of_exercises = int(exercises_quantity)

    if not (0 <  number_of_exercises):
        raise Exception("Number of exercises is out of range")

    exercises = randon_list(listx(), number_of_exercises)
    print(exercises)


def ask_if_stop():
    if input("Do you want proceed? (y/N) ") != 'y':
        exit()

def generate_list():
    while True:
        try:
            execute_generate_list()
        except Exception as ex:
            print('Write only int Numbers!!!!!')
            print(ex)
        finally:
            ask_if_stop()                



    

