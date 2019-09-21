def capturar_valor(mensaje=None):
    try:
        return int(input(mensaje or 'Ingrese un valor: '))
    except:
        print('El valor es incorrecto')
        exit()

L1= capturar_valor('Ingresar el primer lado: ')
L2= capturar_valor('Ingresar el segundo lado: ')
L3= capturar_valor('Ingresar el tercer lado: ')

if L1 == L2 and L2 == L3:
    print('Triangulo Equilatero')
elif (L1 == L2 and L2 != L3) or (L2 == L3 and L3 != L1 ) or (L1 == L3 and L3 != L2):
   print('Triangulo Isoseles')
else:
   print('Trianculo Escaleno')