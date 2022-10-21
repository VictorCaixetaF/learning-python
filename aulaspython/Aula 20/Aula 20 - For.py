'''
For
Iteração de strings com for
função range (start=0, stop, step=1
'''
'''
texto = 'Python'
c = 0

while c < len(texto):
    print(texto[c])
    c += 1
'''
'''
texto = 'Python'

for n, letra in enumerate(texto):
    print(n, letra)
'''
'''
for n in range(50, 10, -2):
    print(n)

for x in range(100):
    if x % 8 == 0:
        print(x)
'''
texto = 'Python'
n_str = ''
for letra in texto:
    if letra == 'n':
        n_str = n_str + letra.upper()
    else:
        n_str += letra
print(n_str)