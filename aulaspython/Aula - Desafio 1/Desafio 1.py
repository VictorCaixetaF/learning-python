nome = 'Victor' 
idade = 33
altura = 1.70
peso = 85.4
ano_atual = 2022
nascimento = ano_atual-idade
imc = peso/(altura**2)

print(f'{nome} tem {idade}, {altura:.2f}m de altura e pesa{peso}kg. \n O IMC de {nome} é {imc:.2f}. \n {nome} nasceu em {nascimento}.')
