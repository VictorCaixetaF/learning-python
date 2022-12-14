import os
palavra = input('Peça alguem para digitar uma palavra: ')
digitados = []
chances = input('Quantas chances você quer? ')
chances = int(chances)

from time import sleep
sleep(2)
os.system('cls')

while True:
    if chances < 1:
        print('Game Over')
        break

    letra = input('Digite uma letra: ')
    num_letra = len(letra)

    if num_letra != 1:
        print('Digite apenas uma letra. Tente novamente.')
        continue

    digitados.append(letra)

    if letra in palavra:
        print(f'Você acertou! A letra é: {letra}')
    else:
        print('Que pena, você errou.')
        digitados.pop()

    temporario = ''
    for secreto in palavra:
        if secreto in digitados:
            temporario += secreto
        else:
            temporario += '*'
    if palavra == temporario:
        print(f'Você acertou! A palavra é: {temporario}')
        break
    else:
        print(f'A palavra está assim: {temporario}')

    if letra not in palavra:
        chances -= 1
        print(f'Você ainda tem {chances} chances.')
        print()
