'''
Operadores Relacionais
== igauldade
> maior
>= maior ou igual
< menor
<= menor ou igual
!= diferente
'''
'''
num_1 = 2  #inteiro
num_2 = '2'  #string
expressao = (num_1 == int(num_2))

print(2 == 2)
print(2 == 1)
print(2 == '2')
print(num_1 == num_2)
print(expressao)
print(num_1 != num_2)
print(num_1 != int(num_2))
'''

nome = input('Qual o seu nome: ')
idade = input('QUal a sua idade: ')
e_maior = 18
jovem = 20
velho = 30

if int(idade) >= jovem and int(idade) <= velho:
    print(f'{nome} esta em análise.')
else:
    print('Emprestimo negado')
