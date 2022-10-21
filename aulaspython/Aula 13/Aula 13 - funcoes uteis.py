#isnumeric, isdigit, isdecimal
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

# print(f'A soma é {int(n1)+int(n2)}')
''' se digitar letra onde é numero? '''

if n1.isnumeric() and n2.isnumeric():
    print('É possível somar.')
    print(f'A soma é {int(n1) + int(n2)}')
elif n1.isdigit() or n2.isdigit():
    print('Não é possível converter em número.')
    if n1.isdecimal() or n2.isdecimal():
        print('Digite somente números inteiros.')
    else:
        print('Impossível tal soma.')