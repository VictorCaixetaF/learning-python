print("CALCULADORA")
print()
while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operadores = input('Digite qual operação (+ - / *): ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not n1.isnumeric() or not n2.isnumeric():
        print('Digite um número!')
        continue
    n1 = float(n1)
    n2 = float(n2)
    if operadores == '+':
        print(f'A soma é {n1+n2}')
    elif operadores == '-':
        print(f'A subtração é {n1-n2}')
    elif operadores == '/':
        print(f'A divisão é {n1/n2}')
    elif operadores == '*':
        print(f'A multiplicação é {n1*n2}')
    else:
        print('Valor não é número.')
