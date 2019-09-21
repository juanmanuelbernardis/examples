def capturar_valor(mensaje=None):
    try:
        return int(input(mensaje or 'Ingrese un valor: '))
    except:
        print('El valor es incorrecto')
        exit()

horas = capturar_valor('Horas trabajadas: ')
antiguedad = capturar_valor('Años en la empresa: ')
cobroxhoras = capturar_valor('Cobro por hora: ')

sueldo = horas * cobroxhoras

if antiguedad >= 5:
    sueldo += 1000

print(sueldo)
