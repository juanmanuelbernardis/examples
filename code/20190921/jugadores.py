def capturar_valor(mensaje=None):
    try:
        return int(input(mensaje or 'Ingrese un valor: '))
    except:
        print('El valor es incorrecto')
        exit()

gj1 = capturar_valor('Ingrese los goles del jugador 1: ')
gj2 = capturar_valor('Ingrese los goles del jugador 2: ')

pj1 = capturar_valor('Ingrese los partidos del jugador 1: ')
pj2 = capturar_valor('Ingrese los partidos del jugador 2: ')


j1 = gj1 / pj1
j2 = gj2 / pj2

if j2 > j1:
    print('Jugador 2')
elif j1 > j2:
    print('Jugador 1')
else:
    print('Eleccion propia')
