

def capturar_valor(mensaje=None):
    try:
        return int(input(mensaje or 'Ingrese un valor: '))
    except:
        print('El valor es incorrecto')
        exit()

valor_1 = capturar_valor('Por favor ingrese un valor: ')
valor_2 = capturar_valor('Por favor ingrese un segundo valor: ')

print(valor_1 + valor_2)
print(valor_1 - valor_2)
print(valor_1 / valor_2)
print(valor_1 * valor_2)
print(valor_1 % valor_2)