'''
como contar quantidade de caracteres dentro da string
'''

usuario = input('Login: ')
qtd_caract = len(usuario)

print(usuario, qtd_caract, type(qtd_caract))

if qtd_caract < 8:
    print('minimo 8 caracteres')
else:
    print('cadastro realizado.')

str1 = input('quantidade de caracteres 1: ')
str2 = input('quantidade de caracteres 2: ')

print(f'A soma dos caracteres é {len(str1)+len(str2)}')
