def capturar_valor(mensaje=None):
    try:
        return int(input(mensaje or 'Ingrese un valor: '))
    except:
        print('El valor es incorrecto')
        exit()

valor = capturar_valor()
if valor >= 100 and valor <= 999:
    print('El valor es correcto:', valor)
else:
    print('El valor no cuenta con 3 cifras')

