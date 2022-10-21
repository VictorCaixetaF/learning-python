nome = input('Digite seu nome: ')
num = len(nome)
if num <= 4:
    print('nome pequeno')
elif num <= 6:
    print ('nome normal')
else:
    print('nome grande')
