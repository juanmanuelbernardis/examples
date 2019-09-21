def capturar_valor(mensaje=None):
    try:
        return int(input(mensaje or 'Ingrese un valor: '))
    except:
        print('El valor es incorrecto')
        exit()

valor_1 = capturar_valor('Ingrese un numero: ')
valor_2 = capturar_valor('Ingrese un segundo numero: ')

if valor_1 % 3 == 0 and valor_2 % 3 == 0:
    print('ambos son divisibles por 3')

elif valor_1 % 3 == 0:

    print('Valor 1 es divisible por 3')
elif valor_2 % 3 == 0:

     print('Valor 2 es divisible por 3')
else:

    print('Ninguno es divisible por 3')


