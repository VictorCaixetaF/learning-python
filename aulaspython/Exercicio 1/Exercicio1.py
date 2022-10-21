'''
Faça um pograma que peça ao usuário para digirar um número int,
informe se este número é para ou impar. Caso não digite um
numero inteiro, informe que não é um número inteiro
'''
n1 = input('Digite um número inteiro: ')
n2 = float()
if n1.isdigit():
    n1 = int(n1)
    if n1 % 2 == 0:
       print('Número par.')
    else:
        print('Número impar.')
else:
    print('Não é número inteiro.')