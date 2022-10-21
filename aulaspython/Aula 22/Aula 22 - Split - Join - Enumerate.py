'''
split
join
enumerate
'''
'''
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista = string.split(' ')
lista2 = string.split(',')
lista3 = string.split('Brasil')
print(lista)
print(lista2)
print(lista3)

palavra = ''
contagem = 0

for valor in lista:
    print(f'A palavra {valor} apreceu {lista.count(valor)}')  #contagem de objetos
    qtd_vezes = lista.count((valor))
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'{palavra} apareceu mais vezes ({contagem}x)')
'''
'''
str = 'o brasil é penta.'
lista = str.split(' ')
str2 = ','.join(lista)
str3 = ''.join(lista)
print(str)
print(lista)
print(str2)
print(str3)
'''
str = 'o brasil é penta.'
lista = str.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)

