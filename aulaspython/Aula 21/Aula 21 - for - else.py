'''
for / else
'''

variavel = ['Victor', 'César', 'Sarah']

for valor in variavel:
    print(valor)
    if valor.lower().startswith('h'):  # startwith - checa valor da str começa com alguma letra
        comeca_v = True
        break

else:
    print("Não existe palavra q começa com v")