hora = input('Digite a hora sem os minutos: ')
if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
       print('valor fora da margem')
    else:
        if hora <= 11:
            print('bom dia')
        elif hora <= 17:
            print('boa tarde')
        else:
            print('boa noite')
else:
    print('Valor não válido')
