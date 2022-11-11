'''map exercises - tuples in list'''

color = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

def join (j):
    c = list(map('_'.join, j))
    return c
    
print(f'The original list: {color}')
print(f'The new list: {join(color)}')
