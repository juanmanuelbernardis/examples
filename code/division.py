def capturar_valor(mensaje=None):
    try:
        return int(input(mensaje or 'Ingrese un valor: '))
    except:
        print('El valor es incorrecto')
        exit()

valor_1 = capturar_valor()
valor_2 = capturar_valor()
if valor_1 % valor_2 == 0:
    print('El resto es 0')
else:
    print('La division no da como resto 0')